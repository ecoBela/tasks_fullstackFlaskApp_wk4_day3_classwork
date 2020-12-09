from flask import Flask, render_template
from repositories import task_repository
# Import Blueprint from flask
from flask import Blueprint
tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route('/tasks')
def tasks():
  # Get all the tasks from the DB
  tasks = task_repository.select_all()
  return render_template("tasks/index.html", all_tasks=tasks)

@tasks_blueprint.route('/tasks/new')
def new_task():
    return render_template("tasks/new.html")

#NEW route
#GET 'tasks/new'
#return to the browswer a new HTML FORM

#CREATE
#POST '/tasks'

#SHOW
#GET 'tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

#UPDATE
#POST '/tasks/

