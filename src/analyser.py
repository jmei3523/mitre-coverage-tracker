# Analyses the loaded detections and produces coverage statistics

# Returns a summary dict with basic coverage numbers
def get_coverage_summary(df):

    # Only count detections that are actually deployed
    active = df[df["status"] == "Active"]

    # How many unique techniques do we have at least one active detection for
    covered_techniques = active["technique_id"].nunique()

    # Total unique techniques across all detections including inactive ones
    total_techniques = df["technique_id"].nunique()

    return {
        "total_detections": len(df),
        "active_detections": len(active),
        "total_techniques": total_techniques,
        "covered_techniques": covered_techniques,
    }

# Returns a dict showing how many techniques are covered per tatic
def get_coverage_by_tactic(df):
    active = df[df["status"] == "Active"]
    
    # Group active detections by tatic and count unique techniques in each coverage
    coverage = (
        active.groupby("tactic")["technique_id"]
        .nunique()
        .reset_index()
    )
    coverage.columns = ["tactic", "techniques_covered"]
    return coverage

# Returns techniques that have no active detection covering them
def get_coverage_gaps(df):
    active =df[df["status"] == "Active"]

    # All unique techniques that appear anywhere in the catalog
    all_techniques = df[["technique_id", "tactic"]].drop_duplicates()

    # Techniques that have at least one active detection
    covered = set(active["technique_id"].unique())

    # Keep only rows where technique is NOT in the covered set
    gaps = all_techniques[~all_techniques["technique_id"].isin(covered)]
    return gaps.reset_index(drop=True)

