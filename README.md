# MITRE ATT&CK Coverage Tracker

A small Python CLI tool I built to practice detection engineering concepts.
It reads a CSV of detection rules, maps them to MITRE ATT&CK techniques, and
tells you where your coverage gaps are.

---

## What it does

- Reads a detection catalog from a CSV file
- Maps each detection to a MITRE ATT&CK technique and tactic
- Shows how many techniques have at least one active detection
- Breaks coverage down by tactic so you can see which attack phases are weak
- Lists techniques with no active detection (the gaps)
- Saves the report to the `reports/` folder

---

## Project structure

```
mitre-coverage-tracker/
├── data/
│   └── detections.csv       # sample detection catalog
├── reports/
│   └── coverage_report.txt  # generated report (gitignored in real use)
├── src/
│   ├── loader.py            # reads and validates the CSV
│   ├── analyser.py          # calculates coverage and finds gaps
│   └── main.py              # run this
├── requirements.txt
└── README.md
```

---

## How to run it

```bash
git clone https://github.com/YOUR_USERNAME/mitre-coverage-tracker.git
cd mitre-coverage-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd src
python main.py ../data/detections.csv
```

The report prints to the terminal and also saves to `reports/coverage_report.txt`.

---

## Detection catalog format

The CSV needs these columns:

| Column | Description | Example |
|---|---|---|
| `detection_id` | unique ID | DET-001 |
| `name` | rule name | PowerShell Encoded Command |
| `technique_id` | MITRE ATT&CK ID | T1059.001 |
| `tactic` | ATT&CK tactic | Execution |
| `platform` | Windows / Linux / Cloud | Windows |
| `severity` | High / Medium / Low | High |
| `status` | Active / Testing / Disabled | Active |

Only `Active` detections count toward coverage. Testing and Disabled ones show
up in the catalog but don't affect the numbers.

---

## Sample output

```
=== MITRE ATT&CK Coverage Report ===

Total detections in catalog : 15
Active detections           : 13
Techniques in catalog       : 11
Techniques with coverage    : 10
Coverage                    : 90.9%

--- Coverage by Tactic ---

  Execution                 2 technique(s) covered
  Persistence               4 technique(s) covered
  Discovery                 1 technique(s) covered
  ...

--- Coverage Gaps ---

  T1033           Discovery
```

---

## Limitations

- Coverage is only measured against what's in the local CSV, not the full ATT&CK matrix
- Doesn't check whether detections actually fire, just that they're marked Active
- No severity weighting — a low rule counts the same as a critical one
- Sample data is hand-crafted; real use would need a SIEM export

---

## What I want to add next in v1.2

- [ ] Pull the full ATT&CK technique list from MITRE's STIX data so gaps are measured against the real matrix
- [ ] JSON output for use with dashboards
- [ ] Severity weighting in coverage scoring
- [ ] Accept Sigma rule files as input instead of CSV
