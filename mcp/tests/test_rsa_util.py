import pytest
import rsa_util


def test_encrypt_decrypt():
    message = "Hello RSA!"
    encrypted = rsa_util.encrypt(message)
    decrypted = rsa_util.decrypt(encrypted)
    assert message == decrypted


def test_unicode():
    message = "你好 RSA!"
    encrypted = rsa_util.encrypt(message)
    decrypted = rsa_util.decrypt(encrypted)
    assert message == decrypted


@pytest.mark.parametrize(
    "message",
    ["Short", "Medium length message", "中文测试", "Hello World! 123 @#$%"],
)
def test_various_messages(message):
    encrypted = rsa_util.encrypt(message)
    decrypted = rsa_util.decrypt(encrypted)
    assert message == decrypted


def test_wolf_encrypt():
    message = """{"code":"1","username":"analyzer1@datatist.com","password":"Abc123@@@@@@","codeKey":"10ffa87a54e1445"}"""
    encrypted = rsa_util.encrypt(message)
    decrypted = rsa_util.decrypt(encrypted)
    assert message == decrypted
