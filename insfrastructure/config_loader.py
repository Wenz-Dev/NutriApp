import json
from pathlib import Path


class ConfigLoader:
    _instance = None
    _config = None

    # Implementación del patrón Singleton para asegurar que solo haya una instancia de ConfigLoader
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Método para leer el archivo config.json y cargar su contenido en la memoria
    def load(self, path: str = "config.json") -> dict:
        if self._config is None:
            config_path = Path(path)
            if not config_path.exists():
                raise FileNotFoundError(f"No se encuentra el archivo: {path}")
            with open(config_path, "r", encoding="utf-8") as f:
                self._config = json.load(f)
        return self._config

    # Método para obtener un valor específico de la configuración
    def get(self, key: str):
        if self._config is None:
            raise ValueError(
                "La configuración no ha sido cargada. Llama a load() primero."
            )
        return self._config.get(key)


# Instancia global del ConfigLoader
config = ConfigLoader()
