from app import app
import os

if __name__ == "__main__":
    # Optionally override debug here based on env or leave as set in __init__.py
    debug_mode = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    app.run(debug=debug_mode)