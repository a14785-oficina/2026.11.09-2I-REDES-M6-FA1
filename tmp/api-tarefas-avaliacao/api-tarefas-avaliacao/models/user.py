from con_sql import bd


class UserModel(bd.Model):
    __tablename__ = "Utilizador"
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    username = bd.Column(bd.String(80), nullable=False)
    email = bd.Column(bd.String(120), unique=True, nullable=False)
    password = bd.Column(bd.String(120), nullable=False)
    tipo = bd.Column(bd.String(20), nullable=False, default="utilizador")
    tarefas = bd.relationship("TaskModel", backref="utilizador", lazy=True)

    # Class Constructor
    def __init__(self, username, email, password, tipo="utilizador"):
        self.username = username
        self.email = email.strip().lower()
        self.password = password
        self.tipo = tipo

    # Method to return the user data in JSON format
    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "tipo": self.tipo
        }

    @classmethod
    def find_user(cls, email):
        user = cls.query.filter_by(email=email.strip().lower()).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_by_id(cls, user_id):
        user = cls.query.filter_by(id=user_id).first()
        if user:
            return user
        return None

    def save_user(self):
        bd.session.add(self)
        bd.session.commit()
