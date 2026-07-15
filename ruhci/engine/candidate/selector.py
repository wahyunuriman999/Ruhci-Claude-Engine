class CandidateSelector:
    def select(self, query: str, all_files: list, max_candidates: int = 200) -> list:
        """
        Filters candidates based on query term overlap with file paths.
        LIMITATION (v0.2.1): Pure path matching can miss highly relevant files 
        that do not contain the query terms in their filepath. 
        A semantic/vector pre-filter is planned for future releases.
        """
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