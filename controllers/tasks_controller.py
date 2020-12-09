from flask import Flask, render_template

#Import Blueprint from flask - this represents a collection of routes; we'll define our routes here
#It's about separation of concerns: we'll register our blueprint with our main app
from flask import Blueprint

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route('/tasks')
def tasks():
    return render_template("tasks/index.html")