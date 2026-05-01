from sqlachemy.orm import Session
from typing import TypeVar, Generic, Type

T = TypeVar("T")

"""Repositorio base"""


class BaseRepository(Generic[T]):
    """Inicia y verifica los datos a usar"""

    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    """Obtiene un registro por su id"""

    def get_by_id(self, id: int) -> T | None:
        return self.session.get(self.model, id)

    """Obtiene todos los registros"""

    def get_all(self) -> list[T]:
        return self.session.query(self.model).all()

    """Guarda un registro"""

    def save(self, entity: T) -> T:
        self.session.add(entity)
        self.session.flush()
        return entity

    """Elimina un registro"""

    def delete(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.flush()
