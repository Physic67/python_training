# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="Shrek", middlename="Vampire", lastname="Kallen", address="Forks, Washington", homephone="495", mobilephone="901", email="123"))
    app.session.logout()
