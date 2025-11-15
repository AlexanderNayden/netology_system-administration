# from myapp import create_app
# from myapp.database import db_session, init_db
# import os
# import pytest
# import tempfile
#
#
# @pytest.fixture(scope="session")
# def app():
#     """Фикстура приложения для тестов"""
#     app = create_app(
#         {"TESTING": True, "DATABASE": tempfile.mktemp(), "WTF_CSRF_ENABLED": False}
#     )
#
#     with app.app_context():
#         init_db()
#
#     yield app
#
#
# @pytest.fixture
# def client(app):
#     """Фикстура тестового клиента"""
#     return app.test_client()
#
#
# @pytest.fixture(autouse=True)
# def run_around_tests():
#     """Выполняется перед и после каждого теста"""
#     # Setup
#     db_session.begin_nested()
#
#     yield
#
#     # Teardown
#     db_session.rollback()
#
#
# @pytest.fixture
# def auth_client(client, sample_user):
#     """Клиент с аутентификацией"""
#     with client.session_transaction() as session:
#         session["user_id"] = sample_user.id
#     return client
