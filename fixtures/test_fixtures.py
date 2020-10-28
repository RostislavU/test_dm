import unittest

from staff_structure import app
from source.models import db, Departament, Employee
from flask_fixtures import FixturesMixin
from config import Config

app.config.from_object(Config)


class TestData(unittest.TestCase, FixturesMixin):
    fixtures = ['Departament1.yml', 'Departament2.yml']
    app = app
    db = db

    def test_departament(self):
        departaments = Departament.query.all()
        assert len(departaments[0].employee) == 4
        assert len(departaments[1].employee) == 4
