from con_sql import bd


class TaskModel(bd.Model):
    __tablename__ = "Tarefa"
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    titulo = bd.Column(bd.String(120), nullable=False)
    descricao = bd.Column(bd.Text, nullable=False)
    estado = bd.Column(bd.String(20), nullable=False)
    utilizador_id = bd.Column(bd.Integer, bd.ForeignKey("Utilizador.id"), nullable=False)

    # Class Constructor
    def __init__(self, titulo, descricao, estado, utilizador_id):
        self.titulo = titulo
        self.descricao = descricao
        self.estado = estado
        self.utilizador_id = utilizador_id

    # Method to return the task data in JSON format
    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "estado": self.estado,
            "utilizador_id": self.utilizador_id
        }

    @classmethod
    def find_task(cls, id_task):
        task = cls.query.filter_by(id=id_task).first()
        if task:
            return task
        return None

    def save_task(self):
        bd.session.add(self)
        bd.session.commit()

    def delete_task(self):
        bd.session.delete(self)
        bd.session.commit()

    def update_task(self, titulo_updated, descricao_updated, estado_updated):
        self.titulo = titulo_updated
        self.descricao = descricao_updated
        self.estado = estado_updated
        bd.session.commit()
