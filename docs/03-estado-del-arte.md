# Ejercicio 3. Estado del arte: cinco artículos

## Artículo 1. Gribkoff (2013): aplicaciones de los autómatas finitos deterministas

**1. Cita (APA 7).** Gribkoff, E. (2013). *Applications of deterministic finite automata* [Documento de curso, ECS 120]. University of California, Davis. https://www.cs.ucdavis.edu/~rogaway/classes/120/spring13/eric-dfa.pdf

**2. Problema que aborda.** Los autómatas finitos deterministas (AFD) suelen verse solo como teoría. El texto muestra que sirven para describir sistemas reales que deben recordar un estado, como una máquina expendedora, un videojuego, un protocolo de red o el autocompletado de un buscador (Gribkoff, 2013, p. 1).

**3. Método o propuesta.** El autor no propone una técnica nueva; modela cuatro casos con diagramas de estados. (a) Una máquina expendedora de refrescos, con nueve estados que representan el dinero depositado y una 5-tupla completa. (b) Un fantasma del juego Pac-Man, con cuatro estados que son sus comportamientos. (c) Una versión simplificada del protocolo TCP, cuyos estados son las etapas de una conexión. (d) El autocompletado de Apache Lucene, para el que amplía el AFD con salidas (máquina de Mealy, un tipo de transductor de estados finitos) y lo ilustra con un ejemplo de seis palabras (pp. 3-9).

**4. Resultado principal.** Muestra que un modelo de estados finitos describe de forma concisa cualquier sistema que deba mantener un estado y que, al añadirle salidas, sirve también para consultar datos: en el ejemplo obtiene la posición de una palabra en una lista ordenada. Afirma que Lucene usó esta idea para reducir de forma drástica la memoria de su autocompletado, pero no presenta mediciones (p. 9).

**5. Tema de la Unidad Temática I.** Unidad I, *Lenguajes regulares*: tema **1.2.3 Autómatas finitos deterministas** (definición formal y funcionamiento), con relación al tema **1.4 Aplicaciones de los lenguajes regulares** (Instituto Politécnico Nacional [IPN], 2021). La máquina de Mealy no aparece en el programa: amplía lo visto en 1.2.3.

**6. Aportación al trabajo del curso.** Muestra que cada estado de un AFD "recuerda" algo de lo leído (por ejemplo, el dinero acumulado), justo lo que se pide justificar en los AFD del Ejercicio 4. También deja ver hasta dónde llega un AFD y cuándo hace falta ampliarlo.

### Respuestas sobre el texto

**¿En qué se diferencian un AFD y una máquina de Mealy, y por qué el autocompletado de Lucene requiere la segunda?**

Un AFD es una 5-tupla `(Q, Σ, δ, q₀, F)`. Lee la cadena completa y solo da un veredicto: la acepta o la rechaza, según si termina en un estado de `F` (Gribkoff, 2013, pp. 1-2). Una máquina de Mealy es una 6-tupla `(Q, Σ, Γ, δ, ω, q₀)`: conserva los estados y las transiciones, pero no tiene estados de aceptación. En su lugar tiene un alfabeto de salida `Γ` y una función de salida `ω: Q × Σ → Γ` que emite un símbolo en cada transición, según el estado actual y el símbolo leído. Por eso no acepta ni rechaza: convierte una cadena de entrada en una cadena de salida, como una función (p. 2).

El autocompletado necesita más que saber si una palabra existe: necesita recuperar información asociada a ella. En el ejemplo del texto, con las palabras `mop`, `moth`, `pop`, `star`, `stop` y `top`, la máquina lee una palabra y suma las salidas de las transiciones que recorre. Para `stop`, `3 + 0 + 1 + 0 = 4`, que es su posición en la lista ordenada (p. 9). Un AFD solo podría decir que `stop` pertenece al conjunto; la máquina de Mealy, además, devuelve dónde está. Y como los términos comparten prefijos y sufijos dentro de la máquina, esta ocupa poca memoria (p. 9). Una salvedad: el texto solo ilustra la búsqueda de una palabra completa; no explica cómo se obtienen las sugerencias a partir de un prefijo.

