from __future__ import annotations

import csv
import sys
from typing import Optional

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
    QVBoxLayout,
)

from graficas import (
    graficar_aproximaciones,
    graficar_error_semilog,
    graficar_metodo_previo,
)
from metodo.biseccion import (
    ResultadoBiseccion,
    biseccion,
    busqueda_incremental,
)
from ui_ventana_principal import Ui_MainWindow


CASOS_PRECARGADOS = [
    {
        "nombre": "Caso Grupo 6 — Circuito RLC serie [0, 400] Ω (εs = 0.05%)",
        "funcion": "exp(-R*0.05/(2*5))*cos(sqrt(1/(5*10^-4) - (R/(2*5))^2)*0.05) - 0.01",
        "xl": 0.0,
        "xu": 400.0,
        "paso": 25.0,
        "es": 0.05,
        "max_iter": 50,
        "verdadero": "328.1514",
        "unidades": "Ω",
    },
    {
        "nombre": "Ejemplo Libro (Chapra Cap. 5) — Paracaidista [12, 16] kg/s (εs = 0.5%)",
        "funcion": "(9.81*68.1/c)*(1 - exp(-(c/68.1)*10)) - 40",
        "xl": 12.0,
        "xu": 16.0,
        "paso": 0.5,
        "es": 0.5,
        "max_iter": 50,
        "verdadero": "14.8011",
        "unidades": "kg/s",
    },
    {
        "nombre": "Referencia Adicional — Paracaidista [12, 20] kg/s (εs = 0.5%)",
        "funcion": "(9.81*68.1/c)*(1 - exp(-(c/68.1)*10)) - 40",
        "xl": 12.0,
        "xu": 20.0,
        "paso": 1.0,
        "es": 0.5,
        "max_iter": 50,
        "verdadero": "14.8011",
        "unidades": "kg/s",
    },
    {
        "nombre": "Referencia Adicional — Diodo semiconductor [0, 1] V (εs = 0.01%)",
        "funcion": "1e-12*(exp(Vd/0.02585) - 1) - (5 - Vd)/1000",
        "xl": 0.0,
        "xu": 1.0,
        "paso": 0.05,
        "es": 0.01,
        "max_iter": 50,
        "verdadero": "0.574147",
        "unidades": "V",
    },
]


