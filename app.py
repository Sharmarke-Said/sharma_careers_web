from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Mogadishu Somalia",
    "salary": "$10_000"
}, {
    "id": 1,
    "title": "Data Scientist",
    "location": "Hargeisa Somalia",
    "salary": "$20_000"
}, {
    "id": 1,
    "title": "Frontend Engineer",
    "location": "Garowe Somalia",
    "salary": "$15_000"
}, {
    "id": 1,
    "title": "Backend Engineer",
    "location": "Mogadishu Somalia",
    "salary": "$10_000"
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='sharma')

@app.route("/api/jobs")
def list_job():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
