from flask import Flask,render_template,url_for,request
import requests as req
from bs4 import BeautifulSoup
import time
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/",methods=["GET", "POST"]) #index (Thai)
def index():
    ###############################################################
    try:
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/D17'
        raw_page = req.get(url)
        soup = BeautifulSoup(raw_page.text, 'html.parser')
        soup = str(soup)
        soup = soup.replace('[\"','')
        soup = soup.replace('\"]','')
        soup = int(soup)
        soup = soup*100
        soup = soup/800
        soup = int(100-soup)
        soup = str(soup)
        percent = "%"
        moisture = soup + percent

        
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/V1'
        raw_page = req.get(url)
        soup1 = BeautifulSoup(raw_page.text, 'html.parser')
        soup1 = str(soup1)
        if soup1 == "[\"1\"]":
            light = "ON"
        elif soup1 == "[\"0\"]":
            light = "OFF"
        else:
            light = "UNKNOW"
    except:
        moisture = "UNKNOWN(ลองใหม่อีกครั้ง)"
        light = "UNKNOWN(ลองใหม่อีกครั้ง)"
    ################################################################
    return render_template("index.html",moisture = moisture,light = light)

@app.route("/openlight",methods=["GET", "POST"]) #index (Thai)
def openlight():
    try:
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/update/V1?value=1'
        req.get(url)
    except:
        openlight()
    ###############################################################
    try:
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/D17'
        raw_page = req.get(url)
        soup = BeautifulSoup(raw_page.text, 'html.parser')
        soup = str(soup)
        soup = soup.replace('[\"','')
        soup = soup.replace('\"]','')
        soup = int(soup)
        soup = soup*100
        soup = soup/800
        soup = int(100-soup)
        soup = str(soup)
        percent = "%"
        moisture = soup + percent

        
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/V1'
        raw_page = req.get(url)
        soup1 = BeautifulSoup(raw_page.text, 'html.parser')
        soup1 = str(soup1)
        if soup1 == "[\"1\"]":
            light = "ON"
        elif soup1 == "[\"0\"]":
            light = "OFF"
        else:
            light = "UNKNOW"
    except:
        moisture = "UNKNOWN(ลองใหม่อีกครั้ง)"
        light = "UNKNOWN(ลองใหม่อีกครั้ง)"
    ################################################################
    return render_template("index.html",moisture = moisture,light = light)

@app.route("/turnofflight",methods=["GET", "POST"]) #index (Thai)
def turnofflight():
    try:
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/update/V1?value=0'
        raw_page = req.get(url)
    except:
        turnofflight()
    ###############################################################
    try:
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/D17'
        raw_page = req.get(url)
        soup = BeautifulSoup(raw_page.text, 'html.parser')
        soup = str(soup)
        soup = soup.replace('[\"','')
        soup = soup.replace('\"]','')
        soup = int(soup)
        soup = soup*100
        soup = soup/800
        soup = int(100-soup)
        soup = str(soup)
        percent = "%"
        moisture = soup + percent

        
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/V1'
        raw_page = req.get(url)
        soup1 = BeautifulSoup(raw_page.text, 'html.parser')
        soup1 = str(soup1)
        if soup1 == "[\"1\"]":
            light = "ON"
        elif soup1 == "[\"0\"]":
            light = "OFF"
        else:
            light = "UNKNOW"
    except:
        moisture = "UNKNOWN(ลองใหม่อีกครั้ง)"
        light = "UNKNOWN(ลองใหม่อีกครั้ง)"
    ################################################################
    return render_template("index.html",moisture = moisture,light = light)


def wateringtheplants():
    url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/update/D0?value=1'
    raw_page = req.get(url)
    url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/update/D0?value=0'
    raw_page = req.get(url)
    time.sleep(7)
    url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/update/D0?value=1'
    raw_page = req.get(url)

@app.route("/watertheplants",methods=["GET", "POST"]) #index (Thai)
def watertheplants():
    try:
        wateringtheplants()
    except:
        watertheplants()
    
    ###############################################################
    try:
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/D17'
        raw_page = req.get(url)
        soup = BeautifulSoup(raw_page.text, 'html.parser')
        soup = str(soup)
        soup = soup.replace('[\"','')
        soup = soup.replace('\"]','')
        soup = int(soup)
        soup = soup*100
        soup = soup/800
        soup = int(100-soup)
        soup = str(soup)
        percent = "%"
        moisture = soup + percent

            
        url = 'http://blynk-cloud.com/cPs4vXujt7N9kL2SKXFJLiwCdf07oOuH/get/V1'
        raw_page = req.get(url)
        soup1 = BeautifulSoup(raw_page.text, 'html.parser')
        soup1 = str(soup1)

        if soup1 == "[\"1\"]":
            light = "ON"
        elif soup1 == "[\"0\"]":
            light = "OFF"
        else:
            light = "UNKNOW"
    except:
        moisture = "UNKNOWN(ลองใหม่อีกครั้ง)"
        light = "UNKNOWN(ลองใหม่อีกครั้ง)"
    ################################################################
    return render_template("index.html",moisture = moisture,light = light)

if __name__ == '__main__':
    app.run()