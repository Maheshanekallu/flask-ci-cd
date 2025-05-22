from flask import Flask
app = Flask(_name_)
import os

secret_key = os.getenv('SECRET_KEY')
debug_mode = os.getenv('DEBUG')
app = Flask(_name_)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def hello():
    return "Hello from Flask CI/CD!"
@app.route('/health')
def health():
    return 'OK', 200

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)