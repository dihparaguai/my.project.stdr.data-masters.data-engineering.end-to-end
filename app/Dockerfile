# Build Spark image with Python dependencies installed
FROM apache/spark:3.5.7

USER root

# Install pip for Python 3
RUN apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/spark-scripts

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

USER spark