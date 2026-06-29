import hashlib


def generate_document_id(text: str):

    return hashlib.md5(
        text.encode("utf-8")
    ).hexdigest()