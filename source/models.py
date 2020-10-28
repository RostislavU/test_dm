from source import db


class Departament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.String(db.String(64))
    parent_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<Departament {self.id} "{self.name}">'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    departament_id = db.Column(db.Integer, db.ForeignKey('departament.id'))
    departament = db.relationship('Departament', backref='employee')

    def __repr__(self):
        return f'<Employee ({self.id}) {self.first_name} {self.last_name} from {self.departament_id}>'