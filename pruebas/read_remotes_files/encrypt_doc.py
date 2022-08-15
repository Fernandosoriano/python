# import urllib.request
# import hashlib
# # import PyPDF2
# import io
# import sys

# URL = 'https://dev-cm-09.storage.googleapis.com/f57827f8-5d08-11ec-a74e-8d9b0df948b3/Contrato%20Multiple%20Declaraciones.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=content-manager%40ent-dev-content-manager-id.iam.gserviceaccount.com%2F20220729%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220729T215351Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&generation=1640055486588645&x-goog-signature=5af48d31aad64ad0cd8919cbd27d58fb24ad0b86f10f56d6b6d68ca9da60b75c3bd7c0d4b3d842a1e82f37887b79da88bb0f6e52964ba1b67fdcb21027d93f1da23cb41291352ef81275c5f9f5236a73927f6fea190e24f22514abd6ddd13f851b78ce7b0a48be9c418fe05dc456bf84eeb68a886a0436c91a56d2a85b9e3420b4101b7cc44476edf4221d992c8146b3f37cd4966d0a35625281b73899466a0324f156144c2ef7b3c72c324b6e79156d6934d047399fa664eb90f977805e4b3b931160ccd177eb4d4a97d0fc70036c23978a6d332cf208f1d166aa46850e94eb921fef9d3dcf770dcf40dfb4435d0ed00f9322ab95daa12cd6c0e9ed55db490f'
# req = urllib.request.Request(URL, headers={'User-Agent' : "Magic Browser"})
# remote_file = urllib.request.urlopen(req).read()   # aquí el archivo está en BYTES
#remote_file_string = io.StringIO(remote_file) #esto falla porque la entrada para stringio debe ser una cadena, no bytes
#remote_file_bytes = io.BytesIO(remote_file)  #Siguen siendo bytes pero en otro tipo de objeto, el cual por cierto no acepta open de plano
#pdfdoc_remote = PyPDF2.PdfFileReader(remote_file_bytes)
#binary_file = bin(int.from_bytes(remote_file, byteorder=sys.byteorder)) #lo convierto a binario , funciona con esto, pero tarda demasiado. y genera un binario igual 
# print (type(remote_file))
# with open(remote_file,"rb") as f:
#     bytes = f.read() # read entire file as bytes
#     readable_hash = hashlib.sha256(bytes).hexdigest();
#     print(readable_hash)

# print(remote_file)  es una cadena con el file en bytes

# with open("bytes_to_file.txt", "wb") as binary_file:   
#     # Write bytes to file:
#     binary_file.write(remote_file)
# with open("bytes_to_file.txt","rb") as f:
#     bytes = f.read() # read entire file as bytes
#     readable_hash = hashlib.sha256(bytes).hexdigest();
#     print(readable_hash)    
# with open('bytes_to_file.txt', 'rb') as f:
#      for line in f:
#          hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
#          print(hashed_line)
               
# ====================================================================================================            
# with open('https://dev-cm-09.storage.googleapis.com/f57827f8-5d08-11ec-a74e-8d9b0df948b3/Contrato%20Multiple%20Declaraciones.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=content-manager%40ent-dev-content-manager-id.iam.gserviceaccount.com%2F20220729%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220729T215351Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&generation=1640055486588645&x-goog-signature=5af48d31aad64ad0cd8919cbd27d58fb24ad0b86f10f56d6b6d68ca9da60b75c3bd7c0d4b3d842a1e82f37887b79da88bb0f6e52964ba1b67fdcb21027d93f1da23cb41291352ef81275c5f9f5236a73927f6fea190e24f22514abd6ddd13f851b78ce7b0a48be9c418fe05dc456bf84eeb68a886a0436c91a56d2a85b9e3420b4101b7cc44476edf4221d992c8146b3f37cd4966d0a35625281b73899466a0324f156144c2ef7b3c72c324b6e79156d6934d047399fa664eb90f977805e4b3b931160ccd177eb4d4a97d0fc70036c23978a6d332cf208f1d166aa46850e94eb921fef9d3dcf770dcf40dfb4435d0ed00f9322ab95daa12cd6c0e9ed55db490f', 'rb') as f:
#      for line in f:
#          hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
#          print(hashed_line)
 
