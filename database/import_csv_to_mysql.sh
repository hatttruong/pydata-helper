#!/bin/sh
DATABASE="vnstock"
TBL_STOCK_PRICES="stock_prices"
TBL_SYMBOL_INFOS="symbol_infos"

stty -echo
printf "Please enter root user MySQL password: "
read rootpasswd
stty echo
printf "\n"
# echo "Password: $rootpasswd"


echo "1. Create $DATABASE database"
mysql -uroot -p${rootpasswd} -e "CREATE DATABASE IF NOT EXISTS ${DATABASE};"

echo "2. Create $TBL_SYMBOL_INFOS table"
mysql -uroot -p${rootpasswd} $DATABASE -e 'DROP TABLE IF EXISTS $TBL_SYMBOL_INFOS;'
mysql -uroot -p${rootpasswd} $DATABASE -e 'CREATE TABLE $TBL_SYMBOL_INFOS(
    symbol VARCHAR(10) NOT NULL,
    name VARCHAR(200),
    exchange VARCHAR(10),
    PRIMARY KEY (symbol)
);'

echo "3. Import data into $TBL_SYMBOL_INFOS table"
mysqlimport -uroot -p${rootpasswd} --verbose --local --fields-terminated-by=, --ignore-lines=1 $DATABASE $TBL_SYMBOL_INFOS.csv


echo "4. Create $TBL_STOCK_PRICES table"
mysql -uroot -p${rootpasswd} $DATABASE -e 'DROP TABLE IF EXISTS $TBL_STOCK_PRICES;'
mysql -uroot -p${rootpasswd} $DATABASE -e 'CREATE TABLE $TBL_STOCK_PRICES (
    symbol VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    open DECIMAL(9,2),
    high DECIMAL(9,2),
    low DECIMAL(9,2),
    close DECIMAL(9,2),
    volume INT,
    PRIMARY KEY (symbol, date)
);'


echo "5. Import data into $TBL_STOCK_PRICES table"
mysqlimport -uroot -p${rootpasswd} --verbose --local --fields-terminated-by=, --ignore-lines=1 $DATABASE $TBL_STOCK_PRICES.csv