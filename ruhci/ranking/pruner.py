class ContextPruner:
    def __init__(self, mode="precision"):
        self.mode = mode
        if mode == "precision":
            self.abs_threshold = 0.25 # Lowered from 0.65 to fit realistic 0.3-0.7 score ranges
            self.rel_ratio = 0.70
            self.gap_threshold = 0.25
        else: # exploration
            self.abs_threshold = 0.15
            self.rel_ratio = 0.40
            self.gap_threshold = 0.50

    def prune(self, ranked_candidates):
        if not ranked_candidates:
            return []

        final_context = []
        rank1_score = ranked_candidates[0]["score"]
        last_accepted_score = rank1_score

        for i, candidate in enumerate(ranked_candidates):
            score = candidate["score"]

            # 1. Dynamic Threshold
            min_relative = rank1_score * self.rel_ratio
            if score < self.abs_threshold or score < min_relative:
                break

            # 2. Cascade Gap Filtering — compare against the last file we
            # actually accepted, not the raw previous row (which may already
            # have been dropped by rule 3 below, making the "gap" meaningless).
            if final_context:
                if (last_accepted_score - score) > self.gap_threshold:
                    break

            # 3. Dependency Evidence — soft signal, not a hard gate.
            # NOTE: HybridRankerV02._compute_dependency_relevance caps the
            # dependency signal at 0.1 for any file with in_degree == 0, and
            # the calibration step multiplies it down further, so a file needs
            # >= 3 inbound imports just to reach 0.4. A hard "dep_score < 0.4:
            # continue" here silently dropped every entry-point, CLI script,
            # or newly-added file no matter how strong its symbol/semantic
            # match was. We now only veto on near-zero dependency evidence AND
            # weak overall relevance — a high final score (i.e. it already
            # passed thresholds 1-2) is allowed to override a low import count.
            dep_score = candidate["signals"]["dependency"]
            if dep_score < 0.15 and score < min_relative * 1.5:
                continue

            final_context.append(candidate)
            last_accepted_score = score

        return final_context