from dataclasses import dataclass
import random
import datetime
from sys import intern
from tkinter import N
from tkinter.messagebox import NO
from typing import final
import uuid
from contextlib import contextmanager
import boto3
from faker import Faker
import time
import psycopg2


STATES_IND = [
    "AN", "AP", "AR", "AS", "BR", "CH", "CT",
    "DN", "DD", "DL", "GA", "GJ", "HR", "HP",
    "JK", "JH", "KA", "KL", "LD", "MP", "MH",
    "MN", "ML", "MZ", "NL", "OR", "PY", "PB",
    "RJ", "SK", "TN", "TG", "TR", "UP", "UT",
    "WB"
]


def _get_orders(num_orders: int, cust_ids: list[int]) -> str:
    # order_id
    # cut_id
    # item_id
    # item_name
    # delivery_date

    items = [
        "item1",
        "item2",
        "item3",
        "item4",
        "item5",
        "item6",
        "item7",
        "item8",
        "item9",
        "item0"
    ]

    output = ""
    for i in range(num_orders):
        output += f'{uuid.uuid4()}, {random.choice(cust_ids)},'
        output += f'{uuid.uuid4()}, {random.choice(items)},'
        output += f'{datetime.now().strftime("%y-%m-%d %H:%M:%S")}'
        output += "\n"

    return output


def _get_customer_data(cust_ids: list[int]) -> list[tuple[int, any, any, str, str, str]]:
    fake_cust = Faker()

    return[
        (
            cust_id,
            fake_cust.first_name(),
            fake_cust.last_name(),
            random.choice(STATES_IND),
            datetime.now().strftime("%y-%m-%d %H:%M:%S"),
            datetime.now().strftime("%y-%m-%d %H:%M:%S"),

        )
        for cust_id in cust_ids
    ]


def insert_data_query() -> str:
    return """
    INSERT INTO customers(
        cust_id, 
        first_name,
        last_name,
        state_code,
        datetime_created,
        datetime_updated
    )    

    VALUES(
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )

    on conflict(cust_id)
    do update set(first_name, last_name, stat_code, datetime_updated)= 
    (EXCLUDED.first_name, EXCLUDED.last_name,
     EXCLUDED.state_code, EXCLUDED.datetime_updated
    );
    """


def generate_data(iteration: int, orders_bucket: str = "my_app_orders_{}".format(datetime.year())):
    cust_ids = [random.randomint(1, 9999) for _ in range(1000)]
    orders_data = _get_orders(10000, cust_ids)
    cust_data = _get_customer_data(cust_ids)

    # sending data to aws s3
    s3 = boto3.client(
        "s3",
        region_name="us-east-1",
        endpoint_url="http://cloud-store:9000"
    )

    if not s3.Bucket(orders_bucket) in s3.buckets.all():
        s3.create_bucket(Bucket=orders_bucket)
        s3.object(orders_bucket, f"data_{str(iteration)}.csv").put(
            Body=orders_data)

    #send customer data to the customer database
    with DBConnection().managed_cursor() as curr:
        insert_query = insert_data_query()
        for cd in cust_data:
            curr.execute(
                insert_query,
                (
                    cd[0],
                    cd[1],
                    cd[2],
                    cd[3],
                    cd[4],
                    cd[5],
                ),
            )


@dataclass
class DBConnection:
    db: str = ""
    username: str = "postgres"
    password: str = "Vaibhav.010402" 
    host: str = "localhost"
    port: int = 5432
    # pwd = "admin"

class Db_conn:
    def __init__(self, db_conn: DBConnection):

        self.conn_url = (
             f"postgresql://{db_conn.username}:{db_conn.password}@"
            f"{db_conn.host}:{db_conn.port}/{db_conn.db}"
        )
    
    @contextmanager
    def managed_cursor(self, cursor_factory = None):
        self.conn = psycopg2.connect(self.conn_url)
        self.conn.autocommit = True
        self.curr = self.con.cursor(cursor_factory = cursor_factory)
        try:
            yield self.curr
        finally:
            self.curr.close()
            self.conn.close()


if __name__ == "__main__":
    itr = 1
    while True:
        generate_data(itr)
        time.sleep(30)
        itr+=1
