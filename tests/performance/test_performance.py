# # tests/performance/test_performance.py
# import pytest
# import time
#
#
# @pytest.mark.performance
# class TestPerformance:
#
#     def test_response_time(self):
#         """Тест времени ответа API"""
#         start_time = time.time()
#         # Вызов API
#         response_time = time.time() - start_time
#         assert response_time < 1.0  # Должен отвечать быстрее 1 секунды
#
#     @pytest.mark.slow
#     def test_memory_usage(self):
#         """Тест использования памяти"""
#         import os
#         import psutil
#
#         process = psutil.Process(os.getpid())
#         memory_before = process.memory_info().rss
#
#         # Выполняем операцию
#         # ...
#
#         memory_after = process.memory_info().rss
#         memory_increase = memory_after - memory_before
#
#         assert memory_increase < 1024 * 1024  # Не более 1MB
