from flask import Flask, request, redirect, render_template_string, url_for, jsonify
import os
import requests

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret")

# In-memory "database"
items = []

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask CRUD</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h2>CRUD Application</h2>
            <form method="POST" action="/add" class="mb-3">
                <div class="input-group">
                    <input type="text" name="item" class="form-control" placeholder="Enter new item" required>
                    <button class="btn btn-primary" type="submit">Add</button>
                </div>
            </form>
            <ul class="list-group">
                {% for item in items %}
                    {% set i = loop.index0 %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <form method="POST" action="/update/{{ i }}" class="d-flex flex-grow-1 me-2">
                        <input type="text" name="item" value="{{ item }}" class="form-control me-2">
                        <button class="btn btn-warning btn-sm" type="submit">Update</button>
                    </form>
                    <form method="POST" action="/delete/{{ i }}">
                        <button class="btn btn-danger btn-sm" type="submit">Delete</button>
                    </form>
                </li>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, items=items)

@app.route("/add", methods=["POST"])
def add_item():
    item = request.form["item"]
    items.append(item)
    return redirect(url_for("index"))

@app.route("/update/<int:index>", methods=["POST"])
def update_item(index):
    items[index] = request.form["item"]
    return redirect(url_for("index"))

@app.route("/delete/<int:index>", methods=["POST"])
def delete_item(index):
    items.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
