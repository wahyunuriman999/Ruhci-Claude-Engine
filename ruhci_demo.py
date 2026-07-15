import os
import sys
from indexer.ast_parser import ASTParser
from indexer.graph_builder import DependencyGraph
from ruhci.engine.candidate.selector import CandidateSelector
from ruhci.ranking.hybrid_ranker import HybridRankerV01

def main():
    print("Initializing Ruhci Demo Engine [Functional Research Preview]...")
    target_repo = "."
    query = "implement recursive AST traversal and rewrite hybrid ranker logic"
    
    print(f"\n[Target Repository]: {target_repo} (Self-scan)")
    print(f"[Query]: {query}")
    
    print("\n[+] Executing Ruhci Intelligence Pipeline...")
    
    # 1. Scan files
    print(" -> Scanning Python files...")
    all_files = []
    for root, dirs, files in os.walk(target_repo):
        # Exclude common noisy directories
        if any(ignored in root for ignored in ["venv", ".git", "__pycache__", "node_modules", "scratch"]):
            continue
        for file in files:
            if file.endswith(".py"):
                # Use forward slashes for consistency
                filepath = os.path.join(root, file).replace('\\', '/')
                if filepath.startswith("./"):
                    filepath = filepath[2:]
                all_files.append(filepath)
                
    # 2. AST Parse
    print(f" -> Parsing AST and extracting symbols for {len(all_files)} files...")
    parser = ASTParser()
    metadatas = []
    metadata_index = {}
    for f in all_files:
        meta = parser.parse_python_file(f)
        metadatas.append(meta)
        metadata_index[f] = meta
        
    # 3. Graph
    print(" -> Constructing Repository Dependency Graph...")
    graph = DependencyGraph()
    graph.build_from_metadata(metadatas)
    
    # 4. Selector
    print(f" -> Filtering {len(all_files)} Candidates...")
    selector = CandidateSelector()
    candidates = selector.select(query, all_files, max_candidates=50)
    print(f"    Selected {len(candidates)} candidates for deep ranking.")
    
    # 5. Ranker
    print(" -> Executing Hybrid Ranking Engine (Symbol + Dependency + Semantic)...")
    ranker = HybridRankerV01()
    results = ranker.rank(query, candidates, metadata_index, graph)
    
    print("\n==================================================")
    print(" RUHCI OPTIMIZED CONTEXT RESULTS (REAL EXECUTION)")
    print("==================================================")
    print("Selected Evidence Files:")
    if not results:
        print(" [!] No files found matching the criteria.")
        
    for i, res in enumerate(results[:5]):
        print(f" [{i+1}] {res['file']} (Score: {res['score']:.4f})")
        print(f"      Signals: Symbol({res['signals']['symbol']:.2f}) Dep({res['signals']['dependency']:.2f}) Sem({res['signals']['semantic']:.2f})")
        
    print("\n[System] Context successfully compiled. Ready for LLM ingestion.")

if __name__ == "__main__":
    main()
