from source import app, db
from source.models import Departament, Employee
from source.routes import index


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Departament': Departament, 'Employee.yml': Employee}