**El autor declara vacío el conjunto de estados de aceptación de la máquina expendedora. ¿Qué consecuencia tiene para la noción de cadena aceptada?**

Un AFD acepta una cadena si termina en un estado de `F`. Con `F = ∅` ningún estado es de aceptación, así que **ninguna cadena se acepta jamás**: el lenguaje del autómata es el conjunto vacío, `L(M) = ∅` (no `{λ}`, que sí contendría una cadena). La figura es coherente con esto, pues no tiene círculos dobles, que es la forma habitual de marcar los estados de aceptación (Gribkoff, 2013, pp. 3-4).

Por eso la noción de "cadena aceptada" pierde sentido aquí: el autómata no se usa para reconocer un lenguaje, sino como **modelo de comportamiento**. Lo que importa es en qué estado está la máquina (cuánto dinero hay) y qué puede hacer desde ahí. Esa información está en la función de transición, no en `F`: en los estados azules (de `$1.25` en adelante) la entrada `select` lleva de vuelta a `$0.00`, mientras que en los demás es un ciclo que se ignora (pp. 3-4). El color azul es solo una señal visual. Además, una máquina expendedora recibe una secuencia de eventos que nunca termina, así que no hay un momento natural para preguntar si la cadena fue aceptada. Si se quisiera definir un lenguaje (por ejemplo, las secuencias de entradas tras las cuales se puede elegir un refresco), habría que poner los estados azules en `F`.

**Una afirmación que convendría verificar en una fuente arbitrada antes de citarla**

La más importante está al final (p. 9): que, al usar un FST, Lucene puede guardar todo el índice en memoria y así lograr consultas mucho más rápidas. Conviene verificarla por tres razones:

1. Es una afirmación de rendimiento sin cifras ni punto de comparación: no dice "más rápidas" que qué.
2. La única fuente que da el autor es el blog de un desarrollador de Lucene, no una publicación arbitrada (McCandless, 2010).
3. Esa fuente no dice lo mismo. Reporta un ahorro grande de memoria (un FST de 69 MB para 9.8 millones de términos de un índice de Wikipedia), pero advierte que, frente a otras estructuras de mapa ordenado, requiere mucha menos RAM y tiene un mayor costo de CPU en cada consulta (McCandless, 2010).

Lo que sí se puede sostener es la ventaja de memoria; la de velocidad dependería de con qué se compare (por ejemplo, con leer los términos del disco). Antes de citarla habría que buscar mediciones en una fuente arbitrada. La técnica que permite ahorrar memoria, la construcción de autómatas acíclicos mínimos que comparten sufijos, sí está en la literatura arbitrada (Daciuk et al., 2000), pero ese artículo no evalúa a Lucene.

Otra afirmación sin respaldo está en la p. 7: que el análisis de seguridad con estados finitos se ha usado en protocolos como SSL y TLS. El texto no cita ningún estudio.

## Artículo 2. Luna-Benoso et al. (2022): detección de melanoma con un clasificador de autómatas celulares

**1. Cita (APA 7).** Luna-Benoso, B., Martínez-Perales, J. C., Cortés-Galicia, J., Flores-Carapia, R. y Silva-García, V. M. (2022). Melanoma detection in dermoscopic images using a cellular automata classifier. *Computers, 11*(1), Artículo 8. https://doi.org/10.3390/computers11010008

**2. Problema que aborda.** Detectar melanoma, el cáncer de piel más agresivo, en imágenes dermatoscópicas. Es difícil porque se parece a los lunares benignos, pero detectarlo a tiempo es decisivo. Proponen un sistema que apoye el diagnóstico clasificando cada lesión (Luna-Benoso et al., 2022, sec. 1).

