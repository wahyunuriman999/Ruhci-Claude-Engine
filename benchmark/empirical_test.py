import os
import sys
import json
from ruhci.engine.core import RuhciEngine

def main():
    repo_path = 'requests_clone'
    if not os.path.exists(repo_path):
        print(f"Error: {repo_path} not found.")
        sys.exit(1)

    print(f"Instantiating RuhciEngine for {repo_path}...")
    engine = RuhciEngine(repo_path)
    
    query = "How are HTTP adapters initialized and managed for sessions?"
    print(f"Query: '{query}'")
    print("Compiling context...")
    
    results = engine.compile_context(query)
    
    output_lines = []
    output_lines.append(f"Empirical Run 001 - Target: {repo_path}")
    output_lines.append(f"Query: {query}")
    output_lines.append("-" * 40)
    for idx, res in enumerate(results[:10]):
        output_lines.append(f"[{idx+1}] File: {res['filepath']}")
        output_lines.append(f"    Score: {res['score']:.4f}")
        output_lines.append(f"    Signals: {json.dumps(res['signals'])}")
    
    out_dir = "benchmark/proof"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "empirical_run_001.txt")
    
    with open(out_path, "w") as f:
        f.write("\n".join(output_lines) + "\n")
        
    print(f"Results written to {out_path}")

if __name__ == '__main__':
    main()
