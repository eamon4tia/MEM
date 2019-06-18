from enum import Enum

from PySide2.QtCore import QParallelAnimationGroup, QPropertyAnimation, QAbstractAnimation
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QWidget


class Spoiler(QWidget):

    class Orientation(Enum):
        HORIZONTAL = 1
        VERTICAL = 2

    def __init__(self, orientation=Orientation.HORIZONTAL, animationDuration = 250, parent=None):
        QWidget.__init__(self, parent)

        self.opened = False
        self.orientation = orientation
        self.animationDuration = animationDuration
        self.mainLayout = None
        self.animator = QParallelAnimationGroup()

        if orientation is self.Orientation.HORIZONTAL:
            self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

            self.setMaximumWidth(0)
            self.setMinimumWidth(0)
            # let the entire widget grow and shrink with its content
            self.animator.addAnimation(QPropertyAnimation(self))
            self.animator.addAnimation(QPropertyAnimation(self, b"minimumWidth"))
            self.animator.addAnimation(QPropertyAnimation(self, b"maximumWidth"))

        elif orientation is self.Orientation.VERTICAL:
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

            self.setMaximumHeight(0)
            self.setMinimumHeight(0)
            # let the entire widget grow and shrink with its content
            self.animator.addAnimation(QPropertyAnimation(self))
            self.animator.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
            self.animator.addAnimation(QPropertyAnimation(self, b"maximumHeight"))

    def open(self):
        self.animator.setDirection(QAbstractAnimation.Forward)
        self.animator.start()
        self.opened = True

    def close(self):
        self.animator.setDirection(QAbstractAnimation.Backward)
        self.animator.start()
        self.opened = False

    def isOpened(self):
        return self.opened

    def setContentLayout(self, contentLayout):
        self.setLayout(contentLayout)

        if self.orientation is self.Orientation.HORIZONTAL:
            collapsedSize = self.maximumWidth()
            contentSize = contentLayout.sizeHint().width()
        elif self.orientation is self.Orientation.VERTICAL:
            collapsedSize = self.maximumHeight()
            contentSize = contentLayout.sizeHint().height()

        i = 0
        while i < self.animator.animationCount():
            animation = self.animator.animationAt(i)
            animation.setDuration(self.animationDuration)
            animation.setStartValue(collapsedSize)
            animation.setEndValue(collapsedSize + contentSize)
            i += 1
