# Spark to Oracle Data Pipeline

This project demonstrates a data pipeline that extracts data from a CSV file and loads it into an Oracle database table using Apache Spark.

## Prerequisites

- Apache Spark
- Python 3
- Oracle JDBC Driver
- Oracle Database

## Setup

1. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

2. **Download the Oracle JDBC Driver:**

    Download the `ojdbc8.jar` file and place it in a known directory. Update the path in the `load_data.py` script.

3. **Update the script:**

    Update the Oracle connection details in `scripts/load_data.py` with your database credentials and connection string.

## Running the Pipeline

Navigate to the `scripts` directory and run the script:

```sh
cd scripts
python load_data.py
