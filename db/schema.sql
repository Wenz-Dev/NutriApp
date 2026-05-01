-- db/schema.sql
-- Esquema inicial NutriApp — Fase 1

-- Tabla principal de pacientes
CREATE TABLE IF NOT EXISTS pacientes (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    rut              TEXT NOT NULL UNIQUE,
    nombre           TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL,  -- formato ISO: YYYY-MM-DD
    sexo             TEXT NOT NULL CHECK (sexo IN ('M', 'F')),
    ocupacion        TEXT,
    objetivo_consulta TEXT,
    fecha_registro   TEXT NOT NULL DEFAULT (DATE('now'))
);

-- Tabla de consultas vinculadas a un paciente
CREATE TABLE IF NOT EXISTS consultas (
    id                       INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id              INTEGER NOT NULL,
    fecha                    TEXT NOT NULL DEFAULT (DATE('now')),

    -- Mediciones
    peso                     REAL NOT NULL,
    talla                    REAL NOT NULL,
    circunferencia_cintura   REAL,

    -- Clínico
    actividad_fisica         TEXT NOT NULL CHECK (actividad_fisica IN ('sedentario', 'ligero', 'moderado', 'activo', 'muy_activo'),
    enfermedades             TEXT,
    enfermedades_hereditarias TEXT,
    enfermedades_tags        TEXT,
    encuesta_alimentaria     TEXT,

    -- Pliegues opcionales
    pliegue_tricipital       REAL,
    pliegue_subescapular     REAL,
    pliegue_suprailiaco      REAL,
    pliegue_abdominal        REAL,
    pliegue_muslo            REAL,

    FOREIGN KEY (paciente_id) REFERENCES pacientes (id) ON DELETE CASCADE
);