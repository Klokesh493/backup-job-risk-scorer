# Skills and verification

## What this repository demonstrates

A backup review queue that scores each job using age since last success, failures in the last 24 hours, encryption status, and workload tier. The CLI returns both the score and the low, medium, or high classification.

## Reproduce the result

The CRM database scores 12 and is high risk. The wiki scores zero and is low risk. Reproduce the primary fixture with `python3 backup_risk.py sample_backups.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

A classification reflects the supplied export and policy weights. Verify actual recoverability with a restore drill.

Prioritize high-risk jobs by checking the most recent successful backup, protection status, and workload tier in the source export.

[backup_risk.py](../backup_risk.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
