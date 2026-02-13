"""Serviço simples de usuário em memória.

Fornece funções: create_user, list_users, get_user_by_cpf, delete_user
Armazenamento: lista de dicionários em memória.
"""

users = []

def create_user(data):
    cpf = data.get("cpf")
    if get_user_by_cpf(cpf) is not None:
        return None

    user = {
        "nome": data.get("nome"),
        "email": data.get("email"),
        "senha": data.get("senha"),
        "cpf": cpf
    }
    users.append(user)
    return user

def list_users():
    return users

def get_user_by_cpf(cpf):
    for u in users:
        if u.get("cpf") == cpf:
            return u
    return None

def delete_user(cpf):
    for u in list(users):
        if u.get("cpf") == cpf:
            users.remove(u)
            return True
    return False