#create a class data that cans tore data points scattered na 2 dimensional space belonging to three different categories. write a function to find the centrois of each category"

class Data:
    def __init__(self, data_points, categories):
        self.data_points = data_points
        self.categories = categories
        self.centroids = {}

    def find_centroids(self):
        for category in self.categories:
            centroid = [0, 0]
            count = 0
            for data_point in self.data_points:
                if data_point[2] == category:
                    centroid[0] += data_point[0]
                    centroid[1] += data_point[1]
                    count += 1
            centroid[0] /= count
            centroid[1] /= count
            self.centroids[category] = centroid

    def get_centroids(self):
        return self.centroids


data_points = [[1, 2, "A"], [3, 4, "B"], [5, 6, "C"], [7, 8, "A"], [9, 10, "B"]]
categories = ["A", "B", "C"]

data = Data(data_points, categories)
data.find_centroids()

centroids = data.get_centroids()

print(centroids)
