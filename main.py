import pygame
import time
from randomstockvaluegen import *
from gridsandlines import *
from menu import *

pygame.init()

screen_width = 1000
screen_height = 500

# Pygame Variables
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("StockSimulator")

# Variables
Money = 5000
selected_item = None
selected_operation = None

# Assets

# Colours
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Text
font = pygame.font.Font('freesansbold.ttf', 16)
MoneyNum = str(Money)

# Functions
def update_money_text(Money):
    return font.render('$' + str(Money), True, WHITE)

MoneyText = update_money_text(Money)
MoneyTextPos = (15, 10)

mytime = time.time()
frequency = 10

running = True
next_update = time.time()+frequency

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            # Check if a stock item is clicked
            if Gold_Rectangle.collidepoint(x, y):
                print("Gold Clicked")
                selected_item = "Gold"
                
            elif Oil_Rectangle.collidepoint(x, y):
                print("Oil Clicked")
                selected_item = "Oil"
                    
            elif Coal_Rectangle.collidepoint(x, y):
                print("Coal Clicked")
                selected_item = "Coal"
                
            # Check if the Buy or Sell button is clicked
            if selected_item and buy_button.collidepoint(x, y):
                selected_operation = "Buy"
                
            elif selected_item and sell_button.collidepoint(x, y):
                selected_operation = "Sell"

    screen.fill(BLACK)
     
    MoneyText = update_money_text(Money)
    draw_grid(screen, grid_size)
    draw_menu(screen)
    screen.blit(MoneyText, MoneyTextPos)

    # Draw the buy and sell buttons if an item is selected
    if selected_item is not None:
        buy_and_sell_button(screen)
    
    # Update stock lines
    draw_stock_line(coal_prices, screen, GREEN)
    draw_stock_line(oil_prices, screen, RED)
    draw_stock_line(gold_prices, screen, GOLD_YELLOW)

    # Update stock prices periodically
    if time.time() > next_update:
        print("Updating stock prices...")
        new_stock_prices()
        next_update = next_update + frequency

                # Trigger the buy and sell menu
    if selected_item and selected_operation:
            print(f"Triggered {selected_operation} menu for {selected_item}")
            buy_and_sell_menu(screen, selected_item)
            selected_operation = None  # Reset operation after triggering
    
    pygame.display.flip()
    time.sleep(1)

pygame.quit()

