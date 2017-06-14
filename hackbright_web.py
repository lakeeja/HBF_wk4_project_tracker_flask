"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    
    project = hackbright.get_grades_by_github(github)
    print project
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           project=project)


   
    

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""
    return render_template('student_search.html')

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""



    github = request.form.get("github")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")

    hackbright.make_new_student(github, first_name, last_name)


    return "made it to student add whew"
@app.route('/project')
def project_info():
    """ list info about a project """
    title = request.args.get('title')
    hackbright.get_project_by_title(title)

    projects = render_template("student_search.html",
                                title=title)
    return project


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
