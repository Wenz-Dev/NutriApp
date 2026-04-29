from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from insfrastructure.config_loader import config
from contextlib import contextmanager


# Clase base para los modelos
class Base(DeclarativeBase):
    pass


# Construye la URL de conexión a la base de datos según la configuración (config.json)
def build_url() -> str:
    db_type = config.get("db_type")

    if db_type == "sqlite":
        path = config.get("sqlite_path")
        return f"sqlite:///{path}"

    db = config.get("external_db")
    return f"{db['engine']}://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['name']}"


# Inicia el engine y retorna la fabrica de sesiones
def init_db() -> sessionmaker:
    url = build_url()
    engine = create_engine(url, echo=False)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


# Variable global para almacenar la fábrica de sesiones
_SessionFactory = None


# Llama solo una vez al main
def setup_database():
    global _SessionFactory
    _SessionFactory = init_db()


# Entrega la sesion lista para usar y la cierra al finalizar
@contextmanager
def get_session():
    session = _SessionFactory()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
