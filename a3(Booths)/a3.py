#sudo apt-get -y install python-pip
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#python get-pip.py
#sudo pip install flask
#sudo pip install bitstring
#sudo pip install python-firebase
#python a3.py in the same folder of code

import time
from bitstring import BitArray
from flask import Flask
from flask import request
from flask import render_template
from firebase import firebase
from bitwise import *
app = Flask(__name__)

firebase=firebase.FirebaseApplication('https://helloworld-163119.firebaseio.com', None)

def booth(mint,rint):
    #fv = input("Input the number of first variable M: ")
    m = mint
    mbinary = "{0:b}".format(m)
    mlen = len("{0:b}".format(m))+1
    if m < 0:
        m = TwoComp( ("{0:0%db}" % mlen).format(m) )    #Calculate the$
    else:
        m = ("{0:0%db}" % mlen).format(m)   #Convert to bits and assig$

    #sv = input("Input the number of second variable R: ")
    r = rint
    rbinary = "{0:b}".format(r)
    rlen = len("{0:b}".format(r))+1

    if r < 0:
        r = TwoComp( ("{0:0%db}" % rlen).format(r) )
    else:
        r = ("{0:0%db}" % rlen).format(r)

    ilen = mlen + rlen + 1                  #The common length of inte$
    a = m + GenZeroStr(rlen + 1)            #A: place M in leftmost po$
    s = TwoComp(m) + GenZeroStr(rlen + 1)   #S: place negative M in le$
    p = GenZeroStr(mlen) + r + "0"          #P: place R by rightmost 0.

    print("Internal variables:")
    print("M = %s" % m)
    print("R = %s" % r)
    print("A = %s" % a)
    print("S = %s" % s)
    print("P = %s\n" % p)

    for i in range(rlen):   #Do operation rlen times
        print("Step %d:" % (i+1))

        op = p[-2:]
        print("    " + "The last 2 bits of p are: %s" % "".join(op))
        if   op == "10":
            print("    " + "P = (P+S) >> 1")
            p = BitAdd(p, s, len(p))
        elif op == "01":
            print("    " + "P = (P+A) >> 1")
            p = BitAdd(p, a, len(p))
        elif op == "00":
            print("    " + "P = P >> 1")
        elif op == "11":
            print("    " + "P = P >> 1")

        p = BitShift(p, 1)
        print("    " + "P = %s\n" % p)

    p = p[:-1]
    print("The answer is: %s" % p)
    d = int(p,2)
    print("The answer in decimal is %s" %d)
    return mbinary ,rbinary ,p ,d


@app.route('/')
def f():
    return render_template("h.html")

@app.route('/',methods=['POST'])
def g():
    if request.method == 'POST':
        if request.form['my-form'] == 'Send':
            text1 = int(request.form['text1'])
            text2 = int(request.form['text2'])
            m,r,p,d=booth(text1,text2)
            return "First no binary: "+str(m)+" "+"Second no binary: "+str(r)+"<br>Answer: "+str(d)+" "+"Answer in Binary: "+str(p) 
        elif request.form['my-form'] == 'Cloud':
            text1 = int(firebase.get('/booth', 'm'))
            text2 = int(firebase.get('/booth', 'r'))
            time.sleep(7)
            m,r,p,d=booth(text1,text2)
            return "First no binary: "+str(m)+" "+"Second no binary: "+str(r)+"<br>Answer: "+str(d)+" "+"Answer in Binary: "+str(p) 

if __name__ == '__main__':
    app.run('localhost',debug=True)

