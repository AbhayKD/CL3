#sudo apt-get -y install python-pip
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#python get-pip.py
#sudo pip install flask
#sudo pip install bitstring
#sudo pip install queuelib
#python a3.py in the same folder of code

import threading,queue
from bitstring import BitArray
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

def inner_sort(array, start_i, compare,queue):
  sorted = True
  for i in range(start_i, len(array) - 1, 2):
    if compare(array[i], array[i + 1]) > 0:
      array[i], array[i + 1] = array[i + 1], array[i]
      sorted = False
  queue.put(sorted)
  

def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0


def oddEven(array, compare=default_compare):
  sorted = False
  queued_req = queue.Queue()
  while not sorted:
    sorted1 = threading.Thread(target=inner_sort,args=(array,1,compare,queued_req))
    sorted2 = threading.Thread(target=inner_sort,args=(array,0,compare,queued_req))
    sorted2.start()
    sorted1.start()
    sorted2.join()
    print sorted2.getName(),"Doing Even Part"
    sorted1.join()
    print sorted1.getName(),"Doing Odd Part"
    sorted = queued_req.get()
  return array

def inputHtml(size):
  html = " "
  for i in range(0,size):
    html += "Enter " + str(i+1) + " number: " + "<input id=\"" +str(i)+ '\" type="text" style="margin:15px 10px;" name="number.' +str(i) +'\"><br>'
  return html


# Routing

@app.route('/')
def f():
    return render_template("h.html")

@app.route('/',methods=['POST'])
def g():
    size = 0
    if request.method == 'POST':
        if request.form['my-form'] == 'Send':
            text1 = int(request.form['text1'])
            size = text1
            return '<!DOCTYPE html><html lang="en"><body><h1>Enter the data</h1><form action="." method="POST">'\
                 + inputHtml(text1) + \
                 '<input type="submit" name="my-form" value="Send Values"></form></body></html>'   

        elif request.form['my-form'] == 'Send Values':
            ary = []
            for key in request.form:
                if key.startswith('number.'):
                    id = key.partition('.')[-1]
                    value = int(request.form[key])
                    ary.insert(int(id),value)
            inString = ', '.join(map(str,ary))
            result = oddEven(ary)
            for i in range(len(result)):
                print result[i]
            outString = ', '.join(map(str,result))
            return "Input sequence: "+ inString + '<br style="margin: 10px;">' + "Output Sequence: "+ outString 

if __name__ == '__main__':
    app.run('localhost',debug=True)

