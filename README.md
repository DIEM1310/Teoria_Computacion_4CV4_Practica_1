# Práctica 1: Operaciones básicas sobre lenguajes

Instituto Politécnico Nacional · Escuela Superior de Cómputo

| Dato | Valor |
|---|---|
| Alumno | Diego Polo Santoscoy |
| Boleta | 2025630828 |
| Grupo | 4CV4 |
| Carrera | Ingeniería en Sistemas Computacionales |
| Unidad de aprendizaje | Teoría de la Computación |
| Profesor | Gabriel Hurtado Avilés |
| Fecha de entrega | 22 de septiembre de 2026 |

## Objetivo

Aplicar los conceptos de la Unidad Temática I al diseño de autómatas finitos en JFLAP y al desarrollo de una aplicación con interfaz gráfica que implementa las operaciones básicas sobre cadenas y lenguajes, y construir el entorno de trabajo (control de versiones y contenedores) que se empleará durante el resto del curso.

## Índice de la práctica

| Ejercicio | Documento |
|---|---|
| 1. Entorno de trabajo: control de versiones y contenedores | [docs/01-entorno.md](docs/01-entorno.md) |
| 2. Investigación: qué es la Teoría de la Computación | [docs/02-investigacion.md](docs/02-investigacion.md) |
| 3. Estado del arte: cinco artículos | [docs/03-estado-del-arte.md](docs/03-estado-del-arte.md) |
| 4. Autómatas finitos en JFLAP | [automatas/](automatas/) |
| 5. Aplicación con interfaz gráfica | [docs/05-aplicacion.md](docs/05-aplicacion.md) |
| Conclusiones | [docs/conclusiones.md](docs/conclusiones.md) |
| Bibliografía | [docs/bibliografia.md](docs/bibliografia.md) |

## Cómo levantar el entorno y ejecutar las pruebas

Hace falta tener **Docker Desktop** instalado y encendido (se usó Docker Desktop, no Podman, con Docker 29.8.1 y Docker Compose v5.5.1). La interfaz de la aplicación usa **Flet 0.86.5**, versión fijada en [requirements.txt](requirements.txt). El detalle del entorno está en [docs/01-entorno.md](docs/01-entorno.md).

Los comandos se ejecutan desde la carpeta `entorno/`:

| Para... | Comando |
|---|---|
| Construir las tres imágenes (Python 3.11, 3.12 y 3.13) | `docker compose build` |
| Ver la versión de Python de cada contenedor | `docker compose run --rm py311 python --version`, y lo mismo con `py312` y `py313` |
| Ejecutar las pruebas en cada contenedor | `docker compose run --rm py311 pytest -q`, y lo mismo con `py312` y `py313` |
| Abrir la interfaz | `docker compose up py312` y abrir http://localhost:8550 en el navegador |
| Apagar y limpiar | `docker compose down` |
