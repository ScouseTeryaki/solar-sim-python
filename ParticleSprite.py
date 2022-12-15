import pygame.gfxdraw


class ParticleSprite(pygame.sprite.Sprite):
    def __init__(self, radius, color):
        super(ParticleSprite, self).__init__()
        self.radius = radius
        self.color = color
        surface = pygame.Surface((self.radius+1, self.radius+1), pygame.SRCALPHA)
        self.surface = surface
        self.rect = self.surface.get_rect()

        self.radius_offset = int(self.radius/2)

        pygame.gfxdraw.aacircle(surface, self.radius_offset, self.radius_offset, self.radius_offset, self.color)
        pygame.gfxdraw.filled_circle(surface, self.radius_offset, self.radius_offset, self.radius_offset, self.color)