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

    user_response = sender_stand_request.post_new_user(get_user_body(name))

    return user_response.json()["authToken"]

# Se corrigieron los puntos señalados

def positive_assert_test(name, token):
    
    body = get_kit_body(name)
    if token:
        header = change_headertoken(get_usertoken(name))
        
    else:
        header = data.headers
        
    response = sender_stand_request.post_new_kit(header=header, body=body)

    assert response.status_code == 201

    assert body["name"] == response.json()["name"]


def negative_assert_test(name, token):
    body = get_kit_body(name)
    if token:
        header = change_headertoken(get_usertoken(name))

    else:
        header = data.headers

    response = sender_stand_request.post_new_kit(header=header, body=body)

    assert response.status_code == 400


############################################################################3
#Test con token generados por un usuario nuevo

def test1_1caracter_name_c ():
    positive_assert_test("a", True)
    # En este caso sale error, pues no se puede generar un token ya que la longuitud de caracteres debe ser mayor a 2 y
    # menor a 15, segun los requisitos para crear un nuevo usuario
    # {'code': 400, 'message': 'Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres.'}

def test2_511caracteres_name_c ():
    name = data.name511caracteres
    positive_assert_test(name, True)
    # Se tiene el mismo comportamiento que el test pasado, solo se aceptan como maximo 15 caracteres para el nombre del usuario


def test3_0caracteres_name_c():
    negative_assert_test("", True)

def test4_512caracteres_name_c():
    name = data.name512caracteres
    negative_assert_test(name, True)

def test5_caracteres_especiales_name_c():
    name = data.name_special
    positive_assert_test(name, True)

def test6_espacio_name_c():
    name = data.name_space
    positive_assert_test(name, True)

def test7_numerosstr_name_c():
    name = data.name_str_numbers
    positive_assert_test(name, True)

def test8_noparametros_c():
    header = change_headertoken(get_usertoken("alberto"))
    response = sender_stand_request.post_new_kit(header=header, body={})

    assert response.status_code == 400

def test9_numeros_name_c():
    negative_assert_test(123, True)

############################################################################3
#Test sin token generados por un usuario nuevo

def test1_1caracter_name_s ():
    positive_assert_test("a", False)

def test2_511caracteres_name_s ():
    name = data.name511caracteres
    positive_assert_test(name, False)

def test3_0caracteres_name_s():
    negative_assert_test("", False)

def test4_512caracteres_name_s():
    name = name = data.name512caracteres
    negative_assert_test(name, False)

def test5_caracteres_especiales_name_s():
    name = data.name_special
    positive_assert_test(name, False)

def test6_espacio_name_s():
    name = data.name_space
    positive_assert_test(name, False)

def test7_numeros_name_s():
    name = data.name_str_numbers
    positive_assert_test(name, False)

def test8_noparametros_s():
    response = sender_stand_request.post_new_kit(header=data.headers, body={})

    assert response.status_code == 400

def test9_numeros_name_s():
    negative_assert_test(123, False)
