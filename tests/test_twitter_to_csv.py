import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import twitter_to_csv

def test_create_headers():
    token = "test_token"
    headers = twitter_to_csv.create_headers(token)
    assert headers["Authorization"] == f"Bearer {token}"

def test_save_and_load_json(tmp_path):
    data = {"test": "value"}
    test_file = tmp_path / "test.json"
    
    twitter_to_csv.save_to_json(data, filename=str(test_file))
    loaded_data = twitter_to_csv.load_from_json(filename=str(test_file))
    
    assert data == loaded_data

def test_save_to_csv(tmp_path):
    sample_data = {
        "data": [
            {
                "id": "1",
                "text": "Test tweet",
                "author_id": "123",
                "created_at": "2025-06-16T00:00:00Z"
            }
        ]
    }
    test_csv = tmp_path / "test.csv"
    twitter_to_csv.save_to_csv(sample_data, filename=str(test_csv))
    
    assert test_csv.exists()
    with open(test_csv) as f:
        content = f.read()
        assert "Test tweet" in content
