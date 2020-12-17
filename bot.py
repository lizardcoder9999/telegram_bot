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


@bot.message_handler(func=lambda msg: msg.text is not None and '!stock=' in msg.text)
def get_stock_info(message):
    filtered_stock = message.text.replace('!stock=','')
    url = f"https://api.twelvedata.com/time_series?symbol={filtered_stock}&interval=1min&apikey=52fa79d6593844eb8a0f210fa1e02784"
    res = requests.get(url)
    stock_res = json.loads(res.text)

    try: 
        bot.reply_to(message,f"Stock: {stock_res['meta']['symbol']}\nInterval: {stock_res['meta']['interval']}\nCurrency: {stock_res['meta']['currency']}\nExchange timezone: {stock_res['meta']['exchange_timezone']}\nExchange: {stock_res['meta']['exchange']}\nType: {stock_res['meta']['type']}\n\nValues: {stock_res['values'][0]}\n\nValues: {stock_res['values'][1]}\n\nValues: {stock_res['values'][2]}\n\nValues: {stock_res['values'][3]}\n\nValues: {stock_res['values'][4]}")

    except:
        bot.reply_to(message,"Stock not found")


@bot.message_handler(func = lambda msg: msg.text is not None and '!exchange_rate=' in msg.text)
def get_exchange_rate(message):
    filtered_exchange = message.text.replace('!exchange_rate=','')
    url = f"https://api.twelvedata.com/exchange_rate?symbol={filtered_exchange}&apikey=52fa79d6593844eb8a0f210fa1e02784"
    res = requests.get(url)
    exchange_res = json.loads(res.text)

    try:
        bot.reply_to(message,f"Symbol: {exchange_res['symbol']}\nRate: {exchange_res['rate']}\nTimestamp: {exchange_res['timestamp']}")

    except:
        bot.reply_to(message,'Symbol not found')


@bot.message_handler(func=lambda msg: msg.text is not None and '!convert_currency=' in msg.text)
def get_conversion_data(message):
    filtered_conversion = message.text.replace('!convert_currency=','')
    symbol,amount = filtered_conversion.split(':')
    url = f"https://api.twelvedata.com/currency_conversion?symbol={symbol}&amount={amount}&apikey=52fa79d6593844eb8a0f210fa1e02784"
    res = requests.get(url)
    conversion_res = json.loads(res.text)

    try:
        bot.reply_to(message,f"Symbol: {conversion_res['symbol']}\nRate: {conversion_res['rate']}\nAmount: {conversion_res['amount']}\ntimestamp: {conversion_res['timestamp']}")
        
    except:
        bot.reply_to(message,"Symbol not found")

@bot.message_handler(func=lambda msg: msg.text is not None and '!realtime_price=' in msg.text)
def get_real_time_price(message):
    filtered_realtime = message.text.replace('realtime_price=','')
    url = f"https://api.twelvedata.com/price?symbol={filtered_realtime}&apikey=52fa79d6593844eb8a0f210fa1e02784"
    res = requests.get(url)
    realtime_res = json.loads(res.text)

    try:
        bot.reply_to(message,f"Price: {realtime_res['price']}") #FIX KEY ERROR BUG

    except:
        bot.reply_to(message,"Symbol not found")


@bot.message_handler(func=lambda msg: msg.text is not None and '!quote=' in msg.text)
def get_quote_data(message):
    filtered_quote = message.text.replace('!quote=','')
    url = f"https://api.twelvedata.com/quote?symbol={filtered_quote}&apikey=52fa79d6593844eb8a0f210fa1e02784"
    res = requests.get(url)
    quote_res = json.loads(res.text)

    try:
        bot.reply_to(message,f"Symbol: {quote_res['symbol']}\nName: {quote_res['name']}\nExchange: {quote_res['exchange']}\nCurrency:{quote_res['currency']}\nDate: {quote_res['datetime']}\nOpen: {quote_res['open']}\nHigh: {quote_res['high']}\nLow: {quote_res['low']}\nClose: {quote_res['close']}\nvolume: {quote_res['volume']}\nPrevious Close: {quote_res['previous_close']}\nChange: {quote_res['change']}\nPercent Change: {quote_res['percent_change']}\nAverage volume: {quote_res['average_volume']}\n\n52 Week\nlow: {quote_res['fifty_two_week']['low']}\nhigh: {quote_res['fifty_two_week']['high']}\nlow change: {quote_res['fifty_two_week']['low_change']}\nhigh change: {quote_res['fifty_two_week']['high_change']}\nlow change percent: {quote_res['fifty_two_week']['low_change_percent']}\nhigh change percent: {quote_res['fifty_two_week']['high_change_percent']}\nrange: {quote_res['fifty_two_week']['range']}\n")

    except:
        bot.reply_to(message,"Symbol not found")



bot.polling()



