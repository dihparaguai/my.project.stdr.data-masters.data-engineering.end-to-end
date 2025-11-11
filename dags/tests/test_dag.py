from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

from jobs.tests.test_pandas import create_and_show_df


with DAG(
    dag_id="python_operator_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    
    pandas_task = PythonOperator(
        task_id="pandas_task",
        python_callable=create_and_show_df
    )

    pandas_task


with DAG(
    dag_id="spark_operator_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    
    spark_task = SparkSubmitOperator(
        task_id='spark_task',
        application='/opt/jobs/tests/test_spark.py',
        conn_id="spark_default",
        verbose=True
    )

    spark_task
