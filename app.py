import streamlit as st
import yfinance as yf
from PIL import Image



image = Image.open("stocks.jpg")

st.image(image, use_column_width = True)
st.write(""""
# Simple Stock Price App  
  
   
""")
tickerSymbol = 'GOOGL'

st.subheader(f"Shown are the stock of closing price and volume of {tickerSymbol}")

print(yf)



tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2020-05-31')

st.write(""" 
## Closing Stocks
""")
st.line_chart(tickerDf.Close)

st.write(""" 
## Stocks by Volume
""")
st.line_chart(tickerDf.Volume)