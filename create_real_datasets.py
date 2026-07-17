import os
import json
import shutil

DATASETS_DIR = r"C:\Users\ROG G532 LV\.gemini\antigravity\scratch\Ruhci-Claude-Engine\benchmark\datasets"

# Clean up existing dummy cases
for repo in ["requests", "flask"]:
    repo_dir = os.path.join(DATASETS_DIR, repo)
    if os.path.exists(repo_dir):
        for f in os.listdir(repo_dir):
            if f.startswith("case_") and f.endswith(".json"):
                os.remove(os.path.join(repo_dir, f))

requests_cases = [
    {
        "id": "req_001",
        "repository": "requests",
        "task": "Easy",
        "query": "How do I completely disable SSL certificate verification for my session?",
        "primary_file": "requests/sessions.py",
        "required_files": ["requests/sessions.py", "requests/adapters.py"],
        "expected_rank": ["requests/sessions.py", "requests/adapters.py"]
    },
    {
        "id": "req_002",
        "repository": "requests",
        "task": "Medium",
        "query": "The json parameter is not serializing my datetime objects properly. Where is the payload prepared?",
        "primary_file": "requests/models.py",
        "required_files": ["requests/models.py"],
        "expected_rank": ["requests/models.py"]
    },
    {
        "id": "req_003",
        "repository": "requests",
        "task": "Hard",
        "query": "I want to increase the connection pool size and max retries using HTTPAdapter",
        "primary_file": "requests/adapters.py",
        "required_files": ["requests/adapters.py"],
        "expected_rank": ["requests/adapters.py"]
    },
    {
        "id": "req_004",
        "repository": "requests",
        "task": "Medium",
        "query": "I am encountering a TooManyRedirects error when a site redirects in an infinite loop. Where is the redirect limit enforced?",
        "primary_file": "requests/sessions.py",
        "required_files": ["requests/sessions.py"],
        "expected_rank": ["requests/sessions.py"]
    }
]

flask_cases = [
    {
        "id": "flask_001",
        "repository": "flask",
        "task": "Medium",
        "query": "RuntimeError: Working outside of application context. I need to push the context manually.",
        "primary_file": "flask/ctx.py",
        "required_files": ["flask/ctx.py", "flask/app.py"],
        "expected_rank": ["flask/ctx.py"]
    },
    {
        "id": "flask_002",
        "repository": "flask",
        "task": "Easy",
        "query": "How do I register a function to run before every request using the @before_request decorator?",
        "primary_file": "flask/app.py",
        "required_files": ["flask/app.py"],
        "expected_rank": ["flask/app.py"]
    },
    {
        "id": "flask_003",
        "repository": "flask",
        "task": "Medium",
        "query": "I want to return a JSON response automatically. Where is the jsonify function defined?",
        "primary_file": "flask/json/__init__.py",
        "required_files": ["flask/json/__init__.py"],
        "expected_rank": ["flask/json/__init__.py", "flask/helpers.py"]
    },
    {
        "id": "flask_004",
        "repository": "flask",
        "task": "Hard",
        "query": "How can I register a custom URL converter (like <my_type:id>) in the app url_map?",
        "primary_file": "flask/app.py",
        "required_files": ["flask/app.py"],
        "expected_rank": ["flask/app.py"]
    }
]

def save_cases(repo, cases):
    repo_dir = os.path.join(DATASETS_DIR, repo)
    os.makedirs(repo_dir, exist_ok=True)
    for c in cases:
        path = os.path.join(repo_dir, f"{c['id']}.json")
        with open(path, 'w') as f:
            json.dump(c, f, indent=4)

save_cases("requests", requests_cases)
save_cases("flask", flask_cases)
print("Real datasets generated!")