**3. Método o propuesta.** Un sistema con tres módulos. (1) Segmentación de la lesión con métodos del dominio espacial: filtro de mediana, binarización de Otsu, limpieza de esquinas y tres erosiones y tres dilataciones con la vecindad de Moore. (2) Extracción de 11 medidas estadísticas de textura, como la media, la desviación estándar, la suavidad y la asimetría. (3) Clasificación con un modelo asociativo basado en autómatas celulares (ACA): en el aprendizaje se construye el autómata a partir de patrones conocidos y, en la recuperación, se aplican erosiones y dilataciones celulares para clasificar un patrón nuevo (secs. 3.1-3.3).

**4. Resultado principal.** Con 190 imágenes de la base PH2, obtienen exactitud de 0.978, sensibilidad de 0.944, especificidad de 0.987 y un área bajo la curva ROC de 0.965. Concluyen que el método es más efectivo que otros del estado del arte, aunque su propia Tabla 3 muestra que en sensibilidad queda por debajo de cuatro de los ocho métodos comparados (secs. 4 y 5).

**5. Tema de la Unidad Temática I.** Unidad I, *Lenguajes regulares*: tema **1.2 Autómatas y lenguajes**, en particular **1.2.3 Autómatas finitos deterministas**, como punto de comparación (IPN, 2021). El autómata celular comparte con el AFD los estados finitos y la función de transición, pero no aparece en el programa.

**6. Aportación al trabajo del curso.** Ayuda a delimitar qué es un AFD: una sola máquina con un estado que lee cadenas, frente a una red de celdas que se actualizan a la vez. Además, muestra una aplicación médica de un modelo de estados y transiciones.

### Respuestas sobre el artículo

**Un autómata celular no es un autómata finito: ¿en qué se asemejan y en qué difieren? ¿Qué son el estado, el vecindario y la regla de transición local?**

**Parecidos.** Los dos son modelos discretos que avanzan paso a paso, con un conjunto finito de estados y una función de transición que decide el siguiente estado a partir del actual (Gribkoff, 2013, p. 1; Luna-Benoso et al., 2022, sec. 2.3). Como un AFD, el autómata celular del artículo es determinista: la misma situación produce siempre el mismo resultado.

**Diferencias.** Un AFD es una sola máquina con un único estado activo. Lee una cadena símbolo por símbolo, su transición `δ: Q × Σ → Q` depende del estado actual y del símbolo leído, y al final acepta o rechaza. Un autómata celular es, en cambio, una red de muchas celdas (un reticulado `ℒ`), cada una con su propio estado. No lee símbolos: su entrada es la configuración inicial, que en el artículo es la imagen, y todas las celdas se actualizan a la vez. No tiene estados de aceptación: el resultado se lee de la configuración final. Por eso, mientras el AFD tiene un estado, el autómata celular tiene un estado por celda, y su "estado global" es la configuración completa `C_t: ℒ → S`. Además, el reticulado del artículo es `ℤ²`, que es infinito.

**Estado, vecindario y regla local.** Según el artículo, un autómata celular es una tupla `(ℒ, S, N, f)` (sec. 2.3):

- El **estado** de una celda es un valor del conjunto finito `S`. En el clasificador, `S = {0, 1}`: cada celda, que corresponde a un píxel, está apagada o encendida (sec. 3.3).
- El **vecindario** de una celda es el conjunto de celdas cuyos estados consulta para decidir el suyo. En los experimentos se usa la vecindad de Moore, es decir, la celda y las ocho que la rodean (sec. 4).
- La **regla de transición local** `f: N → S` calcula el estado de una celda en el tiempo `t + 1` a partir de los estados de su vecindario en `t`. Es "local" porque solo mira al vecindario, y se aplica igual a todas las celdas. En el artículo hay dos reglas: la dilatación (la celda pasa a 1 si al menos una celda del vecindario vale 1) y la erosión (pasa a 1 solo si todas valen 1). Al aplicarlas en secuencia, el autómata recupera patrones y así clasifica (sec. 3.3).

**¿Qué problema abordan los autores y por qué eligen ese modelo?**

