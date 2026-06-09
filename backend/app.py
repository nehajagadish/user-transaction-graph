from fastapi import FastAPI, Query
from database import driver
from models import User, Transaction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="User Transaction Graph API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API Running"}


@app.get("/users")
def get_users(
    limit: int = Query(100),
    skip: int = Query(0),
    name: str | None = None
):
    with driver.session() as session:

        query = "MATCH (u:User) "

        if name:
            query += """
            WHERE toLower(u.name)
            CONTAINS toLower($name)
            """

        query += """
        RETURN u
        SKIP $skip
        LIMIT $limit
        """

        result = session.run(
            query,
            name=name,
            skip=skip,
            limit=limit
        )

        return [dict(record["u"]) for record in result]


@app.get("/transactions")
def get_transactions(
    limit: int = Query(100),
    skip: int = Query(0),
    min_amount: float | None = None
):
    with driver.session() as session:

        query = "MATCH (t:Transaction) "

        if min_amount is not None:
            query += """
            WHERE t.amount >= $min_amount
            """

        query += """
        RETURN t
        SKIP $skip
        LIMIT $limit
        """

        result = session.run(
            query,
            min_amount=min_amount,
            skip=skip,
            limit=limit
        )

        return [dict(record["t"]) for record in result]


@app.get("/relationships/user/{user_id}")
def get_user_relationships(user_id: str):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (u:User {user_id:$user_id})
            OPTIONAL MATCH (u)-[:SENT]->(t)

            RETURN
            u.user_id AS user,
            collect(t.transaction_id) AS transactions
            """,
            user_id=user_id
        )

        record = result.single()

        if record:
            return record.data()

        return {"error": "User not found"}


@app.get("/relationships/transaction/{transaction_id}")
def get_transaction_relationships(transaction_id: str):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (t:Transaction {
                transaction_id:$id
            })

            OPTIONAL MATCH
            (t)-[:RECEIVED_BY]->(u)

            RETURN
            t.transaction_id AS transaction,
            collect(u.user_id) AS users
            """,
            id=transaction_id
        )

        record = result.single()

        if record:
            return record.data()

        return {"error": "Transaction not found"}


@app.post("/users")
def create_user(user: User):

    with driver.session() as session:

        session.run(
            """
            CREATE (u:User {
                user_id:$user_id,
                name:$name,
                email:$email,
                phone:$phone,
                address:$address,
                payment_method:$payment_method
            })
            """,
            **user.dict()
        )

    return {
        "message": "User created",
        "user_id": user.user_id
    }


@app.post("/transactions")
def create_transaction(transaction: Transaction):

    with driver.session() as session:

        session.run(
            """
            CREATE (t:Transaction {
                transaction_id:$transaction_id,
                amount:$amount,
                ip_address:$ip_address,
                device_id:$device_id
            })
            """,
            transaction_id=transaction.transaction_id,
            amount=transaction.amount,
            ip_address=transaction.ip_address,
            device_id=transaction.device_id
        )

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
            **transaction.dict()
        )

        return {
        "message": "Transaction created",
        "transaction_id": transaction.transaction_id
    }


@app.get("/graph")
def get_graph():

    with driver.session() as session:

        result = session.run(
            """
            MATCH (u:User)-[:SENT]->(t:Transaction)

            RETURN
            u.user_id AS user_id,
            t.transaction_id AS transaction_id

            LIMIT 10
            """
        )

        elements = []
        added_nodes = set()

        for record in result:

            user = record["user_id"]
            tx = record["transaction_id"]

            if user not in added_nodes:

                elements.append({
                    "data": {
                        "id": user,
                        "label": user,
                        "type": "user"
                    }
                })

                added_nodes.add(user)

            if tx not in added_nodes:

                elements.append({
                    "data": {
                        "id": tx,
                        "label": tx,
                        "type": "transaction"
                    }
                })

                added_nodes.add(tx)

            elements.append({
                "data": {
                    "id": f"{user}-{tx}",
                    "source": user,
                    "target": tx,
                    "relationship": "sent"
                }
            })
            return elements
@app.get("/graph/user/{user_id}")
def get_user_graph(user_id: str):

    with driver.session() as session:

        result = session.run(
            """
            MATCH (u:User {user_id:$user_id})
            -[:SENT]->
            (t:Transaction)

            RETURN
            u.user_id AS user_id,
            t.transaction_id AS transaction_id

            LIMIT 20
            """,
            user_id=user_id
        )

        elements = []
        added_nodes = set()

        for record in result:

            user = record["user_id"]
            tx = record["transaction_id"]

            if user not in added_nodes:

                elements.append({
                    "data": {
                        "id": user,
                        "label": user,
                        "type": "user"
                    }
                })

                added_nodes.add(user)

            if tx not in added_nodes:

                elements.append({
                    "data": {
                        "id": tx,
                        "label": tx,
                        "type": "transaction"
                    }
                })

                added_nodes.add(tx)

            elements.append({
                "data": {
                    "id": f"{user}-{tx}",
                    "source": user,
                    "target": tx,
                    "relationship": "sent"
                }
            })

        
        return elements

        