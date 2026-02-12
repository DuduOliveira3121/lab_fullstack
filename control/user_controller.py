from service.user_service import UserService
class UserController:

    def get_cep_by_cep(cep):
        user_service = UserService
        return user_service.get_cep_by_cep()