# Ejercicio 1. Entorno de trabajo: control de versiones y contenedores

## Parte A. Investigación

Esta investigación explica, con palabras sencillas, las herramientas que se usan en la práctica para guardar el trabajo (Git y GitHub) y para ejecutarlo siempre en las mismas condiciones (contenedores y entornos virtuales). Los ejemplos salen del propio repositorio de la práctica.

### 1. ¿Qué es un sistema de control de versiones y qué problema resuelve?

Un sistema de control de versiones es un programa que **registra los cambios** hechos a los archivos de un proyecto a lo largo del tiempo, para poder volver a una versión anterior cuando haga falta (Chacon y Straub, 2014). Se parece al "historial de versiones" de Google Docs, pero sirve para carpetas completas de un proyecto.

El problema que resuelve aparece cuando varias personas trabajan juntas. Sin este tipo de sistema, es común guardar copias con nombres como `trabajo_final_2` o `trabajo_final_NUEVO`, y es fácil equivocarse de copia o borrar sin querer el trabajo de alguien más (Chacon y Straub, 2014). Con el control de versiones, cada cambio queda guardado junto con **quién** lo hizo, **cuándo** y **por qué**. Así se pueden comparar versiones, recuperar archivos dañados y trabajar en equipo sin pisarse unos a otros.

### 2. ¿Cuál es la diferencia entre Git y GitHub?

**Git** es la herramienta (un programa) que se instala en la computadora y lleva el registro de los cambios del proyecto. Funciona de forma local, aun sin internet. **GitHub** es una página web (una plataforma) donde se guardan en internet los proyectos hechos con Git y donde varias personas pueden colaborar, por ejemplo revisando cambios y dejando comentarios (GitHub, Inc., s. f.-a).

Para recordarlo: Git es como el **cuaderno donde se anota la historia del proyecto**, y GitHub es la **nube donde se guarda una copia y se comparte**. Git se puede usar sin GitHub, pero GitHub necesita a Git para funcionar (GitHub, Inc., s. f.-a).

### 3. Conceptos básicos de Git y GitHub

Cada concepto se explica con palabras sencillas y con un ejemplo de esta práctica.

- **Repositorio.** Es la carpeta del proyecto que Git vigila. Guarda los archivos y también todo su historial de cambios. Puede haber una copia en internet (en GitHub) y otra en la computadora. *Ejemplo:* el repositorio `Teoria_Computacion_4CV4_Practica_1`, que existe en GitHub y también en una carpeta de la computadora.
- **Confirmación (commit).** Es como un **punto de guardado en un videojuego**: una "foto" del proyecto en un momento dado, acompañada de un mensaje que explica qué se cambió y por qué. Git le asigna un código único para poder volver a ese punto cuando se quiera (Chacon y Straub, 2014). *Ejemplo:* el commit con el mensaje "Agrega readme con datos de la práctica e índice, y .gitignore" guardó en el historial el README y el `.gitignore`.
- **Rama (branch).** Es una **línea de trabajo aparte**, como sacar una copia del trabajo para experimentar sin arruinar el original. Todo repositorio tiene una rama principal, que en GitHub se llama `main` por defecto (GitHub, Inc., s. f.-c). *Ejemplo:* para escribir este documento se crea una rama llamada `investigacion`, de modo que `main` no cambia hasta que el documento esté listo.
- **Fusión (merge).** Es **juntar los cambios de una rama con otra**, como pegar en el original lo que se hizo en la copia. *Ejemplo:* cuando el documento está terminado, la rama `investigacion` se fusiona con `main` y el documento pasa a formar parte de la versión principal.
- **Conflicto de fusión.** Ocurre cuando dos ramas cambiaron **el mismo lugar del mismo archivo de manera distinta** y Git no sabe con cuál quedarse (GitHub, Inc., s. f.-d). Git marca el archivo con los símbolos `<<<<<<<`, `=======` y `>>>>>>>`, y una persona debe elegir qué versión conservar. *Ejemplo:* si en una rama el README dice "Fecha de entrega: 22 de septiembre" y en otra dice "Fecha de entrega: 23 de septiembre", Git no puede decidir cuál es la correcta; quien hace la fusión escoge una y guarda el resultado.
- **Pull Request.** Es una **solicitud que se hace en GitHub** para que los cambios de una rama se incorporen a otra, normalmente a `main`. Antes de aceptar la fusión, otras personas pueden revisar los cambios, comentar y pedir ajustes (GitHub, Inc., s. f.-e). Es como decir: "Revisen lo que hice y, si está bien, agréguenlo al proyecto". *Ejemplo:* un Pull Request titulado "Agrega la investigación de la Parte A", con una descripción de lo que contiene, para llevar la rama `investigacion` a `main`.
- **Archivo `.gitignore`.** Es un archivo de texto con la **lista de cosas que Git debe ignorar**, es decir, que no se guardan en el repositorio: archivos temporales, generados automáticamente o que no forman parte del proyecto (Chacon y Straub, 2014). *Ejemplo:* en esta práctica se ignoran la carpeta `venv/` (el entorno virtual) y `__pycache__/`, porque se pueden volver a crear en cualquier momento.
- **Archivo README.** Es la **portada del proyecto**: un archivo que cuenta de qué trata, quién lo hizo y cómo usarlo. GitHub lo muestra automáticamente al abrir la página del repositorio (GitHub, Inc., s. f.-b). *Ejemplo:* el `README.md` de esta práctica incluye los datos del alumno y el índice de los documentos.

