import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Startup Analysis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor, na=False)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1,col2 = st.columns(2)
    with col1:
        # biggest investments top 5 
        big_series = df[df['investors'].str.contains(investor, na=False)].groupby('startup')['amount'].sum().sort_values(ascending = False).head()
        st.subheader('Biggest Investments')
        
        # display as series
        # st.dataframe(big_series)
        
        # display in graph
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor, na=False)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested in ')
        # display in graph
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    col1,col2 = st.columns(2)
    with col1:
        round_series = (df[df['investors'].str.contains(investor, na=False)]['round'].value_counts())
        st.subheader('Round of Investment')
        # display in graph
        fig2, ax2 = plt.subplots()
        ax2.pie(round_series,labels=round_series.index,autopct="%0.01f%%")
        st.pyplot(fig2)
    with col2:
        city_series = (df[df['investors'].str.contains(investor, na=False)]['city'].value_counts())
        st.subheader('City of Investment')
        # display in graph
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series,labels=city_series.index,autopct="%0.01f%%")
        st.pyplot(fig3)

    df['year'] = df['date'].dt.year
    
    year_series = df[df['investors'].str.contains(investor,na = False)].groupby('year')['amount'].sum()

    st.subheader('Year on Year Investment')
    # display in graph
    fig3, ax3 = plt.subplots()
    ax3.plot(year_series.index,year_series.values)
    st.pyplot(fig3)



st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    selected_investor = st.sidebar.selectbox(
    'Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')

    if btn2 :
        load_investor_details(selected_investor)
        