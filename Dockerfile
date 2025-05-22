# # Use official Python image
# FROM python:3.8-slim

# # Set working directory
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # Copy app code
# COPY . .

# # Expose port
# EXPOSE 5000

# # Run the app
# CMD ["python", "app.py"]


# Use Python base image
FROM python:3.8-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into container's working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose default Render port (Render maps this dynamically)
EXPOSE 10000

# Start using Gunicorn (expand $PORT properly using sh -c)
# CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]
CMD ["python", "app.py"]
