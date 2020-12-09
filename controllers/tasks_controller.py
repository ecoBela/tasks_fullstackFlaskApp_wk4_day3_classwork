from flask import Flask, render_template, request, redirect
from repositories import task_repository
from repositories import user_repository
from models.task import Task
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
    users = user_repository.select_all()
    return render_template("tasks/new.html", all_users=users)

#NEW route
#GET 'tasks/new'
#return to the browswer a new HTML FORM

#CREATE
#POST '/tasks'

@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    description = request.form['description']
    user_id = request.form['user_id']
    duration = request.form['duration']
    completed = request.form['completed']

    #gather all data from form
    #select user object from DB
    user = user_repository.select(user_id)
    #create a new task object
    task = Task( description, user, duration, completed)
    #save task to db
    task_repository.save(task)
    #redirect to INDEX
    return redirect('/tasks')

#SHOW
#GET 'tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

#UPDATE
#POST '/tasks/
#DELETE
#POST'/tasks/<id>'
@tasks_blueprint.route('/tasks/<id>/delete', methods=['POST'])
def delete_task(id):
    task_repository.delete(id)
    return redirect('/tasks')


