import sys
from loader import load_detections
from analyser import get_coverage_summary, get_coverage_by_tactic, get_coverage_gaps

def print_report(df):
    summary = get_coverage_summary(df)
    by_tactic = get_coverage_by_tactic(df)
    gaps = get_coverage_gaps(df)

    print("\n=== MITRE ATT&CK Coverage Report ===\n")

    # Overall numbers
    print(f"Total Detections: {summary['total_detections']}")
    print(f"Active Detections: {summary['active_detections']}")
    print(f"Total Techniques: {summary['total_techniques']}")
    print(f"Covered Techniques: {summary['covered_techniques']}")

    pct = summary['covered_techniques'] / summary['total_techniques'] * 100
    print(f"Coverage                    : {pct:.1f}%")

    # Coverage by tactic
    print("\n--- Coverage by Tactic ---\n")
    for _, row in by_tactic.iterrows():
        print(f" {row['tactic']}: {row['techniques_covered']} techniques covered")

    # Coverage gaps
    print("\n--- Coverage Gaps (Techniques with no active detection) ---\n")
    if gaps.empty:
        print("No gaps found.")
    else:
        for _, row in gaps.iterrows():
            print(f" {row['technique_id']:15} ({row['tactic']})")

    print()

def save_report(df, output_path):

    summary = get_coverage_summary(df)
    by_tactic = get_coverage_by_tactic(df)
    gaps = get_coverage_gaps(df)

    pct = summary['covered_techniques'] / summary['total_techniques'] * 100

    lines = []
    lines.append("=== MITRE ATT&CK Coverage Report ===\n")
    lines.append(f"Total detections in catalog : {summary['total_detections']}")
    lines.append(f"Active detections           : {summary['active_detections']}")
    lines.append(f"Techniques in catalog       : {summary['total_techniques']}")
    lines.append(f"Techniques with coverage    : {summary['covered_techniques']}")
    lines.append(f"Coverage                    : {pct:.1f}%")
    lines.append("\n--- Coverage by Tactic ---\n")

    for _, row in by_tactic.iterrows():
        lines.append(f"  {row['tactic']:<25} {row['techniques_covered']} technique(s) covered")

    lines.append("\n--- Coverage Gaps ---\n")
    if gaps.empty:
        lines.append("  No gaps found.")
    else:
        for _, row in gaps.iterrows():
            lines.append(f"  {row['technique_id']:<15} {row['tactic']}")

    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Report saved to {output_path}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/detections.csv"
    df = load_detections(path)
    print_report(df)
    save_report(df, "../reports/coverage_report.txt")