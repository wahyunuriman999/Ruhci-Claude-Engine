class CandidateSelector:
    def select(self, query: str, all_files: list, max_candidates: int = 200) -> list:
        # Deterministic filtering based on path relevance
        query_terms = set(query.lower().split())
        
        scored_files = []
        for f in all_files:
            score = 0
            f_lower = f.lower()
            for term in query_terms:
                if term in f_lower:
                    score += 1.0
            
            scored_files.append((score, f))
            
        # Sort by score descending, then alphabetically for complete determinism
        scored_files.sort(key=lambda x: (-x[0], x[1]))
        
        top_files = [f[1] for f in scored_files[:max_candidates]]
        return top_files