import pickle
from PIL import Image
import streamlit as st
 
# loading the trained model
model = pickle.load(open('model.pkl','rb'))
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(age,sex,chest_pain,bp,cholesterol,fbs,rest_ecg,heart_rate,exang,oldpeak,slope,ca,thal):   
 
    # Pre-processing user input    
    if sex == "Female":
        sex = 0
    else:
        sex = 1

    if chest_pain == "typical angina":
        chest_pain = 0
    elif chest_pain == "atypical angina":
        chest_pain = 1 
    elif chest_pain == "non-anginal pain":
        chest_pain = 2 
    else :
        chest_pain = 3
 
    if fbs == "No":
        fbs = 0
    else:
        fbs = 1    
 
    if rest_ecg == "normal":
        rest_ecg = 0
    elif rest_ecg == "ST-T wave abnormality":
        rest_ecg = 1  
    else :
        rest_ecg = 2        
    
    if exang == "No":
        exang = 0
    else :
        exang = 1

    if slope == "upsloping":
        slope = 0
    elif slope == "flat":
        slope = 1  
    else :
        slope = 2    

    if thal == "Null":
        thal = 0
    elif thal == "normal":
        thal = 1  
    elif thal == "fixed defect" :
        thal = 2  
    else :
        thal =3

 
    # Making predictions 
    prediction = model.predict( 
        [[age,sex,chest_pain,bp,cholesterol,fbs,rest_ecg,heart_rate,exang,oldpeak,slope,ca,thal]])
     
    if prediction == 0:
        pred = 'Congratulations !!! No heart disease detected'
    else:
        pred = 'Heart disease detected.Please seek doctor's advice'
    return pred
       
# this is the main function in which we define our webpage  
def main():       

    img1 = Image.open('heart.jpg')
    img1 = img1.resize((700,250))
    st.image(img1,use_column_width=False)

    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Heart Disease Prediction</h1> 
    </div> 
    """ 
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    age = st.number_input("Age",value=0) 
    sex = st.selectbox("Sex",('Female','Male')) 
    chest_pain = st.selectbox('Chest Pain',("typical angina","atypical angina","non-anginal pain","asymptomatic"))
    bp = st.number_input('Resting Blood Pressure',max_value=200,value=0)
    cholesterol = st.number_input('Cholestrol level',value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",("No","Yes")) 
    rest_ecg = st.selectbox('Resting ECG',('normal','ST-T wave abnormality','left ventricular hypertrophy by Estes'))
    heart_rate = st.number_input("Maximum Heart Rate",value=0)
    exang = st.selectbox("Exercise induced angina",("No","Yes")) 
    oldpeak = st.number_input("ST depression induced by exercise",value=0.0)
    slope = st.selectbox('Slope of the peak exercise',("upsloping","flat","downsloping"))
    ca = st.number_input("Major Vessels",min_value=0,max_value=3,value=0)
    thal = st.selectbox('Thalassemia',('Null','normal','fixed defect','reversable effect'))

    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(age,sex,chest_pain,bp,cholesterol,fbs,rest_ecg,heart_rate,exang,oldpeak,slope,ca,thal) 
        st.header(result)
if __name__=='__main__': 
    main()
