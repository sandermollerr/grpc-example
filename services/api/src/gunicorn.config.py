# Define application module path
wsgi_app = "src.main:app"

# Bind application to available ip address
bind = "0.0.0.0:80"

# Worker count
workers = 2

# Force Gunicorn to use Uvicorn workers
worker_class = "uvicorn.workers.UvicornWorker"

# Preload whole application once before forking it for workers
preload_app = True

# Write application logs to stdout
accesslog = "-"
errorlog = "-"
