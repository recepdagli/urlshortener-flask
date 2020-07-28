from flask import Flask, render_template, request, url_for, make_response, redirect
import sqlite3
import random
import string

link_host="localhost:5000/l/"

def get_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def getselectdata(link):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    data = cur.execute('SELECT * FROM links where redirect_url="'+str(link)+'"')

    return data

def insertdata(query):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        link = request.form['link']

        created_link = get_random_string(6)
        insertdata("INSERT INTO links VALUES ('"+link+"','"+link_host+created_link+"')")

        return redirect(url_for('done', link=created_link))
    if request.method == 'GET':
        return render_template("index.html")


@app.route('/done/<link>')
def done(link):
    data = getselectdata(link_host+link)
    
    return render_template("done.html",created_link=list(data)[0][1])

@app.route('/l/<link>')
def getlink(link):
    data = getselectdata(link_host+link)
    link=list(data)[0][0]
    
    if(link[0:4]=="http"):
        return redirect(link,code=302)
    else:
        return redirect("https://"+link,code=302)



app.run(host="0.0.0.0")