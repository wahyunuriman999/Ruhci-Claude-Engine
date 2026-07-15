import os

files_to_include = [
    'README.md',
    'ruhci/engine/core.py',
    'ruhci/ranking/hybrid_ranker.py',
    'ruhci/ranking/semantic.py',
    'ruhci_ask.py'
]

output = 'RUHCI_ARCHITECTURE_REVIEW.md'
with open(output, 'w', encoding='utf-8') as outfile:
    outfile.write('# Prompt untuk Claude\n')
    outfile.write('Silakan *copy-paste* seluruh isi file ini ke Claude (Web / Desktop App) untuk meminta feedback.\n\n')
    outfile.write('---\n\n')
    outfile.write('**PROMPT AWAL:**\n\n')
    outfile.write('"Halo Claude! Saya baru saja merancang dan membangun arsitektur mesin pencarian pintar bernama **Ruhci Engine** (Deterministic Context Intelligence Engine). Mesin ini dibangun murni dengan Python tanpa memanggil API LLM sama sekali. Tujuannya adalah memfilter codebase raksasa menjadi beberapa file paling relevan sebelum dikirim ke AI, untuk menghemat jutaan token dan mencegah halusinasi.\n\n')
    outfile.write('Arsitektur ini menggunakan perpaduan AST (Tree-sitter), Dependency Graph (NetworkX), dan TF-IDF murni (ContentAnalyzer) untuk menentukan ranking file. Saya juga mengimplementasikan mekanisme *Semantic Gate* untuk membunuh dominasi file utilitas yang sering di-import tapi tidak relevan secara konteks.\n\n')
    outfile.write('Tolong bertindak sebagai Principal Software Engineer. Baca kode inti dan README di bawah ini, berikan kritik tajam, review jujur terhadap logika Hybrid Ranker saya, dan apakah menurut Anda sistem ini cukup revolusioner dibandingkan dengan metode Vector RAG tradisional yang memakan memori besar."\n\n')
    outfile.write('---\n\n')
    outfile.write('## KODE SUMBER RUHCI\n\n')
    
    for fpath in files_to_include:
        if os.path.exists(fpath):
            outfile.write(f'### File: `{fpath}`\n')
            
            ext = 'python' if fpath.endswith('.py') else 'markdown'
            outfile.write(f'```{ext}\n')
            try:
                with open(fpath, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
            except Exception:
                pass
            outfile.write('\n```\n\n')
            
print(f"File {output} berhasil dibuat!")
