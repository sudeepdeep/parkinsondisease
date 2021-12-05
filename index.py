from flask import Flask, render_template
from flask import *
import pickle as pkl
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    if(request.method == 'POST'):
        if(request.form['1'] != ""):
            val1 = float(request.form['1'])
            val2 = float(request.form['2'])
            val3 = float(request.form['3'])
            val4 = float(request.form['4'])
            val5 = float(request.form['5'])
            val6 = float(request.form['6'])
            val7 = float(request.form['7'])
            val8 = float(request.form['8'])
            val9 = float(request.form['9'])
            val10 =float(request.form['10'])
            val11 =float(request.form['11'])
            val12 = float(request.form['12'])
            val13 = float(request.form['13'])
            val14 = float(request.form['14'])
            val15 = float(request.form['15'])
            val16 = float(request.form['16'])
            val17 = float(request.form['17'])
            val18 = float(request.form['18'])
            val19 = float(request.form['19'])
            val20 = float(request.form['20'])
            val21 = float(request.form['21'])
            val22 = float(request.form['22'])


            model = pkl.load(open('parkinsonmodel.sav', 'rb'))

            res = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15, val16, val17, val18, val19, val20, val21, val22]])[0]
            print(type(res))
            if(res == '1'):  

                msg = "Parkinson Disease is Present"
            elif(res == '0'):  
                msg = "Hurray.. You're Not Infected With Parkinson"

            return render_template('home.html', message = msg)

        else:
            return render_template('home.html')

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)