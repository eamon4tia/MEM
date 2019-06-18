
#!/usr/bin/env python3.5
import sys
from PySide2.QtWidgets import QApplication
from insert_Patients_servers import MainWindow

app = QApplication(sys.argv)

# window= LoginWindow();
OneForeAll = MainWindow()

OneForeAll.show()

sys.exit(app.exec_())

