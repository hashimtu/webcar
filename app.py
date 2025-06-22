from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine

app = Flask(__name__)


def loadjobsfromdb():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
    return jobs


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=jobs)


@app.route('/jobs')
def list_jobs():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
