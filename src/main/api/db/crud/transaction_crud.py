from sqlalchemy.orm import Session
from src.main.api.db.models.transaction_table import Transaction


class TransactionCrudDb:
    @staticmethod
    def get_transaction_by_id(db: Session, transaction_id:int) -> Transaction | None:
        return db.query(Transaction).filter(Transaction.id == transaction_id).first()
    @staticmethod
    def get_transaction_by_account_id(db: Session, account_id:int) -> Transaction | None:
        return db.query(Transaction).filter(Transaction.from_account_id == account_id).first()
    @staticmethod
    def get_transaction_by_to_account_id(db: Session, to_account_id: int) -> Transaction | None:
        return db.query(Transaction).filter(Transaction.to_account_id == to_account_id).first()