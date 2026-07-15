import ast
from typing import List, Dict, Any

class PythonASTSource:
    def _get_decorator_name(self, decorator) -> str:
        if isinstance(decorator, ast.Name):
            return decorator.id
        elif isinstance(decorator, ast.Call):
            return self._get_decorator_name(decorator.func)
        elif isinstance(decorator, ast.Attribute):
            return f"{self._get_decorator_name(decorator.value)}.{decorator.attr}"
        return "unknown_decorator"

    def _get_annotation(self, annotation) -> str:
        if isinstance(annotation, ast.Name):
            return annotation.id
        elif isinstance(annotation, ast.Subscript):
            return f"{self._get_annotation(annotation.value)}[{self._get_annotation(annotation.slice)}]"
        elif isinstance(annotation, ast.Constant):
            return str(annotation.value)
        return "Any"

    def parse(self, file_path: str, content: str) -> List[Dict[str, Any]]:
        raw_records = []
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        raw_records.append({
                            "type": "import",
                            "name": alias.name,
                            "path": file_path,
                            "line": node.lineno
                        })
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        for alias in node.names:
                            raw_records.append({
                                "type": "import_from",
                                "module": node.module,
                                "name": alias.name,
                                "path": file_path,
                                "line": node.lineno
                            })
                elif isinstance(node, ast.ClassDef):
                    bases = [self._get_annotation(b) for b in node.bases]
                    decorators = [self._get_decorator_name(d) for d in node.decorator_list]
                    raw_records.append({
                        "type": "class",
                        "name": node.name,
                        "bases": bases,
                        "decorators": decorators,
                        "path": file_path,
                        "line": node.lineno
                    })
                elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                    decorators = [self._get_decorator_name(d) for d in node.decorator_list]
                    returns = self._get_annotation(node.returns) if node.returns else "None"
                    
                    # Extract calls inside function
                    calls = []
                    for child in ast.walk(node):
                        if isinstance(child, ast.Call):
                            if isinstance(child.func, ast.Name):
                                calls.append(child.func.id)
                            elif isinstance(child.func, ast.Attribute):
                                calls.append(child.func.attr)

                    raw_records.append({
                        "type": "function",
                        "name": node.name,
                        "decorators": decorators,
                        "returns": returns,
                        "calls": calls,
                        "path": file_path,
                        "line": node.lineno
                    })
        except SyntaxError:
            pass
        return raw_records