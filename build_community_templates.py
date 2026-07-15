import os

base_dir = r"C:\Users\ROG G532 LV\.gemini\antigravity\scratch\Ruhci-Claude-Engine"
github_dir = os.path.join(base_dir, ".github")
issue_template_dir = os.path.join(github_dir, "ISSUE_TEMPLATE")

os.makedirs(issue_template_dir, exist_ok=True)

# 1. SECURITY.md (Root)
security_content = """# Security Policy

## Supported Versions

Currently, Ruhci is in Research Preview (v0.1). 
We actively review and apply security patches to the `main` branch.

| Version | Supported          |
| ------- | ------------------ |
| v0.1.x  | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within Ruhci, please do not disclose it publicly. 
Instead, please send an e-mail to **wahyunuriman999@gmail.com** or open a private security advisory on GitHub.

We will review all security reports and work to address them as quickly as possible.
"""
with open(os.path.join(base_dir, "SECURITY.md"), "w", encoding="utf-8") as f:
    f.write(security_content)

# 2. Bug Report Template
bug_report_content = """---
name: Bug report
about: Create a report to help us improve Ruhci
title: '[BUG] '
labels: 'bug'
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. See error '...'

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment (please complete the following information):**
 - OS: [e.g. Windows, Ubuntu, macOS]
 - Python Version [e.g. 3.10]
 - Ruhci Version [e.g. v0.1]
"""
with open(os.path.join(issue_template_dir, "bug_report.md"), "w", encoding="utf-8") as f:
    f.write(bug_report_content)

# 3. Feature Request Template
feature_request_content = """---
name: Feature request
about: Suggest an idea for Ruhci
title: '[FEATURE] '
labels: 'enhancement'
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.
"""
with open(os.path.join(issue_template_dir, "feature_request.md"), "w", encoding="utf-8") as f:
    f.write(feature_request_content)

# 4. Pull Request Template
pr_template_content = """## Description
Please include a summary of the change and which issue is fixed. Please also include relevant motivation and context.

Fixes # (issue)

## Type of change
Please delete options that are not relevant.
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] This change requires a documentation update

## How Has This Been Tested?
Please describe the tests that you ran to verify your changes.

## Checklist:
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] My changes generate no new warnings
"""
with open(os.path.join(github_dir, "PULL_REQUEST_TEMPLATE.md"), "w", encoding="utf-8") as f:
    f.write(pr_template_content)

print("Community templates created successfully!")
