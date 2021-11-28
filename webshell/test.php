<?php
error_reporting(0);
$priv_key = "-----BEGIN PRIVATE KEY-----
MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEA2FXUw5s97bKxqtQz
IIvTFF11gSLeYWT9eMqDcrLSlyyTJ4dvO6dZtlq5tjWJGP32fd5e50zU2KGSI2S+
098j2QIDAQABAkEAs52H2qRxJYLBCpHGpVYSeg0iu4ZE1t5vqTOTMc8RFBuScywF
rACMRZ623AumdcNx614/6bClLA+YKNZQlUQfkQIhAO/kxEtzzOcSEGW1DVptF79O
/Lxsa89hVfO2B1KYNOMtAiEA5twmNpqzYgdJtaXwT5kff1rhJhYjWYST+Og2na/O
3t0CIC07YDut0PO8tzTGJ4dmTHT46rSIaOeIPdGe/9B1/HrdAiA+N0pdIOgDHS+y
MpxG919TtSxEVWcFcwNl6z781CqOSQIhAMZkQLPl3dzTT1Srn0Wb1cl5HczB95cs
ok7dXI72eo6S
-----END PRIVATE KEY-----";
openssl_private_encrypt(time(),$cipher,$priv_key);
$url = $_GET['url'];
$_REQUEST[0] = base64_encode($cipher);
unset($_REQUEST['url']);
$s = http_build_query($_REQUEST);
// echo $s;
// echo $url.'/?'.$s;
echo file_get_contents($url.'&'.$s);