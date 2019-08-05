import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user

from sqlalchemy.exc import IntegrityError


class testUserModel(BaseTestCase):
    def test_add_user(self):
        user = add_user("justatest", "justa@test.com")
        self.assertTrue(user.id)
        self.assertEqual(user.username, "justatest")
        self.assertEqual(user.email, "justa@test.com")
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
        add_user("justatest", "justa@test.com")
        duplicate_user = User(username="justatest", email="justa@test2.com")
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_emial(self):
        add_user("justatest", "justa@test.com")
        duplicate_user = User(username="justanothertestuser", email="justa@test.com")
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = add_user("justatest", "justa@test.com")
        self.assertTrue(isinstance(user.to_json(), dict))


if __name__ == "__main__":
    unittest.main()
