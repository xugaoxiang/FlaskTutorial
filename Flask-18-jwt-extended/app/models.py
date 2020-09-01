from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, username=None, password=None, active=True):
        self.username = username
        self.password = password
        self.active = active

    @staticmethod
    def is_user_exist(username):
        return User.query.filter(User.username == username).first()

    @staticmethod
    def authenticate(username, password):
        flag_user_exist = True
        flag_password_correct = True

        user = User.query.filter(User.username == username).first()
        if user and user.active == 1:
            if not user.password == password:
                flag_password_correct = False
        else:
            flag_user_exist = False

        return flag_user_exist, flag_password_correct, user

    @staticmethod
    def get_users():
        return User.query.filter(User.active == 1).all()

    @staticmethod
    def insert_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update_user():
        db.session.commit()

    @staticmethod
    def deactivate_user():
        db.session.commit()
