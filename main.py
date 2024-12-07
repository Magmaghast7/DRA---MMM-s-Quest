import pygame
pygame.init

running = True

speed = 10
drag = 5
world_pos_x = 0
world_pos_y = 0
player_camera_pos_x = 0
player_camera_pos_y = 0

#floats

#screen
screen = pygame.display.set_mode((700, 600), pygame.RESIZABLE)
clock = pygame.Clock()

#rects
grid = pygame.image.load("Assets/PNGs/grid.png")
mmm = pygame.image.load("Assets/PNGs/MMM.png")
mmm_rect = mmm.get_frect()
grid_rect = grid.get_frect()
mmm = pygame.transform.scale(mmm, (mmm_rect.width / 2, mmm_rect.height / 2))
mmm_rect = mmm.get_frect()
grid = pygame.transform.scale(grid, (grid_rect.width * 5, grid_rect.height * 5))
grid_rect = grid.get_frect()
grid_rect.center = (screen.get_width() * 5, screen.get_height() * 5)
grid_rect.topleft = (0, 0)

while running:
    
    clock.tick(60)
    center = (screen.get_width() / 2, screen.get_height() / 2)
    
    mmm_rect.center = center
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #keys
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w]):
        world_pos_y += speed
        player_camera_pos_y = center[1] + speed * 6

    if (keys[pygame.K_s]):
        world_pos_y -= speed
        player_camera_pos_y = center[1] - speed * 6
        
    if (keys[pygame.K_a]):
        world_pos_x += speed
        player_camera_pos_x = center[0] + speed * 6
        
    if (keys[pygame.K_d]):
        world_pos_x -= speed
        player_camera_pos_x = center[0] - speed * 6
    
    grid_rect.x += (world_pos_x - grid_rect.x) / drag
    grid_rect.y += (world_pos_y - grid_rect.y) / drag
    
    #mmm_rect.centery += (player_camera_pos_y - mmm_rect.centery) / 10
    #mmm_rect.centerx += (player_camera_pos_x - mmm_rect.centerx) / 10
     
    screen.blit(grid, (grid_rect.x, grid_rect.y))
    screen.blit(mmm, (mmm_rect.x, mmm_rect.y))
    pygame.display.update()