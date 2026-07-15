import random

class CandidateSelector:
    def select(self, query: str, all_files: list, max_candidates: int = 200) -> list:
        # Mock logic: in reality this uses keyword matching, path relevance, import relations
        
        # We need a top N buffer + 20 random diversity
        diversity_buffer_size = 20
        top_n = max(0, max_candidates - diversity_buffer_size)
        
        query_terms = query.lower().split()
        
        scored_files = []
        for f in all_files:
            score = 0
            if any(term in f.lower() for term in query_terms):
                score += 1.0
            scored_files.append((score, f))
            
        scored_files.sort(key=lambda x: x[0], reverse=True)
        
        top_files = [f[1] for f in scored_files[:top_n]]
        remaining_files = [f[1] for f in scored_files[top_n:]]
        
        # Add random diversity
        random.seed(42) # Deterministic random
        diversity_files = random.sample(remaining_files, min(len(remaining_files), diversity_buffer_size))
        
        return list(set(top_files + diversity_files))