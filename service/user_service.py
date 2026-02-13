from model.user import User

class UserService:
    def __init__(self):
        self.model = User()

    def create_user(self, data):
        cpf = data.get("cpf")
        if self.get_user_by_cpf(cpf) is not None:
            return None
        return self.model.create_user(data["nome"], data["email"], data["senha"], cpf)

    def list_users(self):
        return self.model.get_all_user()

    def get_user_by_cpf(self, cpf):
        return self.model.get_user_by_cpf(cpf)

    def delete_user(self, cpf):
        return self.model.delete_user_by_cpf(cpf)