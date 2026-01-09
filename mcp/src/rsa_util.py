#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


# 示例公钥和私钥（这些你可以从外部文件中获取，或者使用自己的密钥）
public_key_pem = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCg0gUguagtMMjJ1KD6fpPkWfofbncqpcdJeVBA764C1VjY3/ttzck6+hKsiAdboQJtugH/X4MjRM8EFe488jdPbh64DO/pmXObWj701lPLuHmZ+H9H1MTCiPRGH8UOdHde9r7ZVl1JsOYQHEf8nLQIkU2ifUhjOHFA+5ReH9gTEQIDAQAB
-----END PUBLIC KEY-----"""

private_key_pem = """-----BEGIN RSA PRIVATE KEY-----
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAKDSBSC5qC0wyMnUoPp+k+RZ+h9udyqlx0l5UEDvrgLVWNjf+23NyTr6EqyIB1uhAm26Af9fgyNEzwQV7jzyN09uHrgM7+mZc5taPvTWU8u4eZn4f0fUxMKI9EYfxQ50d172vtlWXUmw5hAcR/yctAiRTaJ9SGM4cUD7lF4f2BMRAgMBAAECgYALtb8x1tLsF3VHXPgrxTO3mOWhjEWZEWEldHPnhoxBII/LmuOP50ATz0m0zmLaxSqMGtMyaR3/X29DeOVUAr8MJ9Zbj2ON1xh0/D941AupShJgQtryXLzrHX8JHbcJbNWJHexgKPN75e516ZUC+sAxwZ3VX4ziexetuJg5bug/wQJBAOOHXzsdubtzQiQTFwMdhXoRNaBcgFNUiKvsYOUjN7GeFN4W+bWDTo/fwbV/lknL3zlLG79RNfeCSct3tcD1ox0CQQC08bg3XgfP7hq6wql9/tb+6Ja0qh4AFQkF5rWNBk+UVu5/XKgxtywxa9A5Ikfdkrq8Pjw08GppX8su70V+VpmFAkEA4PvnKumF0tlxuYI26xmx9rY1tNBDBCM+0eH3Hhzo4XVTZRiK6vVgJdw4C2SSE37IyDqAwXloR8pJdix1SMyb8QJBAKdinLmLYMq3Rz7RaR3HK3gwDYoffRUyYGB3JifJWMCvEn37ZxRmkJk/VSYlUjnkzJ3rLKMEbEwCc+F9MtpGnkkCQBIghTOn/o7CWlAUO83lZBlwZuaTox5/l5LhM2TBLh5PamiI6kX+GrRn4NpTQwfvStkjZZHV8/zZIkWDqeLNkDw=
-----END RSA PRIVATE KEY-----"""


# 加密方法：使用公钥加密
def encrypt(message: str) -> str:
    # 加载公钥
    public_key_obj = RSA.import_key(public_key_pem)

    # 使用OAEP模式创建加密对象
    cipher = PKCS1_v1_5.new(public_key_obj)

    # 加密消息
    encrypted_message = cipher.encrypt(message.encode())

    # 返回加密后的消息，使用base64编码表示
    return base64.b64encode(encrypted_message).decode()


# 解密方法：使用私钥解密
def decrypt(encrypted_message_base64: str) -> str:
    # 将 base64 编码的加密消息解码成字节
    encrypted_message = base64.b64decode(encrypted_message_base64)

    # 加载私钥
    private_key_obj = RSA.import_key(private_key_pem)

    # 使用私钥创建解密对象
    cipher = PKCS1_v1_5.new(private_key_obj)

    # 解密消息
    decrypted_message = cipher.decrypt(encrypted_message, None)

    # 返回解密后的消息
    return decrypted_message.decode()
