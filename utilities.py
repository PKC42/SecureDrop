from threading import stack_size
import hashlib


def check_lower(st):
    for c in st:
        if c.islower():
            return True
    return False

def check_upper(st):
    for c in st:
        if c.isupper():
            return True
    return False

def check_number(st):
    for c in st:
        if c.isdigit():
            return True
    return False

def check_symbol(st):
    special_characters = "!@#$%^&*()-+?_=,<>/\""
    if any(c in special_characters for c in st):
        return True
    return False

def hash_string(st, salt):
    key = hashlib.pbkdf2_hmac('sha256', st.encode('utf-8'), salt, 100000)
    return key