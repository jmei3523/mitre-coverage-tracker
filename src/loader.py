import pandas as pd

REQUIRED_COLUMNS = {"detection_id", "name", "technique_id", "tactic", "platform", "severity", "status"}

# Takes the path to our detections CSV file and loads it into a DataFrame
def load_detections(file_path):
    df = pd.read_csv(file_path)
    # Check if all required columns are present
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {missing}")
    
    #Normalize text fields so casing and whitespace don't cause issues
    df["technique_id"] = df["technique_id"].str.strip().str.upper()
    df["status"] = df["status"].str.strip().str.title()
    df["platform"] = df["platform"].str.strip().str.title()
    df["tactic"] = df["tactic"].str.strip().str.title()
    
    return df