**El problema.** Detectar melanoma en imágenes dermatoscópicas. La detección temprana es decisiva para la supervivencia, pero el diagnóstico es difícil porque el melanoma se parece a los lunares benignos (Luna-Benoso et al., 2022, sec. 1.1). Los autores construyen un sistema de apoyo al diagnóstico que clasifique cada lesión como melanoma o no, para ayudar al especialista a decidir, por ejemplo, si hace falta una biopsia.

**Por qué ese modelo.** Dan dos razones (sec. 1.2). Primero, los autómatas celulares son sencillos de implementar y requieren pocos recursos de cómputo, en comparación con modelos de aprendizaje profundo como AlexNet o VGG16. Segundo, querían llevar conceptos de los autómatas celulares al aprendizaje supervisado, con un modelo asociativo que los propios autores habían propuesto antes. El artículo no reporta mediciones del costo de cómputo, así que la ventaja se afirma, pero no se demuestra.

**¿Qué resultado reportan, con qué imágenes y con qué métricas?**

**Imágenes.** La base PH2: 200 imágenes dermatoscópicas del servicio de dermatología del Hospital Pedro Hispano (Matosinhos, Portugal), de 768 × 560 píxeles y 20 aumentos, con lunares comunes, lunares atípicos y melanomas. Descartaron 10 porque no se pudieron segmentar bien y usaron 190 (sec. 4).

**Métricas.** Exactitud (ACC), sensibilidad (SE) y especificidad (SP), calculadas con la matriz de confusión, y además la curva ROC con su área (AUC) (sec. 4).

**Resultado.** ACC = 0.978, SE = 0.944, SP = 0.987 y AUC = 0.965. La matriz de confusión (Tabla 2) tiene 34 verdaderos positivos, 152 verdaderos negativos, 2 falsos positivos y 2 falsos negativos. Frente a otros ocho métodos (Tabla 3), obtiene la mayor exactitud y la mayor especificidad; en sensibilidad supera a cuatro y queda por debajo de los otros cuatro, algo que los autores reconocen que debe mejorar (sec. 5).

**Salvedades.** El texto no explica cómo dividió las imágenes en entrenamiento y prueba, así que no se sabe si los resultados se midieron con imágenes nuevas. Tampoco aclara si los métodos de la comparación se evaluaron con las mismas imágenes. Los propios autores señalan como límites la poca cantidad de imágenes y que todas se tomaron en las mismas condiciones (sec. 5).

## Artículo 3. Turing (1936): números computables y el Entscheidungsproblem

**1. Cita (APA 7).** Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society, s2-42*(1), 230-265. https://doi.org/10.1112/plms/s2-42.1.230

Sobre las dos fechas que circulan (1936 y 1937), véase la nota al pie.[^fecha]

**2. Problema que aborda.** Responder al Entscheidungsproblem de Hilbert: ¿existe un procedimiento mecánico que decida si cualquier fórmula de la lógica de primer orden es demostrable? Para hacerlo, Turing tuvo que definir con precisión qué significa calcular de forma mecánica (Turing, 1936, pp. 230-231).

**3. Método o propuesta.** Define las "máquinas de computación" (hoy, máquinas de Turing) analizando cómo calcula una persona: una cinta dividida en casillas, una cabeza que ve una casilla a la vez y un número finito de estados (las "m-configuraciones") (§§ 1, 2 y 9). Después prueba que existe una máquina universal (§ 6), aplica un argumento diagonal (§ 8) y lo traslada a la lógica (§ 11). En un apéndice demuestra, en esbozo, que su modelo equivale al cálculo λ de Church.

**4. Resultado principal.** El Entscheidungsproblem no tiene solución: no existe una máquina, ni un procedimiento general, que decida si una fórmula es demostrable (§ 11, p. 259). En el camino demuestra que existe una máquina universal (§ 6) y que ninguna máquina puede decidir si otra produce infinitas cifras (§ 8).

