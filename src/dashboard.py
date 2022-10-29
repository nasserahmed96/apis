from PyQt5.QtWidgets import QWidget
from src.DataAccessObjects.DashboardDao import DashboardDao
import datetime
from python_forms.dashboard_GUI import Ui_dashboard_widget
from src.Managers.invoices_manager import InvoicesManager


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent=parent)
        self.ui = Ui_dashboard_widget()
        self.ui.setupUi(self)
        self.dashboard_dao = DashboardDao()
        self.refresh_insights()
        self.create_invoices_manager = InvoicesManager()
        self.connect_signals_slot()

    def connect_signals_slot(self):
        print('Connect signals slots in Dashboard')
        self.create_invoices_manager.reload_dashboard.connect(self.refresh_insights)

    def refresh_insights(self):
        print('Refresh insights')
        self.ui.invoices_this_month_label.setText(str(self.dashboard_dao.get_invoices_in_month(datetime.datetime.now().date().strftime('%m'))))