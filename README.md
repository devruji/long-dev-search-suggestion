# long-dev-search-suggestion

## Prerequisites

- python 3.10 + (Based on Owner's Environment)

## Get Started

```bash
# Install libs
$ pip install -r requirements.txt
```

```bash
# Inital sqlite_db
$ flask db init
$ flask db migrate
$ flask db upgrade

# Load data to sqlite_db
$ python load_data.py

# Start server
$ python server.py
```

## Example search suggestions on UI
- open: localhost:5000/search
- ![image](https://user-images.githubusercontent.com/43924465/199404045-93a52064-040f-435f-8413-2bdc4291a7c7.png)

## Study from

- [How to Use Flask-SQLAlchemy With Flask Blueprints
  ](https://www.youtube.com/watch?v=WhwU1-DLeVw)
