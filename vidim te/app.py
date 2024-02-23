import pygame
import sys

def draw_eyes(screen, eye_color, pupil_color, eye_radius, pupil_radius, eye_centers, cursor_pos):
    for center in eye_centers:
        pygame.draw.circle(screen, eye_color, center, eye_radius)
        
        # counting poistion of the cursor
        dx = cursor_pos[0] - center[0]
        dy = cursor_pos[1] - center[1]
        length = (dx**2 + dy**2)**0.5
        if length > 0:
            scale = min(pupil_radius / length, 1)
            pupil_pos = (center[0] + dx * scale, center[1] + dy * scale)
        else:
            pupil_pos = center
        
        #drawing eyes
        pygame.draw.circle(screen, pupil_color, pupil_pos, pupil_radius)

def main():
    #setting of the position  and sizeof he window and eyes
    window_size = (800, 600)
    eye_radius = 50
    pupil_radius = 10
    eye_centers = [(200, 200), (600, 200)]  # Pozice očí
    eye_color = (255, 255, 255)  # Barva očí (bílá)
    pupil_color = (0, 0, 0)  # Barva žáků (černá)
    
    pygame.init()
    
    #creating window
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Oči sledující kurzor')
    
    #main cycle of the program
    running = True
    while running:
        #working with event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #getting cursor poistion
        cursor_pos = pygame.mouse.get_pos()
        
        #render of scree 
        screen.fill((0, 0, 0))  #black bg
        draw_eyes(screen, eye_color, pupil_color, eye_radius, pupil_radius, eye_centers, cursor_pos)
        
        # refresh of display
        pygame.display.flip()
    
    #program end
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
