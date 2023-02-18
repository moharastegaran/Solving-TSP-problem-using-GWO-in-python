import matplotlib.pyplot as plt


class PlotSolution:
    def __init__(self, sol, cities):
        self.tour = sol
        self.cities = cities

    def plot(self):
        """
        Get x & y of each city
        Draw connection between every city using arrows in graph
        The red line at the end, indicates a complete route, back to the starting point
        """
        x_cords = [self.cities[self.tour[i-1]].x for i in self.tour]
        y_cords = [self.cities[self.tour[j-1]].y for j in self.tour]
        nums = [self.cities[self.tour[k-1]] for k in self.tour]
        plt.clf()
        plt.plot(x_cords, y_cords)
        for i in range(0, len(self.tour) - 1):
            plt.annotate(text=str(nums[i]), xy=(x_cords[i + 1], y_cords[i + 1]), xytext=(x_cords[i], y_cords[i]),
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.01', color='b'))
        size = len(self.tour)
        # complete route , دور کامل
        plt.annotate(text=str(nums[size - 1]), xy=(x_cords[0], y_cords[0]), xytext=(x_cords[size - 1], y_cords[size - 1]),
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='r'))

        plt.xlabel("X - axis")
        plt.ylabel("Y - axis")
        plt.title("TSP Optimization with GW algorithm")
        plt.pause(0.1)
        plt.show(block=False)
