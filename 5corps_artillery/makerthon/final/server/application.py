from flask import Flask, render_template, request
import sqlite3 as sql
import datetime
import base64
import os
import pandas as pd
from pandas import value_counts

app = Flask(__name__)

@app.route("/")
def list():
     con = sql.connect("database.db")
     cur = con.cursor()
     cur.execute("SELECT rowid, * FROM mask")
     result = cur.fetchall()
     length = len(result)-1
     length1 = length -1
     length2 = length1 -1
     length3 = length2 -1
     length4 = length3 -1
     length5 = length4 -1
     length6 = length5 -1
     length7 = length6 -1
     result0 = result[length]
     result1 = result[length1]
     result2 = result[length2]
     result3 = result[length3]
     result4 = result[length4]
     result5 = result[length5]
     result6 = result[length6]
     result7 = result[length7]
     print(result0)
     con.close()
     return render_template("home.html", result11=result0[1],
result12=result0[2],
result13=result0[3],
result21=result1[1],
result22=result1[2],
result23=result1[3],
result31=result2[1],
result32=result2[2],
result33=result2[3],
result41=result3[1],
result42=result3[2],
result43=result3[3],
result51=result4[1],
result52=result4[2],
result53=result4[3],
result61=result5[1],
result62=result5[2],
result63=result5[3],
result71=result6[1],
result72=result6[2],
result73=result6[3],
result81=result7[1],
result82=result7[2],
result83=result7[3])

@app.route("/upload", methods = ["POST"])
def upload():
    maskfile = request.get_json()
    #for test
    '''if maskfile['name']=="\n":
        maskfile['name']="변우중"'''
    now = datetime.datetime.now()
    current = now + datetime.timedelta(hours=9)
    image = maskfile['image']
    image1 = image[0]
    path = 'static/img' 
    file_list = os.listdir(path) 
    bytes_base64 = image1["data"]
    data = base64.b64decode(bytes_base64)
    open("static/img/{}.jpg".format(len(file_list)),'wb').write(data)
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO mask(name, time, location) VALUES (?,?,?)", (maskfile['name'], current.strftime('%Y-%m-%d %H:%M:%S'), maskfile['location']))
    con.commit()
    con.close()
    return 'OK'


@app.route("/photo1")
def show1():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-1
    picturename = f'img/{length}.jpg'
    return render_template("showphoto.html", picturename = picturename)

@app.route("/photo2")
def show2():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-2
    picturename = f'img/{length}.jpg'
    return render_template("showphoto1.html", picturename = picturename)

@app.route("/photo3")
def show3():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-3
    picturename = f'img/{length}.jpg'
    return render_template("showphoto2.html", picturename = picturename)

@app.route("/photo4")
def show4():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-4
    picturename = f'img/{length}.jpg'
    return render_template("showphoto.html", picturename = picturename)

@app.route("/photo5")
def show5():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-5
    picturename = f'img/{length}.jpg'
    return render_template("showphoto1.html", picturename = picturename)

@app.route("/photo6")
def show6():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-6
    picturename = f'img/{length}.jpg'
    return render_template("showphoto2.html", picturename = picturename)

@app.route("/photo7")
def show7():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-7
    picturename = f'img/{length}.jpg'
    return render_template("showphoto.html", picturename = picturename)

@app.route("/photo8")
def show8():
    way = 'static/img' 
    way_list = os.listdir(way)
    length = len(way_list)-8
    picturename = f'img/{length}.jpg'
    return render_template("showphoto1.html", picturename = picturename)


@app.route("/statistics")
def analysis():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM mask")
    result = cur.fetchall()
    df = pd.DataFrame(result, columns=['number','name','time','location'])
    rank = df["name"].value_counts()
    rank01 = rank.index[0]
    rank11 = rank.index[1]
    rank21 = rank.index[2]
    rank31 = rank.index[3]
    rank41 = rank.index[4]
    rank51 = rank.index[5]
    rank61 = rank.index[6]
    rank71 = rank.index[7]
    rank02 = rank[0]
    rank12 = rank[1]
    rank22 = rank[2]
    rank32 = rank[3]
    rank42 = rank[4]
    rank52 = rank[5]
    rank62 = rank[6]
    rank72 = rank[7]
    return render_template("index.html", rank01 = rank01, rank11=rank11, rank21=rank21, rank31=rank31, rank41=rank41, rank51=rank51, rank61=rank61, rank71=rank71, rank02 = rank02, rank12=rank12, rank22=rank22, rank32=rank32, rank42=rank42, rank52=rank52, rank62=rank62, rank72=rank72)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)