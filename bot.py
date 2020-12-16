import telebot
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError , Timeout, TooManyRedirects
from telebot import util
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


@bot.message_handler(func = lambda msg: msg.text is not None and '!ticker=' in msg.text) 
def get_ticker_info(message):
    filtered_ticker = message.text.replace('!ticker=','')
    url = f'https://api.blockchain.com/v3/exchange/tickers/{filtered_ticker}'
    res = requests.get(url)
    ticker_res = json.loads(res.text)
    try:
        bot.reply_to(message,f"Symbol: {ticker_res['symbol']}\nPrice 24h: {ticker_res['price_24h']}\nVolume 24h: {ticker_res['volume_24h']}\nLast Trade Price: {ticker_res['last_trade_price']}")
    except:
        bot.reply_to(message,"Ticker not found")

    



@bot.message_handler(func = lambda msg: msg.text is not None and '!symbol=' in msg.text)
def get_symbol_info(message):
    filtered_symbol = message.text.replace('!symbol=','')
    url = f"https://api.blockchain.com/v3/exchange/symbols/{filtered_symbol}"
    res = requests.get(url)
    symbol_res = json.loads(res.text)
    try:
        bot.reply_to(message,f"base currency: {symbol_res['base_currency']}\nbase currency scale: {symbol_res['base_currency_scale']}\ncounter currency: {symbol_res['counter_currency']}\ncounter currency scale: {symbol_res['counter_currency_scale']}\nmin price increment: {symbol_res['min_price_increment']}\nmin order size: {symbol_res['min_order_size']}\nmin order size scale: {symbol_res['min_order_size_scale']}\nlot size: {symbol_res['lot_size']}\nlot size scale: {symbol_res['lot_size_scale']}\nstatus: {symbol_res['status']}\nid: {symbol_res['id']}\nauction price: {symbol_res['auction_price']}\nauction size: {symbol_res['auction_size']}\nauction time: {symbol_res['auction_time']}\nimbalance: {symbol_res['imbalance']}")

    except:
        bot.reply_to(message,"Symbol not found")



@bot.message_handler(func = lambda msg: msg.text is not None and '!pair=' in msg.text)
def get_pair_info(message):
    filtered_pair = message.text.replace('!pair=','')
    url = f"https://api.twelvedata.com/time_series?symbol={filtered_pair}&interval=1min&apikey=52fa79d6593844eb8a0f210fa1e02784"
    res = requests.get(url)
    pair_res = json.loads(res.text)
    
    try:
        bot.reply_to(message,f"Symbol: {pair_res['meta']['symbol']}\nInterval: {pair_res['meta']['interval']}\ncurrency base: {pair_res['meta']['currency_base']}\ncurrency quote: {pair_res['meta']['currency_quote']}\ntype: {pair_res['meta']['type']}\n\nValues: {pair_res['values'][0]}\n\nValues: {pair_res['values'][1]}\n\nValues: {pair_res['values'][2]}\n\nValues: {pair_res['values'][3]}\n\nValues: {pair_res['values'][4]}")
    except:
        bot.reply_to(message,"Symbol is invalid")


bot.polling()



