from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

### recipe dataset password: recipes

import os
cloud_config= {
        'secure_connect_bundle': './secure-connect-virtual-fridge.zip'
}
auth_provider = PlainTextAuthProvider('green_fridge', 'bestfridgeforever')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")