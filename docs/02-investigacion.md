# Ejercicio 2. Investigación: qué es la Teoría de la Computación

## 1. ¿Qué es la Teoría de la Computación y qué preguntas se plantea?

La Teoría de la Computación estudia, con modelos matemáticos, qué pueden y qué no pueden hacer las computadoras. Dos autores la presentan así:

- **Sipser (2012)** la organiza alrededor de una pregunta: *¿cuáles son las capacidades y las limitaciones fundamentales de las computadoras?* Tres áreas tradicionales (autómatas, computabilidad y complejidad) están unidas por esa pregunta.
- **Hopcroft, Motwani y Ullman (2007)** parten de los modelos: la teoría de autómatas es el estudio de dispositivos abstractos de cómputo, o "máquinas". Con ellos se estudian los límites del cálculo respondiendo dos preguntas: *¿qué puede hacer una computadora, en absoluto?* (decidibilidad) y *¿qué puede hacer de forma eficiente?* (intratabilidad).

**Comparación.** Coinciden en lo esencial: estudian modelos matemáticos, no computadoras reales, para descubrir los límites de lo calculable. Sipser define el campo por su pregunta central y lo reparte en tres áreas; Hopcroft y sus colegas lo definen por sus modelos y lo resumen en dos preguntas. Esas dos preguntas corresponden a la computabilidad y a la complejidad de Sipser, y las máquinas son la tercera área, la de los autómatas.

## 2. Orígenes

Las ideas de la Teoría de la Computación nacieron de una crisis en las matemáticas:

- **Las paradojas.** En 1901, Bertrand Russell descubrió una contradicción en la teoría de conjuntos: ¿el conjunto de todos los conjuntos que no se contienen a sí mismos se contiene a sí mismo? Si lo hace, no debería; si no lo hace, debería. Así se vio que la teoría de conjuntos "ingenua", en la que se apoyaban las matemáticas, era contradictoria (Deutsch et al., 2026).
- **El programa de Hilbert.** En los años veinte, David Hilbert propuso dar bases firmes a las matemáticas: escribir toda la matemática clásica en sistemas formales de axiomas y demostrar, con métodos finitos y concretos, que esos sistemas no se contradicen (Zach, 2023).
- **El Entscheidungsproblem** (problema de decisión). Hilbert y Ackermann lo plantearon en 1928: encontrar un procedimiento mecánico que decida si cualquier fórmula de la lógica de primer orden es demostrable. Si existiera, cualquier pregunta matemática podría resolverse de forma mecánica (Copeland, 2023).
- **El teorema de incompletitud de Gödel** (1931). Todo sistema formal consistente que exprese la aritmética básica tiene enunciados que no puede probar ni refutar, y tampoco puede demostrar su propia consistencia. Con ello, el programa de Hilbert, tal como se planteó, resultó imposible (Raatikainen, 2025).
- **La respuesta de 1936.** Alonzo Church y Alan Turing demostraron, por separado, que el problema de decisión no tiene solución. Para lograrlo tuvieron que definir con precisión qué es un "procedimiento mecánico", y así nacieron la computabilidad y los modelos de cómputo (Copeland, 2023).

## 3. Las tres ramas

| Rama | Pregunta que responde |
|---|---|
| **Computabilidad** | ¿Qué problemas puede resolver una computadora y cuáles no? Por ejemplo, el problema del paro no tiene solución algorítmica. |
| **Complejidad** | De los problemas que sí se pueden resolver, ¿cuáles se resuelven con eficiencia, es decir, con una cantidad razonable de tiempo y memoria? |
| **Autómatas y lenguajes formales** | ¿Qué modelos de máquina existen, qué lenguajes reconoce o genera cada uno y qué propiedades tienen? |

Fuentes: Sipser (2012) y Hopcroft et al. (2007).

## 4. La tesis de Church-Turing

**Qué afirma.** Todo lo que puede calcularse con un procedimiento efectivo (un método mecánico, paso a paso, como un algoritmo) puede calcularlo una máquina de Turing (Copeland, 2023).

**Modelos equivalentes.** Se demostró que modelos propuestos de forma independiente calculan exactamente las mismas funciones: las máquinas de Turing, las funciones λ-definibles de Church y Kleene, las funciones recursivas de Gödel, los sistemas canónicos de Post, las máquinas de registros y los algoritmos de Markov (Copeland, 2023).

**Por qué es una tesis y no un teorema.** Un teorema se demuestra a partir de definiciones precisas, pero "procedimiento efectivo" es una idea intuitiva e informal. Por eso no se puede demostrar que coincida con lo que hace una máquina de Turing. Lo que la respalda es la evidencia: modelos muy distintos resultaron equivalentes (Copeland, 2023).

## 5. Alfabeto, cadena y lenguaje

**Definiciones formales** (Hopcroft et al., 2007; Sipser, 2012):

