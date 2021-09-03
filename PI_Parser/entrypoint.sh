#!/bin/sh

echo "Waiting for SQS..."

while ! nc -z $RABBITHOSTNAME $RABBITPORTNUM; do
  sleep .1
done

echo "SQS started"


echo "Waiting for Database... "$DBHOST":"$DBPORT

while ! nc -z $DBHOST $DBPORT; do
  sleep 0.1
  echo "Trying "$DBHOST":"$DBPORT
done

echo "Database connected"

exec "$@"
