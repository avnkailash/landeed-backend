# Dynamic Form Backend

The backend has been created using FastAPI to keep the overall setup and code simple.

## Prerequisites

1. Python - 3.12.2
2. Virtual Env

## Installation

1. Ensure python and virtual env are installed in your machine.
2. Create a virtual env to manage the project packages.

```
virtualenv -p python3.12 .venv
```

3. Activate the virtual environment

```
source .venv/bin/activate
```

4. Install the project dependencies

```
pip install -r requirements.txt
```

5. Start the backend instance

```
uvicorn app.main:app
```

The backend should be running on port 8000
