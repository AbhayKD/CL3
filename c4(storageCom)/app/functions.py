import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import gcs_client
from PyQt4 import QtGui

def listChange(cb,te,buckets):
    buckNo = cb.currentIndex()
    objects = buckets[buckNo].list()
    bucket = buckets[buckNo]

    text = 'Contents of bucket '+ str(bucket)
    if objects:
        text += '\t' + '\n\t'.join(map(lambda o: o.name + ' has '+o.size+ ' bytes'  ,objects))
        te.setText(text)
    else:
        text += '\tThere are no objects'
        te.setText(text)


def deleteButton(objects,objectNo):
    with objects[objectNo].open() as obj:
        fileName = obj.name
    if objects:
        obj = objects[objectNo]
        obj.delete()
    text = "Deleted successfully file: " + fileName
    dataDisplayDialog(text)

def readButton(objects,objectNo):
    if objects:
        with objects[objectNo].open() as obj:
            text = 'Contents of file: '+ obj.name +' are :'+ obj.read()
    dataDisplayDialog(str(text))

def InfoButton(buckets,buckNo):
    bucket = buckets[buckNo]
    text = 'Bucket %s is located in %s with storage class %s' % (bucket, bucket.location,bucket.storageClass)
    dataDisplayDialog(text)

def writeButton(buckets,buckNo,fileName,text):
    bucket = buckets[buckNo]
    with bucket.open(str(fileName), 'w') as obj:
        obj.write(str(text) + '\n')
    with bucket.open(str(fileName)) as obj:
        text = "Entered text in "+fileName+ " was "+ obj.read()
    dataDisplayDialog(text)

def dataDisplayDialog(text):
    d=QDialog()
    vbox = QVBoxLayout(d)
    te = QTextEdit(d)
    te.setText(text)
    te.setReadOnly(True)
    te.setAlignment(Qt.AlignCenter)
    vbox.addWidget(te)
    vbox.addStretch()
    d.setWindowTitle("Result")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()

def selectionchange(cb,cb2,buckets):
    cb2.clear()
    objects = buckets[cb.currentIndex()].list()
    for o in objects:
        cb2.addItem(o.name)
    return cb2.currentIndex()
    
