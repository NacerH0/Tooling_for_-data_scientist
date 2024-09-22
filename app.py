import streamlit as st
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt


st.title('Graph maker ')



uploaded_file=st.file_uploader(label="upload your dataframe :" )    

if uploaded_file is not None:
    bytes_data =BytesIO( uploaded_file.getvalue() )
    df=pd.read_excel(bytes_data)

    st.title('Multiple Plots from DataFrame')

    # Loop through each column and create a plot
    for i, column_1 in enumerate(df.columns):
        for column_2 in df.columns[i+1:]:
            # Create a plot
            fig, ax = plt.subplots()
            ax.plot(df[column_1], df[column_2], marker='+', linestyle='')
            ax.set(xlabel=column_1, ylabel=column_2, title=f'{column_1} vs {column_2}')
            
            # Display the plot using Streamlit
            st.pyplot(fig)







