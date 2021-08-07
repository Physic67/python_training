
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    x = Contact(firstname="Edward", middlename="Vampire", lastname="Kallen", address="Forks, Washington",
                homephone="495-1234567", mobilephone="901-1234567", email="123@gmail.ru")
    app.contact.fill_names(x)
    app.contact.add_address(x)
    app.contact.add_phones(x)
    app.contact.save_contact()
    app.session.logout()