from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Nairobi, Kenya',
  'salary': 'KSHS 125,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Mombasa, Kenya',
  'salary': 'KSHS 145,000'
}, {
  'id': 3,
  'title': 'Researcher',
  'location': 'Nairobi, Kenya',
  'salary': 'KSHS 85,000'
}, {
  'id': 4,
  'title': 'Research Assistant',
  'location': 'Nakuru, Kenya',
  'salary': 'KSHS 65,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
