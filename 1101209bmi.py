
w = st.number_input(input('請輸入體重(KG)？'))
h = st.number_input(input('請輸入身高(M)？'))
bmi = BMI(w, h)
st.('BMI為', bmi)
if (bmi < 18):
    print('體重過輕')
elif (bmi < 24):
    print('體重正常')
elif (bmi < 27):
    print('體重過重')
else:
    print('體重肥胖')