class VentanaPrincipal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ultimo_resultado: Optional[ResultadoBiseccion] = None

        # Configurar los 3 lienzos embebidos de Matplotlib en las pestañas
        self.fig_previo, self.canvas_previo = self._crear_lienzo(self.ui.widgetGraficaPrevio)
        self.fig_aprox, self.canvas_aprox = self._crear_lienzo(self.ui.widgetGraficaAprox)
        self.fig_error, self.canvas_error = self._crear_lienzo(self.ui.widgetGraficaError)

        # Configurar tabla
        header = self.ui.tablaResultados.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        # Cargar casos en el QComboBox
        for caso in CASOS_PRECARGADOS:
            self.ui.cmbEjemplos.addItem(caso["nombre"])

        # Conectar señales
        self.ui.cmbEjemplos.currentIndexChanged.connect(self.cargar_ejemplo)
        self.ui.btnGraficarPrevio.clicked.connect(self.ejecutar_metodo_grafico)
        self.ui.btnCalcular.clicked.connect(self.calcular)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnExportarCsv.clicked.connect(self.exportar_csv)

        self.ui.statusbar.showMessage(
            "Asignatura: Cálculo Numérico (MECATR24) | Grupo 6 — Circuito RLC (Método de Bisección)"
        )

        # Precargar el caso del Grupo 6 al iniciar
        self.cargar_ejemplo(0)

    def _crear_lienzo(self, contenedor):
        layout = QVBoxLayout(contenedor)
        layout.setContentsMargins(0, 0, 0, 0)
        fig = Figure(figsize=(6, 4.5), dpi=100)
        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(canvas, contenedor)
        layout.addWidget(toolbar)
        layout.addWidget(canvas)
        return fig, canvas

    def cargar_ejemplo(self, indice: int) -> None:
        if indice < 0 or indice >= len(CASOS_PRECARGADOS):
            return
        caso = CASOS_PRECARGADOS[indice]
        self.ui.txtFuncion.setText(caso["funcion"])
        self.ui.spnXl.setValue(caso["xl"])
        self.ui.spnXu.setValue(caso["xu"])
        self.ui.spnPaso.setValue(caso["paso"])
        self.ui.spnEs.setValue(caso["es"])
        self.ui.spnMaxIter.setValue(caso["max_iter"])
        self.ui.txtValorVerdadero.setText(caso["verdadero"])
        self.ui.txtUnidades.setText(caso["unidades"])
        self.ui.statusbar.showMessage(f"Cargado: {caso['nombre']}")

    def _leer_valor_verdadero(self) -> Optional[float]:
        texto = self.ui.txtValorVerdadero.text().strip()
        if not texto:
            return None
        try:
            return float(texto.replace(",", "."))
        except ValueError as exc:
            raise ValueError(
                "El campo 'Valor verdadero' debe ser un número real válido o dejarse vacío."
            ) from exc

    def ejecutar_metodo_grafico(self) -> None:
        try:
            expr_str = self.ui.txtFuncion.text()
            xl = self.ui.spnXl.value()
            xu = self.ui.spnXu.value()
            paso = self.ui.spnPaso.value()

            intervalos = busqueda_incremental(expr_str, xl, xu, paso)
            graficar_metodo_previo(self.fig_previo, expr_str, xl, xu, intervalos)
            self.canvas_previo.draw()
            self.ui.tabGraficas.setCurrentWidget(self.ui.tabPrevio)

            if intervalos:
                lista_str = ", ".join(f"[{a:.6g}, {b:.6g}]" for a, b in intervalos)
                self.ui.txtResultado.setPlainText(
                    f"Búsqueda incremental (Δx = {paso:g}) en [{xl:g}, {xu:g}]:\n"
                    f"Se detectaron {len(intervalos)} subintervalo(s) con cambio de signo:\n"
                    f"  → {lista_str}\n"
                    f"Puede presionar '2. Calcular Bisección' para hallar la raíz."
                )
            else:
                self.ui.txtResultado.setPlainText(
                    f"Búsqueda incremental (Δx = {paso:g}) en [{xl:g}, {xu:g}]:\n"
                    f"No se detectaron cambios de signo con el paso indicado. "
                    f"Intente reducir Δx o ampliar el intervalo [xl, xu]."
                )
            self.ui.statusbar.showMessage("Método gráfico previo actualizado.")
        except Exception as exc:
            QMessageBox.warning(self, "Error en Método Gráfico", str(exc))

    def calcular(self) -> None:
        try:
            expr_str = self.ui.txtFuncion.text()
            xl = self.ui.spnXl.value()
            xu = self.ui.spnXu.value()
            es = self.ui.spnEs.value()
            max_iter = self.ui.spnMaxIter.value()
            paso = self.ui.spnPaso.value()
            unidad = self.ui.txtUnidades.text().strip()
            valor_verdadero = self._leer_valor_verdadero()

            resultado = biseccion(
                expr_str=expr_str,
                xl=xl,
                xu=xu,
                es=es,
                max_iter=max_iter,
                valor_verdadero=valor_verdadero,
            )
            self.ultimo_resultado = resultado

            self._llenar_tabla(resultado)
            self._mostrar_resumen(resultado, es, unidad)

            # Actualizar las 3 gráficas
            intervalos = busqueda_incremental(expr_str, xl, xu, paso)
            graficar_metodo_previo(self.fig_previo, expr_str, xl, xu, intervalos)
            self.canvas_previo.draw()

            graficar_aproximaciones(self.fig_aprox, expr_str, xl, xu, resultado, unidad)
            self.canvas_aprox.draw()

            graficar_error_semilog(self.fig_error, resultado, es)
            self.canvas_error.draw()

            self.ui.tabGraficas.setCurrentWidget(self.ui.tabAproximaciones)
            self.ui.statusbar.showMessage(
                f"Cálculo completado: {resultado.variable} = {resultado.raiz:.6f} {unidad} "
                f"en {resultado.iteraciones_realizadas} iteraciones."
            )
        except Exception as exc:
            QMessageBox.warning(self, "Error de Validación / Cálculo", str(exc))

    def _llenar_tabla(self, resultado: ResultadoBiseccion) -> None:
        tabla = self.ui.tablaResultados
        tabla.setRowCount(len(resultado.tabla))

        for row_idx, fila in enumerate(resultado.tabla):
            ea_str = f"{fila.ea:.6f} %" if fila.ea is not None else "—"
            et_str = f"{fila.et:.6f} %" if fila.et is not None else "—"

            celdas = [
                str(fila.iteracion),
                f"{fila.xl:.6f}",
                f"{fila.xu:.6f}",
                f"{fila.xr:.6f}",
                f"{fila.f_xl:.8f}",
                f"{fila.f_xr:.8f}",
                f"{fila.producto:.8e}",
                ea_str,
                et_str,
                fila.subintervalo,
            ]
            for col_idx, texto in enumerate(celdas):
                item = QTableWidgetItem(texto)
                if col_idx < 9:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                else:
                    item.setTextAlignment(Qt.AlignCenter)
                tabla.setItem(row_idx, col_idx, item)

    def _mostrar_resumen(
        self, resultado: ResultadoBiseccion, es: float, unidad: str
    ) -> None:
        sufijo_u = f" {unidad}" if unidad else ""
        ea_txt = f"{resultado.ea_final:.6f} %" if resultado.ea_final is not None else "N/A"
        et_txt = f"{resultado.et_final:.6f} %" if resultado.et_final is not None else "No especificado"

        resumen = (
            f"• Raíz encontrada: {resultado.variable} = {resultado.raiz:.6f}{sufijo_u} "
            f"(f({resultado.variable}) = {resultado.f_raiz:.6e})\n"
            f"• Iteraciones realizadas: {resultado.iteraciones_realizadas}  |  "
            f"Iteraciones teóricas n = log2(Δx0 / Ea,d): {resultado.iteraciones_teoricas_exactas:.2f} "
            f"(⌈n⌉ = {resultado.iteraciones_teoricas_enteras})\n"
            f"• Error aproximado alcanzado (εa): {ea_txt} (tolerancia εs = {es:g}%)  |  "
            f"Error verdadero (εt): {et_txt}\n"
            f"• Criterio de parada: {resultado.criterio_parada}"
        )
        self.ui.txtResultado.setPlainText(resumen)

    def limpiar(self) -> None:
        self.ultimo_resultado = None
        self.ui.tablaResultados.setRowCount(0)
        self.ui.txtResultado.clear()
        for fig, canvas in (
            (self.fig_previo, self.canvas_previo),
            (self.fig_aprox, self.canvas_aprox),
            (self.fig_error, self.canvas_error),
        ):
            fig.clear()
            canvas.draw()
        self.ui.statusbar.showMessage("Campos y gráficas limpiados.")

    def exportar_csv(self) -> None:
        if self.ultimo_resultado is None or not self.ultimo_resultado.tabla:
            QMessageBox.information(
                self,
                "Sin resultados",
                "Primero ejecute el cálculo para poder exportar la tabla a CSV.",
            )
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar tabla de iteraciones como CSV",
            "resultados_biseccion_grupo6.csv",
            "Archivos CSV (*.csv)",
        )
        if not ruta:
            return

        try:
            with open(ruta, mode="w", newline="", encoding="utf-8-sig") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(
                    [
                        "i",
                        "xl",
                        "xu",
                        "xr",
                        "f(xl)",
                        "f(xr)",
                        "f(xl)*f(xr)",
                        "ea (%)",
                        "et (%)",
                        "Subintervalo elegido",
                    ]
                )
                for fila in self.ultimo_resultado.tabla:
                    writer.writerow(
                        [
                            fila.iteracion,
                            f"{fila.xl:.8f}",
                            f"{fila.xu:.8f}",
                            f"{fila.xr:.8f}",
                            f"{fila.f_xl:.9f}",
                            f"{fila.f_xr:.9f}",
                            f"{fila.producto:.9e}",
                            f"{fila.ea:.6f}" if fila.ea is not None else "",
                            f"{fila.et:.6f}" if fila.et is not None else "",
                            fila.subintervalo,
                        ]
                    )
            self.ui.statusbar.showMessage(f"Tabla exportada correctamente a: {ruta}")
        except Exception as exc:
            QMessageBox.critical(self, "Error al exportar CSV", str(exc))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())