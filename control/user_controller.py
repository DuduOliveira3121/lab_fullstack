from model.user import User


class UserController:
    def __init__(self):
        # Mantém apenas um wrapper simples para o model
        self.user_model = User()

    # Métodos utilitários podem ser adicionados aqui se necessário