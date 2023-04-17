from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Piterodactyl(Obstacle):
    BIRD = (BIRD, 250)
    
    def __init__(self):
        self.image, self.bird_pos = self.BIRD
        self.type = 0
        super().__init__(self.image, self.type)
        self.rect.y = self.bird_pos
        self.index = 0
    
    def draw(self, screen):
        screen.blit(self.image[self.index // 3], self.rect)
        self.index += 1
        
        if self.index >= 6:
            self.index = 0