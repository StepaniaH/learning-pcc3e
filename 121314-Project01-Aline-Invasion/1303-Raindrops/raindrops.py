import pygame
import sys


class Rain(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the rain image and set its rect attribute.
        try:
            original_image = pygame.image.load("rain.png")
        except pygame.error as e:
            print(f"Disable image loading: {e}")
            sys.exit()
        self.image = pygame.transform.scale(original_image, (10, 20))
        self.rect = self.image.get_rect()

        # Start each new raindrop at the top of the screen.
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        # self.x = float(self.rect.x)
        # print(f"Raindrop size: {self.rect.size}") 

    def check_edges(self):
        """Return True if raindrop is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom

    def update(self):
        """Move the raindrop down."""
        self.rect.y += self.settings.rain_speed
    


class Settings:
    """A class to store all settings for raindrops."""
    def __init__(self):
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Rain settings
        self.rain_speed = 10.0


class Raindrops:
    def __init__(self):
        """Overall class to manage game assets and behavior."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Set up the window and screen.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Raindrops")

        # Create a sprite group to store the raindrops.
        self.raindrops = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypressrs and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keydown events."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_raindrops(self, x_position, y_position):
        """Create the raindrops."""
        new_raindrop = Rain(self)
        new_raindrop.x = x_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)


    def _create_fleet(self):
        """Create the fleet of raindrops."""
        # Create a raindrop and keep adding raindrops until there's no room left.
        # Spacing between raindrops is one raindrop width and one raindrop height.
        raindrop = Rain(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - 3 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                self._create_raindrops(current_x, current_y)
                current_x += 2 * raindrop_width

            # Finished a row; reset x value, and increment y value.
            current_x = raindrop_width
            current_y += 2 * raindrop_height

        print(f"Created {len(self.raindrops)} raindrops")

    def _update_raindrops(self):
        """Update position of raindrops and get rid of old raindrops."""
        self.raindrops.update()

        # Get rid of raindrops that have gone off the screen.
        for raindrop in self.raindrops.copy():
            if raindrop.check_edges():
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run it.
    ai = Raindrops()
    ai.run_game()