- Un **alfabeto** `Σ` es un conjunto finito y no vacío de símbolos. *Ejemplo:* `Σ = {0, 1}`.
- Una **cadena** sobre `Σ` es una secuencia finita de símbolos de `Σ`; su **longitud** `|w|` es el número de símbolos. La **cadena vacía** `λ` (escrita `ε` en algunos libros) no tiene símbolos: `|λ| = 0`. *Ejemplo:* `w = 0110` y `|w| = 4`.
- Un **lenguaje** sobre `Σ` es un conjunto de cadenas sobre `Σ`. *Ejemplo:* `L = {λ, 0, 00, 000, …}`, las cadenas formadas solo por ceros.

**Operaciones sobre cadenas.**

- **Concatenación:** `uv` es `u` seguida de `v`. La cadena `λ` es neutra: `λw = wλ = w`.
- **Potencia:** `w⁰ = λ` y `w^(n+1) = wⁿw`. Ejemplo: `(ab)³ = ababab`.
- **Reflexión:** `w^R` es `w` escrita al revés. Ejemplo: `(abc)^R = cba`.

**Operaciones sobre lenguajes.**

| Operación | Definición |
|---|---|
| Unión `L₁ ∪ L₂` | `{w : w ∈ L₁ o w ∈ L₂}` |
| Intersección `L₁ ∩ L₂` | `{w : w ∈ L₁ y w ∈ L₂}` |
| Diferencia `L₁ − L₂` | `{w : w ∈ L₁ y w ∉ L₂}` |
| Concatenación `L₁L₂` | `{uv : u ∈ L₁ y v ∈ L₂}` |
| Potencia `Lⁿ` | `L⁰ = {λ}` y `L^(n+1) = LⁿL` |
| Reflexión `L^R` | `{w^R : w ∈ L}` |
| Cerradura de Kleene `L*` | `L⁰ ∪ L¹ ∪ L² ∪ …` |
| Cerradura positiva `L⁺` | `L¹ ∪ L² ∪ …` |

**Por qué `Σ⁰ = {λ}`.** `Σⁿ` es el conjunto de las cadenas de longitud `n` sobre `Σ` (Hopcroft et al., 2007). La única cadena de longitud cero es `λ`, así que `Σ⁰ = {λ}`, y no el conjunto vacío. Además, así todo encaja: `Σ^(n+1) = ΣⁿΣ` también vale para `n = 0`, porque `{λ}Σ = Σ`, y la cantidad de cadenas, `|Σ|ⁿ`, vale `1` para `n = 0`. Si `Σ⁰` fuera vacío, todas las potencias lo serían.

**`Σ*` frente a `Σ⁺`.** `Σ*` es el conjunto de todas las cadenas sobre `Σ` e **incluye** a `λ`; `Σ⁺` reúne solo las cadenas **no vacías**, así que `Σ⁺ = Σ* − {λ}`. Por eso un lenguaje sobre `Σ` es cualquier subconjunto de `Σ*`. *Ejemplo:* si `Σ = {a, b}`, entonces `Σ* = {λ, a, b, aa, ab, ba, bb, …}` y `Σ⁺` es el mismo conjunto sin `λ`.

## 6. La jerarquía de Chomsky

En 1959, Noam Chomsky clasificó las gramáticas formales en cuatro tipos, según las reglas que se les permite usar (Chomsky, 1959). A cada tipo le corresponde una clase de lenguajes y un tipo de máquina que reconoce exactamente esa clase (Linz y Rodger, 2022, cap. 11). Cada nivel contiene al de abajo: `regulares ⊂ libres de contexto ⊂ sensibles al contexto ⊂ recursivamente enumerables`.

| Tipo | Lenguajes | Gramática que lo genera | Máquina que lo reconoce |
|---|---|---|---|
| 0 | Recursivamente enumerables | Sin restricciones | Máquina de Turing |
| 1 | Sensibles al contexto | Sensible al contexto (ninguna regla acorta la cadena) | Autómata linealmente acotado |
| 2 | Independientes (libres) del contexto | Independiente del contexto (cada regla reemplaza una sola variable) | Autómata de pila |
| 3 | Regulares | Regular (reglas `A → aB` o `A → a`) | Autómata finito |

## 7. Autómatas finitos y expresiones regulares

**AFD (autómata finito determinista).** Es una quíntupla `M = (Q, Σ, δ, q₀, F)`: `Q` es un conjunto finito de estados, `Σ` el alfabeto, `δ: Q × Σ → Q` la función de transición, `q₀ ∈ Q` el estado inicial y `F ⊆ Q` el conjunto de estados de aceptación (Sipser, 2012). "Determinista" significa que en cada estado y con cada símbolo hay **exactamente una** transición. `M` **acepta** una cadena si, al leerla completa desde `q₀`, termina en un estado de `F`; el lenguaje de `M`, `L(M)`, es el conjunto de cadenas que acepta.

