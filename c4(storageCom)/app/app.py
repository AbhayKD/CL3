import sys, ui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import gcs_client

credentials_file = 'HelloWorld-5b5ab5e9eba6.json'
project_name = 'helloworld-163119'

credentials = gcs_client.Credentials(credentials_file)
project = gcs_client.Project(project_name, credentials)

buckets = project.list()

def window(project,buckets):
 app = QApplication(sys.argv)
 win = QWidget()
 win.setWindowTitle("Cloud App")
 b0=QPushButton("Buckets")
 b1=QPushButton("Bucket Info")
 hbox=QHBoxLayout() 
 vbox=QVBoxLayout()
 hbox.addWidget(b0)
 hbox.addStretch()
 hbox.addWidget(b1)
 vbox.addStretch()
 vbox.addLayout(hbox)
 b0.clicked.connect(lambda:ui.listBuckets(project))
 b1.clicked.connect(lambda:ui.bucketInfo(project))

 hbox2=QHBoxLayout()
 b2=QPushButton("Write Object")
 b3=QPushButton("Read Object")
 hbox2.addWidget(b2)
 hbox2.addStretch()
 hbox2.addWidget(b3)
 vbox.addStretch()
 vbox.addLayout(hbox2)
 b2.clicked.connect(lambda:ui.writeObject(project))
 b3.clicked.connect(lambda:ui.readObject(project))


 hbox3=QHBoxLayout()
 b4=QPushButton("Delete Object")
 b5=QPushButton("List Objects")
 hbox3.addWidget(b4)
 hbox3.addStretch()
 hbox3.addWidget(b5)
 vbox.addStretch()
 vbox.addLayout(hbox3)
 b4.clicked.connect(lambda:ui.deleteObject(project))
 b5.clicked.connect(lambda:ui.listObject(project))

 win.setLayout(vbox)

 win.show()
 sys.exit(app.exec_())


if __name__ == '__main__':
 window(project,buckets)
