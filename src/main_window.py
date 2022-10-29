import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from python_forms.main_window_GUI import Ui_MainWindow
from src.Managers.employees_manager import EmployeesManager
from system_properties import SystemProperties
from src.Managers.clients_manager import ClientsManager
from src.Managers.brokers_manager import BrokersManager
from src.Managers.company_manager import CompaniesManager
from src.Managers.leads_manager import LeadsManager
from src.Managers.invoices_manager import InvoicesManager
from dashboard import Dashboard


class AppMainWindow(QMainWindow):
    reload_dashboard = pyqtSignal()

    def __init__(self, parent=None):
        super(AppMainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.invoices_manager = InvoicesManager()
        self.dashboard = Dashboard()
        self.widgets = dict()
        self.initialize_pages()
        self.connect_signals_slots()
        self.ui.window_content.setCurrentIndex(0)

    def connect_signals_slots(self):
        self.ui.dashboard_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["dashboard"]["index"]))
        self.ui.employees_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["employees_manager"]["index"]))
        self.ui.system_properties_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["system_properties"]["index"]))
        self.ui.clients_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["clients_manager"]["index"]))
        self.ui.companies_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["companies_manager"]["index"])
        )
        self.ui.leads_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["leads_manager"]["index"]))
        self.ui.brokers_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["brokers_manager"]["index"]))
        self.ui.invoices_btn.clicked.connect(
            lambda: self.change_widget(self.widgets["invoices_manager"]["index"]))
        self.invoices_manager.reload_dashboard.connect(self.dashboard.refresh_insights)

    def initialize_pages(self):
        self.widgets = {
            "dashboard":
                {"index": 0, "widget": self.dashboard},
            "system_properties":
                {"index": 1, "widget": SystemProperties()},
            "employees_manager":
                {"index": 2, "widget": EmployeesManager()},
            "clients_manager":
                {"index": 3, "widget": ClientsManager()},
            'companies_manager':
                {"index": 4, "widget": CompaniesManager()},
            "leads_manager":
                {"index": 5, "widget": LeadsManager()},
            "brokers_manager":
                {"index": 6, "widget": BrokersManager()},
            "invoices_manager":
                {"index": 7, "widget": self.invoices_manager}
        }
        [self.ui.window_content.insertWidget(self.widgets[widget]["index"], self.widgets[widget]["widget"]) for widget in self.widgets]

    def change_widget(self, index):
        """
        Change the stacked widget to the widget at index
        :param index:Integer represents the widget's index in the stacked widget
        :return: None
        """
        self.ui.window_content.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec_())