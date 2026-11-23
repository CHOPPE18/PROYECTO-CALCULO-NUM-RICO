from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, List, Optional, Tuple

import numpy as np
import sympy as sp


@dataclass
class IteracionBiseccion:
    """Almacena los datos de una iteración del método de bisección."""

    iteracion: int
    xl: float
    xu: float
    xr: float
    f_xl: float
    f_xr: float
    producto: float
    ea: Optional[float]  # Error relativo porcentual aproximado (%)
    et: Optional[float]  # Error relativo porcentual verdadero (%)
    subintervalo: str


@dataclass
class ResultadoBiseccion:
    """Resultado completo de la ejecución del método de bisección."""

    variable: str
    raiz: float
    f_raiz: float
    iteraciones_realizadas: int
    iteraciones_teoricas_exactas: float
    iteraciones_teoricas_enteras: int
    ea_final: Optional[float]
    et_final: Optional[float]
    criterio_parada: str
    tabla: List[IteracionBiseccion]


def compilar_funcion(
    expr_str: str,
) -> Tuple[sp.Expr, str, Callable[[float], float], Callable[[np.ndarray], np.ndarray]]:
    """
    Interpreta f(x) escrita como texto mediante SymPy y devuelve:
    - Expresión simbólica de SymPy
    - Nombre de la variable independiente detectada (x, R, c, Vd, etc.)
    - Evaluador escalar seguro f(val) -> float
    - Evaluador vectorizado f(arr) -> np.ndarray para graficación y búsqueda incremental
    """
    if not expr_str or not expr_str.strip():
        raise ValueError("Debe ingresar una expresión matemática para f(x).")

    texto_limpio = expr_str.strip().replace("^", "**")
    entorno_local = {"e": sp.E, "pi": sp.pi}

    try:
        expr = sp.sympify(texto_limpio, locals=entorno_local)
    except Exception as exc:
        raise ValueError(f"Expresión inválida en f(x): {exc}") from exc

    simbolos = sorted(expr.free_symbols, key=lambda s: s.name)
    if len(simbolos) > 1:
        nombres = ", ".join(s.name for s in simbolos)
        raise ValueError(
            f"La función debe tener una sola variable independiente. Se detectaron: {nombres}."
        )

    if len(simbolos) == 0:
        valor_const = complex(expr.evalf())
        if abs(valor_const.imag) > 1e-12:
            raise ValueError("La expresión constante produce un número complejo.")
        const_real = float(valor_const.real)
        return (
            expr,
            "x",
            lambda _x: const_real,
            lambda arr: np.full_like(np.asarray(arr, dtype=float), const_real, dtype=float),
        )

    variable = simbolos[0]
    funcion_np = sp.lambdify(variable, expr, modules=["numpy"])

    def f_escalar(x_val: float) -> float:
        with np.errstate(all="ignore"):
            res = funcion_np(float(x_val))

        if isinstance(res, complex) or np.iscomplexobj(res):
            if abs(np.imag(res)) > 1e-10:
                raise ValueError(
                    f"f({x_val:.6g}) produce un valor complejo fuera del dominio real."
                )
            res_float = float(np.real(res))
        else:
            res_float = float(res)

        if math.isnan(res_float) or math.isinf(res_float):
            raise ValueError(
                f"f({x_val:.6g}) no está definida en los reales (NaN o Inf)."
            )
        return res_float

    def f_vectorial(x_arr: np.ndarray) -> np.ndarray:
        arr = np.asarray(x_arr, dtype=float)
        with np.errstate(all="ignore"):
            res = funcion_np(arr)

        res_arr = np.asarray(res)
        if res_arr.ndim == 0:
            res_arr = np.full(arr.shape, res_arr, dtype=complex)

        salida = np.full(arr.shape, np.nan, dtype=float)
        if np.iscomplexobj(res_arr):
            mascara = (np.abs(np.imag(res_arr)) <= 1e-10) & np.isfinite(np.real(res_arr))
            salida[mascara] = np.real(res_arr[mascara])
        else:
            mascara = np.isfinite(res_arr)
            salida[mascara] = res_arr[mascara]
        return salida

    return expr, variable.name, f_escalar, f_vectorial


def busqueda_incremental(
    expr_str: str,
    x_inicio: float,
    x_fin: float,
    paso: float,
) -> List[Tuple[float, float]]:
    """
    Realiza una búsqueda incremental en [x_inicio, x_fin] con incremento delta_x = paso
    y retorna los subintervalos [x_i, x_{i+1}] donde ocurre un cambio de signo.
    """
    if x_fin <= x_inicio:
        raise ValueError("El límite superior debe ser mayor que el límite inferior.")
    if paso <= 0:
        raise ValueError("El paso Δx debe ser estrictamente mayor que cero.")

    _, _, _, f_vec = compilar_funcion(expr_str)

    n_pasos = int(math.ceil((x_fin - x_inicio) / paso))
    if n_pasos > 200_000:
        raise ValueError("El paso Δx es demasiado pequeño para el rango indicado.")

    puntos = np.arange(x_inicio, x_fin, paso, dtype=float)
    if puntos.size == 0 or puntos[-1] < x_fin:
        puntos = np.append(puntos, x_fin)

    valores = f_vec(puntos)
    intervalos: List[Tuple[float, float]] = []

    for i in range(len(puntos) - 1):
        y1, y2 = valores[i], valores[i + 1]
        if math.isnan(y1) or math.isnan(y2):
            continue
        if y1 == 0.0:
            intervalos.append((float(puntos[i]), float(puntos[i + 1])))
        elif y1 * y2 < 0.0:
            intervalos.append((float(puntos[i]), float(puntos[i + 1])))

    return intervalos


