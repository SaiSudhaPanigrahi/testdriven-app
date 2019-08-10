import json
import unittest

from flask import current_app

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

    def test_valid_logout(self):
        add_user("test", "test@test.com", "testpass123")
        with self.client:
            # user login
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "testpass123"}),
                content_type="application/json",
            )
            # valid token logout
            token = json.loads(resp_login.data.decode())["auth_token"]
            response = self.client.get(
                "/auth/logout", headers={"Authorization": f"Bearer {token}"}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.content_type == "application/json")
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["message"] == "Successfully logged out.")

    def test_invalid_logout_token_expired(self):
        add_user("test", "test@test.com", "testpass123")
        current_app.config["TOKEN_EXPIRATION_SECONDS"] = -1
        with self.client:
            # user login
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "testpass123"}),
                content_type="application/json",
            )
            # invalid token logout
            token = json.loads(resp_login.data.decode())["auth_token"]
            response = self.client.get(
                "/auth/logout", headers={"Authorization": f"Bearer {token}"}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertTrue(response.content_type == "application/json")
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Signature expired. Please login again.")

    def test_invalid_logout_token(self):
        with self.client:
            response = self.client.get(
                "/auth/logout", headers={"Authorization": "Bearer invalid"}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertTrue(response.content_type == "application/json")
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Invalid token. Please login again.")

    def test_user_status(self):
        add_user("test", "test@test.com", "testpass123")
        with self.client:
            resp_login = self.client.post(
                "/auth/login",
                data=json.dumps({"email": "test@test.com", "password": "testpass123"}),
                content_type="application/json",
            )
            token = json.loads(resp_login.data.decode())["auth_token"]
            response = self.client.get(
                "/auth/status", headers={"Authorization": f"Bearer {token}"}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.content_type == "application/json")
            self.assertTrue(data["status"] == "success")
            self.assertTrue(data["data"] is not None)
            self.assertTrue(data["data"]["username"] == "test")
            self.assertTrue(data["data"]["email"] == "test@test.com")
            self.assertTrue(data["data"]["active"] is True)

    def test_invalid_status(self):
        with self.client:
            response = self.client.get(
                "/auth/status", headers={"Authorization": "Bearer invalid"}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertTrue(response.content_type == "application/json")
            self.assertTrue(data["status"] == "fail")
            self.assertTrue(data["message"] == "Invalid token. Please login again.")


if __name__ == "__main__":
    unittest.main()
