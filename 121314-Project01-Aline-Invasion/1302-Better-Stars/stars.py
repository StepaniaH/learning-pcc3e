import pygame
from random import randint


class Stars:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class StarField:
    def __init__(self, width, height, star_image, num_stars):
        self.width = width
        self.height = height
        self.star_image = star_image
        self.num_stars = num_stars
        self.stars = []
        self.create_star_field()

    def create_star_field(self):
        for _ in range(self.num_stars):
            x = randint(0, self.width - self.star_image.get_width())
            y = randint(0, self.height - self.star_image.get_height())
            self.stars.append(Stars(x, y, self.star_image))

    def draw(self, surface):
        for star in self.stars:
            star.draw(surface)


class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Stars")

        self.star_image = pygame.image.load("star.png")
        self.star_image = pygame.transform.scale(self.star_image, (50, 50))

        self.star_field = StarField(
            self.width, self.height, self.star_image, 100)

        self.renning = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.renning = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.star_field.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.renning:
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
