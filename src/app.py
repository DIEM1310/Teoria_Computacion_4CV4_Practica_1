"""Interfaz con Flet: operaciones básicas sobre cadenas y lenguajes.

Solo arma la pantalla y llama a las funciones de lenguajes.py; no calcula nada por su cuenta.
"""

from datetime import datetime
from pathlib import Path

import flet as ft

import lenguajes as L

RAIZ = Path(__file__).resolve().parent.parent
CARPETA_SALIDAS = RAIZ / "salidas"
LINEAS_VISIBLES = 500       # líneas que se muestran en pantalla; el archivo guardado lleva todas
GRIS = ft.Colors.BLUE_GREY_700
ROJO = ft.Colors.RED_700
VERDE = ft.Colors.GREEN_800


def guardar_archivo(nombre, texto):
    """Guarda el texto en salidas/ y devuelve la ruta relativa a la carpeta del proyecto."""
    CARPETA_SALIDAS.mkdir(exist_ok=True)
    marca = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = CARPETA_SALIDAS / f"{nombre}_{marca}.txt"
    ruta.write_text(texto, encoding="utf-8", newline="\n")
    return ruta.relative_to(RAIZ)


def tarjeta(titulo, cadenas, ancho):
    """Recuadro con un título y la lista desplazable de las primeras cadenas."""
    visibles = cadenas[:LINEAS_VISIBLES]
    controles = [ft.Text(f"{titulo} ({len(cadenas):,})", weight=ft.FontWeight.BOLD)]
    if not cadenas:
        controles.append(ft.Text("Conjunto vacío (∅)", color=GRIS))
    else:
        if len(cadenas) > LINEAS_VISIBLES:
            controles.append(ft.Text(
                f"Se muestran las primeras {LINEAS_VISIBLES:,}; el archivo guardado las incluye todas.",
                size=12, color=GRIS))
        controles.append(ft.ListView(
            height=min(260, 24 * len(visibles)), spacing=2,
            controls=[ft.Text(L.formatear_cadena(c), selectable=True) for c in visibles]))
    return ft.Card(content=ft.Container(width=ancho, padding=12, content=ft.Column(spacing=8, controls=controles)))


