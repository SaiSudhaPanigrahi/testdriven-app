import json
import unittest

# from project import db
# from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestAuthBlueprint(BaseTestCase):
    def test_user_registration(self):
        with self.client:
            response = self.client.post(
                "/auth/register",
                data=json.dumps(
                    {
                        "username": "justatest",
                        "email": "justa@test.com",
                        "password": "testpass123",
                    }
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Successfully registered.")
            self.assertTrue(data["auth_token"])

    def test_user_registration_duplicate_email(self):
        add_user("test", "test@test.com", "testduplicateemail")
        with self.client:
            response = self.client.post(
                "/auth/register",
                data=json.dumps(
                    {
                        "username": "test",
                        "email": "test@test.com",
                        "password": "test123",
                    }
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.content_type == "application/json")
            self.assertIn("Sorry. That user already exists.", data["message"])
            self.assertIn("fail", data["status"])

    def test_user_registration_duplicate_username(self):
        add_user("test", "test@test.com", "testduplicateusername")
        with self.client:
            response = self.client.post(
                "/auth/register",
                data=json.dumps(
                    {
                        "username": "test",
                        "email": "otheremail@test.com",
                        "password": "test123",
                    }
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.content_type == "application/json")
            self.assertIn("Sorry. That user already exists.", data["message"])
            self.assertIn("fail", data["status"])

    def test_user_registration_invalid_json(self):
        with self.client:
            response = self.client.post(
                "/auth/register", data=json.dumps({}), content_type="application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_user_registration_invalid_json_keys_no_username(self):
        with self.client:
            response = self.client.post(
                "/auth/register",
                data=json.dumps(
                    {"email": "otheremail@test.com", "password": "test123"}
                ),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.content_type == "application/json")
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_user_registration_invalid_json_keys_no_email(self):
        with self.client:
            response = self.client.post(
                "/auth/register",
                data=json.dumps({"username": "test", "password": "test123"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.content_type == "application/json")
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_user_registration_invalid_json_keys_no_password(self):
        with self.client:
            response = self.client.post(
                "/auth/register",
                data=json.dumps({"username": "test", "email": "test@test.com"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.content_type == "application/json")
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_registered_user_login(self):
        with self.client:
            add_user("test", "test@test.com", "testpass123")
            response = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "testpass123"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Successfully logged in.")
            self.assertTrue(data["auth_token"])
            self.assertTrue(response.content_type == "application/json")

    def test_not_registered_user_login(self):
        with self.client:
            response = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "testpass123"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.content_type == "application/json")
            self.assertIn("Invalid credentials.", data["message"])
            self.assertIn("fail", data["status"])


if __name__ == "__main__":
    unittest.main()
