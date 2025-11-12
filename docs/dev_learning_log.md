# Dev Learning Log

- **Continuous record of learnings, errors, and solutions during the project’s development.**

---

### 2025-11-11: Avoiding to restart the notebook when a module changes
*Context*: For testing custom modules, it was necessary to retart the nootebook, but the IDE sometimes stopped working, so I had to close and reopen it to keep working.

*Solution*: Implement the lib `importlib` to implement the method `importlib.reload(<module>)` 

*Learning*: The method `importlib.reload(<module>)` recharges the custom module, avoiding to restart the nootebook. But it only reload modules, if you have a class or function imported, the method can't reload it.

---

### 2025-11-11: How to transform string date into a `datetime` type
*Context*: I needed to send start and end date parameters to Yahoo Finance API in string formart. To get one day of data, is necessary to send current date as the start, and next date as the end.

*Solution*: Add one day to the date paremeter to get the end date correctly.

*Leaning*: The function parameter is a string, so to cast to `datetime` type, I used `datetime.strptime(<date_str>, "%Y-%m-%d")`. Then, to cast the date to string, I used `<date>.strftime("%Y-%m-%d")`.

---

### 2025-11-11: How Airflow (inside a container) and Spark (inside another container) find the script file (job):
*Context*: I was testing a DAG to verify if the test script started by Airflow would work, but it wasn't working.

*Error*: The script file path inside of Airflow and Spark containers are different.

*Solution*: Change the script file path in each container and in the local environment to a commom path.

*Learning*: Airflow works as a driver, it find the file and sends the job to Spark. Then, Spark needs to find the same file, using the path that Airflow has sent before.

---

### 2025-11-07: What's a `.dockerignore`:
*Context*: When building a Docker image, you can copy many files into its layers.

*Learning*: When you use a folder to build a Docker image, some files don't need to be copied. To avoid increasing the image weight, adding extra latency, or exposing sensitive data, you can list ignored files such as: 
- `*.pyc, *.pyo, *.pyd` (Python cache of compiled files)
- `*.db` (database files) 
- `*.log` (log files)
- `*.env` (environment variables files)
- `*.git`(Git repository data)
- `*.gitignore`(similar to `.dockerignore`, but used by Git)
