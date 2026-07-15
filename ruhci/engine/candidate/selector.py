class CandidateSelector:
    def select(self, query: str, all_files: list, graph=None, max_candidates: int = 200) -> list:
        """
        Filters candidates based on query term overlap with file paths, 
        and pulls in highly central hub files from the dependency graph.
        """
        import re
        # Deterministic filtering based on path relevance with safe stemming
        raw_terms = set(re.findall(r'\w+', query.lower()))
        exceptions = {"does", "status", "utils", "this", "is", "has", "was", "as", "its", "us", "analysis", "process", "access"}
        query_terms = {t[:-1] if t.endswith('s') and not t.endswith('ss') and t not in exceptions and len(t) > 3 else t for t in raw_terms}
        
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
        
        # Priority 3 Fix: Organically inject top hub files (high in-degree) 
        # so that core framework files like sessions.py aren't missed by pure path matching
        if graph:
            hub_scores = []
            for f in all_files:
                if graph.graph.has_node(f):
                    hub_scores.append((graph.graph.degree(f), f))
            hub_scores.sort(key=lambda x: (-x[0], x[1]))
            
            # Inject top 10 most imported hub files
            for _, hub_file in hub_scores[:10]:
                if hub_file not in top_files:
                    top_files.append(hub_file)
                
        return top_files