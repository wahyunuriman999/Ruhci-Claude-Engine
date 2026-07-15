# Reproducibility Guide

To ensure scientific validity, all benchmarks and results from the Ruhci Phase 2 trial are strictly reproducible. Follow these steps to execute the benchmark pipeline locally.

## 1. Clone Repository
```bash
git clone https://github.com/wahyunuriman999/Ruhci-Claude-Engine.git
cd Ruhci-Claude-Engine
```

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 3. Setup Benchmark Repositories
The benchmark relies on gold-standard datasets for 5 targets.
```bash
python benchmark/setup_repos.py --targets fastapi requests flask django sqlalchemy
```

## 4. Run Benchmark
Execute the Phase 2 Real API Simulation suite. This will run 25 blind evaluation tasks.
```bash
python benchmark/claude_trial_phase2.py
```

## 5. Generate Report
The script will output the `RUHCI FINAL TRIAL REPORT (PHASE 2: REAL API EXECUTION)` directly to your terminal. Compare your results against the official `scientific_report_v1.0.md`.\n