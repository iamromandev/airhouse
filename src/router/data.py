from fastapi import APIRouter, Depends
from sqlmodel import Session

router = APIRouter(prefix="/data", tags=["Data"])

from src.db.database import Database
from src.db.model.data import DataRead


@router.post("/", response_model=DataRead)
async def read_data(
    session: Session = Depends(Database.get_session)
) -> DataRead:
    return DataRead()
