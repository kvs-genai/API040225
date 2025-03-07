import streamlit as st
import pandas as pd
import numpy as np

st.header("My First Streamlit app")
df = pd.DataFrame(
    {
    "First Column" : [1,2,3,4],
    "Second Column": [11,12,13,14]
    }
)
st.write(df)
st.table(df)

# dataframe = np.random.randn(10,20)
# st.dataframe(dataframe)

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# #st.dataframe(dataframe.style.highlight_max(axis=0))    ## interactive table
# st.table(dataframe) ## static table

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.dataframe(chart_data)
# st.line_chart(chart_data)
# st.bar_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.dataframe(map_data)
# st.map(map_data)

x = st.slider('x',1,20)
st.write(x, 'squared is', x * x)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data