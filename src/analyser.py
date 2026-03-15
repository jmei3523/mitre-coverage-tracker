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