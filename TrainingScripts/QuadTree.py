"""
    The following example is going to be an QuadTree learning materials to help myself to understand it
    The request is coming from Terrain streaming knowledge
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class QuadTreeNode:
    def __init__(self, x, y, width, height, capacity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.capacity = capacity
        self.points = []
        self.children = None

    def is_leaf(self):
        return self.children is None

    def insert(self, point):
        if not (self.x <= point.x < self.x + self.width and
                self.y <= point.y < self.y + self.height):
            return False

        if len(self.points) < self.capacity and self.is_leaf():
            self.points.append(point)
            return True

        if self.is_leaf():
            self.subdivide()

        for child in self.children:
            if child.insert(point):
                return True

    def subdivide(self):
        half_width = self.width / 2
        half_height = self.height / 2
        self.children = [
            QuadTreeNode(self.x, self.y, half_width, half_height, self.capacity),
            QuadTreeNode(self.x + half_width, self.y, half_width, half_height, self.capacity),
            QuadTreeNode(self.x, self.y + half_height, half_width, half_height, self.capacity),
            QuadTreeNode(self.x + half_width, self.y + half_height, half_width, half_height, self.capacity)
        ]
        for point in self.points:
            for child in self.children:
                child.insert(point)
        self.points = []

    def query_range(self, range_x, range_y):
        points_in_range = []
        if not (self.x < range_x[0] + range_x[1] and self.x + self.width > range_x[0] and
                self.y < range_y[0] + range_y[1] and self.y + self.height > range_y[0]):
            return points_in_range

        for point in self.points:
            if range_x[0] <= point.x < range_x[0] + range_x[1] and \
                    range_y[0] <= point.y < range_y[0] + range_y[1]:
                points_in_range.append(point)

        if self.is_leaf():
            return points_in_range

        for child in self.children:
            points_in_range.extend(child.query_range(range_x, range_y))

        return points_in_range


class QuadTree:
    def __init__(self, x, y, width, height, capacity):
        self.root = QuadTreeNode(x, y, width, height, capacity)

    def insert(self, point):
        self.root.insert(point)

    def query_range(self, range_x, range_y):
        return self.root.query_range(range_x, range_y)


def main():
    quadtree = QuadTree(0, 0, 100, 100, 4)

    points = [Point(20, 30), Point(50, 60), Point(80, 20), Point(70, 90)]
    for point in points:
        quadtree.insert(point)

    query_result = quadtree.query_range((40, 40), (50, 50))
    for point in query_result:
        print("Point:", point.x, point.y)


if __name__ == "__main__":
    main()
