import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x_values = np.arange(-29, 31, 3)
y_values = np.sin(x_values)


plt.plot(x_values, y_values, label='선 그래프')





a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
s1 = st.sidebar.radio('선의 형태를 선택하시오', ['-', ':', '-', '--'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['o', '^', 'p', 's'])
x = []
y = []

for i in range(-20, 21, 3):
    x.append(i)
    y.append(-2*i*i + 3*i + 5)
   


plt.plot(x, y, color = c1, linestyle = s1, marker= 'h')
st.pyplot(fig)
import sys
sys.exit()





                                                                                  