# -*- coding: utf-8 -*-
# Archivo generado a partir de ui/ventana_principal.ui
# Regenerar con: pyside6-uic ui/ventana_principal.ui -o ui_ventana_principal.py

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 820)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutMain = QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")

        self.grpParametros = QGroupBox(self.centralwidget)
        self.grpParametros.setObjectName("grpParametros")
        self.gridParametros = QGridLayout(self.grpParametros)
        self.gridParametros.setObjectName("gridParametros")

        self.lblEjemplo = QLabel(self.grpParametros)
        self.lblEjemplo.setObjectName("lblEjemplo")
        self.gridParametros.addWidget(self.lblEjemplo, 0, 0, 1, 1)

        self.cmbEjemplos = QComboBox(self.grpParametros)
        self.cmbEjemplos.setObjectName("cmbEjemplos")
        self.gridParametros.addWidget(self.cmbEjemplos, 0, 1, 1, 3)

        self.lblUnidades = QLabel(self.grpParametros)
        self.lblUnidades.setObjectName("lblUnidades")
        self.gridParametros.addWidget(self.lblUnidades, 0, 4, 1, 1)

        self.txtUnidades = QLineEdit(self.grpParametros)
        self.txtUnidades.setObjectName("txtUnidades")
        self.gridParametros.addWidget(self.txtUnidades, 0, 5, 1, 1)

        self.lblFuncion = QLabel(self.grpParametros)
        self.lblFuncion.setObjectName("lblFuncion")
        self.gridParametros.addWidget(self.lblFuncion, 1, 0, 1, 1)

        self.txtFuncion = QLineEdit(self.grpParametros)
        self.txtFuncion.setObjectName("txtFuncion")
        self.gridParametros.addWidget(self.txtFuncion, 1, 1, 1, 5)

        self.lblXl = QLabel(self.grpParametros)
        self.lblXl.setObjectName("lblXl")
        self.gridParametros.addWidget(self.lblXl, 2, 0, 1, 1)

        self.spnXl = QDoubleSpinBox(self.grpParametros)
        self.spnXl.setObjectName("spnXl")
        self.spnXl.setDecimals(6)
        self.spnXl.setRange(-1000000.0, 1000000.0)
        self.gridParametros.addWidget(self.spnXl, 2, 1, 1, 1)

        self.lblXu = QLabel(self.grpParametros)
        self.lblXu.setObjectName("lblXu")
        self.gridParametros.addWidget(self.lblXu, 2, 2, 1, 1)

        self.spnXu = QDoubleSpinBox(self.grpParametros)
        self.spnXu.setObjectName("spnXu")
        self.spnXu.setDecimals(6)
        self.spnXu.setRange(-1000000.0, 1000000.0)
        self.spnXu.setValue(400.0)
        self.gridParametros.addWidget(self.spnXu, 2, 3, 1, 1)

        self.lblPaso = QLabel(self.grpParametros)
        self.lblPaso.setObjectName("lblPaso")
        self.gridParametros.addWidget(self.lblPaso, 2, 4, 1, 1)

        self.spnPaso = QDoubleSpinBox(self.grpParametros)
        self.spnPaso.setObjectName("spnPaso")
        self.spnPaso.setDecimals(4)
        self.spnPaso.setRange(0.0001, 10000.0)
        self.spnPaso.setValue(10.0)
        self.gridParametros.addWidget(self.spnPaso, 2, 5, 1, 1)

        self.lblEs = QLabel(self.grpParametros)
        self.lblEs.setObjectName("lblEs")
        self.gridParametros.addWidget(self.lblEs, 3, 0, 1, 1)

        self.spnEs = QDoubleSpinBox(self.grpParametros)
        self.spnEs.setObjectName("spnEs")
        self.spnEs.setDecimals(6)
        self.spnEs.setRange(0.000001, 100.0)
        self.spnEs.setValue(0.05)
        self.gridParametros.addWidget(self.spnEs, 3, 1, 1, 1)

        self.lblMaxIter = QLabel(self.grpParametros)
        self.lblMaxIter.setObjectName("lblMaxIter")
        self.gridParametros.addWidget(self.lblMaxIter, 3, 2, 1, 1)

        self.spnMaxIter = QSpinBox(self.grpParametros)
        self.spnMaxIter.setObjectName("spnMaxIter")
        self.spnMaxIter.setRange(1, 1000)
        self.spnMaxIter.setValue(50)
        self.gridParametros.addWidget(self.spnMaxIter, 3, 3, 1, 1)

        self.lblValorVerdadero = QLabel(self.grpParametros)
        self.lblValorVerdadero.setObjectName("lblValorVerdadero")
        self.gridParametros.addWidget(self.lblValorVerdadero, 3, 4, 1, 1)

        self.txtValorVerdadero = QLineEdit(self.grpParametros)
        self.txtValorVerdadero.setObjectName("txtValorVerdadero")
        self.gridParametros.addWidget(self.txtValorVerdadero, 3, 5, 1, 1)

        self.verticalLayoutMain.addWidget(self.grpParametros)

        self.horizontalLayoutBotones = QHBoxLayout()
        self.horizontalLayoutBotones.setObjectName("horizontalLayoutBotones")

        self.btnGraficarPrevio = QPushButton(self.centralwidget)
        self.btnGraficarPrevio.setObjectName("btnGraficarPrevio")
        self.horizontalLayoutBotones.addWidget(self.btnGraficarPrevio)

        self.btnCalcular = QPushButton(self.centralwidget)
        self.btnCalcular.setObjectName("btnCalcular")
        self.horizontalLayoutBotones.addWidget(self.btnCalcular)

        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.horizontalLayoutBotones.addWidget(self.btnLimpiar)

        self.btnExportarCsv = QPushButton(self.centralwidget)
        self.btnExportarCsv.setObjectName("btnExportarCsv")
        self.horizontalLayoutBotones.addWidget(self.btnExportarCsv)

        self.verticalLayoutMain.addLayout(self.horizontalLayoutBotones)

        self.splitterContenido = QSplitter(self.centralwidget)
        self.splitterContenido.setObjectName("splitterContenido")
        self.splitterContenido.setOrientation(Qt.Horizontal)

        self.panelIzquierdo = QWidget(self.splitterContenido)
        self.panelIzquierdo.setObjectName("panelIzquierdo")
        self.verticalLayoutIzq = QVBoxLayout(self.panelIzquierdo)
        self.verticalLayoutIzq.setObjectName("verticalLayoutIzq")

        self.grpResultado = QGroupBox(self.panelIzquierdo)
        self.grpResultado.setObjectName("grpResultado")
        self.verticalLayoutRes = QVBoxLayout(self.grpResultado)
        self.verticalLayoutRes.setObjectName("verticalLayoutRes")

        self.txtResultado = QTextEdit(self.grpResultado)
        self.txtResultado.setObjectName("txtResultado")
        self.txtResultado.setMaximumSize(QSize(16777215, 155))
        self.txtResultado.setReadOnly(True)
        self.verticalLayoutRes.addWidget(self.txtResultado)

        self.verticalLayoutIzq.addWidget(self.grpResultado)

        self.grpTabla = QGroupBox(self.panelIzquierdo)
        self.grpTabla.setObjectName("grpTabla")
        self.verticalLayoutTabla = QVBoxLayout(self.grpTabla)
        self.verticalLayoutTabla.setObjectName("verticalLayoutTabla")

        self.tablaResultados = QTableWidget(self.grpTabla)
        self.tablaResultados.setObjectName("tablaResultados")
        self.tablaResultados.setAlternatingRowColors(True)
        self.tablaResultados.setColumnCount(10)
        encabezados = [
            "i",
            "xl",
            "xu",
            "xr",
            "f(xl)",
            "f(xr)",
            "f(xl)·f(xr)",
            "εa (%)",
            "εt (%)",
            "Subintervalo elegido",
        ]
        for idx, texto in enumerate(encabezados):
            self.tablaResultados.setHorizontalHeaderItem(idx, QTableWidgetItem(texto))

        self.verticalLayoutTabla.addWidget(self.tablaResultados)
        self.verticalLayoutIzq.addWidget(self.grpTabla)

        self.splitterContenido.addWidget(self.panelIzquierdo)

        self.tabGraficas = QTabWidget(self.splitterContenido)
        self.tabGraficas.setObjectName("tabGraficas")

        self.tabPrevio = QWidget()
        self.tabPrevio.setObjectName("tabPrevio")
        self.layoutGraficaPrevio = QVBoxLayout(self.tabPrevio)
        self.widgetGraficaPrevio = QWidget(self.tabPrevio)
        self.widgetGraficaPrevio.setObjectName("widgetGraficaPrevio")
        self.layoutGraficaPrevio.addWidget(self.widgetGraficaPrevio)
        self.tabGraficas.addTab(self.tabPrevio, "Método Gráfico Previo")

        self.tabAproximaciones = QWidget()
        self.tabAproximaciones.setObjectName("tabAproximaciones")
        self.layoutGraficaAprox = QVBoxLayout(self.tabAproximaciones)
        self.widgetGraficaAprox = QWidget(self.tabAproximaciones)
        self.widgetGraficaAprox.setObjectName("widgetGraficaAprox")
        self.layoutGraficaAprox.addWidget(self.widgetGraficaAprox)
        self.tabGraficas.addTab(self.tabAproximaciones, "f(x) y Puntos xr")

        self.tabError = QWidget()
        self.tabError.setObjectName("tabError")
        self.layoutGraficaError = QVBoxLayout(self.tabError)
        self.widgetGraficaError = QWidget(self.tabError)
        self.widgetGraficaError.setObjectName("widgetGraficaError")
        self.layoutGraficaError.addWidget(self.widgetGraficaError)
        self.tabGraficas.addTab(self.tabError, "Convergencia εa (Semilog)")

        self.tabAcercaDe = QWidget()
        self.tabAcercaDe.setObjectName("tabAcercaDe")
        self.layoutAcercaDe = QVBoxLayout(self.tabAcercaDe)
        self.txtAcercaDe = QTextEdit(self.tabAcercaDe)
        self.txtAcercaDe.setObjectName("txtAcercaDe")
        self.txtAcercaDe.setReadOnly(True)
        self.layoutAcercaDe.addWidget(self.txtAcercaDe)
        self.tabGraficas.addTab(self.tabAcercaDe, "Acerca de")

        self.splitterContenido.addWidget(self.tabGraficas)
        self.splitterContenido.setSizes([640, 600])

        self.verticalLayoutMain.addWidget(self.splitterContenido)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                "Cálculo Numérico (MECATR24) — Método de Bisección | Grupo 6",
            )
        )
        self.grpParametros.setTitle("Parámetros del Método de Bisección y Caso de Ingeniería")
        self.lblEjemplo.setText("Caso / Ejemplo:")
        self.lblUnidades.setText("Unidades físicas:")
        self.txtUnidades.setText("Ω")
        self.lblFuncion.setText("Función f(x) = 0:")
        self.lblXl.setText("Extremo inferior (xl):")
        self.lblXu.setText("Extremo superior (xu):")
        self.lblPaso.setText("Paso búsqueda Δx:")
        self.lblEs.setText("Tolerancia εs (%):")
        self.lblMaxIter.setText("Máx. iteraciones:")
        self.lblValorVerdadero.setText("Valor verdadero (opc.):")
        self.btnGraficarPrevio.setText("1. Graficar y Buscar Intervalos (Δx)")
        self.btnCalcular.setText("2. Calcular Bisección")
        self.btnLimpiar.setText("Limpiar")
        self.btnExportarCsv.setText("Exportar CSV")
        self.grpResultado.setTitle("Resumen de Resultados y Análisis de Convergencia")
        self.grpTabla.setTitle("Tabla de Iteraciones")
        self.txtAcercaDe.setHtml(
            """<html><body style="font-family: sans-serif; line-height: 1.5;">
            <h2>Proyecto de Aula — Cálculo Numérico (MECATR24)</h2>
            <p><b>Carrera:</b> Ingeniería Mecatrónica — Quinto Nivel<br>
            <b>Unidad 1:</b> Software para cálculo numérico, teoría del error y ecuaciones no lineales<br>
            <b>Proyecto B:</b> Método de Bisección aplicado al Circuito RLC serie<br>
            <b>Grupo:</b> Grupo 6 &nbsp;|&nbsp; <b>Paralelo:</b> [Colocar Paralelo A o B]</p>
            <h3>Integrantes del Equipo</h3>
            <ul>
              <li>Integrante 1: [Nombre y Apellido — Lógica numérica]</li>
              <li>Integrante 2: [Nombre y Apellido — Diseño Qt Designer e interfaz]</li>
              <li>Integrante 3: [Nombre y Apellido — Validación, pruebas y documentación]</li>
            </ul>
            <p><i>Texto base: Chapra y Canale, Métodos numéricos para ingenieros, Capítulos 3, 4 y 5.</i></p>
            </body></html>"""
        )