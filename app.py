from flask import Flask
from control.user_controller import UserController

app = Flask(__name__)

@app.route("/<cep>")
def get_by_cep(cep):
    user_controller = UserController
    return user_controller.get_cep_by_cep(cep)