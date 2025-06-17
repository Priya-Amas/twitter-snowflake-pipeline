import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        role=os.getenv("SNOWFLAKE_ROLE"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

def upload_and_copy_to_table(file_path):
    conn = get_connection()
    cs = conn.cursor()
    try:
        file_name = os.path.basename(file_path)
        stage = 'my_twitter_stage'  # Set your stage name here
        put_cmd = f"PUT file://{file_path} @{stage} OVERWRITE = TRUE"
        print(f"Uploading {file_path} to stage...")
        cs.execute(put_cmd)

        print("Copying data into table...")
        copy_cmd = f"""
            COPY INTO tweets
            FROM @{stage}/{file_name}
            FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '\"' SKIP_HEADER = 1)
            ON_ERROR = 'CONTINUE'
        """
        cs.execute(copy_cmd)
        print("✅ Data loaded successfully.")

    finally:
        cs.close()
        conn.close()

def load_csv_to_snowflake():
    latest_csv = sorted([f for f in os.listdir("./sql") if f.endswith(".csv")])[-1]
    full_path = os.path.join("./sql", latest_csv)
    upload_and_copy_to_table(full_path)
