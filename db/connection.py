import psycopg2
from app.config.settings import POSTGRES_CONFIG


def get_conn():
    return psycopg2.connect(**POSTGRES_CONFIG)