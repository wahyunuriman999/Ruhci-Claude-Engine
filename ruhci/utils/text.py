import re

def stem_term(term: str) -> str:
    """
    Safely stems a term by removing common suffixes without breaking structural terms.
    """
    if len(term) < 6:
        # Extra rule from selector.py to handle simple plural 's'
        exceptions = {"does", "status", "utils", "this", "is", "has", "was", "as", "its", "us", "analysis", "process", "access"}
        if len(term) > 3 and term.endswith('s') and not term.endswith('ss') and term not in exceptions:
            return term[:-1]
        return term
        
    for suffix in ["ing", "ed", "s", "es", "ly", "tion", "ity", "ment", "able", "ible"]:
        if term.endswith(suffix):
            return term[:-len(suffix)]
    return term

def extract_query_terms(query: str) -> set:
    """
    Extracts, filters, and stems terms from a query string.
    """
    raw_terms = set(re.findall(r'\w+', query.lower()))
    stopwords = {"how", "does", "work", "what", "where", "why", "who", "when", "is", "are", "am", "be", "been", "being", "have", "has", "had", "do", "did", "and", "or", "but", "if", "for", "in", "of", "to", "with", "on", "by", "this", "that", "it", "its", "us", "a", "an", "the"}
    
    query_terms = set()
    for t in raw_terms:
        if t in stopwords: continue
        t = stem_term(t)
        if len(t) > 2:
            query_terms.add(t)
            
    return query_terms
