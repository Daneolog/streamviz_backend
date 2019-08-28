# StreamViz I: Backend

## Setting up database

To get the database setup, MySQL Workbench needs to be downloaded and installed ([link here](https://dev.mysql.com/downloads/workbench/)).

1. Create a **schema** named streamviz
2. Run `clean.py` to create the stream table

## Setup and running things

To get the server running on a local machine, some dependencies need to be installed

**1. Create a pip virtual environment (only needs to be done once per machine)**

- `python -m venv venv` to make a virtual environment named venv (optimal name)
- `source venv/Scripts/activate` if on Windows or

  `source venv/bin/activate` if on Linux

- `pip install -r requirements.txt`

**2. Run the app**

- `python app.py`
- Server will run on `localhost:5000`
