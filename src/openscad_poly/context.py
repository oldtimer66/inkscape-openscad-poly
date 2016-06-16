class ShorterFloat(float):
    """A float which returns only 3 digits after the decimal"""
    def __repr__(self):
        return "%0.3f" % self

class OSCADPolyContext:
    def __init__(self, svg_file):
        self.file = svg_file
        self.polygons = []

    def generate(self):
        # generate list of all modules at top for easy control by uncommenting
        for polygon in self.polygons:

            print "//{}();".format(polygon['id'])

        # generate actual modules from polygons
        for polygon in self.polygons:
            print
            print "module {}()".format(polygon['id'])
            print "    polygon("
            print "        points="
            print "            {},".format(polygon['points'])
            print "        paths="
            print "            {}".format(polygon['paths'])
            print "    );"

    def add_poly(self, poly_id, points, paths):
        shortened_points = [[ShorterFloat(x), ShorterFloat(y)] for x, y in points]
        self.polygons.append({ 'id': poly_id, 'points':shortened_points, 'paths':paths})
