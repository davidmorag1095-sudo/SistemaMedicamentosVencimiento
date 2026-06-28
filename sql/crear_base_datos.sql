CREATE DATABASE IF NOT EXISTS sistema_medicamentos_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE sistema_medicamentos_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    rol VARCHAR(30) NOT NULL,
    activo TINYINT(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS centros_recepcion (
    id_centro INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    responsable VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS medicamentos (
    id_medicamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200),
    categoria VARCHAR(80) NOT NULL,
    presentacion VARCHAR(80) NOT NULL,
    requiere_receta TINYINT(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS donaciones (
    id_donacion INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_centro INT NOT NULL,
    fecha_donacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(30) DEFAULT 'en proceso',
    CONSTRAINT fk_donaciones_usuarios
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_donaciones_centros
        FOREIGN KEY (id_centro) REFERENCES centros_recepcion(id_centro)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS detalle_donacion (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_donacion INT NOT NULL,
    id_medicamento INT NOT NULL,
    cantidad INT NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    lote VARCHAR(50) NOT NULL,
    estado_medicamento VARCHAR(30) DEFAULT 'disponible',
    CONSTRAINT fk_detalle_donacion_donaciones
        FOREIGN KEY (id_donacion) REFERENCES donaciones(id_donacion),
    CONSTRAINT fk_detalle_donacion_medicamentos
        FOREIGN KEY (id_medicamento) REFERENCES medicamentos(id_medicamento)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS solicitudes (
    id_solicitud INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    fecha_solicitud DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(30) DEFAULT 'pendiente',
    observacion VARCHAR(250),
    CONSTRAINT fk_solicitudes_usuarios
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS detalle_solicitud (
    id_detalle_solicitud INT AUTO_INCREMENT PRIMARY KEY,
    id_solicitud INT NOT NULL,
    id_medicamento INT NOT NULL,
    cantidad_solicitada INT NOT NULL,
    cantidad_aprobada INT DEFAULT 0,
    CONSTRAINT fk_detalle_solicitud_solicitudes
        FOREIGN KEY (id_solicitud) REFERENCES solicitudes(id_solicitud),
    CONSTRAINT fk_detalle_solicitud_medicamentos
        FOREIGN KEY (id_medicamento) REFERENCES medicamentos(id_medicamento)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS entregas (
    id_entrega INT AUTO_INCREMENT PRIMARY KEY,
    id_solicitud INT NOT NULL,
    id_detalle_donacion INT NOT NULL,
    id_usuario INT NOT NULL,
    cantidad_entregada INT NOT NULL,
    fecha_entrega DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_entregas_solicitudes
        FOREIGN KEY (id_solicitud) REFERENCES solicitudes(id_solicitud),
    CONSTRAINT fk_entregas_detalle_donacion
        FOREIGN KEY (id_detalle_donacion) REFERENCES detalle_donacion(id_detalle),
    CONSTRAINT fk_entregas_usuarios
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
