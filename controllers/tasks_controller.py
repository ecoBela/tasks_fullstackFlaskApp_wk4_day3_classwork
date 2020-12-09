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

#NEW route
#GET 'tasks/new'

#CREATE
#POST '/tasks'

#SHOW
#GET 'tasks/<id>'





# from flask import Flask, render_template
# from repositories import task_repository
# from flask import Blueprint
# tasks_blueprint = Blueprint("tasks", __name__)
# #Import Blueprint from flask - this represents a collection of routes; we'll define our routes here
# #It's about separation of concerns: we'll register our blueprint with our main app


# @tasks_blueprint.route('/tasks')
# def tasks():
#     #get all tasks from the DB
#     tasks = task_repository.select_all()
#     return render_template("tasks/index.html", all_tasks=tasks)


