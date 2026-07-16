class QueryIntentClassifier:
    def classify(self, query: str):
        query_lower = query.lower()
        intents = []
        
        # 1. Educational / Understanding
        if any(w in query_lower for w in ["how does", "what is", "explain", "why", "concept"]):
            intents.append("Educational")
            
        # 2. Structural / Implementation
        if any(w in query_lower for w in ["how is", "implemented", "architecture", "structure", "where", "pattern"]):
            intents.append("Structural")
            
        # 3. Usage / Examples
        if any(w in query_lower for w in ["how to use", "example", "usage", "snippet", "invoke", "call"]):
            intents.append("Usage")
            
        # Domain specifics
        if any(w in query_lower for w in ["bug", "fix", "issue", "error", "doesn't work"]):
            intents.append("Bug Fix")
        if any(w in query_lower for w in ["auth", "jwt", "token", "login", "security", "credentials"]):
            intents.append("Security")
        if any(w in query_lower for w in ["database", "migration", "sql", "db"]):
            intents.append("Database")
            
        return intents

    def calculate_intent_score(self, intents: list, filepath: str, in_degree: int, semantic_score: float) -> float:
        """
        Calculates a dynamic intent score (0.1 to 1.0) based on detected intents.
        """
        score = 0.5 # Base neutral score
        filepath_lower = filepath.lower()
        
        # Domain-specific boosts
        if "Security" in intents and any(term in filepath_lower for term in ["auth", "security", "middleware", "cert"]):
            score += 0.3
        if "Database" in intents and any(term in filepath_lower for term in ["models", "db", "migrations"]):
            score += 0.3
            
        # Lexical Analytics: Dynamic behavior based on user intent
        
        # Educational: Boosts core files or highly semantic files
        if "Educational" in intents:
            if any(term in filepath_lower for term in ["core", "base", "main", "init", "globals", "ctx"]):
                score += 0.3
            if semantic_score >= 0.7:
                score += 0.2
                
        # Structural: Boosts files that act as dependency hubs
        if "Structural" in intents:
            if in_degree > 5:
                score += 0.3
            if any(term in filepath_lower for term in ["manager", "pool", "factory", "handler", "controller"]):
                score += 0.2
                
        # Usage: Flips the typical "test" penalty to a massive boost
        if "Usage" in intents:
            if "test" in filepath_lower or "example" in filepath_lower or "demo" in filepath_lower:
                score += 0.4
                
        # Default testing penalty if usage is not requested
        if "test" in filepath_lower and "Usage" not in intents and "Bug Fix" not in intents:
            score -= 0.3
            
        return min(1.0, max(0.1, score))