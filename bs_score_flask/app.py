from flask import Flask, render_template,request,redirect,url_for,flash,abort,session,jsonify
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'asdfghjk'

bom_3 = ['Escolha Intensidade','Fair','Fast','Good','Clear','(blank)']


médio_2 = ['Escolha Intensidade','Higher','Slight','Very Slight','Hint','Strong']


ruin_1 = ['Escolha Intensidade','Extreme','Moderate','Not detectable','Lower','Trace']


comenta = {'Escolha comentario':0,'Score':0,'Estery':0,'Body':0,'Fresh':0,'Tart':0,
        'Sweet':0,'Finish':0,'Bitter':0,'Sulfitic':0,'Astringent':0,'Foam':0,'Afterbitterness':0,
        'Hoppy':0,'Balanced':0,'HarshBitterness':0,'Malty':0,'Cooked':0,'GreenApple(acetaldehyde)':0,
        'Herbal':0,'Drinkability':0,'Toasted':0,'Burnt':0,'Dry':0,'Warming':0,'Acetic':0,'Fruity':0,
        'Sulfury':0,'Caramel':0,'Citrus':0,'Flat':0,'RipeFruit':0,'Oxidation':0,'Floral':0,'Solventy':0,
        'Buttery(diacetyl)':0,'Yeasty':0,'Grainy':0,'Thin':0,'FreshlyCutGrass':0,'Honey':0,
        'Fruity:Banana(Isoamyl acetate)':0,'SweetCorn(DMS)':0,'Sour':0,'RottenEggs(H2S)':0,'Sulfury:Onion':0,'Almond':0,
        'Winey':0,'Light-struck':0,'skunky':0}




@app.route('/')
def inicio():
    return render_template('iniciotg1.html', codes = session.keys(),lt = comenta,
    ruin1=ruin_1, medio2= médio_2,bom3=bom_3)
    #return redirect(url_for('comentario'))


@app.route('/adicionar', methods =['GET','POST'])
def adc():
    if request.method == 'POST':
        coment = {'Nome':'','Lote':'','Score':0,'Estery':0,'Body':0,'Fresh':0,'Tart':0,
        'Sweet':0,'Finish':0,'Bitter':0,'Sulfitic':0,'Astringent':0,'Foam':0,'Afterbitterness':0,
        'Hoppy':0,'Balanced':0,'HarshBitterness':0,'Malty':0,'Cooked':0,'GreenApple(acetaldehyde)':0,
        'Herbal':0,'Drinkability':0,'Toasted':0,'Burnt':0,'Dry':0,'Warming':0,'Acetic':0,'Fruity':0,
        'Sulfury':0,'Caramel':0,'Citrus':0,'Flat':0,'RipeFruit':0,'Oxidation':0,'Floral':0,'Solventy':0,
        'Buttery(diacetyl)':0,'Yeasty':0,'Grainy':0,'Thin':0,'FreshlyCutGrass':0,'Honey':0,
        'Fruity:Banana(Isoamyl acetate)':0,'SweetCorn(DMS)':0,'Sour':0,'RottenEggs(H2S)':0,'Sulfury:Onion':0,'Almond':0,
        'Winey':0,'Light-struck':0,'skunky':0}

        coment['Nome'] = request.form['nome']
        coment['Lote'] = request.form['lote']
        

        if request.form.get('comentario1') in coment.keys():
            coment[request.form.get('comentario1')]= int(request.form.get('intensidade1'))
            
           
        if request.form.get('comentario2') in coment.keys():
            coment[request.form.get('comentario2')]= 1
    return jsonify(coment) 
 
    

app.run(debug=True)