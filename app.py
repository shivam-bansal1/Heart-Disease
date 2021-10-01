import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open('model.pkl','rb'))

img1 = Image.open('heart.jpg')
img1 = img1.resize((700,250))
st.image(img1,use_column_width=False)

st.title("Heart Disease Prediction")

age = st.number_input("Age",value=0)

sex_display = ('Female','Male')
sex_options = list(range(len(sex_display)))
sex = st.selectbox("Sex",sex_options,format_func=lambda x: sex_display[x])

    # Chest Pain
chest_pain_display = ("typical angina","atypical angina","non-anginal pain","asymptomatic")
chest_pain_options = list(range(len(chest_pain_display)))
chest_pain = st.selectbox("Chest Pain",chest_pain_options,format_func=lambda x: chest_pain_display[x])

    # Resting blood pressure
bp = st.number_input('Resting Blood Pressure',max_value=200,value=0)

    #Cholesterol
cholesterol = st.number_input('Cholestrol level',value=0)

    #Fasting blood sugar
fbs_display = ("No","Yes")
fbs_options = list(range(len(fbs_display)))
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",fbs_options,format_func=lambda x: fbs_display[x])

    #Resting ECG
rest_ecg_display = ('normal','ST-T wave abnormality','left ventricular hypertrophy by Estes')
rest_ecg_options = list(range(len(rest_ecg_display)))
rest_ecg = st.selectbox("Resting ECG",rest_ecg_options,format_func=lambda x: rest_ecg_display[x])

    #maximum heart rate
heart_rate = st.number_input("Maximum Heart Rate",value=0)

    #Exercise induced angina
exang_display = ("No","Yes")
exang_options =list(range(len(exang_display)))
exang = st.selectbox("Exercise induced angina",exang_options,format_func=lambda x: exang_display[x])

    # ST depression induced by exercise
oldpeak = st.number_input("ST depression induced by exercise",value=0.0)

    #slope of the peak exercise
slope_display = ("upsloping","flat","downsloping")
slope_options =list(range(len(exang_display)))
slope = st.selectbox("Slope of the peak exercise",slope_options,format_func=lambda x: slope_display[x])

    #major vessels
ca = st.number_input("Major Vessels",min_value=0,max_value=3,value=0)

    # Thalassemia
thal_display = ('Null','normal','fixed defect','reversable effect')
thal_options = list(range(len(thal_display)))
thal = st.selectbox("Thalassemia",thal_options,format_func=lambda x: thal_display[x])

if st.button("Predict") :
    features= [[age,sex,chest_pain,bp,cholesterol,fbs,rest_ecg,heart_rate,exang,oldpeak,slope,ca,thal]]
    print(features)

    prediction = model.predict(features)
    #lc = [str(i) for i in prediction]
    #ans = int("".join(lc))
        
    if prediction == 0 :
            st.success("Congratulations!! No heart disease detected")
    else :
            st.warning("Please seek doctor's advice")
