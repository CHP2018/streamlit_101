import streamlit as st
import pandas as pd
menu = ['Home','Readme','Program']
choice=st.sidebar.selectbox('Menu',menu)

if choice == 'Home':
    st.write("Hello world")
    st.header("My project")
    st.image('media\dog-beach-lifesaver.png')  
    st.audio('media\Loi_nho.mp3')
    st.video('media\dogs.mp4')
    st.checkbox("It's OK?")
    
   
    col1,col2=st.columns(2)
    with col1:
        dog_name=st.text_input('What is your dog name?')
        st.write('Your dog name:',dog_name)
    with col2:
        age=st.slider('Dog age:',min_value=0,max_value=100)
        st.write('Your dog age:',age)
elif choice == 'Readme':
    df=pd.read_csv('media\AB_NYC_2019.csv')
    st.dataframe(df)
elif choice =='Program':
    st.audio('media\Impact_Moderato.mp3')
    fileupload =st.file_uploader('Upload file:',type=['jpg','png','jpeg'])
    st.image(fileupload)