from ..utils import GameConfig
from .entity import Entity


class Floor(Entity):
    """
    Represents the moving floor entity in the FlapPyBird game.
    The Floor entity scrolls horizontally to simulate movement. It inherits from Entity and uses the base image.
    The floor's position is updated in the `draw` method to create a looping effect, giving the illusion of continuous motion.
    Attributes:
        vel_x (int): The horizontal velocity of the floor.
        x_extra (int): The extra width used for looping the floor image.
    Methods:
        stop(): Stops the floor's movement by setting its velocity to zero.
        draw(): Updates the floor's position and draws it on the screen.
    """
    def __init__(self, config: GameConfig) -> None:
        super().__init__(config, config.images.base, 0, config.window.vh)
        self.vel_x = 4
        self.x_extra = self.w - config.window.w

    def stop(self) -> None:
        self.vel_x = 0

    def draw(self) -> None:
        self.x = -((-self.x + self.vel_x) % self.x_extra)
        super().draw()
