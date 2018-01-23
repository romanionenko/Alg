def graham_scan(points_array):
    """Returns scanned array of points(convex hull surrounding).

    Keyword arguments:
    points_array -- unsorted array of points
    """

    def cross_product_orientation(point_a, point_b, point_c):
        """Returns the orientation of three points.
        > 0 if clockwise, < 0 if counterclockwise, 0 if co-linear
        """

        return (point_b.get_y() - point_a.get_y()) * \
               (point_c.get_x() - point_a.get_x()) - \
               (point_b.get_x() - point_a.get_x()) * \
               (point_c.get_y() - point_a.get_y())

    convex_hull = []
    sorted_points = sort_points(points_array)
    for point in sorted_points:
        while len(convex_hull) > 1 and cross_product_orientation(convex_hull[-2], convex_hull[-1], point) >= 0:
            convex_hull.pop()
        convex_hull.append(point)
    return convex_hull


def sort_points(points_array):
    """Returns array of points sorted leftmost first, then by slope asc."""

    def sort_by_slope(point):
        """Returns the slope of two points."""

        leftmost_point = points_array[0]
        return (leftmost_point.get_y() - point.get_y()) / \
               (leftmost_point.get_x() - point.get_x())

    points_array.sort()
    return points_array[:1] + sorted(points_array[1:], key=sort_by_slope)
