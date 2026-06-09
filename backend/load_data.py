from database import driver
import csv

session = driver.session()

# ------------------------
# LOAD USERS
# ------------------------

print("Loading users...")

with open("users.csv", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

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
            **row
        )

print("Users Loaded")


# ------------------------
# LOAD TRANSACTIONS
# ------------------------

print("Loading transactions...")

with open(
    "transactions.csv",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    count = 0

    for row in reader:

        session.run(
            """
            CREATE (t:Transaction {
                transaction_id:$transaction_id,
                amount:toFloat($amount),
                ip_address:$ip_address,
                device_id:$device_id
            })
            """,
            **row
        )

        count += 1

        if count % 1000 == 0:
            print(f"{count} loaded")

print("Transactions Loaded")

session.close()