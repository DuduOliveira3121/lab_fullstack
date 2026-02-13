class User:
    def __init__(self):
        self._usuarios = [
            
    {
        "nome": "Ana Beatriz Souza",
        "email": "ana.beatriz@exemplo.com.br",
        "senha": "1234",
        "cpf": "123.456.789-00"
    }, 
    {
        "nome": "Carlos Eduardo Lima",
        "email": "cadu.lima@provedor.net",
        "senha": "5678",
        "cpf": "234.567.890-11"
    },
    {
        "nome": "Maria Neves",
        "email": "mari.neves@webmail.com",
        "senha": "9101112",
        "cpf": "345.678.901-22"
    },
    {
        "nome": "Ricardo Oliveira",
        "email": "ricardo.oliveira@empresa.com",
        "senha": "13141516",
        "cpf": "456.789.012-33"
    },
    {
        "nome": "Fernanda Montenegro Silva",
        "email": "fernanda.ms@exemplo.org",
        "senha": "17181920",
        "cpf": "567.890.123-44"
    }
        ]

    def create_user(self, nome, email, senha, cpf):
        user = {"nome": nome, "email": email, "senha": senha, "cpf": cpf}
        self._usuarios.append(user)
        return user

    def get_user_by_cpf(self, cpf):
        for u in self._usuarios:
            if (u["cpf"] == cpf):
                return u
    
    def get_all_user(self):
        return self._usuarios

    def delete_user_by_cpf(self, cpf):
        for us in self._usuarios:
            if (us["cpf"] == cpf):
                self._usuarios.remove(us)
                return True


def validate_user_data(data):
    if not isinstance(data, dict):
        return False, "Dados devem ser um objeto JSON"

    campos_obrigatorios = ["nome", "email", "senha", "cpf"]
    for campo in campos_obrigatorios:
        if campo not in data or not str(data.get(campo)).strip():
            return False, f"Campo obrigatório ausente ou vazio: {campo}"

    email = data.get("email", "")
    if "@" not in email:
        return False, "Email inválido"

    cpf = str(data.get("cpf", "")).strip()
    if not cpf:
        return False, "CPF inválido"

    return True, None