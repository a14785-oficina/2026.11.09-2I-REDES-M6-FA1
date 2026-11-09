# Registo, login e logout

Ficheiro: [resources/user.py](../../resources/user.py).

Mantém as classes UserRegister/UserLogin/UserLogout e args dentro das classes. O registo aceita só três campos; strict=True rejeita tipo. O login procura email, compara password como no original e devolve access_token. O logout é a extensão já existente no material.

## Código desta versão

```python
from flask_restful import Resource, reqparse
from models.user import UserModel
from hmac import compare_digest
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from blocklist import BLOCKLIST


class UserRegister(Resource):
    args = reqparse.RequestParser()
    args.add_argument("username", type=str, required=True, nullable=False, help="The field 'username' cannot be left blank!")
    args.add_argument("email", type=str, required=True, nullable=False, help="The field 'email' cannot be left blank!")
    args.add_argument("password", type=str, required=True, nullable=False, help="The field 'password' cannot be left blank!")

    def post(self):
        data = UserRegister.args.parse_args(strict=True)
        if not data["username"].strip() or not data["email"].strip() or not data["password"]:
            return {"message": "Username, email and password cannot be empty!"}, 400
        if "@" not in data["email"]:
            return {"message": "Invalid email!"}, 400
        user_found = UserModel.find_user(data["email"])
        if user_found:
            return {"message": "User with this email already exists!"}, 400
        new_user = UserModel(**data)
        new_user.save_user()
        return new_user.json(), 201  # Created


class UserLogin(Resource):
    args = reqparse.RequestParser()
    args.add_argument("email", type=str, required=True, nullable=False, help="The field 'email' cannot be left blank!")
    args.add_argument("password", type=str, required=True, nullable=False, help="The field 'password' cannot be left blank!")

    def post(self):
        data = UserLogin.args.parse_args(strict=True)
        user = UserModel.find_user(data["email"])
        if user and compare_digest(user.password.encode("utf-8"), data["password"].encode("utf-8")):
            token = create_access_token(identity=str(user.id), additional_claims={"tipo": user.tipo})
            return {"access_token": token}, 200
        return {"message": "Email or password is invalid!"}, 401


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()["jti"]
        BLOCKLIST.add(jwt_id)
        return {"message": "Successfully logged out!"}, 200
```

[Voltar ao início](../INICIO.md)
