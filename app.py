from flask import Flask, render_template, jsonify, request

from database import result1, load_jobs_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=result1)


@app.route('/jobs')
def list_jobs():
  return jsonify(result1)


@app.route('/jobs/<id>')
def show_job(id):
  job = load_jobs_from_db(id)
  return render_template('jobpage.html', job=job)
  
@app.route('/jobs/<id>/apply', methods=['post'])
def apply_to_job(id):
  data= request.form
  return render_template('application_submitted.html', application=data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
