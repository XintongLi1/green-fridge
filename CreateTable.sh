curl --request GET \
  --url https://${ASTRA_CLUSTER_ID}-${ASTRA_CLUSTER_REGION}.apps.astra.datastax.com/api/rest/v2/schemas/keyspaces \
  --header 'accept: application/json' \
 # --header 'x-cassandra-request-id: {unique-UUID}' \
  --header "x-cassandra-token: ${ASTRA_AUTHORIZATION_TOKEN}"
