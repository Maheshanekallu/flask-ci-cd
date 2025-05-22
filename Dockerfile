# Use an official Python image
FROM python:3.8-slim

# Set working directory to the current directory (optional)
WORKDIR /home/mahesh/CICD/flask_app

# Copy current directory contents into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (Render uses dynamic ports)
EXPOSE 10000

# Start the app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
