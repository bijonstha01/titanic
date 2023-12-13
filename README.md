## API Endpoint

This project creates an API endpoint using the FastAPI framework in Python, SQLalchemy for database operations, and SQLite as the database. The API endpoint is accessible at [http://localhost:8000/titanic](http://localhost:8000/titanic).

### Steps to Run the API

1. Install the required libraries: pip install fastapi sqlalchemy[sqlite] pandas
2. Run the FastAPI application: uvicorn main:app --reload
3. Open your browser or use a tool like [httpie](https://httpie.io/) to test the API: http://localhost:8000/titanic

## Parsing UBO JSON

The attached ubo.json file is parsed using the provided Python script. The script uses the pandas library to flatten the nested JSON structure into a tabular data frame.

### Steps to Run UBO JSON Parser

1. Ensure you have Python installed.
2. Run the script: python main.py

The tabular data frame from the parsed UBO JSON will be printed in the console.