**5. Tema de la Unidad Temática I.** Unidad I: tema **1.1 Orígenes de la computación**, en especial **1.1.4 Computabilidad y complejidad**, y también **1.1.1 Automatización del cómputo** (IPN, 2021). El modelo y sus resultados se retoman en la Unidad III (3.1 Máquina de Turing y 3.2 Decidibilidad).

**6. Aportación al trabajo del curso.** Es la fuente original de la máquina de Turing, de la máquina universal y de un resultado de indecidibilidad emparentado con el problema del paro. Respalda el apartado de Church-Turing del Ejercicio 2 y muestra que hay problemas que ningún programa puede resolver.

### Respuestas sobre el artículo

**¿Qué resultado se demuestra y qué modelo de cómputo se introduce?**

**Resultado.** Turing demuestra que el Entscheidungsproblem no tiene solución: no puede existir una máquina que, al recibir una fórmula del cálculo funcional restringido (hoy, lógica de primer orden), decida si es demostrable (Turing, 1936, § 11, p. 259). La prueba tiene tres pasos:

1. Con un argumento diagonal, muestra que ninguna máquina puede decidir si otra máquina es "libre de círculos" (es decir, si produce infinitas cifras) ni si llegará a imprimir un símbolo dado (§ 8, pp. 246-248).
2. A cada máquina `M` le asocia una fórmula `Un(M)` que es demostrable si y solo si `M` llega a imprimir un 0 (§ 11, lemas 1 y 2, pp. 261-262).
3. Si existiera un método para decidir la demostrabilidad, decidiría también si `M` imprime un 0, lo cual es imposible por el paso 1 (p. 262).

Este resultado no es el de Gödel: Gödel mostró que hay fórmulas que no se pueden probar ni refutar, y Turing, que no hay un método general para saber si una fórmula es demostrable (p. 259). Como resultados intermedios, prueba que existe una máquina universal, capaz de imitar a cualquier otra a partir de su descripción (§ 6, p. 241), y que los números computables son numerables (§ 5, p. 241).

**Modelo.** Introduce las "máquinas de computación", hoy llamadas máquinas de Turing (§§ 1 y 2, pp. 231-233). Tienen una cinta dividida en casillas, de las que ven una a la vez (el "símbolo explorado"); un número finito de "m-configuraciones", que son sus estados; y una tabla que, según el estado y el símbolo explorado, indica qué hacer: escribir o borrar un símbolo, moverse una casilla a la izquierda o a la derecha y pasar a otro estado. Una máquina "calcula" un número real cuando escribe sus cifras binarias.

**Enuncie con precisión la tesis de Church-Turing y explique por qué se denomina tesis y no teorema.**

**Enunciado.** Toda función efectivamente calculable, es decir, calculable con un procedimiento mecánico y finito como un algoritmo, es computable por una máquina de Turing (Copeland, 2023). La inversa es inmediata, porque una máquina de Turing es en sí un procedimiento mecánico; por eso la tesis afirma que las dos clases de funciones coinciden. Tiene dos versiones equivalentes: la de Church, que identifica lo "efectivamente calculable" con las funciones λ-definibles, y la de Turing, que lo identifica con lo que calculan sus máquinas. Turing demuestra, en esbozo, que sus sucesiones computables y las λ-definibles coinciden (Turing, 1936, pp. 231 y 263-265).

**Por qué es tesis.** Un teorema se demuestra a partir de definiciones precisas, pero aquí uno de los lados, "efectivamente calculable", es una idea intuitiva e informal; por eso no puede demostrarse que coincida con lo que hace una máquina de Turing (Copeland, 2023). El propio Turing lo reconoce: en el § 9 admite que todos los argumentos que se pueden dar son, en el fondo, apelaciones a la intuición y, por eso, poco satisfactorios desde el punto de vista matemático (p. 249). Tampoco usa la palabra "tesis": habla de su "definición" de número computable y de una afirmación que sostiene (*my contention*, p. 232). Lo que respalda la identificación son los tres tipos de argumentos que él distingue en ese mismo apartado: la apelación directa a la intuición, mediante el análisis de cómo calcula una persona; la demostración de que dos definiciones equivalen (el apéndice); y los ejemplos de clases grandes de números computables (§ 10) (pp. 249-258). Después se sumó la evidencia de que otros modelos propuestos de forma independiente resultaron equivalentes (Copeland, 2023).

