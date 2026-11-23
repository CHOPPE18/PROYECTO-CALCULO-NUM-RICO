from __future__ import annotations

from typing import List, Tuple
import numpy as np
from matplotlib.figure import Figure

from metodo.biseccion import ResultadoBiseccion, compilar_funcion


def graficar_metodo_previo(
    fig: Figure,
    expr_str: str,
    xl: float,
    xu: float,
    intervalos_sugeridos: List[Tuple[float, float]] | None = None,
) -> None:
    """
    Gráfica 1: Método gráfico previo de f(x) en [xl, xu] resaltando el eje y=0
    y los subintervalos sugeridos por búsqueda incremental.
    """
    fig.clear()
    ax = fig.add_subplot(111)

    _, var_name, _, f_vec = compilar_funcion(expr_str)
    x_vals = np.linspace(xl, xu, 600)
    y_vals = f_vec(x_vals)

    ax.axhline(0.0, color="#334155", linewidth=1.1, linestyle="--", label="Eje y = 0")
    ax.plot(x_vals, y_vals, color="#1d4ed8", linewidth=2.0, label=f"f({var_name})")

    if intervalos_sugeridos:
        for idx, (a, b) in enumerate(intervalos_sugeridos):
            etiqueta = "Cambio de signo detectado" if idx == 0 else None
            ax.axvspan(a, b, color="#22c55e", alpha=0.25, label=etiqueta)
            ax.plot([(a + b) / 2.0], [0.0], "go", markersize=6)

    ax.set_title("Método Gráfico Previo y Búsqueda Incremental")
    ax.set_xlabel(f"Variable ({var_name})")
    ax.set_ylabel(f"f({var_name})")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="best")
    fig.tight_layout()


def graficar_aproximaciones(
    fig: Figure,
    expr_str: str,
    xl: float,
    xu: float,
    resultado: ResultadoBiseccion,
    unidad: str = "",
) -> None:
    """
    Gráfica 2: Curva f(x) en [xl, xu] junto con las aproximaciones xr de cada iteración
    y la raíz final destacada.
    """
    fig.clear()
    ax = fig.add_subplot(111)

    _, var_name, _, f_vec = compilar_funcion(expr_str)
    x_vals = np.linspace(xl, xu, 600)
    y_vals = f_vec(x_vals)

    ax.axhline(0.0, color="#334155", linewidth=1.0, linestyle="--")
    ax.plot(x_vals, y_vals, color="#2563eb", linewidth=1.8, label=f"f({var_name})")

    xrs = [fila.xr for fila in resultado.tabla]
    frs = [fila.f_xr for fila in resultado.tabla]

    ax.scatter(
        xrs[:-1],
        frs[:-1],
        color="#f59e0b",
        edgecolors="#78350f",
        zorder=4,
        s=45,
        label="Aproximaciones xr (iteraciones)",
    )

    for fila in resultado.tabla[:6]:
        ax.annotate(
            f"i={fila.iteracion}",
            (fila.xr, fila.f_xr),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=8,
            color="#92400e",
        )

    sufijo_u = f" {unidad}" if unidad else ""
    ax.scatter(
        [resultado.raiz],
        [resultado.f_raiz],
        color="#dc2626",
        marker="*",
        s=170,
        zorder=5,
        label=f"Raíz ≈ {resultado.raiz:.6f}{sufijo_u}",
    )

    ax.set_title("Convergencia de Aproximaciones xr sobre f(x)")
    ax.set_xlabel(f"{var_name} ({unidad})" if unidad else var_name)
    ax.set_ylabel(f"f({var_name})")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="best")
    fig.tight_layout()


def graficar_error_semilog(
    fig: Figure,
    resultado: ResultadoBiseccion,
    es: float,
) -> None:
    """
    Gráfica 3: Error relativo aproximado εa (%) contra el número de iteración
    en escala semilogarítmica (eje Y logarítmico).
    """
    fig.clear()
    ax = fig.add_subplot(111)

    iters = [f.iteracion for f in resultado.tabla if f.ea is not None and f.ea > 0]
    eas = [f.ea for f in resultado.tabla if f.ea is not None and f.ea > 0]

    if iters:
        ax.semilogy(
            iters,
            eas,
            marker="o",
            color="#0f766e",
            linewidth=2.0,
            label="Error aproximado εa (%)",
        )
        ax.set_xticks(iters)
    else:
        ax.text(
            0.5,
            0.5,
            "Convergencia exacta en la primera iteración (εa = 0%)",
            ha="center",
            va="center",
            transform=ax.transAxes,
        )

    ax.axhline(
        es,
        color="#dc2626",
        linestyle="--",
        linewidth=1.3,
        label=f"Tolerancia εs = {es}%",
    )

    ax.set_title("Convergencia del Error Aproximado εa (Escala Semilogarítmica)")
    ax.set_xlabel("Iteración (i)")
    ax.set_ylabel("Error aproximado εa (%) [escala log]")
    ax.grid(True, which="both", linestyle=":", alpha=0.6)
    ax.legend(loc="best")
    fig.tight_layout()