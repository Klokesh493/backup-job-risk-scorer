# Backup Job Risk Scorer architecture

Scores backup jobs by age, failure count, encryption status, and protected workload tier.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
