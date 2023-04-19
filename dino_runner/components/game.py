from token import AMPEREQUAL
import pygame
pygame.init()
pygame.mixer.init()

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAME_SPEED, X_POSITION_BACKGROUND, Y_POSITION_BACKGROUND, SCORE_SOUND, SCORE_TXT, CLOUD, DEFAULT_TYPE
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager


class Game:
    def __init__(self): 
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.game_speed = GAME_SPEED
        self.x_pos_bg = X_POSITION_BACKGROUND
        self.y_pos_bg = Y_POSITION_BACKGROUND
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.death_count = 0
        self.sound_score = SCORE_SOUND
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2
        self.x_pos_cloud = 0
        self.y_pos_cloud = 20 
    
    def execute(self): 
        self.running = True
        while self.running:
            if not self.playing: # Vai mostrar o menu antes do jogo começar e quando o jogador perde
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score = 0
        self.game_speed = 20
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self) 
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
    
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0: 
            if self.game_speed < 60:
                self.game_speed += 5
            if self.score % 100 == 0:
                self.score += 1
            self.sound_score.set_volume(0.5)
            self.sound_score.play()
            

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((200, 200, 200))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_cloud()
        self.draw_score()
        self.draw_power_upper_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1000
        self.x_pos_cloud -= self.game_speed
    
    def draw_score(self):
        draw_message_component(
            f"score: {self.score} ",
            self.screen,
            pos_x_center = 1200,
            pos_y_center = 50
        )
    
    def draw_power_upper_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen, 
                    font_size = 18,
                    pos_x_center = 50,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE 
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((220, 220, 220))  
        if self.death_count == 0:
            draw_message_component("Press any key to start.", self.screen)
        else:
            draw_message_component("Press any key to play again.", self.screen, pos_y_center = self.half_screen_height - 40)
            draw_message_component(f"Your score: {self.score}", self.screen, pos_y_center = self.half_screen_height - 80) 
            draw_message_component(f"Death count: {self.death_count}", self.screen, pos_y_center=self.half_screen_height )
            draw_message_component("Better results:", self.screen, pos_y_center=self.half_screen_height + 80)
            self.best_scores()
            
            

        pygame.display.update()
        self.handle_events_on_menu()
        
    def best_scores(self):
        with open(f'{SCORE_TXT}', 'r') as archive:
            all_values = []
            for valor in archive:
                all_values.append(int(valor.replace("\n", '')))
                all_values.sort(reverse=True)
                if len(all_values) > 5:
                    all_values.pop()
            
            count = 0
            while count < len(all_values):
                draw_message_component(f"{count + 1}° - {all_values[count]}", self.screen, pos_y_center=self.half_screen_height + 80 + ((count+1) * 35))
                count += 1
            