FROM python:3.11-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY simple_file_storage_api /app/simple_file_storage_api
COPY setup.py /app/setup.py

# Install package
RUN pip install -e .

# Run the application
CMD ["python", "-m", "simple_file_storage_api"]
