# CN-ParaleloA-Grupo6 — Método de Bisección (Circuito RLC)

Aplicación de escritorio desarrollada en **Python** y **Qt Designer (PySide6)** para resolver ecuaciones no lineales mediante el **Método de Bisección**, aplicada al cálculo de la resistencia crítica $R$ de amortiguamiento en un **circuito RLC serie**.

## Datos de la Asignatura
- **Asignatura:** Cálculo Numérico (`MECATR24`) — Quinto Nivel, Ingeniería Mecatrónica
- **Unidad 1:** Software para cálculo numérico, teoría del error y ecuaciones no lineales
- **Grupo:** Grupo 6 (Proyecto B)

## Integrantes
- **Integrante 1:** [Nombre y Apellido] — Programación de lógica numérica (`metodo/biseccion.py`)
- **Integrante 2:** [Nombre y Apellido] — Diseño de interfaz en Qt Designer (`ui/ventana_principal.ui`) y gráficas
- **Integrante 3:** [Nombre y Apellido] — Pruebas unitarias (`tests/test_metodo.py`), validación y documentación

## Problema de Ingeniería (Circuito RLC)
En un circuito RLC serie con $L = 5\text{ H}$ y $C = 5\times 10^{-4}\text{ F}$, la carga normalizada en $t = 0.05\text{ s}$ debe disiparse al $1\%$ ($q/q_0 = 0.01$), lo que conduce a:

$$f(R) = e^{-\frac{R\cdot 0.05}{2\cdot 5}}\cos\!\left(\sqrt{\frac{1}{5\times 10^{-4}} - \left(\frac{R}{2\cdot 5}\right)^2}\cdot 0.05\right) - 0.01 = 0$$

Con intervalo inicial $[0, 400]\ \Omega$ y tolerancia $\varepsilon_s = 0.05\%$, el método converge en **12 iteraciones** a **$R = 328.2227\ \Omega$** ($\varepsilon_a = 0.0298\%$).

## Instalación y Ejecución
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt

# Si modificas la interfaz en Qt Designer:
pyside6-designer ui/ventana_principal.ui
pyside6-uic ui/ventana_principal.ui -o ui_ventana_principal.py

# Ejecutar la aplicación:
python main.py

# Ejecutar pruebas automatizadas:
pytest -v