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

if __name__ == "__main__":
        path = sys.argv[1] if len(sys.argv) > 1 else "data/detections.csv"
        df = load_detections(path)
        print_report(df)