import pytest
from django.core.management import call_command


@pytest.fixture(scope='session', autouse=True)
def load_fixtures(django_db_setup, django_db_blocker):
    fixtures = ['fixtures/competence.json', 'fixtures/users.json']
    with django_db_blocker.unblock():
        for fixture in fixtures:
            call_command('loaddata', fixture)
