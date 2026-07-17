import os
import json
import glob
import time
from ruhci.engine.core import RuhciEngine

def format_percentage(value):
    return f"{value * 100:.1f}%"

def main():
    print("=" * 60)
    print(" RUHCI ENGINE - BENCHMARK RUNNER ")
    print("=" * 60)
    
    benchmark_dir = os.path.join(os.path.dirname(__file__), "benchmark", "datasets")
    
    if not os.path.exists(benchmark_dir):
        print(f"Error: Benchmark directory not found at {benchmark_dir}")
        return

    # Group JSON files by repository
    repo_datasets = {}
    
    json_files = glob.glob(os.path.join(benchmark_dir, "**", "*.json"), recursive=True)
    
    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                repo_name = data.get("repository", "").lower()
                if not repo_name:
                    continue
                    
                if repo_name not in repo_datasets:
                    repo_datasets[repo_name] = []
                repo_datasets[repo_name].append(data)
            except Exception as e:
                print(f"Failed to parse {jf}: {e}")
                
    if not repo_datasets:
        print("No datasets found.")
        return
        
    print(f"Found {len(json_files)} test cases across {len(repo_datasets)} repositories.\n")
    
    overall_metrics = {
        "total_cases": 0,
        "hits_at_1": 0,
        "hits_at_3": 0,
        "sum_mrr": 0.0,
        "time_ms": 0.0
    }
    
    for repo_name, cases in repo_datasets.items():
        # Check if local clone exists
        clone_dir = f"{repo_name}_clone"
        if not os.path.exists(clone_dir) or not os.path.isdir(clone_dir):
            print(f"[-] SKIPPING '{repo_name}' (Directory '{clone_dir}' not found locally)")
            continue
            
        print(f"[+] BENCHMARKING '{repo_name}' ({len(cases)} cases) in '{clone_dir}'...")
        
        # Initialize engine
        start_init = time.time()
        engine = RuhciEngine(target_dir=clone_dir)
        init_time = (time.time() - start_init) * 1000
        print(f"    Engine initialized & cached in {init_time:.1f}ms")
        
        repo_metrics = {
            "total_cases": len(cases),
            "hits_at_1": 0,
            "hits_at_3": 0,
            "sum_mrr": 0.0,
            "time_ms": 0.0
        }
        
        for case in cases:
            query = case.get("query", "")
            primary_file = case.get("primary_file", "")
            
            if not query or not primary_file:
                continue
                
            start_q = time.time()
            results = engine.compile_context(query)
            q_time = (time.time() - start_q) * 1000
            repo_metrics["time_ms"] += q_time
            
            # Find rank of primary_file
            # Results contain {'filepath': ..., 'score': ...}
            rank = 0
            primary_file_norm = primary_file.replace('\\', '/')
            for i, res in enumerate(results):
                res_path = res['filepath'].replace('\\', '/')
                if res_path.endswith(primary_file_norm) or primary_file_norm in res_path:
                    rank = i + 1
                    break
                    
            if rank == 1:
                repo_metrics["hits_at_1"] += 1
                repo_metrics["hits_at_3"] += 1
                repo_metrics["sum_mrr"] += 1.0
            elif 1 < rank <= 3:
                repo_metrics["hits_at_3"] += 1
                repo_metrics["sum_mrr"] += (1.0 / rank)
            elif rank > 3:
                repo_metrics["sum_mrr"] += (1.0 / rank)
                print(f"      [MISS] '{query}'\n        Expected: {primary_file}\n        Got Top 3:")
                for r in results[:3]:
                    print(f"          - {r['filepath']} (Score: {r['score']})")
            else:
                print(f"      [MISS] '{query}'\n        Expected: {primary_file}\n        Got Top 3:")
                for r in results[:3]:
                    print(f"          - {r['filepath']} (Score: {r['score']})")
                
        # Aggregate
        overall_metrics["total_cases"] += repo_metrics["total_cases"]
        overall_metrics["hits_at_1"] += repo_metrics["hits_at_1"]
        overall_metrics["hits_at_3"] += repo_metrics["hits_at_3"]
        overall_metrics["sum_mrr"] += repo_metrics["sum_mrr"]
        overall_metrics["time_ms"] += repo_metrics["time_ms"]
        
        # Repo Report
        r1 = repo_metrics["hits_at_1"] / repo_metrics["total_cases"]
        r3 = repo_metrics["hits_at_3"] / repo_metrics["total_cases"]
        mrr = repo_metrics["sum_mrr"] / repo_metrics["total_cases"]
        avg_time = repo_metrics["time_ms"] / repo_metrics["total_cases"]
        
        print(f"    -> Recall@1: {format_percentage(r1)} | Recall@3: {format_percentage(r3)} | MRR: {mrr:.3f} | Avg Speed: {avg_time:.1f}ms/query\n")

    if overall_metrics["total_cases"] > 0:
        print("=" * 60)
        print(" FINAL REPORT ")
        print("=" * 60)
        tc = overall_metrics["total_cases"]
        r1 = overall_metrics["hits_at_1"] / tc
        r3 = overall_metrics["hits_at_3"] / tc
        mrr = overall_metrics["sum_mrr"] / tc
        avg_time = overall_metrics["time_ms"] / tc
        
        print(f"Total Repositories Evaluated : {len([k for k in repo_datasets.keys() if os.path.exists(f'{k}_clone')])}")
        print(f"Total Test Cases Evaluated   : {tc}")
        print(f"Global Recall@1 (Top 1)      : {format_percentage(r1)}")
        print(f"Global Recall@3 (Top 3)      : {format_percentage(r3)}")
        print(f"Mean Reciprocal Rank (MRR)   : {mrr:.3f}")
        print(f"Average Speed Per Query      : {avg_time:.1f} ms")
        print("=" * 60)

if __name__ == "__main__":
    main()
