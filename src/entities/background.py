from ..utils import GameConfig
from .entity import Entity


class Background(Entity):
    """
    Represents the background entity in the FlapPyBird game.

    This class is responsible for rendering the background image across the entire game window.

    Args:
        config (GameConfig): The game configuration object containing window dimensions and image resources.

    Attributes:
        Inherits all attributes from the Entity base class, including position and size.
    """
    def __init__(self, config: GameConfig) -> None:
        super().__init__(
            config,
            config.images.background,
            0,
            0,
            config.window.width,
            config.window.height,
        )
