from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for job in result.all():
      jobs.append(job)

    return jobs


@app.route("/")
def start():
  jobs = load_jobs_from_db()
  return render_template('index.html', jobs=jobs, company_name='ProSurge')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  # print("Hi, there")
  app.run(host="0.0.0.0", debug=True)
