# Base image
FROM python:3.11

# Avoid prompts during package installation (for example, tzdata installation asks for timezone input, which would block the build, so the installation will use default values)
ENV DEBIAN_FRONTEND=noninteractive

# Define Spark environment variables, to run Spark without writing full path every time
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Define Python interpreter for PySpark workers and driver (setting to python3 to match base image)
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# Install OpenJDK 21 (required by Spark), wget (to download Spark), tar (to extract Spark) and ca-certificates (to ensure HTTPS works correctly) 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless \ 
    wget \
    tar \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Define Java environment variables, needed for Spark finding Java installation to run correctly
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Download Apache Spark 3.5.7 (with Hadoop 3) using wget in /tmp/, tar to extract it, and install Spark into SPARK_HOME, remove /tmp/ file after installation
RUN wget "https://archive.apache.org/dist/spark/spark-3.5.7/spark-3.5.7-bin-hadoop3.tgz" -O /tmp/spark.tgz \
    && mkdir -p $SPARK_HOME \
    && tar -xzf /tmp/spark.tgz --strip-components=1 -C $SPARK_HOME \
    && rm /tmp/spark.tgz

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files to the container (uncomment when needed to reproduce full app environment)
# COPY . /opt/app