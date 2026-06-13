# Propuesta: backups con pg_dump desde la terminal

## Contexto

`pg_dump` viene incluido con el paquete `postgresql-client` que ya instalamos en el devcontainer. No requiere ningún cambio de dependencias.

## El problema

`pg_dump` escribe el backup donde el usuario indique. Sin configuración extra, el alumno tendría que escribir la ruta completa cada vez:

```bash
pg_dump veterinariadb > data/veterinariadb.sql
```

El objetivo es que el backup vaya a `data/` automáticamente, igual que los backups de pgAdmin.

## Propuesta: función `pgbackup` en el shell

Extender el `postCreateCommand` en `devcontainer.json` para agregar una función al `.bashrc` del contenedor `workspace`:

```json
"postCreateCommand": "sudo apt-get update -qq && sudo apt-get install -y postgresql-client && echo 'pgbackup() { local db=${1:-$PGDATABASE}; pg_dump \"$db\" > /workspaces/postgrespace/data/${db}.sql && echo \"Backup guardado en data/${db}.sql\"; }' >> ~/.bashrc"
```

Con esto el alumno solo escribe:

```bash
# Respalda la base de datos activa (PGDATABASE)
pgbackup

# O especificando la base de datos
pgbackup veterinariadb
```

Y el archivo aparece en `data/veterinariadb.sql`, junto a los backups de pgAdmin.

## Lo que NO cambia

- `pg_dump` sigue funcionando exactamente igual para quien quiera usarlo directamente.
- No se agrega ningún archivo extra al proyecto — solo una línea al `postCreateCommand` ya existente.
- El `postgresql-client` ya está instalado; solo se encadena la función con `&&`.

## Restaurar un backup

Con el archivo `.sql` en `data/`, la restauración desde terminal sería:

```bash
psql veterinariadb < data/veterinariadb.sql
```

---

¿Apruebas este enfoque?
