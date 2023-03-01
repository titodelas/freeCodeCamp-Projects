import random
from prob_calculator import Hat, experiment
import unittest

random.seed(95)

hat = Hat(blue=4, red=2, green=6)
expected_balls = {"blue": 2, "red": 1}
num_balls_drawn = 4
num_experiments = 3000

probability = experiment(hat=hat, expected_balls=expected_balls,
                          num_balls_drawn=num_balls_drawn, 
                          num_experiments=num_experiments)

print(f"Probability: {probability:.3f}")


# Run unit tests automatically
if __name__ == "__main__":
    unittest.main(module='test_module', exit=False)
