from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/data", tags=["Data"])

from src.db.database import Database
from src.db.model.data import Data, DataRead

from src.service.data import DataService


@router.get("/", response_model=List[DataRead])
async def read_data(
    session: Session = Depends(Database.get_session)
) -> List[Data]:
    service = DataService(session)
    return service.get_all()
