import pygame

#Colours
GOLD_YELLOW = (255, 255, 51)
GRAY = (100, 100,  100)
BLACK  = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GUNMETAL_GRAY = (129, 133, 137)
WHITE = (255,  255, 255)

pygame.init()

# Rectangle Settings
Gold_Rectangle = pygame.Rect(0, 470, 60, 30)
Oil_Rectangle = pygame.Rect(60, 470, 60, 30)
Coal_Rectangle = pygame.Rect(120, 470, 60, 30)

# Text Settings
font = pygame.font.Font('freesansbold.ttf', 15)
font1 = pygame.font.Font('freesansbold.ttf', 32)

# Render Text
Gold_Surface =  font.render("Gold", True, BLACK)
Gold_Rect = Gold_Surface.get_rect(topleft=(Gold_Rectangle.left  +  10, Gold_Rectangle.top  + 10))

Oil_Surface =  font.render("Oil", True, BLACK)
Oil_Rect = Oil_Surface.get_rect(topleft=(Oil_Rectangle.left  +  10, Oil_Rectangle.top  + 10))

Coal_Surface =  font.render("Coal", True, BLACK)
Coal_Rect = Coal_Surface.get_rect(topleft=(Coal_Rectangle.left  +  10, Coal_Rectangle.top  + 10))

# Buy and Sell Button
buy_button = pygame.Rect(730, 10, 45, 20)
sell_button = pygame.Rect(770, 10, 45, 20)

Buy_Surface =  font.render("Buy", True, BLACK)
Buy_Rect = Buy_Surface.get_rect(topleft=(buy_button.left  +  5, buy_button.top  + 5))

Sell_Surface =  font.render("Sell", True, BLACK)
Sell_Rect = Sell_Surface.get_rect(topleft=(sell_button.left  +  5, sell_button.top  + 5))

Buy_Text_Pos = ((350,  485))

#Draw Menu Function
def draw_menu(screen):

    # Gold Menu Bar
    pygame.draw.rect(screen, GOLD_YELLOW, Gold_Rectangle)
    screen.blit(Gold_Surface, Gold_Rect)

    # Oil Menu Bar
    pygame.draw.rect(screen, GRAY, Oil_Rectangle)
    screen.blit(Oil_Surface, Oil_Rect)

    # Oil Menu Bar
    pygame.draw.rect(screen, GUNMETAL_GRAY, Coal_Rectangle)
    screen.blit(Coal_Surface, Coal_Rect)

def buy_and_sell_button(screen):

    pygame.draw.rect(screen, GREEN, buy_button)
    screen.blit(Buy_Surface, Buy_Rect)
    
    pygame.draw.rect(screen, RED, sell_button)
    screen.blit(Sell_Surface, Sell_Rect)

def buy_and_sell_menu(screen, stock):
    print(f"Displaying Buy/Sell Menu for {stock}")
    
    # Ensure contrast between text and background
    BuyText_Surface = font.render(f"Buy Order Placed For {stock}", True, WHITE)
    
    # Debugging: Check the text position
    print(f"Blitting text at position: {Buy_Text_Pos}")
    
    screen.blit(BuyText_Surface, Buy_Text_Pos)

