# Use a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the project directory to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn  # Install Gunicorn for production use

# Expose the port that the app will run on
EXPOSE 5000

# Command to run the application using Gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
