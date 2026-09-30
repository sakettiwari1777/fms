from tc_auth.db import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime

class FundTransaction(Base):
    __tablename__ = "fund_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, nullable=False)
    team_id = Column(Integer, nullable=False)

    amount = Column(Numeric(12, 2), nullable=False)
    transaction_id = Column(String(255), nullable=True, unique=True)

    receipt = Column(String(500), nullable=True)
    status = Column(String(50), nullable=False, default="pending")

    payment_method = Column(String(50), nullable=False)

    type = Column(String(20), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )