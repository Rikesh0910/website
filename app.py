from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Software Engineer',
  'location': 'Chennai, India',
  'salary': '1,00,000'
 },

 {
  'id': 2,
  'title': 'Data analyst',
  'location': 'Delhi, India',
  'salary': '2,00,000'
 },
        
 {
  'id': 3,
  'title': 'Test Engineer',
  'location': 'Bangalore, India',
  'salary': '2,00,000'
 }
]
  
@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS, name='Ricky')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)