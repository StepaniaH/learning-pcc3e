from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """A class to generate a random walk"""
    def __init__(self, num_points=5000):
        """Initialize attributes of a random walk"""
        self.num_points = num_points

        # All walks start at the (0, 0) point
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Add the new position to the walk.
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Get the next step in the walk"""
        return (choice([-1, 1]) * choice([0, 1, 2, 3, 4]))


rw = RandomWalk(num_points=5000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values)

plt.show()


