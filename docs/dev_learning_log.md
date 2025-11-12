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