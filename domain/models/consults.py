from sqlachemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Date, Float, Text, String, Enum as SAEnum
from infrastructure.database import Base
from datetime import date
import enum


# Enumeracion de niveles de actividad fisica
class NivelActividad(enum.Enum):
    SEDENTARIO = "sedentario"
    LIGERO = "ligero"
    MODERADO = "moderado"
    ACTIVO = "activo"
    MUY_ACTIVO = "muy_activo"


# Modelo de datos para la tabla "consulta"
class Consulta(Base):
    __tablemame__ = "consultas"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    paciente_id: Mapped[int] = mapped_column(ForeignKey("pacientes.id"), nullable=False)
    fecha: Mapped[date] = mapped_column(Date, default=date.today)
    # Mediciones
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    cinrcunferencia_cintura: Mapped[float] = mapped_column(Float, nullable=True)
    # Clinico
    actividad_fisica: Mapped[NivelActividad] = mapped_column(
        SAEnum(NivelActividad), nullable=False
    )
    enfermedades: Mapped[str] = mapped_column(Text, nullable=True)
    enfermedades_hereditarias: Mapped[str] = mapped_column(Text, nullable=True)
    enfermedades_tags: Mapped[str] = mapped_column(String(500), nullable=True)
    encuesta_alimentaria: Mapped[str] = mapped_column(Text, nullable=True)
    # Plieges
    pliegue_tricipital: Mapped[float] = mapped_column(Float, nullable=True)
    pliegue_subescapular: Mapped[float] = mapped_column(Float, nullable=True)
    pliegue_suprailiaco: Mapped[float] = mapped_column(Float, nullable=True)
    pliegue_abdominal: Mapped[float] = mapped_column(Float, nullable=True)
    pliegue_muslo: Mapped[float] = mapped_column(Float, nullable=True)

    # Relacion con paciente
    paciente: Mapped["Paciente"] = relationship("Paciente", back_populates="consultas")

    # Representacion del objeto para debugging
    def __repr__(self):
        return f"<Consulta {self.id} - Paciente {self.paciente_id} - {self.fecha})>"
