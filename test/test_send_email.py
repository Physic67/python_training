

def test_send_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.send_email()
    app.session.logout()