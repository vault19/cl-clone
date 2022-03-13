import os
import multiprocessing

bind = "127.0.0.1:" + os.getenv("GUNICORN_PORT", "8000"),
# bind = "unix:/run/kurzy-website/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1

proc_name = os.getenv("GUNICORN_PROC_NAME", "pomoc.vault19.eu")

accesslog = os.getenv("GUNICORN_PROC_NAME", "logs/gunicorn_access.log")
errorlog = os.getenv("GUNICORN_PROC_NAME", "logs/gunicorn_error.log")
