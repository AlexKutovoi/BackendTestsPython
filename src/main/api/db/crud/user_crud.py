from sqlalchemy.orm.session import Session
from src.main.api.db.models.user_table import User


class UserCrudDb:
    @staticmethod
    def get_user_by_username(db: Session, username: str ) -> User | None:
        return db.query(User).filter_by(username=username).first()
    @staticmethod
    def get_user_by_role(db: Session, role: str ) -> User | None:
        return db.query(User).filter_by(role=role).first()