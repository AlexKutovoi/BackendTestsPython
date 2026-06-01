from src.main.api.db.models.account_table import Account
from sqlalchemy.orm import Session


class AccountCrubDb:
    @staticmethod
    def get_account_by_id(db: Session , account_id:int) -> Account | None:
        return db.query(Account).filter(Account.id == account_id).first()

