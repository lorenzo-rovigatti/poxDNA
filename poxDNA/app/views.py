'''
Created on 26 Jul 2016

@author: rovigattil
'''

from app import app
from flask import render_template, redirect, abort
from flask_security import login_required
from flask_security.core import current_user
from models import db, User, Project, Task
from functools import wraps

def access_to_project_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if 'id_project' in kwargs:
            project = Project.query.get(kwargs['id_project'])
            if project == None or current_user not in project.users:
                return abort(404)
            
        return func(*args, **kwargs)
    
    return decorated_view

@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/projects')
@login_required
def projects():
    projects = User.query.filter_by(id=current_user.get_id()).first().projects
#     projects = Project.query.filter().all()
    return render_template('project/list.html', projects=projects)

@app.route('/project/new', methods=['GET', 'POST'])
@app.route('/project/edit/<id_project>', methods=['GET', 'POST'])
@login_required
@access_to_project_required
def project(id_project=None):
    from forms import ProjectForm
    if id_project != None:
        project = Project.query.get(id_project)
        action = "Save"
    else:
        project = Project()
        action = "Create"
        
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        form.populate_obj(project)
        project.users.append(current_user)
        db.session.add(project)
        db.session.commit()
        return redirect('/projects')
    
    return render_template('project/form.html', form=form, action=action)

@app.route('/project/del/<id_project>')
@login_required
@access_to_project_required
def project_delete(id_project):
    Project.query.filter_by(id=id_project).delete()
    db.session.commit()
    return redirect('/projects')

@app.route('/project/<id_project>')
@login_required
@access_to_project_required
def project_view(id_project):
    project = Project.query.filter_by(id=id_project).first()
    return render_template('project/view.html', project=project)


@app.route('/project/<id_project>/task/new', methods=['GET', 'POST'])
@app.route('/project/<id_project>/task/edit/<id_task>', methods=['GET', 'POST'])
@login_required
@access_to_project_required
def task(id_project, id_task=None):
    project = Project.query.get(id_project)
    
    from forms import TaskForm
    if id_task != None:
        task = task.query.get(id_task)
        action = "Save"
    else:
        task = Task()
        action = "Add"
        
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        form.populate_obj(task)
        db.session.add(task)
        db.session.commit()
        return redirect('/tasks')
    
    return render_template('project/task/form.html', form=form, action=action, project=project)

@app.route('/project/<id_project>/task/del/<id_task>')
@login_required
@access_to_project_required
def task_delete(id_project, id_task):
    task.query.filter_by(id=id_task).delete()
    db.session.commit()
    return redirect('/tasks')

@app.route('/project/<id_project>/task/<id_task>')
@login_required
@access_to_project_required
def task_view(id_project, id_task):
    task = task.query.filter_by(id=id_task).first()
    return render_template('project/task/view.html', task=task)
