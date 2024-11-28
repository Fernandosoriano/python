# test_multiply_table.py
import pytest
from excersises_list import multiply_table  
from hypothesis import given, strategies as st

# def test_multiply_table():
#     num = 3
#     expected_output = (
#         "Tabla del número 3: \n"
#         "3 X 1 = 3\n"
#         "3 X 2 = 6\n"
#         "3 X 3 = 9\n"
#         "3 X 4 = 12\n"
#         "3 X 5 = 15\n"
#         "3 X 6 = 18\n"
#         "3 X 7 = 21\n"
#         "3 X 8 = 24\n"
#         "3 X 9 = 27\n"
#         "3 X 10 = 30\n"
#     )
#     assert multiply_table(num) == expected_output

# # You can add more test cases if you want to test other numbers.
# def test_multiply_table_for_different_number():
#     num = '5'
#     expected_output = (
#         "Tabla del número 5: \n"
#         "5 X 1 = 5\n"
#         "5 X 2 = 10\n"
#         "5 X 3 = 15\n"
#         "5 X 4 = 20\n"
#         "5 X 5 = 25\n"
#         "5 X 6 = 30\n"
#         "5 X 7 = 35\n"
#         "5 X 8 = 40\n"
#         "5 X 9 = 45\n"
#         "5 X 10 = 50\n"
#     )
#     assert multiply_table(num) == expected_output
# =================================================================================================
@pytest.mark.parametrize("num, expected_output", [
    (1, "Tabla del número 1: \n1 X 1 = 1\n1 X 2 = 2\n1 X 3 = 3\n1 X 4 = 4\n1 X 5 = 5\n1 X 6 = 6\n1 X 7 = 7\n1 X 8 = 8\n1 X 9 = 9\n1 X 10 = 10\n"),
    (2, "Tabla del número 2: \n2 X 1 = 2\n2 X 2 = 4\n2 X 3 = 6\n2 X 4 = 8\n2 X 5 = 10\n2 X 6 = 12\n2 X 7 = 14\n2 X 8 = 16\n2 X 9 = 18\n2 X 10 = 20\n"),
    (3, "Tabla del número 3: \n3 X 1 = 3\n3 X 2 = 6\n3 X 3 = 9\n3 X 4 = 12\n3 X 5 = 15\n3 X 6 = 18\n3 X 7 = 21\n3 X 8 = 24\n3 X 9 = 27\n3 X 10 = 30\n"),
    # Se pueden agregar más casos aquí
])
def test_multiply_table(num, expected_output):
    assert multiply_table(num) == expected_output
# =============================================================================================================



