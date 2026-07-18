import csv
import sys


def risk_score(row):
    score = int(row["hours_since_success"]) // 12 + int(row["failures_24h"]) * 3
    if row["encrypted"].lower() != "yes":
        score += 5
    if row["tier"].lower() == "critical":
        score += 4
    return score


def classify(row):
    score = risk_score(row)
    return "high" if score >= 10 else "medium" if score >= 5 else "low"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['job']} {classify(row)} {risk_score(row)}")


if __name__ == "__main__":
    main(sys.argv[1])