En conjunto, el flujo de trabajo típico es: se crea una **rama**, se hacen varios **commits** en ella, se abre un **Pull Request** en GitHub y, una vez revisado, se hace la **fusión** con `main`.

### 4. ¿Qué es un contenedor y en qué se diferencia de una máquina virtual?

Un **contenedor** es una "caja cerrada" donde se ejecuta una aplicación junto con todo lo que necesita para funcionar (técnicamente, es un proceso aislado). No depende de lo que esté instalado en la computadora y casi no influye sobre ella ni sobre otros contenedores (Docker, Inc., s. f.-e). Gracias a esto, el programa se ejecuta de la misma manera en distintas computadoras.

Una **máquina virtual** hace algo parecido, pero de forma más pesada: simula una computadora completa, con su propio sistema operativo (como Windows, macOS o Linux). Una manera de imaginarlo es esta: la máquina virtual es una **casa completa**, con su propia cocina, baño y tuberías; el contenedor es un **departamento** dentro de un edificio, con su espacio cerrado pero compartiendo con los demás la estructura y las tuberías, es decir, el "núcleo" del sistema operativo (Docker, Inc., s. f.-e; Microsoft, 2025).

| | Máquina virtual | Contenedor |
|---|---|---|
| **Arranque** | Más lento: debe encender un sistema operativo completo. | Rápido: no enciende un sistema operativo, solo inicia el programa. |
| **Tamaño** | Grande: suele ocupar decenas de gigabytes. | Pequeño: suele ocupar decenas de megabytes. |
| **Aislamiento** | Muy fuerte: cada máquina tiene su propio sistema operativo completo y queda separada del resto. | Más ligero: los contenedores comparten el núcleo del sistema operativo, por lo que la separación no es tan fuerte como en una máquina virtual. |

Fuentes de la tabla: Docker, Inc. (s. f.-f) y Microsoft (2025).

### 5. Imagen, contenedor, volumen y puerto publicado

- **Imagen.** Es la **receta lista para usar**: un paquete con todos los archivos, programas y configuraciones que hacen falta para crear un contenedor. Una vez creada no se puede modificar; si se necesita un cambio, se crea otra imagen a partir de ella (Docker, Inc., s. f.-g). *Ejemplo:* `python:3.12-slim` es una imagen que ya trae Python 3.12; en esta práctica se parte de ella para construir las imágenes del proyecto.
- **Contenedor.** Es el **platillo ya cocinado**: una imagen puesta en marcha. La imagen es la fuente de los archivos y la configuración con que arranca el contenedor (Docker, Inc., s. f.-g), y de una misma imagen pueden salir varios contenedores. *Ejemplo:* al ejecutar el servicio `py312`, Docker crea un contenedor llamado `tc_p1_py312` a partir de la imagen construida con Python 3.12.
- **Volumen.** Es un **espacio de almacenamiento fuera del contenedor**, conectado a él. Sirve para que los archivos no se pierdan, porque lo que un contenedor guarda dentro de sí mismo desaparece cuando se elimina (Docker, Inc., s. f.-d). Es como conectar una memoria USB: aunque se quite el contenedor, lo guardado en la USB sigue existiendo. *Ejemplo:* en el archivo `compose.yml` de esta práctica, la línea `..:/app` conecta la carpeta del proyecto de la computadora con la carpeta `/app` del contenedor, así el contenedor ve siempre el código y las pruebas más recientes. *Nota:* Docker distingue entre los *volúmenes* que él mismo administra y los *bind mounts*, que enlazan una carpeta concreta de la computadora, como en este ejemplo (Docker, Inc., s. f.-d); en el enunciado de la práctica se le llama volumen a ambos casos.
- **Puerto publicado.** Un puerto es como un **número de puerta o ventanilla** por donde una aplicación recibe visitas. Como el contenedor está aislado, desde la computadora no se puede entrar a él directamente. **Publicar un puerto** es abrir una conexión entre un puerto de la computadora y uno del contenedor, para poder usar la aplicación desde el navegador (Docker, Inc., s. f.-b). Se escribe `puerto_de_la_computadora:puerto_del_contenedor`. *Ejemplo:* en esta práctica, `8550:8550` conecta el puerto 8550 de la computadora con el 8550 del contenedor, y por eso la interfaz se abre en el navegador en `http://localhost:8550`.

### 6. ¿Qué es un entorno virtual de Python y por qué no cambia la versión del intérprete?

