import os
from indexer.ast_parser import ASTParser
from indexer.graph_builder import DependencyGraph
from ruhci.engine.candidate.selector import CandidateSelector
from ruhci.ranking.hybrid_ranker import HybridRankerV02

class RuhciEngine:
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.ranker = HybridRankerV02()

    def compile_context(self, query: str) -> list[dict]:
        all_files = []
        for root, dirs, files in os.walk(self.target_dir):
            if any(ignored in root for ignored in ['venv', '.git', '__pycache__', 'node_modules', 'scratch']):
                continue
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file).replace('\\', '/')
                    if filepath.startswith('./'):
                        filepath = filepath[2:]
                    all_files.append(filepath)

        parser = ASTParser()
        metadatas = []
        metadata_index = {}
        for f in all_files:
            meta = parser.parse_python_file(f)
            metadatas.append(meta)
            metadata_index[f] = meta

        graph = DependencyGraph()
        graph.build_from_metadata(metadatas)

        selector = CandidateSelector()
        candidates = selector.select(query, all_files, graph=graph, max_candidates=50)

        results = self.ranker.rank(query, candidates, metadata_index, graph)
        
        formatted_results = []
        for r in results:
            formatted_results.append({
                'filepath': r['file'],
                'score': r['score'],
                'signals': r.get('signals', {})
            })
        return formatted_results
