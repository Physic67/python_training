# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
        app.login(username="admin", password="secret")
        x = Contact(firstname="Edward", middlename="Vampire", lastname="Kallen", address="Forks, Washington", homephone="495-1234567", mobilephone="901-1234567")
        app.fill_names(x)
        app.add_address(x)
        app.add_phones(x)
        app.save_contact()

