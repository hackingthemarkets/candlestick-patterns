import csv


def is_bearish_candlestick(candle):
    return candle['Close'] < candle['Open']


def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and current_day['Close'] > previous_day['Open'] \
        and current_day['Open'] < previous_day['Close']:
        return True

    return False


with open('pizza.csv') as f:
    reader = csv.DictReader(f)
    candles = list(reader)

for i in range(1, len(candles)):
    print(candles[i])

    if is_bullish_engulfing(candles, i):
        print("{} is a bullish engulfing".format(candles[i]['Date']))