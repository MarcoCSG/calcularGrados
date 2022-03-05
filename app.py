
from flask import Flask, jsonify, request

app = Flask(__name__)
#from conversiones import conversiones

@app.route('/temperatura', methods=['GET'])    
def getTempertura():
    umedida = request.args.get('umedida')
    grados = float(request.args.get('grados'))
    if(umedida=="celcius"):
        t1 = (grados*1.8)+32
        t2 = (grados + 273.15)
        t3 = ((grados * 9/5) + 491.67) 
        t4 = (grados * (4/5))
    elif(umedida=="fahrenheit"):
        t1 = (grados - 32)/(1.8)
        t2 = (grados + 459.67)/(1.8)
        t3 = (grados + 459.67)
        t4 = 4*(grados - 32) / 9
    elif(umedida=="kelvin"):
        t1 = (grados - 273.15)
        t2 = 1.8 *(grados - 273.15) + 32
        t3 = (grados - 273.15)* 1.8 + 491.67
        t4 = (grados -273.15)*1.8
    elif(umedida=="rankine"):
        t1 = (grados - 491.67) * (5/9)
        t2 = (grados-459.67)
        t3 = (grados*(5/9))
        t4 = 4*(grados - 491.67)/9
    elif(umedida=="reaumur"):
        t1 = (5*grados)/4
        t2 = (grados+ 2.25) + 32
        t3 = ((5 * grados) /4) + 273.15
        t4 = (grados *2.25) + 491.67

    return jsonify({"t1":t1, "t2":t2, "t3":t3, "t4":t4})

if __name__== '__main__':
    app.run(debug=True, port=4000)