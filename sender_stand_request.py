import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta lo


def post_new_kit(header, body):

    return requests.post(configuration.URL_SERVICE + configuration.NEW_KIT_PATH,
                  headers=header,
                  json=body)

