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

## Business problem

An operator reviewing multiple backup jobs needs to prioritize stale or repeatedly failed protection for critical workloads.

## Project walkthrough

```mermaid
flowchart LR
    A["Backup job records"]
    B["Score age, failures, encryption, and tier"]
    C["Compare score to thresholds"]
    D["High or medium risk"]
    E["Low risk"]
    A --> B --> C
    C --> D
    C --> E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 backup_risk.py sample_backups.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
