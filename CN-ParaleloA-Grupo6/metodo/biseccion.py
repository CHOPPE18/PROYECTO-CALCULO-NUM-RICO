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
     Expresión simbólica de SymPy
     Nombre de la variable independiente detectada (x, R, c, Vd, etc.)
     Evaluador escalar seguro f(val) -> float
     Evaluador vectorizado f(arr) -> np.ndarray para graficación y búsqueda incremental
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


def calcular_iteraciones_teoricas(
    xl_inicial: float,
    xu_inicial: float,
    es_porcentaje: float,
    referencia_raiz: float,
) -> Tuple[float, int]:
    """
    Calcula el número teórico de iteraciones mediante:
        n = log2(Δx0 / Ea,d)
    donde Δx0 = xu - xl y Ea,d = (εs / 100) * |referencia_raiz| (o εs/100 si la raíz es 0).
    """
    dx0 = abs(xu_inicial - xl_inicial)
    escala = abs(referencia_raiz) if abs(referencia_raiz) > 1e-12 else 1.0
    ea_deseado = (es_porcentaje / 100.0) * escala

    if ea_deseado <= 0.0 or dx0 <= ea_deseado:
        return 1.0, 1

    n_exacto = math.log2(dx0 / ea_deseado)
    return n_exacto, int(math.ceil(n_exacto))


def biseccion(
    expr_str: str,
    xl: float,
    xu: float,
    es: float = 0.05,
    max_iter: int = 100,
    valor_verdadero: Optional[float] = None,
) -> ResultadoBiseccion:
    """
    Implementación manual del método de bisección (Chapra & Canale, Cap. 5).

    Parámetros:
        expr_str: expresión matemática f(x) como texto.
        xl: límite inferior del intervalo.
        xu: límite superior del intervalo.
        es: tolerancia porcentual deseada εs (%).
        max_iter: número máximo de iteraciones permitidas.
        valor_verdadero: valor exacto opcional para calcular εt (%).
    """
    if xu <= xl:
        raise ValueError("El extremo superior xu debe ser mayor que el extremo inferior xl.")
    if es <= 0:
        raise ValueError("La tolerancia εs (%) debe ser mayor que cero.")
    if max_iter < 1:
        raise ValueError("El máximo de iteraciones debe ser al menos 1.")

    _, var_name, f, _ = compilar_funcion(expr_str)

    xl_0, xu_0 = float(xl), float(xu)
    fl = f(xl_0)
    fu = f(xu_0)

    if fl * fu > 0.0:
        raise ValueError(
            f"No hay cambio de signo en el intervalo [{xl_0}, {xu_0}]: "
            f"f({xl_0}) = {fl:.6g} y f({xu_0}) = {fu:.6g} tienen el mismo signo."
        )

    tabla: List[IteracionBiseccion] = []
    xr_anterior: Optional[float] = None
    xr = xl_0
    fr = fl
    ea: Optional[float] = None
    et: Optional[float] = None
    criterio_parada = f"Máximo de iteraciones alcanzado ({max_iter})"

    for i in range(1, max_iter + 1):
        xr = (xl + xu) / 2.0
        fl = f(xl)
        fr = f(xr)
        producto = fl * fr

        if xr_anterior is not None:
            if xr != 0.0:
                ea = abs((xr - xr_anterior) / xr) * 100.0
            else:
                ea = abs(xr - xr_anterior) * 100.0
        else:
            ea = None

        if valor_verdadero is not None and valor_verdadero != 0.0:
            et = abs((valor_verdadero - xr) / valor_verdadero) * 100.0
        elif valor_verdadero == 0.0:
            et = abs(xr) * 100.0
        else:
            et = None

        if producto < 0.0:
            subintervalo = "[xl, xr]"
            xu = xr
        elif producto > 0.0:
            subintervalo = "[xr, xu]"
            xl = xr
        else:
            subintervalo = "Raíz exacta"
            ea = 0.0

        tabla.append(
            IteracionBiseccion(
                iteracion=i,
                xl=xl if subintervalo == "[xr, xu]" else (xr if subintervalo == "Raíz exacta" else xl),
                xu=xu,
                xr=xr,
                f_xl=fl,
                f_xr=fr,
                producto=producto,
                ea=ea,
                et=et,
                subintervalo=subintervalo,
            )
        )

        # Restaurar xl/xu de inicio de iteración en la fila registrada para mayor claridad
        if subintervalo == "[xl, xr]":
            tabla[-1].xl = xl
            tabla[-1].xu = xr
        elif subintervalo == "[xr, xu]":
            tabla[-1].xl = xr
            tabla[-1].xu = xu

        if producto == 0.0:
            criterio_parada = f"Raíz exacta encontrada (f(xr) = 0) en la iteración {i}"
            break

        if ea is not None and ea < es:
            criterio_parada = (
                f"Tolerancia cumplida: εa ({ea:.6f}%) < εs ({es:.6f}%) en la iteración {i}"
            )
            break

        xr_anterior = xr

    # Nota: en cada fila guardamos los extremos vigentes AL INICIO de la iteración i
    # Reconstruimos xl_inicio y xu_inicio de cada fila para mostrar exactamente el intervalo partido
    xl_rec, xu_rec = xl_0, xu_0
    for fila in tabla:
        fila.xl = xl_rec
        fila.xu = xu_rec
        if fila.subintervalo == "[xl, xr]":
            xu_rec = fila.xr
        elif fila.subintervalo == "[xr, xu]":
            xl_rec = fila.xr

    ref = valor_verdadero if valor_verdadero is not None else xr
    n_teo_exacto, n_teo_entero = calcular_iteraciones_teoricas(xl_0, xu_0, es, ref)

    return ResultadoBiseccion(
        variable=var_name,
        raiz=xr,
        f_raiz=fr,
        iteraciones_realizadas=len(tabla),
        iteraciones_teoricas_exactas=n_teo_exacto,
        iteraciones_teoricas_enteras=n_teo_entero,
        ea_final=tabla[-1].ea,
        et_final=tabla[-1].et,
        criterio_parada=criterio_parada,
        tabla=tabla,
    )