import pygame, sys  
from pygame.locals import *  
import cv2  
import numpy as np  
from keras.models import load_model  
  
# Window and color settings  
WINDOWSIZEX = 640  
WINDOWSIZEY = 480  
BOUNDRYINC = 5  
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
RED = (255, 0, 0)  
  
# Load model  
MODEL = load_model("bestmodel.h5")  
  
# Labels  
LABELS = {  
    0: "Zero", 1: "One",  
    2: "Two", 3: "Three",  
    4: "Four", 5: "Five",  
    6: "Six", 7: "Seven",  
    8: "Eight", 9: "Nine"  
}  
  
# Pygame initialization  
pygame.init()  
DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))  
pygame.display.set_caption("Digit Recogniser")  
  
iswriting = False  
number_xcord = []  
number_ycord = []  
  
# Font for displaying predictions  
font = pygame.font.Font(None, 48)
predicted_label = ""  

# Restart button setup
button_font = pygame.font.Font(None, 36)
restart_rect = pygame.Rect(WINDOWSIZEX - 120, 10, 100, 40)  # Position & size
  
# Main loop  
while True:  
    for event in pygame.event.get():  
        if event.type == QUIT:  
            pygame.quit()  
            sys.exit()  
  
        if event.type == MOUSEMOTION and iswriting:  
            xcord, ycord = event.pos  
            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord), 4, 0)  
            number_xcord.append(xcord)  
            number_ycord.append(ycord)  
  
        if event.type == MOUSEBUTTONDOWN:  
            if restart_rect.collidepoint(event.pos):  
                DISPLAYSURF.fill(BLACK)  # Clear screen  
                predicted_label = ""  
                continue  
            iswriting = True  
            predicted_label = ""  # Clear previous prediction when starting new digit  
  
        if event.type == MOUSEBUTTONUP:  
            iswriting = False  
            if number_xcord and number_ycord:  
                number_xcord = sorted(number_xcord)  
                number_ycord = sorted(number_ycord)  
  
                rect_min_x, rect_max_x = max(number_xcord[0] - BOUNDRYINC, 0), min(WINDOWSIZEX, number_xcord[-1] + BOUNDRYINC)  
                rect_min_y, rect_max_y = max(number_ycord[0] - BOUNDRYINC, 0), min(WINDOWSIZEY, number_ycord[-1] + BOUNDRYINC)  
  
                number_xcord = []  
                number_ycord = []  
  
                img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x:rect_max_x, rect_min_y:rect_max_y].T.astype(np.float32)  
  
                # Preprocess for model  
                image = cv2.resize(img_arr, (28, 28))  
                image = np.pad(image, (10, 10), constant_values=0)  
                image = cv2.resize(image, (28, 28))/255  
  
                prediction = MODEL.predict(image.reshape(1, 28, 28, 1))  
                predicted_label = LABELS[int(np.argmax(prediction))]  
                print("Predicted Digit:", predicted_label)  
  
    # Clear the top area for displaying text  
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, WINDOWSIZEX, 60))  
    
    # Render prediction text  
    if predicted_label:  
        text_surface = font.render(f"Prediction: {predicted_label}", True, RED)  
        DISPLAYSURF.blit(text_surface, (10, 10))  
    
    # Draw Restart button  
    pygame.draw.rect(DISPLAYSURF, (200, 200, 200), restart_rect)  
    DISPLAYSURF.blit(button_font.render("Restart", True, BLACK), (WINDOWSIZEX - 115, 15))  
  
    pygame.display.update()