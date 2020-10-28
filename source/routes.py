from flask import request
from source import app
from source.models import db, Departament, Employee


@app.route('/')
@app.route('/index')
def index():
    deps = Departament.query.all()
    result: str = ''
    if deps:
        for dep in deps:
            result += f"GET <a href='/department-tree/?root-id={dep.id}'>root_id={dep.id}</a>\n"
        return result
    return 'Empty data'


@app.route('/department-tree', methods=['POST'])
def get_department_tree():
    if request.method == 'POST':
        root_id = request.args.get('root-id')
        dep = Departament.query.get(root_id)
        return dep


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404