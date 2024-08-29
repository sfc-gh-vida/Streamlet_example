# Streamlit App with Snowflake Integration

This repository contains a Streamlit app that integrates with Snowflake to display and manage data. The setup includes creating a virtual environment, installing necessary dependencies, and using SnowSQL for database operations.

## Table of Contents
- [Setup](#setup)
  - [1. Create a Virtual Environment](#1-create-a-virtual-environment)
  - [2. Install Python and Streamlit](#2-install-python-and-streamlit)
  - [3. Set Up Snowflake Connector and SnowSQL](#3-set-up-snowflake-connector-and-snowsql)
  - [4. Create Snowflake Database, Schema, and Table](#4-create-snowflake-database-schema-and-table)
  - [5. Running the Streamlit App](#5-running-the-streamlit-app)
- [Usage](#usage)
- [Common Commands](#common-commands)

## Setup

### 1. Create a Virtual Environment

1. Ensure you have Python installed. You can check by running:

    ```bash
    python3 --version
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

    - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

### 2. Install Python and Streamlit

1. Install the required Python packages:

    ```bash
    pip install streamlit pandas
    ```

2. Add these dependencies to `requirements.txt`:

    ```text
    streamlit
    pandas
    snowflake-connector-python
    python-dotenv
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### 3. Set Up Snowflake Connector and SnowSQL

1. **Install SnowSQL** (for macOS using Homebrew):

    ```bash
    brew install --cask snowflake-snowsql
    ```

2. Verify the installation:

    ```bash
    snowsql --version
    ```

3. **Connect to Snowflake** using SnowSQL:

    ```bash
    snowsql -a <account_name> -u <username> -d <database_name> -s <schema_name>
    ```

4. Create a `.env` file in your project root to store Snowflake credentials:

    ```plaintext
    SNOWFLAKE_USER=your_username
    SNOWFLAKE_PASSWORD=your_password
    SNOWFLAKE_ACCOUNT=your_account
    SNOWFLAKE_WAREHOUSE=your_warehouse
    SNOWFLAKE_DATABASE=your_database
    SNOWFLAKE_SCHEMA=your_schema
    ```

### 4. Create Snowflake Database, Schema, and Table

1. **Create a Database**:

    Run the following command in SnowSQL to create a new database:

    ```sql
    CREATE DATABASE test_db;
    ```

2. **Create a Schema**:

    After creating the database, create a schema within that database:

    ```sql
    USE DATABASE test_db;
    CREATE SCHEMA my_schema;
    ```

3. **Create a Table**:

    Now create a table within the schema to store user data:

    ```sql
    USE SCHEMA vida_schema;
    CREATE TABLE user (
        id INTEGER,
        name STRING,
        created_on TIMESTAMP
    );
    ```

4. **Insert Initial Data**:

    Optionally, insert some initial data into the `user` table:

    ```sql
    INSERT INTO user (id, name, created_on) VALUES
    (1, 'Alice', CURRENT_TIMESTAMP),
    (2, 'Bob', CURRENT_TIMESTAMP),
    (3, 'Kenneth', CURRENT_TIMESTAMP);
    ```

### 5. Running the Streamlit App

1. To start the Streamlit app, run:

    ```bash
    streamlit run app.py
    ```

2. Open your browser to `http://localhost:8501` to see the app.

## Usage

- The app connects to a Snowflake database and displays data from a `user` table.
- Users can add new entries to the `user` table via a form in the Streamlit app.
- The app uses a `.env` file to securely store Snowflake credentials.

## Common Commands

- **Activate virtual environment**:

    ```bash
    source venv/bin/activate
    ```

- **Deactivate virtual environment**:

    ```bash
    deactivate
    ```

- **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

- **Run Streamlit app**:

    ```bash
    streamlit run app.py
    ```

- **Connect to Snowflake with SnowSQL**:

    ```bash
    snowsql -a <account_name> -u <username> -d <database_name> -s <schema_name>
    ```

---

This `README.md` file documents the setup and usage of the Streamlit app with Snowflake integration. It covers everything from setting up a virtual environment and connecting to Snowflake, to creating the necessary database, schema, and table. :)

