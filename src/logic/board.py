import numpy as np

from pprint import pprint

from src.logic.utils import ConfigManager, SerializableDict


class Board:
    def __init__(self) -> None:
        self.config = SerializableDict(**ConfigManager.load_config())

        self.grid = None

        self.rows = None
        self.squares = None
        self.columns = None
    
    def create_board(self) -> None:
        self.grid = np.zeros((self.config.board_size, self.config.board_size), dtype=np.uint8)

    def display(self) -> None:
        if self.grid is None:
            pprint("No board was created! Please create a board...")
        else:
            pprint(self.grid)

