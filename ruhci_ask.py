#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
from ruhci.engine.core import RuhciEngine

def get_top_files_content(engine: RuhciEngine, query: str, top_n: int = 3, explain: bool = False) -> str:
    print(f"\n[Ruhci] Analyzing repository locally (0 API calls)...")
    results = engine.compile_context(query)
    
    if not results:
        return ""
        
    context_text = "Here are the most relevant files from the repository:\n\n"
    
    valid_count = 0
    for i, res in enumerate(results):
        if valid_count >= top_n:
            break
            
        filepath = res['filepath']
        score = res['score']
        
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
                
        # Issue #5: Check if file is essentially empty or just a scaffold
        lines = [line.strip() for line in content.split('\n') if line.strip() and not line.strip().startswith('#')]
        
        is_scaffold = False
        if len(lines) < 10:
            if any("NotImplementedError" in line or "pass" in line for line in lines):
                is_scaffold = True
                
        if not content.strip() or is_scaffold:
            print(f"  [Skip] Ignored scaffold/empty file: {filepath}")
            continue
            
        print(f"  [{valid_count+1}] Selected: {filepath} (Score: {score:.3f})")
        if explain:
            signals = res.get('signals', {})
            print(f"      -> Breakdown: {signals}")
            
        context_text += f"--- FILE: {filepath} ---\n```python\n{content}\n```\n\n"
        valid_count += 1
        
    return context_text

def execute_ai_agent(query: str, context: str, agent: str):
    """
    Executes the specified AI CLI proxy/agent by passing the context and query.
    Supports free-claude-code, ollama, or standard claude CLI.
    """
    final_prompt = f"Context from Ruhci Engine:\n{context}\nUser Query: {query}"
    
    print(f"\n[Bridge] Forwarding highly-filtered context to {agent}...")
    
    try:
        if agent == "free-claude-code":
            cmd = ["npx", "-y", "claude", "-p", final_prompt]
        elif agent == "ollama":
            # Just an example for Ollama using a generic run command
            cmd = ["ollama", "run", "llama3", final_prompt]
        else:
            # Fallback to standard claude or any custom command
            cmd = [agent, "-p", final_prompt]
            
        print(f"[Bridge] Executing: {' '.join(cmd)}")
        is_windows = sys.platform == "win32"
        subprocess.run(cmd, check=True, shell=is_windows)
    except Exception as e:
        print(f"\n[Error] Failed to execute agent ({agent}): {e}")
        print("Fallback: You can copy the context manually. Dumping to 'ruhci_output.txt'")
        with open("ruhci_output.txt", "w", encoding="utf-8") as f:
            f.write(final_prompt)

def main():
    parser = argparse.ArgumentParser(description="Ruhci CLI Bridge to Free AI Agents")
    parser.add_argument("query", type=str, help="The query or task you want the AI to solve")
    parser.add_argument("--repo", type=str, default=".", help="Path to the repository")
    parser.add_argument("--top", type=int, default=3, help="Number of files to extract")
    parser.add_argument("--agent", type=str, default="claude", help="The AI CLI to route to (claude, ollama, free-claude-code)")
    parser.add_argument("--dry-run", action="store_true", help="Just print the context, do not execute AI")
    parser.add_argument("--explain", action="store_true", help="Print scoring breakdown for selected files")
    
    args = parser.parse_args()
    
    # Need to make sure Ruhci can be imported from current dir
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    engine = RuhciEngine(args.repo)
    context = get_top_files_content(engine, args.query, args.top, explain=args.explain)
    
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
        execute_ai_agent(args.query, context, args.agent)

if __name__ == "__main__":
    main()
