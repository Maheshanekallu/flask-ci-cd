import os
from flask import Flask

app = Flask(__name__)

# Load secret key and debug mode from environment variables with defaults
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # fallback if env var missing
app.debug = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

# Import routes after app creation so they can use `app`
from . import routes
