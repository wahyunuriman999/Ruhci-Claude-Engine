from ruhci.ranking.intent import QueryIntentClassifier

class HybridRankerV01:
    def __init__(self):
        self.intent_classifier = QueryIntentClassifier()
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

    def rank(self, query: str, candidates: list, metadata_index: dict, graph) -> list:
        import re
        intents = self.intent_classifier.classify(query)
        ranked_results = []
        query_terms = set(re.findall(r'\w+', query.lower()))
        
        for filepath in candidates:
            meta = metadata_index.get(filepath)
            if not meta:
                continue
                
            # 1. Symbol Match (Strongest Evidence)
            symbol_score = 0.1
            if meta.symbols:
                total_symbols = len(meta.symbols)
                matched_symbols = sum(1 for sym in meta.symbols for term in query_terms if term in sym.name.lower())
                ratio = matched_symbols / total_symbols if total_symbols > 0 else 0
                # Scale the ratio so that a small fraction (e.g. 5%) can still yield a decent score, but cap at 1.0
                symbol_score = min(1.0, 0.1 + (ratio * 5.0))
            
            # 2. Dependency Relevance
            dependency_score = self._compute_dependency_relevance(filepath, graph)
            
            # 3. Semantic Similarity (Mocked with path overlap for now)
            semantic_score = min(1.0, sum(1 for term in query_terms if term in filepath.lower()) * 0.2)
            
            # 4. Intent Score
            intent_score = 1.0 if self.intent_classifier.get_role_boost(intents, filepath) > 1.0 else 0.5
            
            # 5. Role Score
            role_score = 0.5
            if "utils" in filepath or "core" in filepath or "security" in filepath:
                role_score = 0.8
            
            # 6. Path Score
            path_score = 1.0 if any(term in filepath.lower() for term in query_terms) else 0.3
            
            # FUSION
            final_score = (
                (symbol_score * self.weights["symbol"]) +
                (dependency_score * self.weights["dependency"]) +
                (semantic_score * self.weights["semantic"]) +
                (intent_score * self.weights["intent"]) +
                (role_score * self.weights["role"]) +
                (path_score * self.weights["path"])
            )
            
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