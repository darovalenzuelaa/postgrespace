# ¿Qué es GitHub Codespaces?

## Concepto simple

GitHub Codespaces es **VS Code en la nube**. 

En lugar de tener VS Code en tu máquina, lo ejecutas en un servidor de GitHub, en el navegador.

```
Lo que normalmente ves:
Tu máquina → VS Code → Tu código

Con Codespaces:
Tu máquina → Navegador → Servidor de GitHub → VS Code → Tu código
```

## ¿Por qué existe?

Imagina estos escenarios:

| Escenario | Sin Codespaces | Con Codespaces |
|-----------|----------------|----------------|
| **Tu computadora no es muy potente** | Sufre 😢 | Funciona perfecto ✓ |
| **Necesitas trabajar en múltiples máquinas** | Sincronizar todo | Abre en cualquier navegador |
| **Quieres desarrollar desde una Tablet** | Imposible | Abre en el navegador ✓ |
| **Necesitas una máquina Windows/Mac/Linux** | Compra otro | Elige en GitHub ✓ |

## En este proyecto

Este repositorio está optimizado para Codespaces:

1. **Fork el repositorio** (copia en tu cuenta de GitHub)
2. **Clic en "Code" → "Codespaces"** → "Create codespace on main"
3. **Espera a que inicie** (primeros 2-3 minutos)
4. **Se abre VS Code en el navegador** con todo preconfigurado

No necesitas instalar nada en tu máquina.

## Vs Dev Containers

| Aspecto | Dev Containers | Codespaces |
|--------|-----------------|-----------|
| **Dónde corre** | En tu máquina (Docker) | En servidor de GitHub |
| **Requisitos** | Docker instalado | Solo navegador |
| **Potencia** | Depende de tu PC | Servidor potente de GitHub |
| **Internet** | No necesario | Necesario |
| **Costo** | Gratis | Gratis con límites, luego pago |

## Cómo acceder

### Opción 1: VS Code en el navegador (web)
```
GitHub Codespace → VS Code web → Tu código
```

### Opción 2: VS Code en tu máquina (desktop)
```
GitHub Codespace → Abre en VS Code local → Tu código

(Es más estable y rápido)
```

## Límites gratuitos (GitHub)

| Plan | Tiempo de cómputo/mes | Almacenamiento/mes |
|------|----------------------|-------------------|
| **GitHub Free** | 120 horas | 15 GB |
| **GitHub Pro** | 180 horas | 20 GB |

Para este laboratorio educativo: **Más que suficiente**.

> **Información oficial** — [Consulta los límites actualizados en GitHub Docs](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces)

## Ventajas para estudiantes

✅ No requiere instalar Docker  
✅ No contamina tu computadora  
✅ Funciona en cualquier dispositivo  
✅ Puedes trabajar desde diferentes máquinas  
✅ GitHub gestiona las actualizaciones  

## Desventajas

❌ Requiere conexión a internet  
❌ Puede ser más lento que local  
❌ Límite de horas gratuitas  

## Relación con Dev Containers

Codespaces **usa Dev Containers** internamente. Es decir:

```
GitHub Codespaces
└── Lee .devcontainer/devcontainer.json
└── Crea un contenedor Docker en un servidor
└── Abre VS Code dentro del contenedor
└── Lo muestra en tu navegador
```

[Aprende más sobre Dev Containers](DEVCONTAINER.md)
