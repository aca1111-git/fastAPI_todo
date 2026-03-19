from app.db.base import Base
from app.db.session import engine

from app.models.todo import TodoDB  # noqa: F401
from app.models.user import UserDB   # noqa: F401

def init_db():
    
    Base.metadata.create_all(bind=engine)
