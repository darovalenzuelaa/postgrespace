# ¿Qué es `.gitkeep`?

## El problema

Git tiene una limitación: **solo versiona archivos, no carpetas vacías**.

Imagina que clonamos este proyecto:

```
postgrespace/
├── data/          ← ¿Se crea esta carpeta vacía?
└── .devcontainer/
```

Sin un archivo dentro de `data/`, Git la ignoraría y la carpeta **no se crearía** al clonar. Los alumnos tendrían que crear la carpeta manualmente.

## La solución: `.gitkeep`

`.gitkeep` es un **archivo vacío** que actúa como marcador. Su único propósito es "ocupar" la carpeta para que Git la versione.

```
postgrespace/
├── data/
│   └── .gitkeep   ← Hace que Git version la carpeta
└── .devcontainer/
```

Ahora cuando alguien clona el repositorio, **la carpeta `data/` aparece automáticamente**.

## ¿Es un estándar oficial?

No. Es una **convención comunitaria**. Git no reconoce `.gitkeep` de forma especial, pero la comunidad lo adoptó porque es simple y efectivo.

## Alternativas

| Opción | Ventaja | Desventaja |
|--------|---------|-----------|
| **`.gitkeep`** | Simple, transparente, convención conocida | Archivo "ficticio" sin propósito real |
| **`.gitignore`** | Es un archivo "real" con propósito | Menos obvio que la carpeta debe existir |
| **Script de setup** | Automático, profesional | Más complejidad |

## En este proyecto

Se usa `.gitkeep` en `data/` porque:
- ✅ Los alumnos clonan y esperan que todo funcione
- ✅ Sin la carpeta, pgAdmin no encontraría la ruta `/data`
- ✅ Es simple y no requiere pasos adicionales

## Otros archivos similares

Verás `.gitkeep` en muchos proyectos open-source para:
- Carpetas de logs
- Directorios de caché
- Directorios de descargas
- Cualquier carpeta que "debe existir" pero estará vacía al inicio
