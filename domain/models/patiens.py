from sqlalchemy import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Enum as SAEnum
from infrastructure.database import Base
from datetime import date
import enum


# Enumeración para el sexo del paciente
class Sexo(enum.Enum):
    M = "M"
    F = "F"


# Modelo de datos para la tabla "pacientes"
class Paciente(Base):
    __tablename__ = "pacientes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rut: Mapped[str] = mapped_column(String(12), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    fecha_nacimento: Mapped[date] = mapped_column(Date, nullable=False)
    sexo: Mapped[Sexo] = mapped_column(SAEnum(Sexo), nullable=False)
    ocupacion: Mapped[str] = mapped_column(String(100), nullable=True)
    objetivo_consulta: Mapped[str] = mapped_column(String(500), nullable=True)
    fecha_registro: Mapped[date] = mapped_column(
        Date, default=date.today, nullable=False
    )

    # Relación con consultas
    consultas: Mapped[list["Consulta"]] = relationship(
        back_populates="paciente", casecade="all, delete-orphan"
    )

    # Representación legible del objeto Paciente
    def __repr__(self):
        return f"<Paciente {self.rut} - {self.nombre}>"
