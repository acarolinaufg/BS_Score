from flask import Flask, render_template,request,redirect,url_for,flash,abort,session,jsonify
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'asdfghjk'

@app.route('/')
def inicio():
    return render_template('inicio1.html', codes = session.keys())
    #return redirect(url_for('comentario'))


@app.route('/adicionar', methods =['GET','POST'])
def adicionar():
    
    if request.method == 'POST':
        coment = {'Nome':'','Lote':'','banana':0, 'maca':0, 'abacaxi':0, 'morango':0, 'uva':0}
        coment['Nome'] = request.form['nome']
        coment['Lote'] = request.form['lote']
        

        if request.form.get('comentario1') in coment.keys():
            coment[request.form.get('comentario1')]= int(request.form.get('intensidade1'))
            
           
        if request.form.get('comentario2') in coment.keys():
            coment[request.form.get('comentario2')]= 1
            return coment
 
        
        


    