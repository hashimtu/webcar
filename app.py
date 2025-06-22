from flask import Flask, render_template, jsonify

from database import result1

app = Flask(__name__)






@app.route('/')
def hello_world():
  return render_template('home.html', jobs=result1)


@app.route('/jobs')
def list_jobs():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
