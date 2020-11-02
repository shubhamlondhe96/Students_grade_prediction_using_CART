import streamlit as st
import joblib
import os
os.getcwd()

model = joblib.load("Random_Forest_new.pkl")




st.markdown(f'''<center><h1 style="font-family:cursive;color:rgb(0,250,200);text-decoration-line:overline underline;text-decoration-style:double ;">AIS Solutions Pvt Ltd.</h1></center>''',unsafe_allow_html=True)
st.markdown(f'''<center><h1 style="background-color:DodgerBlue ;">Students Grade Prediction Using CART</h1><center>''',unsafe_allow_html=True)
# upload file where you have to test 


age = st.slider("Age", 0, 7,9)


Medu = st.slider("Medu", 1, 4,3)


Fedu = st.slider("Fedu", 1, 4,3)



traveltime = st.slider("traveltime", 0, 3,4)



studytime = st.slider("studytime", 0, 3,4)



failures = st.slider("failures", 0, 3,3)



famrel = st.slider("famrel", 0, 4,2)



freetime = st.slider("freetime", 0, 4,5)



goout = st.slider("goout", 0, 4, 5)



Dalc = st.slider("Dalc", 0, 4, 5)



Walc = st.slider("Walc", 0, 4, 5)


health	= st.slider("health	", 0, 4, 5)



absences= st.slider("absences	", 0, 20, 22)


st.write("Select below option if response is Yes (or 1) ")


a1 = st.checkbox("school_MS")

if a1:
	school_MS = 1
else:
	school_MS = 0




a3 = st.checkbox("address_U")

if a3:
	address_U = 1
else:
	address_U = 0









a5 = st.checkbox("Pstatus_T")

if a5:
	Pstatus_T = 1
else:
	Pstatus_T = 0









a18 = st.checkbox("guardian_other")

if a18:
	guardian_other = 1
else:
	guardian_other = 0

a19 = st.checkbox("schoolsup_yes")

if a19:
	schoolsup_yes = 1
else:
	schoolsup_yes = 0

a15 = st.checkbox("reason_other")

if a15:
	reason_other = 1
else:
	reason_other = 0



lst = [absences,
 failures,
 goout,
 freetime,
 Medu,
 age,
 Fedu,
 health,
 studytime,
 Walc,
 famrel,
 school_MS,
 guardian_other,
 traveltime,
 Dalc,
 reason_other,
 address_U,
 Pstatus_T,
 schoolsup_yes]


if st.button("Predict"):
	x = model.predict([lst])[0]
	if x==1:
		st.header('PASS')
	else:
		st.header('FAIL')
