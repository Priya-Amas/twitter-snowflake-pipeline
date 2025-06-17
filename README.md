# 🐦 Twitter to Snowflake Data Pipeline

This is an end-to-end real-world data pipeline that:

1. Fetches tweets from Twitter API (v2)
2. Saves them as CSV
3. Uploads to Snowflake via Python
4. Orchestrates with Apache Airflow

---

## 🚀 Technologies Used

- Python 🐍
- Snowflake ❄️
- Airflow 🛫
- Git & GitHub
- Bash (Ubuntu WSL)

---

## 📁 Project Structure

(venv) priya@LAPTOP-J0SSV9L1:~/projects$ tree -L 3
.
└── snowflake_twitter_pipeline
    ├── airflow
    │   ├── airflow.cfg
    │   ├── airflow.db
    │   ├── dags
    │   ├── logs
    │   └── webserver_config.py
    ├── cached_tweets.json
    ├── requirements.txt
    ├── sql
    │   ├── tweets_20250616_203428.csv
    │   ├── tweets_20250616_203731.csv
    ├── src
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── load_to_snowflake.py
    │   └── twitter_to_csv.py
    ├── tests
    │   ├── __pycache__
    │   └── test_twitter_to_csv.py
    └── venv
        ├── bin
        ├── include
        ├── lib
        ├── lib64 -> lib
        ├── pyvenv.cfg
        └── share



---

## 🛠️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/snowflake_twitter_pipeline.git
   cd snowflake_twitter_pipeline

2.Create and activate virtualenv:

bash:

python3 -m venv venv
source venv/bin/activate

3.Install requirements:

bash:

pip install -r requirements.txt
Set your environment variables in .env file.

Run Airflow:

bash:

airflow db migrate
airflow scheduler
airflow webserver

✅ DAG Tasks
fetch_tweets: Gets tweets using Twitter API and saves as CSV

load_to_snowflake: Uploads CSV to Snowflake using Python connector

🔒 Security
Secrets like API keys and credentials are stored in .env and excluded from Git using .gitignore.

---


👩‍💻 Author
Priya A
Snowflake Data Engineer