**¿Qué dificultad presenta la lectura, siendo un texto de hace más de setenta años con una notación distinta de la del curso, y cómo se resuelve?**

**Dificultad principal.** El vocabulario y la notación, que no son los del curso:

- Turing dice "m-configuración" donde hoy se dice estado, y sus máquinas no reconocen cadenas: escriben las cifras de un número real.
- Las tablas "esqueleto" con letras góticas y griegas de los §§ 4 y 7 (la máquina universal) y las fórmulas del § 11, escritas en el cálculo funcional de Hilbert, son muy densas.
- La versión disponible es una reproducción escaneada, con partes difíciles de leer.
- "Libre de círculos" significa que la máquina imprime infinitas cifras; se parece más a "no se detiene" que al "se detiene" del problema del paro que se ve hoy.

**Cómo se resuelve.** Primero, se arma una tabla de equivalencias con el vocabulario del curso:

| Turing (1936) | En el curso |
|---|---|
| m-configuración | estado |
| símbolo explorado | símbolo que lee la cabeza |
| configuración completa | estado, contenido de la cinta y posición de la cabeza |
| operaciones `P`, `E`, `L`, `R` | escribir, borrar, mover a la izquierda, mover a la derecha |
| máquina "libre de círculos" | máquina que imprime infinitas cifras |
| descripción estándar (S.D) y número de descripción (D.N) | codificación de la máquina como cadena y como número |

Segundo, se lee primero lo esencial (§§ 1-3, 5-6, 8 y 11) y se deja para después el detalle de las tablas de la máquina universal, que no hace falta para seguir el argumento. Tercero, se contrasta el argumento diagonal del § 8 con su versión moderna, la del problema del paro (Sipser, 2012, cap. 4).

[^fecha]: Se cita como 1936 porque es el año en que el trabajo se leyó ante la London Mathematical Society (12 de noviembre de 1936, según la primera página del artículo; Turing, 1936, p. 230) y en que empezó a publicarse, pues salió por partes a fines de ese año. El registro del DOI, en cambio, lo fecha en 1937 porque toma la fecha del volumen 42 de la serie 2, que reúne esas partes y abarca 1936-1937. Por eso algunas fuentes lo citan como 1937 y otras como "1936-37".

## Artículo 4. Ferreira et al. (2021): aprender el autómata de un protocolo de red

**1. Cita (APA 7).** Ferreira, T., Brewton, H., D'Antoni, L. y Silva, A. (2021). Prognosis: Closed-box analysis of network protocol implementations. En *Proceedings of the 2021 ACM SIGCOMM 2021 Conference* (pp. 762-774). Association for Computing Machinery. https://doi.org/10.1145/3452296.3472938

**2. Problema que aborda.** Los errores en las implementaciones de protocolos de red (TCP, QUIC) causan fallas y brechas de seguridad, y verificarlas exige mucha experiencia. Buscan una forma general y reutilizable de detectarlos sin saber de antemano qué propiedad violan (Ferreira et al., 2021, sec. 1).

**3. Método o propuesta.** Prognosis es un marco modular con tres partes. (1) Un adaptador traduce entre paquetes reales y símbolos abstractos, aprovechando una implementación de referencia en lugar de programar la lógica del protocolo. (2) Un módulo de aprendizaje activo, con consultas de pertenencia y de equivalencia (algoritmo TTT), aprende máquinas de Mealy del protocolo y, con un solucionador SMT, las amplía con registros para capturar números de secuencia. (3) Un módulo de análisis revisa el determinismo, compara los modelos de dos implementaciones y verifica propiedades (secs. 2-5).

