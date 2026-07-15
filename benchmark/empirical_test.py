import os
import sys
import subprocess
from loguru import logger
from ruhci.engine.core import RuhciEngine

def clone_repo(repo_url, dest_dir):
    if not os.path.exists(dest_dir):
        logger.info(f"Cloning {repo_url} into {dest_dir}...")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, dest_dir], check=True)

def main():
    test_cases = [
        {
            "repo": "https://github.com/psf/requests.git",
            "dir": "requests_clone",
            "query": "How does SSL certificate verification work?"
        },
        {
            "repo": "https://github.com/pallets/flask.git",
            "dir": "flask_clone",
            "query": "How is the application context managed and pushed to the stack?"
        },
        {
            "repo": "https://github.com/urllib3/urllib3.git",
            "dir": "urllib3_clone",
            "query": "How is connection pooling implemented and managed?"
        }
    ]
    
    os.makedirs("benchmark/proof", exist_ok=True)
    proof_file = "benchmark/proof/empirical_run_002.txt"
    
    with open(proof_file, "w") as f:
        f.write("Empirical Run 002 - Validation Across 3 Repositories\n")
        f.write("========================================================\n\n")
        
        for case in test_cases:
            clone_repo(case["repo"], case["dir"])
            
            f.write(f"Target Repository: {case['dir']}\n")
            f.write(f"Query: {case['query']}\n")
            f.write("-" * 40 + "\n")
            
            print(f"Instantiating RuhciEngine for {case['dir']}...")
            engine = RuhciEngine(case["dir"])
            
            print(f"Query: '{case['query']}'")
            print("Compiling context...")
            results = engine.compile_context(case['query'])
            
            for i, res in enumerate(results[:5]):
                f.write(f"[{i+1}] File: {res['filepath']}\n")
                f.write(f"    Score: {res['score']:.4f}\n")
                f.write(f"    Signals: {res['signals']}\n")
            
            f.write("\n\n")
            
    print(f"Results written to {proof_file}")

if __name__ == '__main__':
    main()
