from PySide2.QtGui import QIcon
from PySide2.QtCore import \
    Qt,\
    Slot,\
    SLOT,\
    QSize,\
    QPoint,\
    Signal
from PySide2.QtWidgets import \
    QWidget,\
    QDialog,\
    QPushButton,\
    QHBoxLayout,\
    QCalendarWidget

class DatePicker(QWidget):

    selectionChanged = Signal()

    def __init__(self, parent=None):
        super(DatePicker, self).__init__(parent)
        self.button = QPushButton(self)
        icon = QIcon("logo.svg")
        self.button.setIcon(icon)
        self.setFixedSize(32, 32)
        self.button.setFixedSize(32, 32)
        self.button.setIconSize(QSize(22, 22))

        self.__margin__ = 5

        self.dialog = QDialog()
        self.dialog.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.Popup)
        self.dialog.setFixedSize(480, 240)
        self.dialog.setLayout(QHBoxLayout())
        self.calender = QCalendarWidget(self)
        self.dialog.layout().addWidget(self.calender)
        self.dialog.layout().setContentsMargins(0, 0, 0, 0)
        self.dialog.layout().setSpacing(0)

        self.button.clicked.connect(self, SLOT("showCalender()"))

        self.calender.selectionChanged.connect(self.__emitSelectionChanged__)

    @Slot()
    def showCalender(self):
        print('in show')

        p = self.mapToGlobal(QPoint(0, self.height() + self.__margin__))

        self.dialog.setGeometry(p.x(), p.y(), 0, 0)
        self.dialog.show()

    def setIcon(self, icon):
        if type(icon) is QIcon:
            self.button.setIcon(icon)
        elif type(icon) is str:
            self.button.setIcon(QIcon(icon))
        else:
            raise Exception('Wrong argument type, icon should be either PySide2.QtGui.QIcon or str "string"')

    def icon(self):
        return self.button.icon()


    def setIconSize(self, iconsize):
        if type(iconsize) is QSize:
            self.button.setIconSize(iconsize)
        elif type(iconsize) is int:
            self.button.setIcon(QSize(iconsize, iconsize))
        elif type(type) is iter:
            import collections
            if isinstance(iconsize, collections.Iterable):
                if len(iconsize) == 1:
                    self.setIconSize(iconsize[0])
                elif len(iconsize) == 2:
                    self.setIconSize(QSize(iconsize[0], iconsize[1]))
                else:
                    raise Exception()
        else:
            raise Exception("Wrong argument type, iconSize should be either PySide2.QtCore.QSize or int value or width and height "
                            "or iterable contains one QSize, one int or two int values for width and height respectively")

    def iconSize(self):
        return self.button.iconSize()



    def setFirstDayOfWeek(self, dayOfWeek):
        if type(dayOfWeek) is Qt.DayOfWeek:
            self.calender.setFirstDayOfWeek(dayOfWeek)
        elif type(dayOfWeek) is int:
            if dayOfWeek < 1 or dayOfWeek > 7:
                raise Exception("Wrong argument, dayOfWeek should be from 1 to 7 (Monday --> Sunday)")
            self.calender.setFirstDayOfWeek(Qt.DayOfWeek(dayOfWeek))
        else:
            raise Exception("Wrong type, dayOfWeek should be either PySide2.QtCore.Qt.DayOf or int (1 --> 7) (Monday --> Sunday)")

    def firstDayOfWeek(self):
        self.calender.firstDayOfWeek()


    def selectedDate(self):

        self.calender.selectedDate()



    def setSelectedDate(self, args, kwargs):
        self.calender.setSelectedDate(args, kwargs)


    def minimumDate(self):
        self.calender.minimumDate()

    def setMinimumDate(self):
        self.calender.setMinimumDate()

    def selectedDate(self):

        return self.calender.selectedDate()


    def __emitSelectionChanged__(self):
        self.selectionChanged.emit();

