# Backup Job Risk Scorer architecture

Scores backup jobs by age, failure count, encryption status, and protected workload tier.

```mermaid
flowchart LR
    N0["sample_backups.csv"]
    N1["backup_risk.py"]
    N2["risk score / classify"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