**AFN (autómata finito no determinista).** Tiene los mismos cinco componentes, pero `δ: Q × (Σ ∪ {λ}) → P(Q)`, donde `P(Q)` es el conjunto de subconjuntos de `Q` (Sipser, 2012). En cada paso puede haber varias transiciones, ninguna, o transiciones que no leen símbolo (con `λ`). Acepta una cadena si **al menos una** de las trayectorias posibles termina en un estado de aceptación.

**Equivalencia.** Todo AFN tiene un AFD equivalente, que acepta el mismo lenguaje. La construcción de subconjuntos convierte cada conjunto de estados posibles del AFN en un solo estado del AFD, por lo que el AFD puede necesitar hasta `2ⁿ` estados si el AFN tiene `n` (Hopcroft et al., 2007; Sipser, 2012). Ambos reconocen la misma clase de lenguajes, los regulares, que son también los que describen las expresiones regulares.

**Expresión regular.** Se define por recursión: `∅`, `λ` y cada símbolo `a ∈ Σ` son expresiones regulares, y si `R₁` y `R₂` lo son, también `(R₁ ∪ R₂)`, `(R₁R₂)` y `(R₁)*` (Sipser, 2012). Ejemplo: `(0 ∪ 1)*1` describe las cadenas binarias que terminan en 1.

**Tres problemas reales.**

1. **Validar datos en formularios web.** El atributo `pattern` de HTML recibe una expresión regular que el texto escrito debe cumplir por completo; por ejemplo, `[a-z]{4,8}` exige de 4 a 8 letras minúsculas (MDN Contributors, 2026).
2. **Analizar el código fuente en un compilador.** Los elementos del lenguaje (identificadores, números, palabras reservadas) se describen con expresiones regulares, por ejemplo `[A-Za-z_][A-Za-z0-9_]*` para un identificador, y el compilador las convierte en autómatas finitos que leen el programa (Aho et al., 2007). Thompson (1968) describió cómo transformar una expresión regular en un programa que localiza en un texto las cadenas que la cumplen.
3. **Buscar patrones en proteínas.** La base de datos PROSITE describe sitios funcionales con patrones parecidos a expresiones regulares; por ejemplo, `N-{P}-[ST]-{P}` señala posibles sitios de N-glicosilación: una asparagina, luego cualquier aminoácido excepto prolina, luego serina o treonina, y otro que no sea prolina (SIB Swiss Institute of Bioinformatics, s. f.).

## Referencias

Aho, A. V., Lam, M. S., Sethi, R. y Ullman, J. D. (2007). *Compilers: Principles, techniques, and tools* (2.ª ed.). Pearson Education.

Chomsky, N. (1959). On certain formal properties of grammars. *Information and Control, 2*(2), 137-167. https://doi.org/10.1016/S0019-9958(59)90362-6

Copeland, B. J. (2023). The Church-Turing thesis. En E. N. Zalta y U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. Metaphysics Research Lab, Stanford University. Recuperado el 21 de septiembre de 2026, de https://plato.stanford.edu/entries/church-turing/

Deutsch, H., Marshall, O. e Irvine, A. D. (2026). Russell's paradox. En E. N. Zalta y U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. Metaphysics Research Lab, Stanford University. Recuperado el 21 de septiembre de 2026, de https://plato.stanford.edu/entries/russell-paradox/

Hopcroft, J. E., Motwani, R. y Ullman, J. D. (2007). *Teoría de autómatas, lenguajes y computación* (3.ª ed.). Pearson Educación.

Instituto Politécnico Nacional. (2021). *Teoría de la Computación: Programa sintético*. Escuela Superior de Cómputo. https://www.escom.ipn.mx/docs/oferta/uaISC2020/teoriaComputacion_ISC2020.pdf

Linz, P. y Rodger, S. H. (2022). *An introduction to formal languages and automata* (7.ª ed.). Jones & Bartlett Learning.

MDN Contributors. (2026, 20 de abril). *pattern*. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern

Raatikainen, P. (2025). Gödel's incompleteness theorems. En E. N. Zalta y U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. Metaphysics Research Lab, Stanford University. Recuperado el 21 de septiembre de 2026, de https://plato.stanford.edu/entries/goedel-incompleteness/

SIB Swiss Institute of Bioinformatics. (s. f.). *PDOC00001: N-glycosylation site*. PROSITE. Recuperado el 21 de septiembre de 2026, de https://prosite.expasy.org/PDOC00001

Sipser, M. (2012). *Introduction to the theory of computation* (3.ª ed.). Cengage Learning.

Thompson, K. (1968). Programming techniques: Regular expression search algorithm. *Communications of the ACM, 11*(6), 419-422. https://doi.org/10.1145/363347.363387

Zach, R. (2023). Hilbert's program. En E. N. Zalta y U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. Metaphysics Research Lab, Stanford University. Recuperado el 21 de septiembre de 2026, de https://plato.stanford.edu/entries/hilbert-program/
