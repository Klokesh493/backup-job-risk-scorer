# Backup Job Risk Scorer walkthrough

## Business problem

An operator reviewing multiple backup jobs needs to prioritize stale or repeatedly failed protection for critical workloads.

## Reproduce the workflow

Run `python3 backup_risk.py sample_backups.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
crm-db high 12
wiki low 0
```

The sample supplies these fields. `job`, `tier`, `hours_since_success`, `failures_24h`, `encrypted`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