**4. Resultado principal.** Reproduce un estudio previo de TCP con unas 300 líneas de instrumentación, frente a más de 3,000 del trabajo anterior. En varias implementaciones de QUIC encuentra una ambigüedad del estándar, que el IETF corrigió, y errores que los desarrolladores confirmaron; uno permitiría un ataque de negación de servicio (secs. 6 y 8). El método busca errores: no ofrece garantías formales (sec. 1).

**5. Tema de la Unidad Temática I.** Unidad I, *Lenguajes regulares*: tema **1.2.3 Autómatas finitos deterministas** (una máquina de Mealy es un AFD con salidas) y tema **1.4 Aplicaciones de los lenguajes regulares** (IPN, 2021).

**6. Aportación al trabajo del curso.** Muestra a los autómatas como herramienta para analizar software real: cada estado resume lo que ya ocurrió en una conexión. Continúa el Artículo 1 (TCP y máquinas de Mealy) y aporta un ejemplo de aplicación fuera de la teoría.

## Artículo 5. Churchill, Biderman y Herrick (2020): *Magic: The Gathering* es Turing completo

**1. Cita (APA 7).** Churchill, A., Biderman, S. y Herrick, A. (2020). Magic: The Gathering is Turing complete. En M. Farach-Colton, G. Prencipe y R. Uehara (Eds.), *10th International Conference on Fun with Algorithms (FUN 2021)* (LIPIcs, Vol. 157, Art. 9, pp. 9:1-9:19). Schloss Dagstuhl – Leibniz-Zentrum für Informatik. https://doi.org/10.4230/LIPIcs.FUN.2021.9

**2. Problema que aborda.** Averiguar si existe un juego real, con sus reglas normales, cuyo mejor movimiento sea indecidible, pregunta abierta durante una década. Muestran que en *Magic* ni siquiera se puede decidir quién gana cuando todas las jugadas son obligadas (Churchill et al., 2020, sec. 1).

**3. Método o propuesta.** Incrustan una máquina de Turing universal (la de Rogozhin, con 2 estados y 18 símbolos) en una partida de *Magic*. La cinta son criaturas cuyo poder y resistencia indican su distancia a la cabeza y cuyo tipo de criatura codifica el símbolo. Las reglas de la máquina se codifican con habilidades que se activan solas, y todas las jugadas de los dos jugadores son obligatorias. Si la máquina se detiene, gana el primer jugador; si no, la partida cae en un ciclo infinito y se declara empate (secs. 3 y 4).

**4. Resultado principal.** El Teorema 1: determinar el resultado de una partida de *Magic* en la que todas las jugadas restantes son obligadas es indecidible. Por tanto, jugar de forma óptima es al menos tan difícil como el problema del paro. La construcción cabe en un mazo de 60 cartas legal en el formato Legacy (secs. 1 y 5).

**5. Tema de la Unidad Temática I.** Unidad I: tema **1.1 Orígenes de la computación**, en especial **1.1.4 Computabilidad y complejidad** (IPN, 2021). El modelo y el problema del paro se estudian a fondo en la Unidad III (3.1 Máquina de Turing y 3.2 Decidibilidad).

**6. Aportación al trabajo del curso.** Muestra la máquina de Turing y el problema del paro en acción, fuera de las matemáticas. Refuerza el Artículo 3 y la tesis de Church-Turing: si un sistema puede simular una máquina de Turing, es tan potente como ella.

## Cierre: comparación de los cinco textos

| Texto | Arbitrado | Año | Modelo que usa | Campo de aplicación |
|---|---|---|---|---|
| 1. Gribkoff | No (documento de curso) | 2013 | AFD y máquina de Mealy | Máquinas expendedoras, videojuegos, protocolos de red y buscadores |
| 2. Luna-Benoso et al. | Sí (*Computers*) | 2022 | Autómata celular | Medicina: detección de melanoma en imágenes |
| 3. Turing (original elegido) | Sí (*Proceedings of the London Mathematical Society*) | 1936 | Máquina de Turing | Lógica matemática: el Entscheidungsproblem |
| 4. Ferreira et al. (localizado) | Sí (ACM SIGCOMM) | 2021 | Máquinas de Mealy aprendidas | Redes: análisis de protocolos |
| 5. Churchill et al. (localizado) | Sí (FUN, LIPIcs) | 2020 | Máquina de Turing universal | Juegos: complejidad de *Magic* |

