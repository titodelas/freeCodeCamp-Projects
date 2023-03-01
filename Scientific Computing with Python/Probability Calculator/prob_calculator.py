import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, value in kwargs.items():
            for val in range(value):
                self.contents.append(color)

    def draw(self, n_balls):
        if n_balls >= len(self.contents):
            balls_drawn = copy.deepcopy(self.contents)
            self.contents = []
            return balls_drawn
        balls_drawn = random.sample(self.contents, n_balls)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successes = 0
    for i in range(num_experiments):
        random.seed(i)
        full_hat = copy.deepcopy(hat)
        balls_drawn = full_hat.draw(num_balls_drawn)
        success = all(balls_drawn.count(color) >= count
                      for color, count in expected_balls.items())
        if success:
            num_successes += 1
    return num_successes / num_experiments
