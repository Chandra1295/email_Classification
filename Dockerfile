# Use a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the project directory to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]

