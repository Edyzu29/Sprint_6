import data
import sender_stand_request
from create_kit_name_kit_test import positive_and_negative_assert_test

############################################################################3
#Test sin token generados por un usuario nuevo

def test1_1caracter_name_s ():
    positive_and_negative_assert_test("a", False, "Positive")

def test2_511caracteres_name_s ():
    name = data.name511caracteres
    positive_and_negative_assert_test(name, False, "Positive")

def test3_0caracteres_name_s():
    positive_and_negative_assert_test("", False, "Negative")

def test4_512caracteres_name_s():
    name = name = data.name512caracteres
    positive_and_negative_assert_test(name, False, "Negative")

def test5_caracteres_especiales_name_s():
    name = data.name_special
    positive_and_negative_assert_test(name, False, "Positive")

def test6_espacio_name_s():
    name = data.name_space
    positive_and_negative_assert_test(name, False, "Positive")

def test7_numeros_name_s():
    name = data.name_str_numbers
    positive_and_negative_assert_test(name, False, "Positive")

def test8_noparametros_s():
    response = sender_stand_request.post_new_kit(header=data.headers, body={})

    assert response.status_code == 400

def test9_numeros_name_s():
    positive_and_negative_assert_test(123, False, "Negative")