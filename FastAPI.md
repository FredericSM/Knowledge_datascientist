# Uvicorn Quick Guide

Run a FastAPI app with:
```bash
uvicorn module:app [options]
```
-module = Python file name (without .py)
-app = FastAPI instance inside the file

Useful options:
```markdown
--reload → auto-reload on code changes (dev)
--host 0.0.0.0 → listen on all interfaces (Docker, server, LAN)
--port 8080 → set custom port (default = 8000)
--workers 4 → multiple worker processes (prod)
--proxy-headers → trust proxy headers (e.g. X-Forwarded-For)
--log-level info → logging level (debug, info, warning, …)
```
Examples:
```bash
uvicorn app:app --reload
uvicorn app:app --host 0.0.0.0 --port 8080
uvicorn app:app --workers 4 --host 0.0.0.0 --port 8000
```