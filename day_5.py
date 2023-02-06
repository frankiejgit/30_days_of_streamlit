import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# Set title at top of page
st.header('st.write')

# Write a string with an emoji (markdown format)
st.write('Hello, *World!* :sunglasses:')

# Write a number
st.write(1234)

# Write a pandas DataFrame
df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
})

st.write(df)

# Pass multiple arguments at once
st.write('Below is a dataframe', df, 'above is a dataframe')

# Display a visualization
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c']
)

st.write(c)