from PySide import QtGui, QtCore
from view import menuw

import supervisor
import defaults

if __name__ == '__main__':
    import sys

    # Instantiate the supervisor
    supervisor.Supervisor()


    app = QtGui.QApplication(sys.argv)
    window = menuw.MainW()
    window.main()

    defaults.setupTestDefaults()

    sys.exit(app.exec_())
