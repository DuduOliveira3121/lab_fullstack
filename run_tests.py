"""Teste rápido dos requisitos: validação e CRUD em memória.

Execute: python run_tests.py
"""
import sys
from model.user import validate_user_data
from service.user_service import UserService


def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)


def ok(msg):
    print("OK:", msg)


def main():
    svc = UserService()

    # 1) Lista inicial (há usuários seed no model)
    users = svc.list_users()
    if not isinstance(users, list):
        fail("list_users não retornou lista")
    ok(f"list_users retornou {len(users)} usuários")

    # 2) Validação: falta campo
    invalid = {"nome": "João", "email": "joao@ex.com", "senha": "1"}  # sem cpf
    valid_flag, err = validate_user_data(invalid)
    if valid_flag:
        fail("validate_user_data aceitou dados sem cpf")
    ok("validate_user_data rejeitou entrada sem cpf")

    # 3) Criar usuário válido
    new = {"nome": "Teste", "email": "t@x.com", "senha": "pw", "cpf": "999.999.999-99"}
    valid_flag, err = validate_user_data(new)
    if not valid_flag:
        fail(f"validação falhou para dados válidos: {err}")
    created = svc.create_user(new)
    if created is None:
        fail("create_user retornou None para novo cpf válido")
    ok("create_user criou usuário novo com sucesso")

    # 4) Criar duplicado (mesmo cpf)
    dup = {"nome": "Dup", "email": "d@x.com", "senha": "pw", "cpf": "999.999.999-99"}
    created2 = svc.create_user(dup)
    if created2 is not None:
        fail("create_user permitiu CPF duplicado")
    ok("create_user rejeitou CPF duplicado")

    # 5) Buscar por CPF
    found = svc.get_user_by_cpf("999.999.999-99")
    if not found or found.get("nome") != "Teste":
        fail("get_user_by_cpf não retornou o usuário esperado")
    ok("get_user_by_cpf retornou usuário correto")

    # 6) Deletar usuário
    deleted = svc.delete_user("999.999.999-99")
    if not deleted:
        fail("delete_user falhou ao remover usuário")
    ok("delete_user removeu usuário com sucesso")

    # 7) Confirmar remoção
    after = svc.get_user_by_cpf("999.999.999-99")
    if after is not None:
        fail("Usuário ainda encontrado após delete")
    ok("Usuário não encontrado após delete — OK")

    print("\nTodos os testes passaram.")


if __name__ == '__main__':
    main()
