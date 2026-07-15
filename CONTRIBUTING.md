# Contributing to Ruhci

First off, thank you for considering contributing to Ruhci! It's people like you that make Ruhci a world-class context intelligence engine for AI.

We welcome community contributions, particularly in exposing failures in our AST parsing, proposing improvements to our hybrid ranking engine, and extending support for new frameworks.

## 1. Where to Start
- **Did you find a bug?** Please submit it using our Bug Report issue template.
- **Do you want to request a feature?** Please use the Feature Request issue template.
- **Want to break our parser?** Head over to our `benchmark/community/` directory to learn how to submit "Failure Cases" so we can analyze them scientifically.

## 2. Setting Up Your Development Environment
1. Clone the repository: `git clone https://github.com/wahyunuriman999/Ruhci-Claude-Engine.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment and install dependencies: `pip install -r requirements.txt`

## 3. Pull Request Process
1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure your code lints and tests pass.
5. Issue that pull request using our Pull Request Template!

## 4. Code Style & Architecture Philosophy
Please remember the 4 golden rules of Ruhci's design philosophy (`docs/design_philosophy.md`) when contributing:
1. *Never send unnecessary files.*
2. *Never trust semantic similarity alone.*
3. *Never hide uncertainty.*
4. *Prefer deterministic evidence over probabilistic guessing.*

## 5. Community Validation Hub
If you are contributing an edge case or a benchmark test to the Community Hub:
1. Ensure your payload conforms to `benchmark/community/submit_template.json`.
2. Clearly explain *why* Ruhci failed to fetch the right context in your test.

Thank you for contributing to the future of deterministic AI tools!
