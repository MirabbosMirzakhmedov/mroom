import base64
import os


def gen_token(byte_length: int) -> str:
    token: str = base64.urlsafe_b64encode(
        s=os.urandom(byte_length)
    ).decode()

    return token

def gen_session_token():
    gen_token(64)
