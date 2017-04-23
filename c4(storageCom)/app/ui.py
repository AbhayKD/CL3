import sys,functions
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import gcs_client
from PyQt4 import QtGui

def listBuckets(project):
    buckets = project.list()
    msg=QMessageBox()
    msg.setText("List of Buckets")
    #msg.setInformativeText("This is additional information")
    msg.setWindowTitle("Buckets")
    msg.setDetailedText('\n'.join(map(str, buckets)))
    msg.setStandardButtons(QMessageBox.Ok)
    #msg.buttonClicked.connect(msgbtn)
    retval=msg.exec_()
    print "value of pressed message box button:", retval


def bucketInfo(project):
    buckets = project.list()
    text = list(map(str, buckets))
    d=QDialog()
    layout = QVBoxLayout(d)
    buttons = []
    for key in text:
        buttons.append(QPushButton(key,d))
        layout.addWidget(buttons[-1]) 
    buttons[0].clicked.connect(lambda:functions.InfoButton(buckets,0))
    buttons[1].clicked.connect(lambda:functions.InfoButton(buckets,1))
    d.setWindowTitle("Dialog")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()


def writeObject(project):
    buckets = project.list()
    text = list(map(str, buckets))
    d=QDialog()
    layout = QFormLayout(d)
    cb = QComboBox()
    for i in text:
        cb.addItem(i)
    l = QLabel("Choose Bucket from list")
    buckNo = cb.currentIndex()

    layout.addRow(l,cb)
    l1 = QLabel("Enter File Name")
    le1 = QLineEdit(d)

    layout.addRow(l1,le1)
    l2 = QLabel("Enter Text")
    le2 = QLineEdit(d)

    layout.addRow(l2,le2)
    b = QPushButton("OK")
    b.clicked.connect(lambda:functions.writeButton(buckets,buckNo,le1.text(),le2.text()))
    layout.addRow(b)
    d.setWindowTitle("Write Object")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()

def readObject(project):
    buckets = project.list()
    text = list(map(str, buckets))
    d=QDialog()
    layout = QFormLayout(d)
    cb = QComboBox()
    for i in text:
        cb.addItem(i)
    l = QLabel("Choose Bucket from list")
    layout.addRow(l,cb)
    cb2 = QComboBox()
    cb.activated.connect(lambda:functions.selectionchange(cb,cb2,buckets))
    l1 = QLabel("Choose file from list")
    objects = buckets[cb.currentIndex()].list()

    layout.addRow(l1,cb2)
    b = QPushButton("OK")
    b.clicked.connect(lambda:functions.readButton(objects,cb2.currentIndex()))
    layout.addRow(b)
    d.setWindowTitle("Read Object")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()

def deleteObject(project):
    buckets = project.list()
    text = list(map(str, buckets))
    d=QDialog()
    layout = QFormLayout(d)
    cb = QComboBox()
    for i in text:
        cb.addItem(i)
    l = QLabel("Choose Bucket from list")
    layout.addRow(l,cb)
    cb2 = QComboBox()
    cb.activated.connect(lambda:functions.selectionchange(cb,cb2,buckets))
    l1 = QLabel("Choose file from list")
    objects = buckets[cb.currentIndex()].list()

    layout.addRow(l1,cb2)
    b = QPushButton("OK")
    b.clicked.connect(lambda:functions.deleteButton(objects,cb2.currentIndex()))
    layout.addRow(b)
    d.setWindowTitle("Delete Object")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()


def listObject(project):
    buckets = project.list()
    text = list(map(str, buckets))
    d=QDialog()
    layout = QFormLayout(d)
    cb = QComboBox()
    for i in text:
        cb.addItem(i)
    l = QLabel("Choose Bucket from list")
    layout.addRow(l,cb)
    te = QTextEdit(d)
    cb.activated.connect(lambda:functions.listChange(cb,te,buckets))
    te.setReadOnly(True)
    te.setAlignment(Qt.AlignCenter)
    layout.addRow(te)
    d.setWindowTitle("List Objects")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()

