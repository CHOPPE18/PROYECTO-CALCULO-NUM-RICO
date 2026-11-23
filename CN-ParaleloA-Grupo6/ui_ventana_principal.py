# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QSplitter, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1260, 820)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutMain = QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.grpParametros = QGroupBox(self.centralwidget)
        self.grpParametros.setObjectName(u"grpParametros")
        self.gridParametros = QGridLayout(self.grpParametros)
        self.gridParametros.setObjectName(u"gridParametros")
        self.lblEjemplo = QLabel(self.grpParametros)
        self.lblEjemplo.setObjectName(u"lblEjemplo")

        self.gridParametros.addWidget(self.lblEjemplo, 0, 0, 1, 1)

        self.cmbEjemplos = QComboBox(self.grpParametros)
        self.cmbEjemplos.setObjectName(u"cmbEjemplos")

        self.gridParametros.addWidget(self.cmbEjemplos, 0, 1, 1, 3)

        self.lblUnidades = QLabel(self.grpParametros)
        self.lblUnidades.setObjectName(u"lblUnidades")

        self.gridParametros.addWidget(self.lblUnidades, 0, 4, 1, 1)

        self.txtUnidades = QLineEdit(self.grpParametros)
        self.txtUnidades.setObjectName(u"txtUnidades")

        self.gridParametros.addWidget(self.txtUnidades, 0, 5, 1, 1)

        self.lblFuncion = QLabel(self.grpParametros)
        self.lblFuncion.setObjectName(u"lblFuncion")

        self.gridParametros.addWidget(self.lblFuncion, 1, 0, 1, 1)

        self.txtFuncion = QLineEdit(self.grpParametros)
        self.txtFuncion.setObjectName(u"txtFuncion")

        self.gridParametros.addWidget(self.txtFuncion, 1, 1, 1, 5)

        self.lblXl = QLabel(self.grpParametros)
        self.lblXl.setObjectName(u"lblXl")

        self.gridParametros.addWidget(self.lblXl, 2, 0, 1, 1)

        self.spnXl = QDoubleSpinBox(self.grpParametros)
        self.spnXl.setObjectName(u"spnXl")
        self.spnXl.setDecimals(6)
        self.spnXl.setMinimum(-1000000.000000000000000)
        self.spnXl.setMaximum(1000000.000000000000000)

        self.gridParametros.addWidget(self.spnXl, 2, 1, 1, 1)

        self.lblXu = QLabel(self.grpParametros)
        self.lblXu.setObjectName(u"lblXu")

        self.gridParametros.addWidget(self.lblXu, 2, 2, 1, 1)

        self.spnXu = QDoubleSpinBox(self.grpParametros)
        self.spnXu.setObjectName(u"spnXu")
        self.spnXu.setDecimals(6)
        self.spnXu.setMinimum(-1000000.000000000000000)
        self.spnXu.setMaximum(1000000.000000000000000)
        self.spnXu.setValue(400.000000000000000)

        self.gridParametros.addWidget(self.spnXu, 2, 3, 1, 1)

        self.lblPaso = QLabel(self.grpParametros)
        self.lblPaso.setObjectName(u"lblPaso")

        self.gridParametros.addWidget(self.lblPaso, 2, 4, 1, 1)

        self.spnPaso = QDoubleSpinBox(self.grpParametros)
        self.spnPaso.setObjectName(u"spnPaso")
        self.spnPaso.setDecimals(4)
        self.spnPaso.setMinimum(0.000100000000000)
        self.spnPaso.setMaximum(10000.000000000000000)
        self.spnPaso.setValue(10.000000000000000)

        self.gridParametros.addWidget(self.spnPaso, 2, 5, 1, 1)

        self.lblEs = QLabel(self.grpParametros)
        self.lblEs.setObjectName(u"lblEs")

        self.gridParametros.addWidget(self.lblEs, 3, 0, 1, 1)

        self.spnEs = QDoubleSpinBox(self.grpParametros)
        self.spnEs.setObjectName(u"spnEs")
        self.spnEs.setDecimals(6)
        self.spnEs.setMinimum(0.000001000000000)
        self.spnEs.setMaximum(100.000000000000000)
        self.spnEs.setValue(0.050000000000000)

        self.gridParametros.addWidget(self.spnEs, 3, 1, 1, 1)

        self.lblMaxIter = QLabel(self.grpParametros)
        self.lblMaxIter.setObjectName(u"lblMaxIter")

        self.gridParametros.addWidget(self.lblMaxIter, 3, 2, 1, 1)

        self.spnMaxIter = QSpinBox(self.grpParametros)
        self.spnMaxIter.setObjectName(u"spnMaxIter")
        self.spnMaxIter.setMinimum(1)
        self.spnMaxIter.setMaximum(1000)
        self.spnMaxIter.setValue(50)

        self.gridParametros.addWidget(self.spnMaxIter, 3, 3, 1, 1)

        self.lblValorVerdadero = QLabel(self.grpParametros)
        self.lblValorVerdadero.setObjectName(u"lblValorVerdadero")

        self.gridParametros.addWidget(self.lblValorVerdadero, 3, 4, 1, 1)

        self.txtValorVerdadero = QLineEdit(self.grpParametros)
        self.txtValorVerdadero.setObjectName(u"txtValorVerdadero")

        self.gridParametros.addWidget(self.txtValorVerdadero, 3, 5, 1, 1)


        self.verticalLayoutMain.addWidget(self.grpParametros)

        self.horizontalLayoutBotones = QHBoxLayout()
        self.horizontalLayoutBotones.setObjectName(u"horizontalLayoutBotones")
        self.btnGraficarPrevio = QPushButton(self.centralwidget)
        self.btnGraficarPrevio.setObjectName(u"btnGraficarPrevio")

        self.horizontalLayoutBotones.addWidget(self.btnGraficarPrevio)

        self.btnCalcular = QPushButton(self.centralwidget)
        self.btnCalcular.setObjectName(u"btnCalcular")

        self.horizontalLayoutBotones.addWidget(self.btnCalcular)

        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.horizontalLayoutBotones.addWidget(self.btnLimpiar)

        self.btnExportarCsv = QPushButton(self.centralwidget)
        self.btnExportarCsv.setObjectName(u"btnExportarCsv")

        self.horizontalLayoutBotones.addWidget(self.btnExportarCsv)


        self.verticalLayoutMain.addLayout(self.horizontalLayoutBotones)

        self.splitterContenido = QSplitter(self.centralwidget)
        self.splitterContenido.setObjectName(u"splitterContenido")
        self.splitterContenido.setOrientation(Qt.Horizontal)
        self.panelIzquierdo = QWidget(self.splitterContenido)
        self.panelIzquierdo.setObjectName(u"panelIzquierdo")
        self.verticalLayoutIzq = QVBoxLayout(self.panelIzquierdo)
        self.verticalLayoutIzq.setObjectName(u"verticalLayoutIzq")
        self.grpResultado = QGroupBox(self.panelIzquierdo)
        self.grpResultado.setObjectName(u"grpResultado")
        self.verticalLayoutRes = QVBoxLayout(self.grpResultado)
        self.verticalLayoutRes.setObjectName(u"verticalLayoutRes")
        self.txtResultado = QTextEdit(self.grpResultado)
        self.txtResultado.setObjectName(u"txtResultado")
        self.txtResultado.setMaximumSize(QSize(16777215, 155))
        self.txtResultado.setReadOnly(True)

        self.verticalLayoutRes.addWidget(self.txtResultado)


        self.verticalLayoutIzq.addWidget(self.grpResultado)

        self.grpTabla = QGroupBox(self.panelIzquierdo)
        self.grpTabla.setObjectName(u"grpTabla")
        self.verticalLayoutTabla = QVBoxLayout(self.grpTabla)
        self.verticalLayoutTabla.setObjectName(u"verticalLayoutTabla")
        self.tablaResultados = QTableWidget(self.grpTabla)
        if (self.tablaResultados.columnCount() < 10):
            self.tablaResultados.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tablaResultados.setObjectName(u"tablaResultados")
        self.tablaResultados.setAlternatingRowColors(True)
        self.tablaResultados.setColumnCount(10)

        self.verticalLayoutTabla.addWidget(self.tablaResultados)


        self.verticalLayoutIzq.addWidget(self.grpTabla)

        self.splitterContenido.addWidget(self.panelIzquierdo)
        self.tabGraficas = QTabWidget(self.splitterContenido)
        self.tabGraficas.setObjectName(u"tabGraficas")
        self.tabPrevio = QWidget()
        self.tabPrevio.setObjectName(u"tabPrevio")
        self.layoutGraficaPrevio = QVBoxLayout(self.tabPrevio)
        self.layoutGraficaPrevio.setObjectName(u"layoutGraficaPrevio")
        self.widgetGraficaPrevio = QWidget(self.tabPrevio)
        self.widgetGraficaPrevio.setObjectName(u"widgetGraficaPrevio")

        self.layoutGraficaPrevio.addWidget(self.widgetGraficaPrevio)

        self.tabGraficas.addTab(self.tabPrevio, "")
        self.tabAproximaciones = QWidget()
        self.tabAproximaciones.setObjectName(u"tabAproximaciones")
        self.layoutGraficaAprox = QVBoxLayout(self.tabAproximaciones)
        self.layoutGraficaAprox.setObjectName(u"layoutGraficaAprox")
        self.widgetGraficaAprox = QWidget(self.tabAproximaciones)
        self.widgetGraficaAprox.setObjectName(u"widgetGraficaAprox")

        self.layoutGraficaAprox.addWidget(self.widgetGraficaAprox)

        self.tabGraficas.addTab(self.tabAproximaciones, "")
        self.tabError = QWidget()
        self.tabError.setObjectName(u"tabError")
        self.layoutGraficaError = QVBoxLayout(self.tabError)
        self.layoutGraficaError.setObjectName(u"layoutGraficaError")
        self.widgetGraficaError = QWidget(self.tabError)
        self.widgetGraficaError.setObjectName(u"widgetGraficaError")

        self.layoutGraficaError.addWidget(self.widgetGraficaError)

        self.tabGraficas.addTab(self.tabError, "")
        self.tabAcercaDe = QWidget()
        self.tabAcercaDe.setObjectName(u"tabAcercaDe")
        self.layoutAcercaDe = QVBoxLayout(self.tabAcercaDe)
        self.layoutAcercaDe.setObjectName(u"layoutAcercaDe")
        self.txtAcercaDe = QTextEdit(self.tabAcercaDe)
        self.txtAcercaDe.setObjectName(u"txtAcercaDe")
        self.txtAcercaDe.setReadOnly(True)

        self.layoutAcercaDe.addWidget(self.txtAcercaDe)

        self.tabGraficas.addTab(self.tabAcercaDe, "")
        self.splitterContenido.addWidget(self.tabGraficas)

        self.verticalLayoutMain.addWidget(self.splitterContenido)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabGraficas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"C\u00e1lculo Num\u00e9rico (MECATR24) \u2014 M\u00e9todo de Bisecci\u00f3n | Grupo 6", None))
        self.grpParametros.setTitle(QCoreApplication.translate("MainWindow", u"Par\u00e1metros del M\u00e9todo de Bisecci\u00f3n y Caso de Ingenier\u00eda", None))
        self.lblEjemplo.setText(QCoreApplication.translate("MainWindow", u"Caso / Ejemplo:", None))
        self.lblUnidades.setText(QCoreApplication.translate("MainWindow", u"Unidades f\u00edsicas:", None))
        self.txtUnidades.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.txtUnidades.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej.: \u03a9, kg/s, V", None))
        self.lblFuncion.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n f(x) = 0:", None))
        self.txtFuncion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej.: exp(-R*0.05/(2*5))*cos(sqrt(1/(5*10^-4) - (R/(2*5))^2)*0.05) - 0.01", None))
        self.lblXl.setText(QCoreApplication.translate("MainWindow", u"Extremo inferior (xl):", None))
        self.lblXu.setText(QCoreApplication.translate("MainWindow", u"Extremo superior (xu):", None))
        self.lblPaso.setText(QCoreApplication.translate("MainWindow", u"Paso b\u00fasqueda \u0394x:", None))
        self.lblEs.setText(QCoreApplication.translate("MainWindow", u"Tolerancia \u03b5s (%):", None))
        self.lblMaxIter.setText(QCoreApplication.translate("MainWindow", u"M\u00e1x. iteraciones:", None))
        self.lblValorVerdadero.setText(QCoreApplication.translate("MainWindow", u"Valor verdadero (opc.):", None))
        self.txtValorVerdadero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej.: 328.1514 (para calcular \u03b5t)", None))
        self.btnGraficarPrevio.setText(QCoreApplication.translate("MainWindow", u"1. Graficar y Buscar Intervalos (\u0394x)", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"2. Calcular Bisecci\u00f3n", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnExportarCsv.setText(QCoreApplication.translate("MainWindow", u"Exportar CSV", None))
        self.grpResultado.setTitle(QCoreApplication.translate("MainWindow", u"Resumen de Resultados y An\u00e1lisis de Convergencia", None))
        self.grpTabla.setTitle(QCoreApplication.translate("MainWindow", u"Tabla de Iteraciones", None))
        ___qtablewidgetitem = self.tablaResultados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"i", None))
        ___qtablewidgetitem1 = self.tablaResultados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"xl", None))
        ___qtablewidgetitem2 = self.tablaResultados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"xu", None))
        ___qtablewidgetitem3 = self.tablaResultados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"xr", None))
        ___qtablewidgetitem4 = self.tablaResultados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"f(xl)", None))
        ___qtablewidgetitem5 = self.tablaResultados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"f(xr)", None))
        ___qtablewidgetitem6 = self.tablaResultados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"f(xl)\u00b7f(xr)", None))
        ___qtablewidgetitem7 = self.tablaResultados.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u03b5a (%)", None))
        ___qtablewidgetitem8 = self.tablaResultados.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u03b5t (%)", None))
        ___qtablewidgetitem9 = self.tablaResultados.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Subintervalo elegido", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabPrevio), QCoreApplication.translate("MainWindow", u"M\u00e9todo Gr\u00e1fico Previo", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabAproximaciones), QCoreApplication.translate("MainWindow", u"f(x) y Puntos xr", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabError), QCoreApplication.translate("MainWindow", u"Convergencia \u03b5a (Semilog)", None))
        self.txtAcercaDe.setHtml(QCoreApplication.translate("MainWindow", u"<html><body style=\"font-family: sans-serif; line-height: 1.5;\">\n"
"<h2>Proyecto de Aula \u2014 C\u00e1lculo Num\u00e9rico (MECATR24)</h2>\n"
"<p><b>Carrera:</b> Ingenier\u00eda Mecatr\u00f3nica \u2014 Quinto Nivel<br>\n"
"<b>Unidad 1:</b> Software para c\u00e1lculo num\u00e9rico, teor\u00eda del error y ecuaciones no lineales<br>\n"
"<b>Proyecto B:</b> M\u00e9todo de Bisecci\u00f3n aplicado al Circuito RLC serie<br>\n"
"<b>Grupo:</b> Grupo 6 &nbsp;|&nbsp; <b>Paralelo:</b> A</p>\n"
"<h3>Integrantes del Equipo</h3>\n"
"<ul>\n"
"<li>Integrante 1: JOHNNY MANUEL FLORES MENENDEZ \u2014 Programaci\u00f3n de l\u00f3gica num\u00e9rica</li>\n"
"<li>Integrante 2: CARLOS STEVEN HOPPE BARCIA \u2014 Dise\u00f1o de interfaz en Qt Designer y gr\u00e1ficas</li>\n"
"<li>Integrante 3: JENS LEONARD VERA PANCHANA \u2014 Pruebas unitarias, validaci\u00f3n y documentaci\u00f3n </li>\n"
"</ul>\n"
"</body></html>", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabAcercaDe), QCoreApplication.translate("MainWindow", u"Acerca de", None))
    # retranslateUi

