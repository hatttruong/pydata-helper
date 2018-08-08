# Mics Readme

**1. How to import data in csv format into MySql**

- `prepare_data.py`: prepare csv with file name is table name, field names is columns corresponding in MySql. In this example, I have 2 tables naming **symbol_infos** and **stock_prices**
- `import_csv_to_mysql.sh`: run this shell script to import data. Update these variables correctly:
```
DATABASE="vnstock"
TBL_STOCK_PRICES="stock_prices"
TBL_SYMBOL_INFOS="symbol_infos"
```