def main(page: ft.Page):
    page.title = "Operaciones básicas sobre cadenas y lenguajes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    ultimo = {}     # lo último que se calculó en cada pestaña, para poder guardarlo

    def avisar(control, texto, color):
        control.value = texto
        control.color = color
        control.visible = True

    # ------------------------- Operación 1 -------------------------
    entrada1 = ft.TextField(label="Cadena", hint_text="Ejemplo: abc (vacío = λ)", width=360, autofocus=True)
    mensaje1 = ft.Text(visible=False)
    resumen1 = ft.Text(visible=False, weight=ft.FontWeight.BOLD)
    resultados1 = ft.Row(wrap=True, spacing=12, vertical_alignment=ft.CrossAxisAlignment.START)

    def calcular1(e):
        w = (entrada1.value or "").strip()
        try:
            pre, suf, sub = L.prefijos(w), L.sufijos(w), L.subcadenas(w)
        except ValueError as error:      # incluye LimiteExcedido
            ultimo.pop("op1", None)
            guardar1.disabled = True
            resumen1.visible = False
            resultados1.controls = []
            avisar(mensaje1, str(error), ROJO)
        else:
            ultimo["op1"] = w
            guardar1.disabled = False
            mensaje1.visible = False
            avisar(resumen1,
                   f"Longitud {len(w)}  ·  Prefijos: {len(pre)}  ·  Sufijos: {len(suf)}  ·  "
                   f"Subcadenas distintas: {len(sub):,} (máximo posible: {L.cantidad_maxima_subcadenas(len(w)):,})",
                   None)
            resultados1.controls = [tarjeta("Prefijos", pre, 200), tarjeta("Sufijos", suf, 200),
                                    tarjeta("Subcadenas distintas", sub, 260)]
        page.update()

    def guardar_op1(e):
        ruta = guardar_archivo("prefijos_sufijos_subcadenas", L.texto_operacion1(ultimo["op1"]))
        avisar(mensaje1, f"Guardado en {ruta}", VERDE)
        page.update()

    entrada1.on_submit = calcular1
    guardar1 = ft.Button(content="Guardar en archivo", icon=ft.Icons.SAVE, disabled=True, on_click=guardar_op1)

    vista1 = ft.Column(spacing=14, scroll=ft.ScrollMode.AUTO, expand=True, controls=[
        ft.Text("Escribe una cadena para ver todos sus prefijos, sufijos y subcadenas distintas. "
                f"{L.LAMBDA} es la cadena vacía.", color=GRIS),
        ft.Row(wrap=True, controls=[entrada1, ft.Button(content="Calcular", icon=ft.Icons.PLAY_ARROW,
                                                        on_click=calcular1), guardar1]),
        mensaje1, resumen1, resultados1,
    ])

    # ------------------------- Operación 2 -------------------------
    alfabeto2 = ft.TextField(label="Alfabeto", hint_text="Ejemplo: a, b", width=260)
    longitud2 = ft.TextField(label="Longitud máxima", hint_text="Ejemplo: 3", width=180,
                             keyboard_type=ft.KeyboardType.NUMBER)
    mensaje2 = ft.Text(visible=False)
    resumen2 = ft.Text(visible=False, weight=ft.FontWeight.BOLD)
    resultados2 = ft.Row(wrap=True, spacing=12, vertical_alignment=ft.CrossAxisAlignment.START)

    def calcular2(positiva):
        def manejador(e):
            try:
                simbolos = L.parsear_alfabeto(alfabeto2.value or "")
                try:
                    n = int((longitud2.value or "").strip())
                except ValueError:
                    raise ValueError("La longitud máxima debe ser un número entero.") from None
                cadenas = (L.cerradura_positiva if positiva else L.cerradura_kleene)(simbolos, n)
            except ValueError as error:      # incluye LimiteExcedido
                ultimo.pop("op2", None)
                guardar2.disabled = True
                resumen2.visible = False
                resultados2.controls = []
                avisar(mensaje2, str(error), ROJO)
            else:
                ultimo["op2"] = (simbolos, n, cadenas, positiva)
                guardar2.disabled = False
                mensaje2.visible = False
                nombre = "Σ⁺" if positiva else "Σ*"
                avisar(resumen2, f"{nombre} con Σ = {{{', '.join(simbolos)}}} y longitud máxima {n}: "
                                 f"{len(cadenas):,} cadenas", None)
                resultados2.controls = [tarjeta(nombre, cadenas, 360)]
            page.update()
        return manejador

    def guardar_op2(e):
        simbolos, n, cadenas, positiva = ultimo["op2"]
        nombre = "cerradura_positiva" if positiva else "cerradura_kleene"
        ruta = guardar_archivo(nombre, L.texto_cerradura(simbolos, n, cadenas, positiva))
        avisar(mensaje2, f"Guardado en {ruta}", VERDE)
        page.update()

    guardar2 = ft.Button(content="Guardar en archivo", icon=ft.Icons.SAVE, disabled=True, on_click=guardar_op2)

    vista2 = ft.Column(spacing=14, scroll=ft.ScrollMode.AUTO, expand=True, controls=[
        ft.Text("Calcula Σ* (con λ) o Σ⁺ (sin λ) para un alfabeto, hasta la longitud que elijas. "
                f"Se rechaza lo que pase de {L.LIMITE_CADENAS:,} cadenas o de longitud {L.LONGITUD_MAXIMA:,}.",
                color=GRIS),
        ft.Row(wrap=True, controls=[alfabeto2, longitud2]),
        ft.Row(wrap=True, controls=[
            ft.Button(content="Calcular Σ*", icon=ft.Icons.PLAY_ARROW, on_click=calcular2(False)),
            ft.Button(content="Calcular Σ⁺", icon=ft.Icons.PLAY_ARROW, on_click=calcular2(True)),
            guardar2]),
        mensaje2, resumen2, resultados2,
    ])

    # ------------------------- Pantalla -------------------------
    page.add(
        ft.Text("Operaciones básicas sobre cadenas y lenguajes", size=24, weight=ft.FontWeight.BOLD),
        ft.Tabs(length=2, expand=True, content=ft.Column(expand=True, controls=[
            ft.TabBar(tabs=[ft.Tab(label="Prefijos, sufijos y subcadenas"), ft.Tab(label="Cerraduras Σ* y Σ⁺")]),
            ft.TabBarView(expand=True, controls=[vista1, vista2]),
        ])),
    )


if __name__ == "__main__":
    ft.run(main)