**Qué tienen en común.** Los cinco usan una máquina abstracta, definida por estados y reglas de transición, para razonar sobre un sistema: un AFD o una máquina de Mealy (Artículos 1 y 4), un autómata celular (2) o una máquina de Turing (3 y 5). **En rigor difieren mucho.** Turing y Churchill et al. demuestran teoremas; Luna-Benoso et al. y Ferreira et al. evalúan con experimentos y no ofrecen garantías formales, algo que Ferreira et al. dicen expresamente; Gribkoff no es arbitrado ni cita fuentes. **En propósito también:** enseñar aplicaciones (1), clasificar imágenes (2), fundar la computación y demostrar un límite (3), encontrar errores en protocolos (4) y mostrar que un juego real es indecidible (5). **Problema abierto.** Cómo dar más poder expresivo a un modelo sin perder la verificación automática: los modelos con registros de Prognosis necesitan números, pero verificar sus propiedades es, en general, indecidible, y Turing y Churchill et al. muestran por qué existen esos límites (Ferreira et al., 2021, sec. 5).

## Referencias

Churchill, A., Biderman, S. y Herrick, A. (2020). Magic: The Gathering is Turing complete. En M. Farach-Colton, G. Prencipe y R. Uehara (Eds.), *10th International Conference on Fun with Algorithms (FUN 2021)* (LIPIcs, Vol. 157, Art. 9, pp. 9:1-9:19). Schloss Dagstuhl – Leibniz-Zentrum für Informatik. https://doi.org/10.4230/LIPIcs.FUN.2021.9

Copeland, B. J. (2023). The Church-Turing thesis. En E. N. Zalta y U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. Metaphysics Research Lab, Stanford University. Recuperado el 21 de septiembre de 2026, de https://plato.stanford.edu/entries/church-turing/

Daciuk, J., Mihov, S., Watson, B. W. y Watson, R. E. (2000). Incremental construction of minimal acyclic finite-state automata. *Computational Linguistics, 26*(1), 3-16. https://doi.org/10.1162/089120100561601

Ferreira, T., Brewton, H., D'Antoni, L. y Silva, A. (2021). Prognosis: Closed-box analysis of network protocol implementations. En *Proceedings of the 2021 ACM SIGCOMM 2021 Conference* (pp. 762-774). Association for Computing Machinery. https://doi.org/10.1145/3452296.3472938

Gribkoff, E. (2013). *Applications of deterministic finite automata* [Documento de curso, ECS 120]. University of California, Davis. https://www.cs.ucdavis.edu/~rogaway/classes/120/spring13/eric-dfa.pdf

Instituto Politécnico Nacional. (2021). *Teoría de la Computación: Programa sintético*. Escuela Superior de Cómputo. https://www.escom.ipn.mx/docs/oferta/uaISC2020/teoriaComputacion_ISC2020.pdf

Luna-Benoso, B., Martínez-Perales, J. C., Cortés-Galicia, J., Flores-Carapia, R. y Silva-García, V. M. (2022). Melanoma detection in dermoscopic images using a cellular automata classifier. *Computers, 11*(1), Artículo 8. https://doi.org/10.3390/computers11010008

McCandless, M. (2010, 3 de diciembre). *Using finite state transducers in Lucene* [Entrada de blog]. Changing Bits. https://blog.mikemccandless.com/2010/12/using-finite-state-transducers-in.html

Sipser, M. (2012). *Introduction to the theory of computation* (3.ª ed.). Cengage Learning.

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society, s2-42*(1), 230-265. https://doi.org/10.1112/plms/s2-42.1.230
