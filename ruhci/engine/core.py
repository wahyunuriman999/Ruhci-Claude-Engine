import os
from indexer.ast_parser import ASTParser
from indexer.graph_builder import DependencyGraph
from ruhci.engine.candidate.selector import CandidateSelector
from ruhci.ranking.hybrid_ranker import HybridRankerV02

class RuhciEngine:
    def __init__(self, target_dir: str, extensions: list = None):
        self.target_dir = target_dir
        self.extensions = extensions or [".py"]
        self.ranker = HybridRankerV02()

    def compile_context(self, query: str) -> list[dict]:
        all_files = []
        excluded_files = set(os.environ.get("RUHCI_EXCLUDE_FILES", "").split(","))
        for root, dirs, files in os.walk(self.target_dir):
            if any(ignored in root for ignored in ['venv', '.git', '__pycache__', 'node_modules', 'scratch']):
                continue
            for file in files:
                if any(file.endswith(ext) for ext in self.extensions) and file not in excluded_files:
                    filepath = os.path.join(root, file).replace('\\', '/')
                    if filepath.startswith('./'):
                        filepath = filepath[2:]
                    all_files.append(filepath)

        # Pre-cache all contents
        for f in all_files:
            # Full path handling in case target_dir is not '.'
            if os.path.isabs(f):
                full_path = f
            else:
                full_path = os.path.join(self.target_dir, f) if self.target_dir != '.' else f
            self.ranker.content_analyzer._read_file(full_path)
            # Create a reverse index mapping to avoid O(N*M) lookups later
            self.ranker.content_analyzer._path_index[f] = full_path

        cache_dir = os.path.join(self.target_dir, ".ruhci_cache") if self.target_dir != '.' else ".ruhci_cache"
        parser = ASTParser(cache_dir=cache_dir)
        metadatas = []
        metadata_index = {}
        for f in all_files:
            # We should pass full path if needed, but keeping original logic
            meta = parser.parse_python_file(f)
            metadatas.append(meta)
            metadata_index[f] = meta
        # Flush the mtime+size keyed cache once per run, not per file, to
        # avoid a disk write on every single parsed file.
        parser.save_cache()

        graph = DependencyGraph()
        graph.build_from_metadata(metadatas)

        selector = CandidateSelector()
        # Pass the pre-warmed analyzer to selector
        candidates = selector.select(query, all_files, graph=graph, analyzer=self.ranker.content_analyzer, max_candidates=50)

        results = self.ranker.rank(query, candidates, metadata_index, graph)
        
        formatted_results = []
        for r in results:
            formatted_results.append({
                'filepath': r['file'],
                'score': r['score'],
                'signals': r.get('signals', {})
            })
        return formatted_results
