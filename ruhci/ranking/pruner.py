class ContextPruner:
    def __init__(self, mode="precision"):
        self.mode = mode
        if mode == "precision":
            self.abs_threshold = 0.25 # Lowered from 0.65 to fit realistic 0.3-0.7 score ranges
            self.rel_ratio = 0.70
            self.gap_threshold = 0.25
        else: # exploration
            self.abs_threshold = 0.30
            self.rel_ratio = 0.50
            self.gap_threshold = 0.40

    def prune(self, ranked_candidates):
        if not ranked_candidates:
            return []
            
        final_context = []
        rank1_score = ranked_candidates[0]["score"]
        
        for i, candidate in enumerate(ranked_candidates):
            score = candidate["score"]
            
            # 1. Dynamic Threshold
            min_relative = rank1_score * self.rel_ratio
            if score < self.abs_threshold or score < min_relative:
                break
                
            # 2. Cascade Gap Filtering
            if i > 0:
                prev_score = ranked_candidates[i-1]["score"]
                if (prev_score - score) > self.gap_threshold:
                    break
                    
            # 3. Dependency Evidence Lock
            if i > 0:
                dep_score = candidate["signals"]["dependency"]
                if dep_score < 0.4:
                    continue
            
            final_context.append(candidate)
            
        return final_context