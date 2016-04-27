from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)
    html = render_template('student_info.html', first = first, last = last, github=github, grades=grades)
    # return "%s is the GitHub account for %s %s" % (github, first, last)

    print grades 

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template('student_search.html')

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get("first")
    last = request.form.get("last")
    github = request.form.get("github")
    hackbright.make_new_student(first, last, github)

    return redirect ("/success")

@app.route("/student_add_form")
def get_student_info():
    """Retrieve student information"""

    return render_template("student-add.html")


@app.route("/success")
def success():
    """Renders successful submission template."""

    return render_template("success.html")
    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
