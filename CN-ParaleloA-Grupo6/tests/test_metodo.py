import pytest

from metodo.biseccion import biseccion, busqueda_incremental


def test_caso_grupo6_circuito_rlc():
    """Validación oficial Grupo 6 (Sección 8): Circuito RLC [0, 400] Ω, εs = 0.05%."""
    expr = "exp(-R*0.05/(2*5))*cos(sqrt(1/(5*10^-4) - (R/(2*5))^2)*0.05) - 0.01"
    res = biseccion(expr, xl=0.0, xu=400.0, es=0.05, max_iter=50, valor_verdadero=328.1514)

    assert res.variable == "R"
    assert res.iteraciones_realizadas == 12
    assert round(res.raiz, 4) == pytest.approx(328.2227, abs=1e-4)
    assert res.ea_final is not None and res.ea_final < 0.05
    assert res.iteraciones_teoricas_enteras == 12


def test_ejemplo_libro_paracaidista_chapra():
    """Validación ejemplo del libro (Chapra Cap. 5) y Grupo 5: Paracaidista [12, 20] kg/s."""
    expr = "(9.81*68.1/c)*(1 - exp(-(c/68.1)*10)) - 40"
    res = biseccion(expr, xl=12.0, xu=20.0, es=0.5, max_iter=50, valor_verdadero=14.8011)

    assert res.variable == "c"
    assert res.iteraciones_realizadas == 7
    assert round(res.raiz, 4) == pytest.approx(14.8125, abs=1e-4)
    assert res.ea_final is not None and res.ea_final < 0.5


def test_referencia_grupo4_diodo():
    """Validación cruzada con caso de referencia Diodo [0, 1] V, εs = 0.01%."""
    expr = "1e-12*(exp(Vd/0.02585) - 1) - (5 - Vd)/1000"
    res = biseccion(expr, xl=0.0, xu=1.0, es=0.01, max_iter=50, valor_verdadero=0.574147)

    assert res.variable == "Vd"
    assert res.iteraciones_realizadas == 15
    assert round(res.raiz, 6) == pytest.approx(0.574127, abs=1e-5)


def test_error_sin_cambio_de_signo():
    """Debe lanzar ValueError cuando f(xl)*f(xu) > 0."""
    with pytest.raises(ValueError, match="No hay cambio de signo"):
        biseccion("x^2 + 4", xl=-2.0, xu=2.0, es=0.01)


def test_busqueda_incremental_rlc():
    """La búsqueda incremental en [0, 400] con paso 25 debe detectar [325, 350]."""
    expr = "exp(-R*0.05/(2*5))*cos(sqrt(1/(5*10^-4) - (R/(2*5))^2)*0.05) - 0.01"
    intervalos = busqueda_incremental(expr, x_inicio=0.0, x_fin=400.0, paso=25.0)

    assert len(intervalos) == 1
    assert intervalos[0] == pytest.approx((325.0, 350.0))


def test_comparacion_con_scipy_en_pruebas():
    """Verificación externa de alta precisión contra la raíz reportada (328.1514 Ω)."""
    expr = "exp(-R*0.05/(2*5))*cos(sqrt(1/(5*10^-4) - (R/(2*5))^2)*0.05) - 0.01"
    res = biseccion(expr, xl=0.0, xu=400.0, es=1e-6, max_iter=100)
    assert res.raiz == pytest.approx(328.1514, abs=1e-4)