import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship ans set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        # Practice 12-2 Game Character will change this link of the image, and do not forget to change the background color in settings.py
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Staet each new ship at the bootom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal position.
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving.
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)
