# CRUD e permissões

Ficheiro: [resources/task.py](../../resources/task.py).

Tasks trata de GET/POST da coleção. Task trata de GET/PUT/DELETE de um ID. O parser Task.args é usado pelo POST e PUT. Os métodos consultam a conta, procuram a tarefa e verificam o tipo/proprietário diretamente. No PUT enviam-se titulo, descricao e estado.

## Código desta versão

```python
from flask_restful import Resource, reqparse
from models.task import TaskModel
from models.user import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity


# List and insert tasks
class Tasks(Resource):
    @jwt_required()
    def get(self):
        user = UserModel.find_user_by_id(get_jwt_identity())
        if not user:
            return {"message": "User not authenticated!"}, 401
        if user.tipo == "admin":
            return {"tarefas": [task.json() for task in TaskModel.query.all()]}, 200
        return {"tarefas": [task.json() for task in TaskModel.query.filter_by(utilizador_id=user.id).all()]}, 200

    @jwt_required()
    def post(self):
        user = UserModel.find_user_by_id(get_jwt_identity())
        if not user:
            return {"message": "User not authenticated!"}, 401
        data = Task.args.parse_args(strict=True)
        if not data["titulo"].strip():
            return {"message": "The title cannot be empty!"}, 400
        new_task = TaskModel(utilizador_id=user.id, **data)
        new_task.save_task()
        return new_task.json(), 201  # Created


# List, update and delete a specific task
class Task(Resource):
    args = reqparse.RequestParser()
    args.add_argument("titulo", type=str, required=True, nullable=False, help="The field 'titulo' cannot be left blank!")
    args.add_argument("descricao", type=str, required=True, nullable=False, help="The field 'descricao' cannot be left blank!")
    args.add_argument("estado", type=str, required=True, nullable=False, choices=("Pendente", "Em curso", "Concluída"), help="Use Pendente, Em curso or Concluída!")

    @jwt_required()
    def get(self, id_task):
        user = UserModel.find_user_by_id(get_jwt_identity())
        if not user:
            return {"message": "User not authenticated!"}, 401
        task_found = TaskModel.find_task(id_task)
        if not task_found:
            return {"message": "Task not found!"}, 404
        if user.tipo != "admin" and task_found.utilizador_id != user.id:
            return {"message": "You don't have permission to access this task!"}, 403
        return task_found.json(), 200

    @jwt_required()
    def put(self, id_task):
        user = UserModel.find_user_by_id(get_jwt_identity())
        if not user:
            return {"message": "User not authenticated!"}, 401
        task_found = TaskModel.find_task(id_task)
        if not task_found:
            return {"message": "Task not found!"}, 404
        if user.tipo != "admin" and task_found.utilizador_id != user.id:
            return {"message": "You don't have permission to update this task!"}, 403
        data = Task.args.parse_args(strict=True)
        if not data["titulo"].strip():
            return {"message": "The title cannot be empty!"}, 400
        task_found.update_task(data["titulo"], data["descricao"], data["estado"])
        return task_found.json(), 200

    @jwt_required()
    def delete(self, id_task):
        user = UserModel.find_user_by_id(get_jwt_identity())
        if not user:
            return {"message": "User not authenticated!"}, 401
        task_found = TaskModel.find_task(id_task)
        if not task_found:
            return {"message": "Task not found!"}, 404
        if user.tipo != "admin" and task_found.utilizador_id != user.id:
            return {"message": "You don't have permission to delete this task!"}, 403
        task_found.delete_task()
        return {"message": "Task has been deleted!"}, 200
```

[Voltar ao início](../INICIO.md)
