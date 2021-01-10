# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import seaborn as sns
import json
import time

st.set_page_config(page_title='Cryptocurrency Stats', page_icon=':dollar:', layout='wide', initial_sidebar_state='auto')

st.markdown("<hr><h1 style='text-align: center; color: black;'>₿ Crypto Price App 😵</h1><hr>", unsafe_allow_html=True)
st.markdown("""
This app retrieves cryptocurrency prices for the **top 10** cryptocurrencies .Use the filters on the **side-bar** to get the Price Data and other results :wink:
""")
st.markdown("""
* **Data source:** [CoinMarketCap](http://coinmarketcap.com).
""")

col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))


col1.header('Filter ✂️')

def highlighter(val):
    color='red' if val==0 else 'green'
    return 'background-color: %s' % color

# Web scraping of CoinMarketCap data
@st.cache()
def load_data():
    cmc = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(cmc.content, 'html.parser')
    data = soup.find('script', id='__NEXT_DATA__', type='application/json')
    coins = {}
    coin_data = json.loads(data.contents[0])
    listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    for i in listings:
      coins[str(i['id'])] = i['slug']

    coin_name = []
    coin_symbol = []
    market_cap = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []
    price = []
    volume_24h = []

    for i in listings:
      coin_name.append(i['slug'])
      coin_symbol.append(i['symbol'])
      price.append(i['quote']['USD']['price'])
      percent_change_1h.append(i['quote']['USD']['percent_change_1h'])
      percent_change_24h.append(i['quote']['USD']['percent_change_24h'])
      percent_change_7d.append(i['quote']['USD']['percent_change_7d'])
      market_cap.append(i['quote']['USD']['market_cap'])
      volume_24h.append(i['quote']['USD']['volume_24h'])

    df = pd.DataFrame(columns=['coin_name', 'coin_symbol', 'market_cap', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'price', 'volume_24h'])
    df['coin_name'] = coin_name
    df['coin_symbol'] = coin_symbol
    df['price'] = price
    df['percent_change_1h'] = percent_change_1h
    df['percent_change_24h'] = percent_change_24h
    df['percent_change_7d'] = percent_change_7d
    df['market_cap'] = market_cap
    df['volume_24h'] = volume_24h
    return df

df = load_data()
#print(df.dtypes)

sorted_coin = sorted( df['coin_name'].head(10) )

try:
    selected_coin = col1.multiselect('Cryptocurrency', sorted_coin, sorted_coin)

    df_selected_coin = df[ (df['coin_name'].isin(selected_coin)) ]
    df_coins = df_selected_coin[:10]

    percent_timeframe = col1.selectbox('Percent change time frame',
                                        ['7d','24h', '1h'])
    percent_dict = {"7d":'percent_change_7d',"24h":'percent_change_24h',"1h":'percent_change_1h'}
    selected_percent_timeframe = percent_dict[percent_timeframe]

    sort_values = col1.selectbox('Sort values?', ['Yes', 'No'])

    col2.subheader('Price Data of Selected Cryptocurrency')
    col2.write('Data Dimension: ' + str(df_selected_coin.shape[0]) + ' rows and ' + str(df_selected_coin.shape[1]) + ' columns.')

    cm = sns.light_palette("#2ecc71", as_cmap=True)
    col2.dataframe(df_coins.style.background_gradient(cmap=cm))


    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
        return href

    col2.markdown(filedownload(df_selected_coin), unsafe_allow_html=True)


    col2.subheader('Table of % Price Change')
    df_change = pd.concat([df_coins.coin_name, df_coins.percent_change_1h, df_coins.percent_change_24h, df_coins.percent_change_7d], axis=1)
    df_change = df_change.set_index('coin_name')
    df_change['positive_percent_change_1h'] = df_change['percent_change_1h'] > 0
    df_change['positive_percent_change_24h'] = df_change['percent_change_24h'] > 0
    df_change['positive_percent_change_7d'] = df_change['percent_change_7d'] > 0

    col2.dataframe(df_change.style.background_gradient(cmap=cm))
    col2.markdown(filedownload(df_change), unsafe_allow_html=True)

    col3.subheader('Bar plot of % Price Change')

    if percent_timeframe == '7d':
        if sort_values == 'Yes':
            df_change = df_change.sort_values(by=['percent_change_7d'])
        col3.write('*7 days period*')
        plt.figure(figsize=(4,5))
        plt.subplots_adjust(top = 1, bottom = 0)
        df_change['percent_change_7d'].plot(kind='barh', color=df_change.positive_percent_change_7d.map({True: 'g', False: 'r'}))
        col3.pyplot(plt)
    elif percent_timeframe == '24h':
        if sort_values == 'Yes':
            df_change = df_change.sort_values(by=['percent_change_24h'])
        col3.write('*24 hour period*')
        plt.figure(figsize=(4,5))
        plt.subplots_adjust(top = 1, bottom = 0)
        df_change['percent_change_24h'].plot(kind='barh', color=df_change.positive_percent_change_24h.map({True: 'g', False: 'r'}))
        col3.pyplot(plt)
    else:
        if sort_values == 'Yes':
            df_change = df_change.sort_values(by=['percent_change_1h'])
        col3.write('*1 hour period*')
        plt.figure(figsize=(4,5))
        plt.subplots_adjust(top = 1, bottom = 0)
        df_change['percent_change_1h'].plot(kind='barh', color=df_change.positive_percent_change_1h.map({True: 'g', False: 'r'}))
        col3.pyplot(plt)
except ValueError:
    st.warning('Please select any cryptocurrency/cryptocurrencies from the Sidebar')

st.markdown("<br><br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Issue-Crypto Price WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
