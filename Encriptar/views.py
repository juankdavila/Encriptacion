from django.http import HttpResponse
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import base64

def encriptar_texto(request):
    IVKEY = "R3PR353N"
    EncryptionK = "rpaSPvIvVLlrcmtzPU9/c67Gkj7yL1S5"

    sTexto = request.GET.get('texto', '')
    
    IV = IVKEY.encode('ascii')
    EncryptionKey = base64.b64decode(EncryptionK)
    des = DES3.new(EncryptionKey, DES3.MODE_CBC, IV)
    BUFFER = pad(sTexto.encode('utf-8'), DES3.block_size)
    encrypted_text = des.encrypt(BUFFER)
    encrypted_base64 = base64.b64encode(encrypted_text).decode('utf-8')
    return HttpResponse(encrypted_base64, content_type='text/plain')


