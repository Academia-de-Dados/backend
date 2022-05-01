from os import getenv
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
PATH_DOTENV = BASE_DIR / '.env'
load_dotenv(PATH_DOTENV)

bind = f'0.0.0.0:{getenv("GUNICORN_PORT", "8000")}'

timeout = getenv('GUNICORN_TIMEOUT', '1000')
threads = getenv('GUNICORN_THREADS', '10')

workers = getenv('GUNICORN_WORKERS', '10')
worker_class = getenv('GUNICORN_WORKER_CLASS', 'uvicorn.workers.UvicornWorker')

loglevel = getenv('GUNICORN_LOG_LEVEL', 'info')
errorlog = getenv('GUNICORN_ERROR_LOG', '-')
accesslog = getenv('GUNICORN_ACCESS_LOG', '-')