# DUDA   ????????????'
# habra alguna forma de ponerlo tipo:'
# with open('https://e6v4p8w2.rocketcdn.me/Users/datagy/Desktop/sample.txt', 'rb') as f:      

# ======================================================================================================
#EN local funciona
# with open('C:/Users/Praxis/Documents/Contrato Multiple Declaraciones.pdf', 'rb') as f:
#      for line in f:
#          hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
#          print(hashed_line)
# ===========================================================================================================

# import urllib.request
# import hashlib
# URL = 'https://dev-cm-09.storage.googleapis.com/f57827f8-5d08-11ec-a74e-8d9b0df948b3/Contrato%20Multiple%20Declaraciones.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=content-manager%40ent-dev-content-manager-id.iam.gserviceaccount.com%2F20220729%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220729T215351Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&generation=1640055486588645&x-goog-signature=5af48d31aad64ad0cd8919cbd27d58fb24ad0b86f10f56d6b6d68ca9da60b75c3bd7c0d4b3d842a1e82f37887b79da88bb0f6e52964ba1b67fdcb21027d93f1da23cb41291352ef81275c5f9f5236a73927f6fea190e24f22514abd6ddd13f851b78ce7b0a48be9c418fe05dc456bf84eeb68a886a0436c91a56d2a85b9e3420b4101b7cc44476edf4221d992c8146b3f37cd4966d0a35625281b73899466a0324f156144c2ef7b3c72c324b6e79156d6934d047399fa664eb90f977805e4b3b931160ccd177eb4d4a97d0fc70036c23978a6d332cf208f1d166aa46850e94eb921fef9d3dcf770dcf40dfb4435d0ed00f9322ab95daa12cd6c0e9ed55db490f'
# def encrypt_document_sha256(url_doc):
#     list_encrypt = []
#     doc_encrypt = ""
#     req = urllib.request.Request(url_doc, headers={'User-Agent' : "Magic Browser"})
#     remote_file = urllib.request.urlopen(req).read()   # aquí el archivo está en BYTES
#     with open("bytes_to_file.pdf", "wb") as binary_file:   
#     # Write bytes to file:
#         binary_file.write(remote_file)
#     with open('bytes_to_file.pdf', 'rb') as f:
#      for line in f:
#          hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
#          list_encrypt.append(hashed_line)
#     return (doc_encrypt.join(list_encrypt))
    
# print(encrypt_document_sha256(URL))

# ======================================================================================================================
import urllib.request
import hashlib
URL = 'https://dev-cm-09.storage.googleapis.com/f57827f8-5d08-11ec-a74e-8d9b0df948b3/Contrato%20Multiple%20Declaraciones.pdf?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=content-manager%40ent-dev-content-manager-id.iam.gserviceaccount.com%2F20220729%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220729T215351Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&generation=1640055486588645&x-goog-signature=5af48d31aad64ad0cd8919cbd27d58fb24ad0b86f10f56d6b6d68ca9da60b75c3bd7c0d4b3d842a1e82f37887b79da88bb0f6e52964ba1b67fdcb21027d93f1da23cb41291352ef81275c5f9f5236a73927f6fea190e24f22514abd6ddd13f851b78ce7b0a48be9c418fe05dc456bf84eeb68a886a0436c91a56d2a85b9e3420b4101b7cc44476edf4221d992c8146b3f37cd4966d0a35625281b73899466a0324f156144c2ef7b3c72c324b6e79156d6934d047399fa664eb90f977805e4b3b931160ccd177eb4d4a97d0fc70036c23978a6d332cf208f1d166aa46850e94eb921fef9d3dcf770dcf40dfb4435d0ed00f9322ab95daa12cd6c0e9ed55db490f'
def encrypt_document_sha256(url_doc):
    req = urllib.request.Request(URL, headers={'User-Agent' : "Magic Browser"})
    remote_file = urllib.request.urlopen(req).read()   # aquí el archivo está en BYTES
    with open("bytes_to_file.txt", "wb") as binary_file:   
        # Write bytes to file:
        binary_file.write(remote_file)
    with open("bytes_to_file.txt","rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
    return (readable_hash)   
    
print(encrypt_document_sha256(URL))


    


    







