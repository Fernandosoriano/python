
import requests
# from requests.auth import HTTPDigestAuth
# from requests_toolbelt.multipart.encoder import MultipartEncoder


def solictar_login_naat(grantype, username, password):
     try:
         solicta_login_naat_url = 'https://uat.firmaautografa.com/authorization-server/oauth/token'
         print("URL_solicita_generacion_docs:")
         print(solicta_login_naat_url)
        #  data = {
        #     "grant_type": grantype,
        #     "username": username,
        #     "password": password
        #      }
         multipart_form_data = {
                'grant_type': (None, grantype),
                'username': (None, username),
                'password': (None, password)
                            }
         print ('BODY solicitar genera docs:')
         print(multipart_form_data)
        #  print('token', get_token(genera_docs_url))
         headers = {
                    'Authorization': 'Basic ZmFkOmZhZHNlY3JldA=='                          
                   }
         r = requests.post(solicta_login_naat_url,
                        #   json = data,
                        #   files = data,
                        files = multipart_form_data,
                        headers = headers
                        #   auth = HTTPDigestAuth('fad', 'fadsecret')
                          )
         respuesta = r.json()
         print('CODE_solicita_genera_docs:', r.status_code)
         if r.status_code == 500:
             respuesta = r
         else:
             respuesta = r.json()
         print("RESPONSE_solcita_generacion_docs: ")
         print(respuesta)
         return respuesta, r.status_code
     except Exception as e:
         print(e)
         return None
     
solictar_login_naat('password','hahernandez@na-at.com.mx','bcc6140ea61458c1b9645d5806dbc4b372f92c444ee5c751730f5a0ba40b622b')