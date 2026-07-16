from ruhci.ranking.intent import QueryIntentClassifier
from ruhci.ranking.semantic import ContentAnalyzer
import re

class HybridRankerV02:
    """
    V0.4 Hybrid Ranker (Vector-Semantic Search Preview).
    Combines multiple signals for final ranking.
    
    Resolved Limitations from v0.3:
    1. Blind to Content: Now uses `ContentAnalyzer` (TF-IDF/Term Frequency) to give 
       semantic scores to files with zero AST symbols (e.g. certs.py).
    2. Dependency Dominance: Implemented Semantic Gate. High in-degree files (models.py) 
       are penalized if they do not possess any symbol or semantic relevance to the query.
    """
    def __init__(self):
        self.intent_classifier = QueryIntentClassifier()
        self.content_analyzer = ContentAnalyzer()
        # Updated Guardrail Weights
        self.weights = {
            "symbol": 0.40,
            "dependency": 0.25,
            "semantic": 0.15,
            "intent": 0.10,
            "role": 0.05,
            "path": 0.05
        }

    def _compute_dependency_relevance(self, filepath: str, graph) -> float:
        if not graph or not graph.graph.has_node(filepath):
            return 0.1
        # Simple centrality based on in-degree in the dependency graph
        in_degree = graph.graph.in_degree(filepath)
        return min(1.0, 0.1 + (in_degree * 0.1))

    def _stem_term(self, term: str) -> str:
        # Do not stem very short or common structural terms
        if len(term) < 6:
            return term
        for suffix in ["ing", "ed", "s", "es", "ly", "tion", "ity", "ment", "able", "ible"]:
            if term.endswith(suffix):
                return term[:-len(suffix)]
        return term

    def rank(self, query: str, candidates: list, metadata_index: dict, graph) -> list:
        # Word tokenization for query terms (ignore punctuation) with safe stemming
        raw_terms = set(re.findall(r'\w+', query.lower()))
        stopwords = {"how", "does", "work", "what", "where", "why", "who", "when", "is", "are", "am", "be", "been", "being", "have", "has", "had", "do", "did", "and", "or", "but", "if", "for", "in", "of", "to", "with", "on", "by", "this", "that", "it", "its", "us", "a", "an", "the"}
        
        query_terms = set()
        for t in raw_terms:
            if t in stopwords: continue
            t = self._stem_term(t)
            if len(t) > 2:
                query_terms.add(t)
        
        intents = self.intent_classifier.classify(query)
        ranked_results = []
        
        for filepath in candidates:
            meta = metadata_index.get(filepath)
            if not meta:
                continue
                
            # 1. Symbol Match (Strongest Evidence)
            symbol_score = 0.1
            if meta.symbols:
                matched_terms = set()
                for sym in meta.symbols:
                    for term in query_terms:
                        if term in sym.name.lower():
                            matched_terms.add(term)
                ratio = len(matched_terms) / len(query_terms) if query_terms else 0
                symbol_score = min(1.0, 0.1 + (ratio * 0.9))
            
            # 2. Semantic Similarity (Content-based via TF-IDF emulation)
            # Replaces the mock path-based semantic score from v0.3
            semantic_score = self.content_analyzer.analyze(filepath, query_terms)
            
            # 3. Dependency Relevance
            dependency_score = self._compute_dependency_relevance(filepath, graph)
            
            # DEPENDENCY-SEMANTIC CALIBRATION
            # Prevent files with huge dependency scores (like models.py) from dominating 
            # if their semantic relevance is low.
            dependency_score *= min(1.0, semantic_score * 4.0)
            
            # 4. Intent Score
            in_degree = graph.graph.in_degree(filepath) if graph and graph.graph.has_node(filepath) else 0
            intent_score = self.intent_classifier.calculate_intent_score(
                intents=intents,
                filepath=filepath,
                in_degree=in_degree,
                semantic_score=semantic_score
            )
            
            # 5. Role Score
            role_score = 0.5
            if "utils" in filepath or "core" in filepath or "security" in filepath:
                role_score = 0.8
            
            # 6. Path Score
            filename_no_ext = filepath.lower().replace('\\', '/').split('/')[-1].replace('.py', '')
            path_score = 1.0 if any(term in filepath.lower() or term in filename_no_ext for term in query_terms) else 0.3
            
            # Fusion Calculation
            final_score = (
                (symbol_score * self.weights["symbol"]) +
                (dependency_score * self.weights["dependency"]) +
                (semantic_score * self.weights["semantic"]) +
                (intent_score * self.weights["intent"]) +
                (role_score * self.weights["role"]) +
                (path_score * self.weights["path"])
            )
            
            # Explicit final penalties
            filepath_lower = filepath.lower()
            if "test" in filepath_lower:
                final_score *= 0.5
                
            ranked_results.append({
                "file": filepath,
                "score": final_score,
                "signals": {
                    "symbol": symbol_score,
                    "dependency": dependency_score,
                    "semantic": semantic_score,
                    "intent": intent_score,
                    "role": role_score,
                    "path": path_score
                }
            })
            
        ranked_results.sort(key=lambda x: x["score"], reverse=True)
        return ranked_results