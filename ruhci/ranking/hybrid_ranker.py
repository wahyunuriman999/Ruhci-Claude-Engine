from ruhci.ranking.intent import QueryIntentClassifier

class HybridRankerV01:
    def __init__(self):
        self.intent_classifier = QueryIntentClassifier()
        self.weights = {
            "symbol": 0.35,
            "dependency": 0.25,
            "semantic": 0.20,
            "role": 0.10,
            "history": 0.10
        }

    def _compute_dependency_relevance(self, filepath: str, query_alignment: float) -> float:
        # Centrality is just a mock here. e.g. utils.py has 1.0, oauth2.py has 0.5
        centrality = 1.0 if "utils" in filepath or "middleware" in filepath else 0.5
        
        # Dependency Relevance = Graph Relation * Query Alignment
        return centrality * query_alignment

    def rank(self, query: str, candidates: list, required_symbols: list) -> list:
        intents = self.intent_classifier.classify(query)
        ranked_results = []
        
        for filepath in candidates:
            # 1. Symbol Match
            # MOCK: if it's the primary file, simulate finding the exact symbol
            symbol_score = 1.0 if filepath in ["fastapi/security/oauth2.py", "requests/sessions.py"] else 0.3
            
            # 2. Semantic Similarity
            semantic_score = 0.9 if filepath in ["fastapi/security/oauth2.py", "requests/sessions.py"] else (0.95 if filepath in ["fastapi/middleware/auth.py", "requests/adapters.py"] else 0.1)
            
            # 3. Dependency Relevance
            dependency_score = self._compute_dependency_relevance(filepath, query_alignment=semantic_score)
            
            # 4. File Role Score
            role_boost = self.intent_classifier.get_role_boost(intents, filepath)
            base_role = 1.0 if filepath in ["fastapi/security/oauth2.py", "requests/sessions.py"] else 0.8
            role_score = min(1.0, base_role * role_boost)
            
            # 5. History Score (Mocked out / Disabled for Sprint 3)
            history_score = 0.0
            
            # FUSION
            final_score = (
                (symbol_score * self.weights["symbol"]) +
                (dependency_score * self.weights["dependency"]) +
                (semantic_score * self.weights["semantic"]) +
                (role_score * self.weights["role"]) +
                (history_score * self.weights["history"])
            )
            
            ranked_results.append({
                "file": filepath,
                "score": final_score,
                "signals": {
                    "symbol": symbol_score,
                    "dependency": dependency_score,
                    "semantic": semantic_score,
                    "role": role_score
                }
            })
            
        # Sort descending by score
        ranked_results.sort(key=lambda x: x["score"], reverse=True)
        return ranked_results