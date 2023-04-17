from random import randint
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self):
        self.CACTUS = [
            (LARGE_CACTUS, 300),
            (SMALL_CACTUS, 325),
        ]
        image, cactus_pos = self.CACTUS[randint(0, 1)]
        self.type = randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos