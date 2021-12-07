import pytest

from emaillib import Email, MailAdminClient


@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


def test_email_received(receiving_user, sending_user):
    email = Email(subject="Hi!", body="How's it going?")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox