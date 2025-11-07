FROM apache/airflow:2.11.0-python3.10

USER root

# Install OpenJDK 17 to run Spark jobs
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install additional Python dependencies (like pyspark, providers, etc.)
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt