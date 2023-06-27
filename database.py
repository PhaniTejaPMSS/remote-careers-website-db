from sqlalchemy import create_engine
import os

# print(sqlalchemy.__version__)

db_conn_str = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   result_dict = []

#   for row in result.all():
#     result_dict.append(dict(row))

#   print(result.all())
