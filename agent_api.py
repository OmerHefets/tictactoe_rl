import random
import numpy as np
import grid_api as g
import nn_api as nn


class Agent:

    def __init__(self):
        self.wins = 0
        self.losses = 0

    def action_pipeline(self):