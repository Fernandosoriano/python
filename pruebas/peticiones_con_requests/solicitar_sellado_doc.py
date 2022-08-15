
import requests
# from requests.auth import HTTPDigestAuth
# from requests_toolbelt.multipart.encoder import MultipartEncoder
import urllib.request
import hashlib
import solicitar_login

URLPDF = 'https://dev-cm-09.storage.googleapis.com/f57827f8-5d08-11ec-a74e-8d9b0df948b3/Contrato%20Multiple%20Declaraciones.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=content-manager%40ent-dev-content-manager-id.iam.gserviceaccount.com%2F20220729%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220729T215351Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&generation=1640055486588645&x-goog-signature=5af48d31aad64ad0cd8919cbd27d58fb24ad0b86f10f56d6b6d68ca9da60b75c3bd7c0d4b3d842a1e82f37887b79da88bb0f6e52964ba1b67fdcb21027d93f1da23cb41291352ef81275c5f9f5236a73927f6fea190e24f22514abd6ddd13f851b78ce7b0a48be9c418fe05dc456bf84eeb68a886a0436c91a56d2a85b9e3420b4101b7cc44476edf4221d992c8146b3f37cd4966d0a35625281b73899466a0324f156144c2ef7b3c72c324b6e79156d6934d047399fa664eb90f977805e4b3b931160ccd177eb4d4a97d0fc70036c23978a6d332cf208f1d166aa46850e94eb921fef9d3dcf770dcf40dfb4435d0ed00f9322ab95daa12cd6c0e9ed55db490f'
URLXML = 'https://dev-cm-10.storage.googleapis.com/be753e3e-61af-11ec-9715-4d960ffeffb6/Contrato%20Multiple%20Declaraciones.xml?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=content-manager%40ent-dev-content-manager-id.iam.gserviceaccount.com%2F20220729%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220729T215351Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&generation=1646951569256149&x-goog-signature=31faf134aca735e2bae19b3d04352628e6fe4def8a7bef210c499b724891a66cdf7eb67a3566e2091db3bcca6602f2be965f417e4b9f9c715be9a6704c1bb2a31185c3c217e9d481da9c24f1b09ee82b86259e3acf6956f0af60a36fd431faa23be30bb2388d9e9b7e8ff0cae178b73c547dbe15b4f64e3cc81d95acc4a6f213dac9543329021b819966910ceed8636bab07a7290236cdc3a76b7c91768e2a70ec09bc1cca8cb81cfe0064c68261f30f25cc7850bbabfd9e5efd0f44380246b6d92bc8ae8d8bb69c8a695c31a195cf476cf6050d8525cd92c306714978d13a1578633ab57b5063db962e339e9aa12051f069d62aa3fa08500184695b2a4b2f10'

def encrypt_document_sha256(url_doc):
    req = urllib.request.Request(url_doc, headers={'User-Agent' : "Magic Browser"})
    remote_file = urllib.request.urlopen(req).read()   # aquí el archivo está en BYTES
    with open("bytes_file.pdf", "wb") as binary_file:   
        # Write bytes to file:
        binary_file.write(remote_file)
    with open("bytes_file.pdf","rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
    return (readable_hash)   

hash_pdf = encrypt_document_sha256(URLPDF)
token_autorizacion_response, code = solicitar_login.solictar_login_naat('password','hahernandez@na-at.com.mx','bcc6140ea61458c1b9645d5806dbc4b372f92c444ee5c751730f5a0ba40b622b')
access_token = token_autorizacion_response.get('access_token')
# print('hash_pdf:')
# print(hash_pdf)
# print('access_token:')
# print(access_token)
# print('type_access_token:')
# print(type(access_token))

# import urllib
# from xml.dom.minidom import parse, parseString
# u1 = urllib.request.urlopen(URLXML)
# u1 = urllib.request.urlopen('http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')
# dom = parse(u1)
# print (dom)

def solictar_sellado_doc(url_xml, hash, token):
     print('hash:')
     print(hash)
     print('token:')
     print(token)
     try:
        req = urllib.request.Request(url_xml, headers={'User-Agent' : "Magic Browser"})
        remote_file = urllib.request.urlopen(req).read()   # aquí el archivo está en BYTES        
        with open("bytes_file.xml", "wb") as binary_file:   
        # Write bytes to file:
            binary_file.write(remote_file)
                    
        solictar_sellado_doc_url = 'https://uat.firmaautografa.com/requisitions/createCRPDFFile'
        print("URL_solictar_sellado_doc:")
        print(solictar_sellado_doc_url)
        multipart_form_data = {
                # 'upload': ('custom_file_name.zip', open('myfile.zip', 'rb')),
                'pdf': ('custom_file_name.pdf', open('bytes_file.pdf', 'rb')),
                'xml': ('dom', open('bytes_file.xml', 'rb')),
                # 'xml': (None, dom),
                'hash': (None, hash)
                            }
        
        headers = {
                    # 'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token            
                   }
        
        r = requests.post(solictar_sellado_doc_url,
                        #   json = data,
                        #   files = data,
                        files = multipart_form_data,
                        headers = headers,
                        #   auth = HTTPDigestAuth('fad', 'fadsecret')
                          )
        respuesta = r.json()
        print('CODE_solictar_sellado_doc:', r.status_code)
        if r.status_code == 500:
             respuesta = r
        else:
             respuesta = r.json()
        print("RESPONSE_solictar_sellado_doc: ")
        print(respuesta)
        return respuesta, r.status_code
     except Exception as e:
         print(e)
         return None
     
solictar_sellado_doc(URLXML, hash_pdf, access_token)
