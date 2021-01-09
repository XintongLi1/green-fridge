curl --request POST \
  --url https://$ASTRA_DB_ID-$ASTRA_DB_REGION.apps.astra.datastax.com/api/rest/v2/namespaces/$ASTRA_DB_KEYSPACE/collections/hello_docs \
  -H "X-Cassandra-Token: $ASTRA_AUTHORIZATION_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "unique_id",
    "other": "This is nonsensical stuff."
  }'
