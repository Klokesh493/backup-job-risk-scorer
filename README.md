# Backup Job Risk Scorer

Scores backup jobs by age, failure count, encryption status, and protected workload tier.

Focus: Backup-platform DevSecOps reliability.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 backup_risk.py sample_backups.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
