from sqlalchemy import asc
from domain.models.patiens import Patiens
from domain.models.consults import Consults
from insfrastructure.repositories.base_repository import BaseRepository


class RepositoryPatiens(BaseRepository[Patiens]):
    """Repositorio de pacientes"""

    def get_by_rut(self, rut: str) -> Patiens | None:
        """Busca un paciente por su rut"""
        return self.session.filter(Patiens.rut == rut).first()

    def get_all_order(self) -> list[Patiens]:
        """Obtiene todos los pacientes ordenados por nombre"""
        return self.session.query(Patiens).order_by(asc(Patiens.name)).all()

    def get_consults(self, patiens_id: int) -> list[Consults]:
        """Obtiene las consultas de un paciente"""
        return (
            self.session.query(Consults).filter(Consults.patiens_id == patiens_id).all()
        )

    def get_first_consult(self, patiens_id: int) -> Consults | None:
        """Obtiene la primera consulta de un paciente"""
        return (
            self.session.query(Consults)
            .filter(Consults.patiens_id == patiens_id)
            .order_by(asc(Consults.date))
            .first()
        )

    def get_last_consult(self, patiens_id: int) -> Consults | None:
        """Obtiene la última consulta de un paciente"""
        return (
            self.session.query(Consults)
            .filter(Consults.patiens_id == patiens_id)
            .order_by(asc(Consults.date))
            .last()
        )
