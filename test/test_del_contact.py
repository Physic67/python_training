from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="Edward", middlename="Vampire", lastname="Kallen", address="Forks, Washington", homephone="495-1234567", mobilephone="901-1234567", email="123@gmail.ru"))
    app.contact.delete_first_contact()
