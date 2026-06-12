from pathlib import Path
import pandas as pd
import sqlite3
import logging

# ----------------------------
# PATH SETUP (NO HARDCODING)
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# ----------------------------
# LOGGING SETUP
# ----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# LOAD DATA
# ----------------------------
def load_data():
    try:
        files = list(DATA_RAW.glob("*.csv"))

        if not files:
            raise FileNotFoundError("No CSV files found in data/raw/")

        dfs = []

        for file in files:
            df = pd.read_csv(file)

            # Track source file
            df["source_file"] = file.name

            dfs.append(df)

        combined_df = pd.concat(dfs, ignore_index=True)

        logging.info(f"Loaded {len(files)} files")
        logging.info(f"Total rows: {len(combined_df)}")

        return combined_df

    except Exception as e:
        logging.error(f"Error in load_data: {e}")
        raise

# ----------------------------
# CLEAN DATA (FIXED HERE)
# ----------------------------
def clean_data(df):
    try:
        # Standardize column names
        df.columns = df.columns.str.lower().str.strip()

        # Remove duplicates
        df = df.drop_duplicates()

        # FIX: correct forward fill (NO fillna(method=))
        df = df.ffill()

        # Optional safety fill for remaining nulls
        df = df.bfill()

        # Convert date columns if exist
        for col in df.columns:
            if "date" in col:
                df[col] = pd.to_datetime(df[col], errors="coerce")

        logging.info("Data cleaned successfully")

        return df

    except Exception as e:
        logging.error(f"Error in clean_data: {e}")
        raise

# ----------------------------
# SAVE PROCESSED CSV
# ----------------------------
def save_processed(df):
    output_file = DATA_PROCESSED / "cleaned_data.csv"
    df.to_csv(output_file, index=False)

    logging.info(f"Saved processed CSV -> {output_file}")

# ----------------------------
# SAVE TO SQLITE DB
# ----------------------------
def save_to_db(df):
    try:
        conn = sqlite3.connect(DB_PATH)

        # Main table
        df.to_sql("nav_data", conn, if_exists="replace", index=False)

        conn.close()

        logging.info(f"Saved data to SQLite DB -> {DB_PATH}")

    except Exception as e:
        logging.error(f"Database error: {e}")
        raise

# ----------------------------
# MAIN PIPELINE
# ----------------------------
def run_etl():
    logging.info("ETL Pipeline started")

    df = load_data()
    df = clean_data(df)

    save_processed(df)
    save_to_db(df)

    logging.info("ETL Pipeline completed successfully")

# ----------------------------
# ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    run_etl()