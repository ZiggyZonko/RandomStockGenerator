import random
import array as arr
import time
import pygame

x = 0

screen_width = 1000
screen_height = 500

stock_prices = ([0, 0, 0])
oil_prices = ([0])
gold_prices = ([0])
coal_prices = ([0])
#Order = Gold, Oil, Coal

#Colours
GREEN = (0, 255, 0)

def new_stock_prices():
    rangeforvalue = random.uniform(0, 5)
    below_or_above = random.randint(0, 1)

    # Gold Prices
    gold_prices[0] = random.uniform(100, 200)
    if below_or_above == 1:
        gold_prices.append(gold_prices[0] + rangeforvalue)
    else:
        gold_prices.append(gold_prices[0] - rangeforvalue)

    # Oil Prices
    oil_prices[0] = random.uniform(100, 200)
    if below_or_above == 1:
        oil_prices.append(oil_prices[0] + rangeforvalue)
    else:
        oil_prices.append(oil_prices[0] - rangeforvalue)

    # Coal Prices
    coal_prices[0] = random.uniform(100, 200)
    if below_or_above == 1:
        coal_prices.append(coal_prices[0] + rangeforvalue)
    else:
        coal_prices.append(coal_prices[0] - rangeforvalue)

    print(gold_prices, oil_prices, coal_prices)

def draw_stock_line(prices, screen, color):
    max_x = screen_width - 100
    max_y = screen_height - 100
    spacing_x = max_x / len(prices)
    
    max_price = max(prices)
    min_price = min(prices)
    price_range = max_price - min_price
    if price_range == 0:  
        price_range = 1
    
    scaled_prices = [(price - min_price) / price_range * max_y for price in prices]

    for i in range(len(prices) - 1):
        pygame.draw.line(
            screen,
            color,
            (i * spacing_x + 50, screen_height - 50 - scaled_prices[i]),
            ((i + 1) * spacing_x + 50, screen_height - 50 - scaled_prices[i + 1]),
            2
        )

