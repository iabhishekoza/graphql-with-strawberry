This project uses Python. In order to build the project locally, run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

To start the server, from the root directory, run:

```bash
uvicorn main:app --reload
```

Right now, the server returns a simple "Hello World" message from `http://localhost:8000`.

The `final` branch of this repo contains the final stage of the course, with all of the steps and code completed! If you get stuck, you can refer to it and compare your code.