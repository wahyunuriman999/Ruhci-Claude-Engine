class QueryIntentClassifier:
    def classify(self, query: str):
        query_lower = query.lower()
        intents = []
        
        if any(w in query_lower for w in ["bug", "fix", "issue", "error", "doesn't work"]):
            intents.append("Bug Fix")
        if any(w in query_lower for w in ["auth", "jwt", "token", "login", "security", "credentials"]):
            intents.append("Security")
            intents.append("Authentication")
        if any(w in query_lower for w in ["database", "migration", "sql"]):
            intents.append("Database")
            
        return intents

    def get_role_boost(self, intents, filepath: str) -> float:
        boost = 1.0
        if "Authentication" in intents or "Security" in intents:
            if any(term in filepath for term in ["auth", "security", "middleware"]):
                boost = 1.5
        if "Database" in intents:
            if any(term in filepath for term in ["models", "db", "migrations"]):
                boost = 1.5
        
        if "test" in filepath:
            boost = 0.5 # Default demote testing files unless query explicitly asks for tests
            
        return boost