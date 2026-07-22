class CandidateSelector:
    def select(self, query: str, all_files: list, graph=None, analyzer=None, max_candidates: int = 200) -> list:
        """
        Filters candidates based on query term overlap with file paths and file contents,
        and pulls in highly central hub files from the dependency graph.
        """
        import os
        from ruhci.utils.text import extract_query_terms
        
        # Deterministic filtering based on path relevance with safe stemming
        query_terms = extract_query_terms(query)
        
        scored_files = []
        for f in all_files:
            score = 0
            f_lower = f.lower()
            
            # Match path
            for term in query_terms:
                if term in f_lower:
                    score += 2.0  # Path match gets higher weight
                    
            # Match content if analyzer is provided
            if analyzer:
                # Use the O(1) reverse index built during pre-caching
                full_path = getattr(analyzer, '_path_index', {}).get(f)
                cached_content = analyzer._content_cache.get(full_path or f)
                            
                if cached_content:
                    for term in query_terms:
                        if term in cached_content:
                            score += 1.0  # Content match gets lower weight but is enough to select it
            
            scored_files.append((score, f))
            
        # Sort by score descending, then alphabetically for complete determinism
        scored_files.sort(key=lambda x: (-x[0], x[1]))
        
        # Only select files that got at least some score
        top_files = [f[1] for f in scored_files if f[0] > 0][:max_candidates]
        
        # Priority 3 Fix: Organically inject top hub files (high in-degree) 
        # so that core framework files like sessions.py aren't missed by pure path matching
        if graph:
            hub_scores = []
            for f in all_files:
                if graph.graph.has_node(f):
                    hub_scores.append((graph.graph.degree(f), f))
            hub_scores.sort(key=lambda x: (-x[0], x[1]))
            
            # Inject top 10 most imported hub files, respecting max_candidates limit
            for _, hub_file in hub_scores[:10]:
                if len(top_files) >= max_candidates:
                    break
                if hub_file not in top_files:
                    top_files.append(hub_file)
                
        return top_files