from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
model1=pickle.load(open('model1.pkl','rb'))
scaler1=pickle.load(open('scaler1.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')    
@app.route('/diabetes_prediction',methods=['GET','POST'])
def diabetes_prediction():
    features=[float(i) for i in request.form.values()]
    features_arr=[np.array(features)]
    predictt=model.predict(features_arr)
    final_predict=predictt[0]
    outputt=''
    if final_predict==0:
        outputt+='not have diabetes'
    else:
        outputt+='have diabetes.Please consult a doctor'    
    return render_template('diabetes.html',display_predicted=f'You may {outputt}')
@app.route('/cardio_disease')
def cardio_disease():
    return render_template('heartdisease.html')    
@app.route('/cardio_predict',methods=['GET','POST'])
def cardio_disease_prediction():
    features=[int(i) for i in request.form.values()]
    dataframe=pd.DataFrame([features])
    if features[1]==1:
        gender_dum=pd.DataFrame([[0]])
    else:
        gender_dum=pd.DataFrame([[1]])
    if features[6]==1:
        cholesterol_dum=pd.DataFrame([[0,0]])
    elif features[6]==2:
        cholesterol_dum=pd.DataFrame([[1,0]])
    else:
        cholesterol_dum=pd.DataFrame([[0,1]])
    if features[7]==1:
        gluc_dum=pd.DataFrame([[0,0]])
    elif features[7]==2:
        gluc_dum=pd.DataFrame([[1,0]])
    else:
        gluc_dum=pd.DataFrame([[0,1]])            
    #gender_dum = pd.get_dummies(dataframe[1],drop_first=True)
    #cholesterol_dum = pd.get_dummies(dataframe[6],drop_first=True)
    #gluc_dum = pd.get_dummies(dataframe[7],drop_first=True)
    dataframe.drop(columns=[1,6,7],axis=1,inplace=True)
    dataframe=pd.concat([dataframe,gender_dum,cholesterol_dum,gluc_dum],axis=1)
    features_arr1=dataframe.iloc[:,:].values
    features_arr1=scaler1.transform(features_arr1)
    predictt1=model1.predict(features_arr1)
    final_predict1=predictt1[0]
    outputt1=''
    if final_predict1==0:
        outputt1+='not have CardioVascular Disease'
    else:
        outputt1+='have CardioVascular Disease.Please consult a doctor'    
    return render_template('heartdisease.html',display_predicted=f'You may {outputt1}')    
        
if __name__ == "__main__":
    app.run(debug=True)    