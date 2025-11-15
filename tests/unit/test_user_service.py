# from myapp.models import User
# from myapp.services.user_service import UserService
# import pytest
# from unittest.mock import Mock, patch
#
#
# class TestUserService:
#
#     @patch("myapp.services.user_service.Database")
#     def test_create_user(self, mock_db):
#         # Arrange
#         mock_db_instance = Mock()
#         mock_db.return_value = mock_db_instance
#         service = UserService()
#
#         # Act
#         result = service.create_user("john@example.com", "John Doe")
#
#         # Assert
#         mock_db_instance.save.assert_called_once()
#         assert result.email == "john@example.com"
#
#     def test_get_user_not_found(self):
#         service = UserService()
#
#         with patch.object(service.db, "get_user", return_value=None):
#             result = service.get_user(999)
#
#         assert result is None
