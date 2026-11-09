from flask import Flask
from flask_restful import Api
from resources.task import Task, Tasks
from resources.user import UserRegister, UserLogin, UserLogout
from models.user import UserModel
from con_sql import bd
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST

# Variable representing the Flask application
app = Flask(__name__)

# Variable representing the Flask-RESTful API
api = Api(app)
jwt = JWTManager(app)

# Configurations for the database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "a_chave_da_api_tarefas_para_os_testes_da_avaliacao"
app.config["JWT_BLACKLIST_ENABLED"] = True


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return {"message": "Please log in again."}, 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return {"message": "Invalid token!"}, 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return {"message": "Token expired. Please log in again."}, 401


# Routes
api.add_resource(Tasks, "/tarefas")
api.add_resource(Task, "/tarefas/<int:id_task>")
api.add_resource(UserRegister, "/registo")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogout, "/logout")

if __name__ == "__main__":
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
        admin = UserModel.query.filter_by(tipo="admin").first()
        if not admin:
            if UserModel.find_user("admin@exemplo.pt"):
                raise RuntimeError("The initial admin email already belongs to another account.")
            admin = UserModel("admin", "admin@exemplo.pt", "Admin123!", tipo="admin")
            admin.save_user()
    app.run(host="127.0.0.1", port=5000, debug=True)
