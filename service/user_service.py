from model.user import User
class UserService:

    def get_cep_by_cep(cep):
        user_model = User
        for c in user_model.get_ceps():
            if (c["cep"] == cep):
                return c
            
        return user_model.getceps()