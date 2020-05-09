import hashlib
from typing import Tuple


def get_username_hash(user_name) -> int:
    user_name_hash = int(hashlib.sha256(user_name.encode()).hexdigest(), base=16)
    return user_name_hash


def get_password_hash(password) -> int:
    password_hash = int(hashlib.sha256(password.encode()).hexdigest(), base=16)
    print("password in hash: " + hex(password_hash) + "\n")
    return password_hash


def get_address_database(user_name_hash: int, password_hash: int) -> Tuple[str, str]:
    user_xor_password = user_name_hash ^ password_hash
    address = hex(user_xor_password)[2:4]
    x = address[0]
    y = address[1]
    print("username XOR password: " + hex(user_xor_password) + "\n")
    print("Database Address: " + x + ", " + y + "\n")
    return x, y


def get_address_PUF(password_hash: int) -> tuple:
    address = hex(password_hash)[2:]
    x = address[:2]
    y = address[2:4]
    print("PUF Address: " + x + ", " + y + "\n")
    return x, y


# print(get_address_PUF("yj345@nau"))
