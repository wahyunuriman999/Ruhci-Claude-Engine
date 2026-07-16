import re
import os

class ContentAnalyzer:
    """
    v0.4 Content Analyzer
    Reads raw file content to calculate Term Frequency (TF) for query terms.
    This resolves the "Blind to Content" limitation for files like `certs.py`
    that do not have top-level AST symbols.
    """
    
    def __init__(self):
        # Cache to avoid re-reading the same file multiple times if called iteratively
        self._content_cache = {}

    def _read_file(self, filepath: str) -> str:
        if filepath in self._content_cache:
            return self._content_cache[filepath]
            
        if not os.path.exists(filepath):
            return ""
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                self._content_cache[filepath] = content
                return content
        except Exception:
            # Fallback for weird encodings
            try:
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read().lower()
                    self._content_cache[filepath] = content
                    return content
            except Exception:
                return ""

    def analyze(self, filepath: str, query_terms: set) -> float:
        """
        Analyzes the content of the file and returns a semantic score (0.0 to 1.0)
        based on the occurrence of query_terms.
        """
        if not query_terms:
            return 0.0
            
        content = self._read_file(filepath)
        if not content:
            return 0.0

        # Fast path: if none of the terms are in the content string at all, return 0
        if not any(term in content for term in query_terms):
            return 0.0

        # Tokenize content
        content_tokens = re.findall(r'\w+', content)
        content_term_counts = {term: 0 for term in query_terms}
        
        # Count frequencies
        for token in content_tokens:
            for term in query_terms:
                # Require exact match for short terms (< 4 chars) to prevent false positives like 'ssl' in 'sesslink'
                if len(term) < 4:
                    if term == token:
                        content_term_counts[term] += 1
                else:
                    # substring match to handle stemming variations inside the content 
                    # e.g., term 'certificate' matching token 'certifi' or 'cert'
                    if term in token or (len(token) > 3 and token in term):
                        content_term_counts[term] += 1

        matched_terms = sum(1 for term, count in content_term_counts.items() if count > 0)
        total_terms = len(query_terms)
        
        # Coverage ratio (how many of the unique query terms were found)
        coverage_score = matched_terms / total_terms
        
        # Frequency bonus (rewards files that mention the terms multiple times)
        total_hits = sum(content_term_counts.values())
        freq_bonus = min(1.0, total_hits / (total_terms * 3.0)) # cap bonus at 3 hits per term
        
        # Final semantic score: 80% coverage, 20% frequency
        semantic_score = (coverage_score * 0.8) + (freq_bonus * 0.2)
        
        return min(1.0, semantic_score)
