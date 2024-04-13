import streamlit as st
st.write("Hello World!")
st.write("Hello Streamlit!")


st.write("_____________________________________________________________________")
st.title ("this is the app title")#Hàmnàychophépbạnthêmtiêuđềcủaứngdụng.
st.header("this is the markdown")#Hàmnàyđượcsửdụngđểthiếtlậpmarkdown.
st.markdown("this is the header")#Hàmnàyđượcsửdụngđểđặttiêuđềcủamộtphần
st.subheader("this is the subheader")#Hàmnàyđượcsửdụngđểđặttiêuđềphụcủamộtphần.
st.caption("this is the caption")#Hàmnàyđượcsửdụngđểviếtchúthích.
st.code("x=2021")#Hàmnàyđượcsửdụngđểđặtcode.
st.latex(r''' a+a r^1+a r^2+a r^3 ''')#HàmnàydùngđểhiểnthịcácbiểuthứctoánhọcđượcđịnhdạnglàLaTeX.


st.write("_____________________________________________________________________")
st.subheader("Image : ")
st.image("E:/Background/My Picture/1.jpg")

st.subheader("Audio : ")
st.audio("D:/Toeic/Day5/5.5.mp3")

st.subheader("Video : ")
st.video("E:/Background/My Picture/5341017828778.mp4")


st.write("_____________________________________________________________________")
st.write("Widgets")
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
st.write("______________________________________")
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')


st.write("_____________________________________________________________________")
st.sidebar.write("Thanh bên(sidebar)")
st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("click")
st.sidebar.radio("Giới Tính",["Nam","Nữ"])


st.write("_____________________________________________________________________")
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)