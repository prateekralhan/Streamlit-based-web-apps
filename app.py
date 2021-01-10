import yfinance as yf
import streamlit as st
import datetime
import time
import pandas as pd

begin_date = datetime.date(2010,1,1)
current_date = datetime.date.today()

st.set_page_config(page_title='Stock Price App', page_icon='🇮🇳', layout='wide', initial_sidebar_state='auto')
st.markdown('<style>body{background-color: #fffff;}</style>',unsafe_allow_html=True)

@st.cache(persist=True,show_spinner=True)
def load_data():
    df=pd.read_excel('tickers.xlsx',sheet_name='INDIA')
    df['Ticker']=df['Ticker'].astype('string')
    return df

@st.cache(persist=True,show_spinner=True)
def filter(dataset,company,exchange):
    result=dataset[(dataset['Name']==company) & (dataset['Exchange']==exchange)]['Ticker'].values[0]
    return result

st.markdown("<hr><h1 style='text-align: center; color: black;'>📈 🇮🇳 Stock Price App ₹</h1><hr>", unsafe_allow_html=True)

data_load_state = st.text('Loading data...')
dataset=load_data()
data_load_state.text('Done!! (using st.cache)')
data_load_state.empty()

col1, col2, col3, col4 = st.beta_columns(4)

with col1:
    company_name = st.selectbox("Choose the Company...", dataset.Name.unique())
with col2:
    exchange_name = st.selectbox("Choose the Exchange...", dataset.Exchange.unique())
with col3:
    start_date = st.date_input('Start date', begin_date)
with col4:
    end_date = st.date_input('End date', current_date)


if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')

try:
    tickerSymbol = filter(dataset,company_name,exchange_name)
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

    st.markdown('### Note: The dropdown gives suggestions of only top **1000** values! :smile:',unsafe_allow_html=True)
    st.write("""
    ## Closing Price
    """)
    st.area_chart(tickerDf.Close)
    st.write("""
    ## Volume Price
    """)
    st.area_chart(tickerDf.Volume)


except IndexError:
    st.warning("""
### Please select the other *Exchange* ! :smile:
""")

st.markdown("<br><br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Issue-Stock Price WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)




