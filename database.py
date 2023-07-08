from sqlalchemy import create_engine, text
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


def load_a_job_from_db(id_of_click):
  with engine.connect() as conn:
    query = text("SELECT * FROM jobs where id=:val").bindparams(
      val=id_of_click)
    result = conn.execute(query)
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      return rows[0]


def add_submit_data_into_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      'insert into applications(job_id, full_name, email, linkedin_url, education, work_exp, resume_file) values(:job_id, :full_name, :email, :linkedin_url, :education, :work_exp, :resume_file)'
    ).bindparams(job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin'],
                 education=data['education'],
                 work_exp=data['work_exp'],
                 resume_file=data['resume'])
    conn.execute(query)
