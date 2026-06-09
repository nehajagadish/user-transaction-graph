from database import driver

with driver.session() as session:

    queries = [

        """
        MATCH (a:User),(b:User)
        WHERE a.email = b.email
        AND a.user_id < b.user_id
        MERGE (a)-[:SHARED_EMAIL]->(b)
        """,

        """
        MATCH (a:User),(b:User)
        WHERE a.phone = b.phone
        AND a.user_id < b.user_id
        MERGE (a)-[:SHARED_PHONE]->(b)
        """,

        """
        MATCH (a:User),(b:User)
        WHERE a.address = b.address
        AND a.user_id < b.user_id
        MERGE (a)-[:SHARED_ADDRESS]->(b)
        """,

        """
        MATCH (a:User),(b:User)
        WHERE a.payment_method = b.payment_method
        AND a.user_id < b.user_id
        MERGE (a)-[:SHARED_PAYMENT]->(b)
        """
    ]

    for query in queries:
        print("Running query...")
        session.run(query)

print("Shared relationships created")