import telebot
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError , Timeout, TooManyRedirects
import json

bot = telebot.TeleBot("1429907822:AAEr4wvDXqPRqhoG3I7JPsGA_TI305_bDsE")
coinmarket_api_key = "0a066999-5d88-4ddc-8379-0a33d7ddba81"

api_headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': str(coinmarket_api_key)
}

coinmarket_crypto_endpoint_url = " https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"


@bot.message_handler(commands=['start','help'])
def welcome(message):
    bot.reply_to(message,"Hello")


# @bot.message_hander(func= lamda msg: msg.text is not None and '!btcinfo' in msg.txt)
# def get_crypto_price(message):
#     parameters = {
#         "symbol":'BTC'
#     }
#     session = Session()
#     session.headers.update(api_headers)
#     try:
#         response = session.get(url,params=parameters)
#         btc_info_data = json.loads(response.text)
#         bot.reply_to
    
#     except (ConnectionError,Timeout,TooManyRedirects) as e:
#         print(e)


@bot.message_handler(func = lambda msg: msg.text is not None and '!ticker=' in msg.text) 
def get_ticker_info(message):
    filtered_symbol = message.text.replace('!ticker=','')
    url = f'https://api.blockchain.com/v3/exchange/tickers/{filtered_symbol}'
    res = requests.get(url)
    ticker_res = json.loads(res.text)
    bot.reply_to(message,f"Symbol: {ticker_res['symbol']}\nPrice 24h: {ticker_res['price_24h']}\nVolume 24h: {ticker_res['volume_24h']}\nLast Trade Price: {ticker_res['last_trade_price']}")



#sample response
# {
#     "symbol": "BTC-USD",
#     "price_24h": 19284.2,
#     "volume_24h": 392.43106795,
#     "last_trade_price": 19461.5
# }



bot.polling()

