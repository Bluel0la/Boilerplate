from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.sql import func
from api.db.database import Base

class PlagiarismCheck(Base):
    __tablename__ = "plagiarism_checks"

    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(Integer, ForeignKey("reports.id"), nullable=False)
    similarity_score = Column(Float, nullable=False)  # Percentage (e.g., 12.5)
    checked_at = Column(DateTime(timezone=True), server_default=func.now())
