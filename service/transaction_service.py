from db import FundTransaction
from decimal import Decimal
from connect import session_factory
from fastapi import HTTPException
from typing import Literal



def create_transaction(
    account_id: int,
    team_id: int,
    amount: Decimal,
    transaction_id: str,
    payment_method: str,
    type: str,
    receipt: str | None = None,
    status: str = "pending",
):
    with session_factory() as db:  
        transaction = FundTransaction(
            account_id=account_id,
            team_id=team_id,
            amount=amount,
            transaction_id=transaction_id,
            receipt=receipt,
            status=status,
            payment_method=payment_method,
            type=type,
        )

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction
    

def query_transaction(
    value,
    field: str = Literal["account_id","team_id","transaction_id","status","type"],
):
    
    with session_factory() as db: 
        return (
            db.query(FundTransaction)
            .filter(field == value)
            .all()
        )