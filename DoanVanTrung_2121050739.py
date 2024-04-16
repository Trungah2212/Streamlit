import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Đoàn Văn Trung - 2121050739",layout = 'wide')
st.header("Interactive Dashboard")
st.subheader("Interact with this dashboard using the widgets on the sidebar")
data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/movies.csv")
data.info()
data.duplicated()
data.count()
data.dropna()

year_list = data['year'].unique().tolist()
score_rating = data['score'].unique().tolist()
genre_list = data['genre'].unique().tolist()

with st.sidebar:
    st.write("Select a range on the slider (it represents movie score) to view the total number of movies in a genre that falls within that range ")
    new_score_rating = st.sidebar.slider('Choose a value:', 1.00, 10.00, (3.00, 4.00))
    st.write("Select your preferred genre(s) and year to view the movies released that year and on that genre")
    new_genre_list = st.multiselect('Choose Genre:',genre_list, default = ['Animation', 'Horror', 'Fantasy', 'Romance'])
    year = st.selectbox('Choose a Year', year_list, 0)

score_info = (data['score'].between(*new_score_rating))
new_genre_year = (data['genre'].isin(new_genre_list)) & (data['year'] == year)

col1, col2 = st.columns([2,3])
with col1:
    st.write("""#### Lists of movies filtered by year and Genre """)
    dataframe_genre_year = data[new_genre_year].groupby(['name', 'genre'])['year'].sum()
    dataframe_genre_year = dataframe_genre_year.reset_index()
    st.dataframe(dataframe_genre_year, width = 400)

with col2:
    st.write("""#### User score of movies and their genre """)
    rating_count_year = data[score_info].groupby('genre')['score'].count()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x = 'genre', y = 'score')
    st.plotly_chart(figpx)


st.write("""Average Movie Budget, Grouped by Genre""")
avg_budget = data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig = plt.figure(figsize = (19, 10))

plt.bar(genre, avg_bud, color = 'maroon')
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing The Average Budget of Movies in Each Genre')
st.pyplot(fig)