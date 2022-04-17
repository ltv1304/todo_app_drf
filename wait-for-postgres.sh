#!/bin/sh
# wait-for-postgres.sh
set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=${POSTGRES_PASSWORD} psql -h "$host" -d "todoDB" -U ${POSTGRES_USER} -c '\q';>&2 echo "Postgres is unavailable - sleeping"
    do sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
