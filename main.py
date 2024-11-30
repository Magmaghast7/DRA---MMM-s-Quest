import pygame

pygame.init
running = True

screen = pygame.display.set_mode((700, 600), pygame.RESIZABLE)

grid = pygame.image.load("Assets/PNGs/grid.png")
mmm = pygame.image.load("Assets/PNGs/MMM.png")
mmm_rect = mmm.get_rect()
grid_rect = grid.get_rect()

mmm = pygame.transform.scale(mmm, (mmm_rect.width / 2, mmm_rect.height / 2))
mmm_rect = mmm.get_rect()

grid = pygame.transform.scale(grid, (grid_rect.width * 2, grid_rect.height * 2))
grid_rect = grid.get_rect()
grid_rect.center = (screen.get_width() * 2, screen.get_height() * 2)
grid_rect.topleft = (0, 0)

while running:
    
    mmm_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    screen.blit(grid, (grid_rect.x, grid_rect.y))
    screen.blit(mmm, (mmm_rect.x, mmm_rect.y))
    pygame.display.update()