#!/bin/bash

DB_CLIENT=mariadb
DB_SERVER=mariadb
#DB_NAME='staging'
USER=root
EXISTS_CMD="SELECT * FROM information_schema.tables WHERE table_schema = '$DB_NAME' AND table_name = 'notes' LIMIT 1;"
DROP_CMD="DROP TABLE notes;"
CREATE_CMD="CREATE TABLE IF NOT EXISTS notes (id integer NOT NULL AUTO_INCREMENT, data text, ipaddress text, hostname text, secret boolean, PRIMARY KEY (id));"

# Check if table exists
EXISTS=$($DB_CLIENT -u $USER --password=$DB_ROOT_PWD -h $DB_SERVER -e "$EXISTS_CMD")
retVal=$?
if [ -z "$EXISTS" ]; then
    echo "Error: Table does not exists."
    echo "Attempting to create it."
    # Create it
    $DB_CLIENT -u $USER --password=$DB_ROOT_PWD -h $DB_SERVER -e "$CREATE_CMD" $DB_NAME
    if [ $retVal -ne 0 ]; then
        echo "Error: Creating the table failed"
        exit $retVal
    fi
else
    # If it does exist, delete it
    $DB_CLIENT -u $USER --password=$DB_ROOT_PWD -h $DB_SERVER -e "$DROP_CMD" $DB_NAME
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: Dropping the table failed."
        exit $retVal
    fi

    # Recreate it with empty values
    $DB_CLIENT -u $USER --password=$DB_ROOT_PWD -h $DB_SERVER -e "$CREATE_CMD" $DB_NAME
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: Creating the table failed"
        exit $retVal
    fi
fi

echo "Success!"
exit 0
