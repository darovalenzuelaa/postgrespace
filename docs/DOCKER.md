# ¿Qué es Docker?

## Concepto simple

Docker es como una **caja de embalaje digital**. Imagina que necesitas enviar una aplicación:

- Sin Docker: Tienes que decirle a alguien "instala PostgreSQL versión 16, pgAdmin versión X, con estas configuraciones exactas..."
- Con Docker: Le envías una "caja" (contenedor) que ya tiene todo configurado y listo.

## ¿Por qué es útil?

### 1. **Consistencia**
Si funciona en tu máquina, funciona en cualquier máquina. No hay sorpresas.

```
Tu computadora          →  Servidor en la nube      →  Máquina de otro alumno
(funciona)                 (funciona igual)              (funciona igual)
```

### 2. **No contaminas tu sistema**
Sin Docker, instalar PostgreSQL modifica tu máquina. Con Docker, todo está aislado.

```
Tu máquina (limpia)
├── navegador
├── VS Code
└── Docker
    └── postgrespace (PostgreSQL, pgAdmin)
       (todo dentro, sin afectar tu máquina)
```

### 3. **Fácil compartir**
En lugar de un manual de 20 páginas, compartes un archivo: `docker-compose.yml`

## Contenedores vs Máquinas Virtuales

| Característica | Docker | Máquina Virtual |
|----------------|--------|-----------------|
| **Tamaño** | Pequeño (MB) | Grande (GB) |
| **Velocidad** | Muy rápido | Más lento |
| **Sistema Operativo** | Comparte el del host | Sistema completo separado |
| **Uso de recursos** | Eficiente | Consume más |

## En este proyecto

En `postgrespace` usamos Docker para ejecutar:

```
postgrespace/
└── .devcontainer/
    └── docker-compose.yml
        ├── postgres:16 (contenedor de base de datos)
        └── pgadmin:latest (contenedor de interfaz)
```

En lugar de instalar PostgreSQL en tu máquina, se ejecuta dentro de Docker.

## Términos clave

- **Contenedor**: Una "caja" en ejecución con una aplicación
- **Imagen**: El plano de una caja (las instrucciones para crear el contenedor)
- **Docker Compose**: Una herramienta que permite ejecutar múltiples contenedores juntos

## ¿Necesito saber mucho de Docker?

No. Para este proyecto solo necesitas:
1. Entender que PostgreSQL y pgAdmin están aislados en contenedores
2. Que cambios en tu máquina no afectan los contenedores (y viceversa)
3. Que todo está configurado en `.devcontainer/docker-compose.yml`

El profesor se encargó del resto.
