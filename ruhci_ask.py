#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
from ruhci.engine.core import RuhciEngine

def get_top_files_content(engine: RuhciEngine, query: str, top_n: int = 3) -> str:
    print(f"\n[Ruhci] Analyzing repository locally (0 API calls)...")
    results = engine.compile_context(query)
    
    if not results:
        return ""
        
    context_text = "Here are the most relevant files from the repository:\n\n"
    
    for i, res in enumerate(results[:top_n]):
        filepath = res['filepath']
        score = res['score']
        print(f"  [{i+1}] Selected: {filepath} (Score: {score:.3f})")
        
        full_path = os.path.join(engine.target_dir, filepath)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            try:
                with open(full_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            except Exception:
                content = "<unreadable binary or missing file>"
                
        context_text += f"--- FILE: {filepath} ---\n```python\n{content}\n```\n\n"
        
    return context_text

def execute_free_claude_code(query: str, context: str):
    """
    Executes free-claude-code by passing the context and query.
    Note: free-claude-code acts as a drop-in proxy for Anthropic's 'claude' CLI.
    """
    final_prompt = f"Context from Ruhci Engine:\n{context}\nUser Query: {query}"
    
    print("\n[Bridge] Forwarding highly-filtered context to free-claude-code...")
    
    # We use npx to ensure we're using the latest free-claude-code or locally installed claude
    # The actual claude CLI accepts `-p` for prompt. 
    
    try:
        # Since 'free-claude-code' wraps the official CLI, we try executing it.
        # Alternatively, we can use `npx -y free-claude-code` if it has its own binary.
        cmd = ["npx", "-y", "claude", "-p", final_prompt]
        print(f"[Bridge] Executing: {' '.join(cmd)}")
        
        # Subprocess call with shell=True on windows is sometimes needed for npx
        is_windows = sys.platform == "win32"
        subprocess.run(cmd, check=True, shell=is_windows)
    except Exception as e:
        print(f"\n[Error] Failed to execute free-claude-code: {e}")
        print("Please ensure you have Node.js installed and the CLI available.")
        print("Fallback: You can copy the context manually. Dumping to 'ruhci_output.txt'")
        with open("ruhci_output.txt", "w", encoding="utf-8") as f:
            f.write(final_prompt)

def main():
    parser = argparse.ArgumentParser(description="Ruhci CLI Bridge to free-claude-code")
    parser.add_argument("query", type=str, help="The query or task you want the AI to solve")
    parser.add_argument("--repo", type=str, default=".", help="Path to the repository")
    parser.add_argument("--top", type=int, default=3, help="Number of files to extract")
    parser.add_argument("--dry-run", action="store_true", help="Just print the context, do not execute AI")
    
    args = parser.parse_args()
    
    # Need to make sure Ruhci can be imported from current dir
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    engine = RuhciEngine(args.repo)
    context = get_top_files_content(engine, args.query, args.top)
    
    if not context:
        print("[Ruhci] No Python files found or indexed.")
        return
        
    if args.dry_run:
        print("\n--- DRY RUN ---")
        print("Context ready. Length:", len(context))
        with open("ruhci_output.txt", "w", encoding="utf-8") as f:
            f.write(f"Query: {args.query}\n\n{context}")
        print("Dumped to ruhci_output.txt")
    else:
        execute_free_claude_code(args.query, context)

if __name__ == "__main__":
    main()
