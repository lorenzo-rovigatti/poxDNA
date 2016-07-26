'''
Created on 26 Jul 2016

@author: rovigattil
'''

from app import app
from flask import render_template, redirect
from flask_security import login_required
from flask_security.core import current_user
from models import db, User, Project

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
def project_delete(id_project):
    Project.query.filter_by(id=id_project).delete()
    db.session.commit()
    return redirect('/projects')

@app.route('/project/<id_project>')
@login_required
def project_view(id_project):
    project = Project.query.filter_by(id=id_project).first()
    return render_template('project/view.html', project=project)
