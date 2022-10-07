from flask import Flask,request,jsonify
import pandas as pd
import joblib
import json
import m2cgen as m2c 
import warnings                        # To ignore any warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)



cropModel1 = joblib.load('crop-predictions-98accuracy.joblib')
cropModel2 = joblib.load('crop-predictions-99RF.joblib')
cropModel3 = joblib.load('crop-predictions-99Naive.joblib')
@app.route("/predict",methods=['GET','POST'])
def predict():
  if request.method == 'POST':
    data = request.get_json( )
    passdata = list()
    for i in data:
      passdata.append(data[i])
    predicted = list()
    predicted.append(cropModel1.predict([passdata]))       
    predicted.append(cropModel2.predict([passdata]))       
    predicted.append(cropModel3.predict([passdata]))
    #print(predicted[0][1])
    sendData = {
      "data1" : predicted[0][0],
      "data2" : predicted[1][0],
      "data3" : predicted[2][0]
    }
    print(sendData)     
    return sendData, 201
    

abc = [90,50,20,21,60,6,90]
# N	P	K	temperature	humidity	ph	rainfall	label
# 79	51	16	25.33797709	68.49835977	6.586244581	96.46380213 maize
# 25	78	76	17.48042641	15.7559405	7.228963452	66.96980581	chickpea
# 37	70	25	19.73136909	24.89487354	5.819403771	84.06354115	kidneybeans
# 24	37	21	30.573999	58.22686794	5.818219385	62.74803826	mothbeans

# print('predicted value od model1 : ' , cropModel1.predict([abc]))
# print('predicted value of model2 : ' , cropModel2.predict([abc]))
# print('predicted value of model3 : ' , cropModel3.predict([abc]))

if __name__ == "__main__":
  app.run(port=8000)
