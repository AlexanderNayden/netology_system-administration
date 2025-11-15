# from myapp.utils.math_operations import Calculator, add, divide
# import pytest
#
#
# class TestMathOperations:
#     """Тесты для математических операций"""
#
#     def test_add_positive_numbers(self):
#         assert add(2, 3) == 5
#
#     def test_add_negative_numbers(self):
#         assert add(-1, -1) == -2
#
#     @pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
#     def test_add_with_parameters(self, a, b, expected):
#         assert add(a, b) == expected
#
#
# class TestCalculator:
#     """Тесты для класса Calculator"""
#
#     def test_calculator_initialization(self):
#         calc = Calculator()
#         assert calc.memory == 0
#
#     def test_calculator_add(self):
#         calc = Calculator()
#         calc.add(5)
#         assert calc.memory == 5
#
#     def test_divide_by_zero(self):
#         with pytest.raises(ValueError, match="Cannot divide by zero"):
#             divide(10, 0)
