# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 backup_risk.py sample_backups.csv
crm-db high 12
wiki low 0
test_critical_failing_backup_is_high_risk (test_backup_risk.BackupRiskTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
