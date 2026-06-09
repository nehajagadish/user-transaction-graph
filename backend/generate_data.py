from faker import Faker
import csv
import random

fake = Faker()

TOTAL_USERS = 500
TOTAL_TRANSACTIONS = 100000


def generate_users():

    shared_emails = [
        "shared1@test.com",
        "shared2@test.com",
        "shared3@test.com"
    ]

    shared_phones = [
        "9999999991",
        "9999999992",
        "9999999993"
    ]

    with open(
        "users.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "user_id",
            "name",
            "email",
            "phone",
            "address",
            "payment_method"
        ])

        for i in range(1, TOTAL_USERS + 1):

            email = (
                random.choice(shared_emails)
                if random.random() < 0.1
                else fake.email()
            )

            phone = (
                random.choice(shared_phones)
                if random.random() < 0.1
                else fake.phone_number()
            )

            writer.writerow([
                f"U{i}",
                fake.name(),
                email,
                phone,
                fake.city(),
                random.choice([
                    "Visa",
                    "MasterCard",
                    "PayPal"
                ])
            ])


def generate_transactions():

    with open(
        "transactions.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "transaction_id",
            "sender",
            "receiver",
            "amount",
            "ip_address",
            "device_id"
        ])

        for i in range(
            1,
            TOTAL_TRANSACTIONS + 1
        ):

            writer.writerow([
                f"T{i}",
                f"U{random.randint(1,500)}",
                f"U{random.randint(1,500)}",
                round(
                    random.uniform(10, 5000),
                    2
                ),
                f"192.168.{random.randint(1,30)}.{random.randint(1,255)}",
                f"D{random.randint(1,100)}"
            ])


if __name__ == "__main__":

    generate_users()
    generate_transactions()

    print("Data Generated")