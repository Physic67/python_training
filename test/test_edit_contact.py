# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Shrek", middlename="Vampire", lastname="Kallen", address="Forks, Washington", homephone="495", mobilephone="901", email="123"))
