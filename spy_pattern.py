import csv

def is_bullish_candlestick(candle):
    return float(candle['Close']) > float(candle['Open'])

def is_bearish_candlestick(candle):
    return float(candle['Close']) < float(candle['Open'])

def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and float(current_day['Close']) > float(previous_day['Open']) \
        and float(current_day['Open']) < float(previous_day['Close']):
        return True

    return False

def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bullish_candlestick(previous_day) \
        and float(current_day['Open']) > float(previous_day['Close']) \
        and float(current_day['Close']) < float(previous_day['Open']):
        return True

    return False

sp500_file = open('sp500_companies.csv')
sp500_companies = csv.reader(sp500_file)

for company in sp500_companies:
    ticker, company_name = company
    history_file = open('history/{}.csv'.format(ticker))
    reader = csv.DictReader(history_file)
    candles = list(reader)
    candles = candles[-2:]

    if len(candles) > 1:
        if is_bullish_engulfing(candles, 1):
            print('{} - {} is bullish engulfing'.format(ticker, candles[1]['Date']))
        if is_bearish_engulfing(candles, 1):
            print('{} - {} is bearish engulfing'.format(ticker, candles[1]['Date']))    