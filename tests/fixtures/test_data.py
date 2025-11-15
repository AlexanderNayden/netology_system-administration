# from myapp.models import Order, Product, User
# import pytest
#
#
# @pytest.fixture
# def sample_user():
#     """Фикстура тестового пользователя"""
#     return User(id=1, name="Test User", email="test@example.com", is_active=True)
#
#
# @pytest.fixture
# def sample_product():
#     """Фикстура тестового товара"""
#     return Product(id=1, name="Test Product", price=100.0, stock_quantity=10)
#
#
# @pytest.fixture
# def sample_order(sample_user, sample_product):
#     """Фикстура тестового заказа"""
#     return Order(id=1, user=sample_user, products=[sample_product], total_amount=100.0)
#
#
# @pytest.fixture
# def mock_external_api():
#     """Фикстура для мока внешнего API"""
#     with patch("myapp.services.payment_gateway.requests") as mock_requests:
#         mock_response = Mock()
#         mock_response.status_code = 200
#         mock_response.json.return_value = {"status": "success"}
#         mock_requests.post.return_value = mock_response
#         yield mock_requests
