# from google.cloud import secretmanager

# PROJECT_ID = 'com-dev-autograph-signature'
# print(PROJECT_ID)
# SECRET_ID_PASS = 'NAAT_PASSWORD'
# print(SECRET_ID_PASS)
# SECRET_ID_USER = 'NAAT_USER'
# print(SECRET_ID_USER)

# secrets = secretmanager.SecretManagerServiceClient()
# PASS = secrets.access_secret_version(request={"name": "projects/"+PROJECT_ID+"/secrets/"+SECRET_ID_PASS+"/versions/latest"}).payload.data.decode("utf-8")
# USER = secrets.access_secret_version(request={"name": "projects/"+PROJECT_ID+"/secrets/"+SECRET_ID_USER+"/versions/latest"}).payload.data.decode("utf-8")

# print(PASS)
# print(USER)


response = {
    "codigo_ejecucion": 200,
    "documentos": [
        {
            "documentos": [
                127,
                140
            ],
            "fallidos": [],
            "id_proceso_venta": 6692751
        }
    ],
    "mensaje_ejecucion": "Documentos generados correctamente"
}

arr_documents = response.get('documentos')[0].get('documentos')
print(arr_documents)
