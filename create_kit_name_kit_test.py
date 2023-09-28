import data
import sender_stand_request

def change_headertoken(token):

    new_header = data.headers2.copy()

    new_header["Authorization"] = "Bearer " + token

    return new_header

def get_kit_body(first_name):

    current_body = data.kit_body.copy()

    current_body["name"] = first_name

    return current_body

def get_user_body(first_name):

    current_body = data.user_new.copy()

    current_body["firstName"] = first_name

    return current_body

def get_usertoken(name):

    user_repsonse = sender_stand_request.post_new_user(get_user_body(name))

    return user_repsonse.json()["authToken"]

# Pruebas y Negativas positicas con Token generado por usuario nuevo
def positive_assert_test_cToken(name):

    body = get_kit_body(name)
    header = change_headertoken(get_usertoken(name))

    response = sender_stand_request.post_new_kit(header=header, body=body)

    assert response.status_code == 201

    assert body["name"] == response.json()["name"]

def negative_assert_test_cToken(name):

    body = get_kit_body(name)
    header = change_headertoken(get_usertoken(name))

    response = sender_stand_request.post_new_kit(header=header, body=body)

    assert response.status_code == 400

# Pruebas y Negativas positicas sin Token

def positive_assert_test_sToken(name):

    body = get_kit_body(name)

    response = sender_stand_request.post_new_kit(header=data.headers, body=body)

    assert response.status_code == 201

    assert body["name"] == response.json()["name"]

def negative_assert_test_sToken(name):

    body = get_kit_body(name)

    response = sender_stand_request.post_new_kit(header=data.headers, body=body)

    assert response.status_code == 400



############################################################################3
#Test con token generados por un usuario nuevo

def test1_1caracter_name_c ():
    positive_assert_test_cToken("a")
    # En este caso sale error, pues no se puede generar un token ya que la longuitud de caracteres debe ser mayor a 2 y
    # menor a 15, segun los requisitos para crear un nuevo usuario
    # {'code': 400, 'message': 'Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres.'}

def test2_511caracteres_name_c ():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert_test_cToken(name)
    # Se tiene el mismo comportamiento que el test pasado, solo se aceptan como maximo 15 caracteres para el nombre del usuario


def test3_0caracteres_name_c():
    negative_assert_test_cToken("")

def test4_512caracteres_name_c():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert_test_cToken(name)

def test5_caracteres_especiales_name_c():
    name = "№%@"
    positive_assert_test_cToken(name)

def test6_espacio_name_c():
    name = " A Aaa "
    positive_assert_test_cToken(name)

def test7_numerosstr_name_c():
    name = "123"
    positive_assert_test_cToken(name)

def test8_noparametros_c():
    header = change_headertoken(get_usertoken("alberto"))
    response = sender_stand_request.post_new_kit(header=header, body={})

    assert response.status_code == 400

def test9_numeros_name_c():
    negative_assert_test_cToken(123)

############################################################################3
#Test sin token generados por un usuario nuevo

def test1_1caracter_name_s ():
    positive_assert_test_sToken("a")

def test2_511caracteres_name_s ():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert_test_sToken(name)

def test3_0caracteres_name_s():
    negative_assert_test_sToken("")

def test4_512caracteres_name_s():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert_test_sToken(name)

def test5_caracteres_especiales_name_s():
    name = "№%@"
    positive_assert_test_sToken(name)

def test6_espacio_name_s():
    name = " A Aaa "
    positive_assert_test_sToken(name)

def test7_numeros_name_s():
    name = "123"
    positive_assert_test_sToken(name)

def test8_noparametros_s():
    response = sender_stand_request.post_new_kit(header=data.headers, body={})

    assert response.status_code == 400

def test9_numeros_name_s():
    negative_assert_test_sToken(123)
