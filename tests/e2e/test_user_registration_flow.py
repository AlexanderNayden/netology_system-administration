# import pytest
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
#
#
# class TestUserRegistrationE2E:
#     """End-to-end тесты полного цикла регистрации"""
#
#     @pytest.fixture
#     def browser(self):
#         driver = Chrome()
#         driver.implicitly_wait(10)
#         yield driver
#         driver.quit()
#
#     def test_complete_user_registration_flow(self, browser, live_server):
#         # 1. Открываем страницу регистрации
#         browser.get(f"{live_server.url}/register")
#
#         # 2. Заполняем форму
#         browser.find_element(By.NAME, "email").send_keys("test@example.com")
#         browser.find_element(By.NAME, "password").send_keys("secure_password")
#         browser.find_element(By.NAME, "confirm_password").send_keys("secure_password")
#
#         # 3. Отправляем форму
#         browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#
#         # 4. Проверяем редирект и успешную регистрацию
#         assert "login" in browser.current_url
#         assert "Registration successful" in browser.page_source
#
#     def test_purchase_flow(self, browser, live_server):
#         # Полный цикл: регистрация → вход → покупка
#         pass
