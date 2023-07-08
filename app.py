from flask import Flask, render_template, jsonify, request
from database import engine, load_a_job_from_db, add_submit_data_into_db
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for job in result.all():
      jobs.append(job)

    return jobs


@app.route("/job/<id>")
def show_job(id):
  job = load_a_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)


@app.route("/")
def start():
  jobs = load_jobs_from_db()
  return render_template('index.html', jobs=jobs, company_name='ProSurge')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>/apply", methods=['POST'])
def apply_for_job(id):
  jobs = load_a_job_from_db(id)
  data = request.form

  add_submit_data_into_db(id, data)

  if not data:
    return 'Empty data'
  # return jsonify(data)
  return render_template('app_submitted.html', data=data, jobs=jobs)


if __name__ == "__main__":
  # print("Hi, there")
  app.run(host="0.0.0.0", debug=True)
