# from myapp.database import Database
# from myapp.models import User
# import pytest
#
#
# class TestDatabaseIntegration:
#     """Тесты интеграции с базой данных"""
#
#     @pytest.fixture
#     def db_connection(self):
#         # Используем тестовую БД
#         db = Database(test_mode=True)
#         db.connect()
#         yield db
#         db.cleanup()
#         db.disconnect()
#
#     def test_user_crud_operations(self, db_connection):
#         # Create
#         user = User(name="Test User", email="test@example.com")
#         saved_user = db_connection.save_user(user)
#         assert saved_user.id is not None
#
#         # Read
#         retrieved_user = db_connection.get_user(saved_user.id)
#         assert retrieved_user.name == "Test User"
#
#         # Update
#         retrieved_user.name = "Updated Name"
#         db_connection.update_user(retrieved_user)
#
#         # Verify update
#         updated_user = db_connection.get_user(saved_user.id)
#         assert updated_user.name == "Updated Name"
#
#         # Delete
#         db_connection.delete_user(saved_user.id)
#         assert db_connection.get_user(saved_user.id) is None
#
#     def test_database_transactions(self, db_connection):
#         # Тестирование транзакций
#         with db_connection.transaction():
#             user1 = User(name="User1", email="user1@example.com")
#             user2 = User(name="User2", email="user2@example.com")
#             db_connection.save_user(user1)
#             db_connection.save_user(user2)
#
#         # Проверяем, что оба пользователя сохранены
#         assert db_connection.get_user_by_email("user1@example.com") is not None
#         assert db_connection.get_user_by_email("user2@example.com") is not None
