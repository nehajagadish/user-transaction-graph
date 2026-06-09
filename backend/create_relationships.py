from database import driver
import csv

session = driver.session()

print("Creating transaction links...")

with open(
    "transactions.csv",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    count = 0

    for row in reader:

        session.run(
            """
            MATCH (s:User {user_id:$sender})
            MATCH (r:User {user_id:$receiver})
            MATCH (t:Transaction {
                transaction_id:$transaction_id
            })

            MERGE (s)-[:SENT]->(t)
            MERGE (t)-[:RECEIVED_BY]->(r)
            """,
            **row
        )

        count += 1

        if count % 1000 == 0:
            print(count)

print("Done")