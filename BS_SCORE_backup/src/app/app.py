from flask import Flask, render_template,request,redirect,url_for,flash,abort,session,jsonify
import json
import os.path
from werkzeug.utils import secure_filename
import numpy as np
import pickle
import MySQLdb
#carregando o modelo
model = pickle.load(open('models\Modelo_treinado_BS.pkl', 'rb'))


#Fazer a conecxão com o banco de dados do MySQL
con = MySQLdb.connect(
    host = '127.0.0.1:3306',
    user = "root",
    passwd="Ambev@2015",
    db = "BS_Score"
)




app = Flask(__name__)
app.secret_key = 'asdfghjk'

bom_3 = ['Escolha Intensidade','Fair','Fast','Good','Clear','(blank)']


médio_2 = ['Higher','Slight','Very Slight','Hint','Strong']


ruim_1 = ['Extreme','Moderate','Not detectable','Lower','Trace']


comenta = {'Escolha comentario':0,'Estery':0,'Body':0,'Fresh':0,'Tart':0,
        'Sweet':0,'Finish':0,'Bitter':0,'Sulfitic':0,'Astringent':0,'Foam':0,'Afterbitterness':0,
        'Hoppy':0,'Balanced':0,'HarshBitterness':0,'Malty':0,'Cooked':0,'GreenApple':0,
        'Herbal':0,'Drinkability':0,'Toasted':0,'Burnt':0,'Dry':0,'Warming':0,'Acetic':0,'Fruity':0,
        'Sulfury':0,'Caramel':0,'Citrus':0,'Flat':0,'RipeFruit':0,'Oxidation':0,'Floral':0,'Solventy':0,
        'Buttery':0,'Yeasty':0,'Grainy':0,'Thin':0,'FreshlyCutGrass':0,'Honey':0,
        'FruityBanana':0,'SweetCorn':0,'Sour':0,'RottenEggs':0,'SulfuryOnion':0,'Almond':0,
        'Winey':0,'Light_struck_skunky':0}




@app.route('/')
def inicio():
    return render_template('iniciotg1.3.html', codes = session.keys(),lt = comenta,
    ruim1=ruim_1, medio2= médio_2,bom3=bom_3)
    #return redirect(url_for('comentario'))


@app.route('/adicionar', methods =['GET','POST'])
def adc():
    if request.method == 'POST':
        coment = {'Nome':'','Lote':'','nota_dada':'','Score_predito':0,'Score':0,'Estery':0,'Body':0,'Fresh':0,'Tart':0,
        'Sweet':0,'Finish':0,'Bitter':0,'Sulfitic':0,'Astringent':0,'Foam':0,'Afterbitterness':0,
        'Hoppy':0,'Balanced':0,'HarshBitterness':0,'Malty':0,'Cooked':0,'GreenApple':0,
        'Herbal':0,'Drinkability':0,'Toasted':0,'Burnt':0,'Dry':0,'Warming':0,'Acetic':0,'Fruity':0,
        'Sulfury':0,'Caramel':0,'Citrus':0,'Flat':0,'RipeFruit':0,'Oxidation':0,'Floral':0,'Solventy':0,
        'Buttery':0,'Yeasty':0,'Grainy':0,'Thin':0,'FreshlyCutGrass':0,'Honey':0,
        'FruityBanana':0,'SweetCorn':0,'Sour':0,'RottenEggs':0,'SulfuryOnion':0,'Almond':0,
        'Winey':0,'Light_struck_skunky':0}
        
        coment['Nome'] = request.form['nome']
        coment['Lote'] = request.form['lote']
        coment['nota_dada'] = request.form['nota']
       

        if request.form.get('comentario1') in coment.keys():
            coment[request.form.get('comentario1')]= int(request.form.get('intensidade1'))
            
           
        if request.form.get('comentario2') in coment.keys():
            coment[request.form.get('comentario2')]= int(request.form.get('intensidade2'))
        
        if request.form.get('comentario3') in coment.keys():
            coment[request.form.get('comentario3')]= int(request.form.get('intensidade3'))

        if request.form.get('comentario4') in coment.keys():
            coment[request.form.get('comentario4')]= int(request.form.get('intensidade4'))

        if request.form.get('comentario5') in coment.keys():
            coment[request.form.get('comentario5')]= int(request.form.get('intensidade5'))

        if request.form.get('comentario6') in coment.keys():
            coment[request.form.get('comentario6')]= int(request.form.get('intensidade6'))

        #==================================================================================
      
        teste = np.array([[coment['Estery'],coment['Body'],coment['Fresh'],
        coment['Tart'],coment['Sweet'],coment['Finish'],coment['Bitter'],coment['Sulfitic'],
        coment['Astringent'],coment['Foam'],coment['Afterbitterness'],coment['Hoppy'],
        coment['Balanced'],coment['HarshBitterness'],coment['Malty'],coment['Cooked'],coment['GreenApple'],
        coment['Herbal'],coment['Drinkability'],coment['Toasted'],coment['Burnt'],coment['Dry'],
        coment['Warming'],coment['Acetic'],coment['Fruity'],coment['Sulfury'],coment['Caramel'],
        coment['Citrus'],coment['Flat'],coment['RipeFruit'],coment['Oxidation'],coment['Floral'],
        coment['Solventy'],coment['Buttery'],coment['Yeasty'],coment['Grainy'],
        coment['Thin'],coment['FreshlyCutGrass'],coment['Honey'],coment['FruityBanana'],
        coment['SweetCorn'],coment['Sour'],coment['RottenEggs'],coment['SulfuryOnion'],
        coment['Almond'],coment['Winey'],coment['Light_struck_skunky']]]) 

        #Predizendo o valor do BS 
        classe = model.predict(teste)[0]
        print("O valor predito da nota do BS é: {}" .format(str(classe)))
        coment['Score_predito'] = classe
        print(coment)
        
        
        return render_template("pg_inicial.html",teste=f'O valor predito do BS é {classe:.2f}')

@app.route('/pg_inicial')
def index():
    return redirect(url_for('inicio'))       
 
    

app.run(debug=True, host='0.0.0.0')