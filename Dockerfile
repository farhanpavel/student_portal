FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install Python dependencies
COPY django_app/requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project
COPY django_app/ /code/

# Expose port
EXPOSE 8000

# Run the application
CMD ["bash", "-c", "while ! nc -z db 3306; do sleep 1; done && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]