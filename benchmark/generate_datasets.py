import os
import json

repos = ["FastAPI", "Requests", "Flask", "Django", "SQLAlchemy"]

def get_primary_file(repo):
    mapping = {
        "FastAPI": "fastapi/security/oauth2.py",
        "Requests": "requests/sessions.py",
        "Flask": "flask/app.py",
        "Django": "django/db/models/query.py",
        "SQLAlchemy": "sqlalchemy/orm/session.py"
    }
    return mapping.get(repo, f"{repo.lower()}/main.py")

dataset_dir = os.path.join(os.path.dirname(__file__), "datasets")

# Create 10 files per repo
for repo in repos:
    repo_dir = os.path.join(dataset_dir, repo.lower())
    os.makedirs(repo_dir, exist_ok=True)
    
    primary = get_primary_file(repo)
    
    for i in range(1, 11):
        # Determine case type: 3 Easy, 4 Ambiguous, 3 Negative
        if i <= 3:
            case_type = "Easy"
            query = f"Fix {repo} basic issue"
            forbidden = [f"{repo.lower()}/random_test.py"]
        elif i <= 7:
            case_type = "Ambiguous"
            query = f"Fix {repo} complex ambiguous issue"
            forbidden = [f"{repo.lower()}/test_ambiguous.py"]
        else:
            case_type = "Negative"
            query = f"Database migration failure for {repo}"
            forbidden = [f"{repo.lower()}/database.py", f"tests/test_database.py"]

        data = {
            "id": f"{repo.lower()}_case_{i:03d}",
            "repository": repo,
            "task": case_type,
            "query": query,
            "primary_file": primary,
            "required_files": [primary],
            "supporting_files": [f"{repo.lower()}/utils.py"],
            "forbidden_files": forbidden,
            "required_symbols": ["main_class"],
            "expected_rank": [primary, f"{repo.lower()}/utils.py"]
        }
        
        filepath = os.path.join(repo_dir, f"case_{i:03d}.json")
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)