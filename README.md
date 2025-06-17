# 🐦 Twitter to Snowflake Data Pipeline

This is an end-to-end real-world data pipeline that:

1. Fetches tweets from Twitter API (v2)
2. Saves them as CSV files
3. Uploads the CSVs to Snowflake
4. Orchestrates everything using Apache Airflow

---

## 🚀 Technologies Used

- **Python** 🐍
- **Snowflake** ❄️
- **Apache Airflow** 🛫
- **Git & GitHub**
- **Bash (Ubuntu via WSL2)**

---

## 📁 Project Structure

```bash
.
└── snowflake_twitter_pipeline
    ├── airflow/
    │   ├── airflow.cfg
    │   ├── airflow.db
    │   ├── dags/
    │   ├── logs/
    │   └── webserver_config.py
    ├── cached_tweets.json
    ├── requirements.txt
    ├── sql/
    │   ├── tweets_<timestamp>.csv
    ├── src/
    │   ├── __init__.py
    │   ├── load_to_snowflake.py
    │   └── twitter_to_csv.py
    ├── tests/
    │   └── test_twitter_to_csv.py
    └── venv/
```

---

## 🛠️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/snowflake_twitter_pipeline.git
cd snowflake_twitter_pipeline
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root folder and add your secrets:

```
TWITTER_BEARER_TOKEN=your_twitter_token
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
SNOWFLAKE_STAGE=your_internal_stage
```

> **Note:** `.env` is excluded from Git using `.gitignore`.

---

## 🌀 Running Apache Airflow

### Initialize Airflow DB

```bash
airflow db migrate
```

### Start Airflow

```bash
airflow scheduler
airflow webserver
```

Then visit: [http://localhost:8080](http://localhost:8080)

---

## ✅ Airflow DAG Tasks

- `fetch_tweets`: Fetches recent tweets from the Twitter API and saves them as CSVs.
- `load_to_snowflake`: Uploads those CSV files into a Snowflake table using the Python connector.

---

## 🧪 Testing

```bash
pytest tests/
```

Tests are written using `pytest` to validate the tweet-fetching and transformation logic.

---

## 🔒 Security

- All sensitive keys are stored in a `.env` file.
- `.gitignore` ensures no credentials are pushed to GitHub.

---

## 👩‍💻 Author

**Priya A**  
Snowflake Data Engineer

---

## ⭐️ Give it a Star

If you find this project helpful, feel free to ⭐️ the repo to support the author!