Python es un programa que ejecuta otros programas escritos en ese lenguaje; a ese programa se le llama **intérprete**. Muchos proyectos usan **bibliotecas**, que son paquetes de código ya hecho (como `flet` o `pytest`), y proyectos distintos pueden necesitar versiones distintas de la misma biblioteca. Un **entorno virtual** es una **carpeta aislada con su propia colección de bibliotecas** para un solo proyecto, de manera que lo que se instala ahí no se mezcla con otros proyectos ni con el Python del sistema (Python Software Foundation, s. f.). Es como tener una **caja de herramientas propia para cada proyecto**.

El entorno virtual **no modifica la versión del intérprete** porque **no trae un Python nuevo**: se construye sobre un Python que ya está instalado (el que se usó para crearlo) y lo reutiliza mediante una copia o un enlace a ese programa (Python Software Foundation, s. f.). Por eso, un entorno creado con Python 3.12 será de Python 3.12, y uno creado con Python 3.13 será de 3.13. Para usar otra versión hay que crear el entorno con otro intérprete que ya esté instalado. *Ejemplo:* en el `Dockerfile` de esta práctica, la orden `python -m venv /opt/venv` crea el entorno con el Python de la imagen; por eso se usan tres contenedores, cada uno con su versión de Python (3.11, 3.12 y 3.13) y su propio entorno virtual.

### 7. ¿Por qué conviene fijar la versión de la imagen (`python:3.12-slim`) en lugar de usar `python:latest`?

Las imágenes se identifican con una **etiqueta**, que es lo que va después de los dos puntos. En la imagen oficial de Python, la etiqueta `latest` significa "la versión más reciente", así que cambia cada vez que sale una nueva versión de Python; al consultar Docker Hub en septiembre de 2026 apuntaba a Python 3.14.7 (Docker, Inc., s. f.-c). Si se usara `python:latest`, el proyecto podría construirse hoy con una versión de Python y, meses después, con otra distinta, y programas que funcionaban podrían dejar de hacerlo. Es como pedir "la pieza más nueva" en lugar del "modelo exacto": no se sabe cuál llegará. Fijar la versión asegura que todos usen la misma y que el entorno sea **reproducible**, es decir, que se pueda construir de nuevo igual en otra computadora o en otro momento (Docker, Inc., s. f.-a).

Una precisión: una etiqueta como `3.12-slim` sigue recibiendo pequeñas correcciones dentro de la misma versión (por ejemplo, de seguridad). Si se necesitara una reproducción todavía más exacta, se puede fijar también la "huella" única de la imagen (Docker, Inc., s. f.-a). La parte `-slim` indica una versión **reducida** de la imagen, con solo lo mínimo para ejecutar Python; pesa menos, aunque trae menos herramientas, por lo que a veces falla la instalación de bibliotecas que necesitan herramientas extra (Docker, Inc., s. f.-c).

## Referencias

Chacon, S. y Straub, B. (2014). *Pro Git* (2.ª ed.). Apress. https://git-scm.com/book/es/v2

Docker, Inc. (s. f.-a). *Building best practices*. Docker Docs. Recuperado el 21 de septiembre de 2026, de https://docs.docker.com/build/building/best-practices/

Docker, Inc. (s. f.-b). *Publishing and exposing ports*. Docker Docs. Recuperado el 21 de septiembre de 2026, de https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/

Docker, Inc. (s. f.-c). *python - Official Image*. Docker Hub. Recuperado el 21 de septiembre de 2026, de https://hub.docker.com/_/python

Docker, Inc. (s. f.-d). *Volumes*. Docker Docs. Recuperado el 21 de septiembre de 2026, de https://docs.docker.com/engine/storage/volumes/

Docker, Inc. (s. f.-e). *What is a container?* Docker Docs. Recuperado el 21 de septiembre de 2026, de https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/

Docker, Inc. (s. f.-f). *What is a container?* [Página de recursos]. Docker. Recuperado el 21 de septiembre de 2026, de https://www.docker.com/resources/what-container/

Docker, Inc. (s. f.-g). *What is an image?* Docker Docs. Recuperado el 21 de septiembre de 2026, de https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/

GitHub, Inc. (s. f.-a). *About Git*. GitHub Docs. Recuperado el 21 de septiembre de 2026, de https://docs.github.com/en/get-started/using-git/about-git

GitHub, Inc. (s. f.-b). *About the repository README file*. GitHub Docs. Recuperado el 21 de septiembre de 2026, de https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

GitHub, Inc. (s. f.-c). *Branches*. GitHub Docs. Recuperado el 21 de septiembre de 2026, de https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

GitHub, Inc. (s. f.-d). *Merge conflicts*. GitHub Docs. Recuperado el 21 de septiembre de 2026, de https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts

GitHub, Inc. (s. f.-e). *Pull requests*. GitHub Docs. Recuperado el 21 de septiembre de 2026, de https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests

Microsoft. (2025). *Containers vs. virtual machines*. Microsoft Learn. https://learn.microsoft.com/en-us/virtualization/windowscontainers/about/containers-vs-vm

Python Software Foundation. (s. f.). *venv — Creation of virtual environments*. Python 3.14.7 documentation. Recuperado el 21 de septiembre de 2026, de https://docs.python.org/3/library/venv.html
