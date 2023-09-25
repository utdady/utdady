gdict = {'a': ['c', 'd'], 'b': [], 'c': ['b'], 'd': ['b', 'c']}

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def __iter__(self):
        self.__iter__obj = iter(self.gdict)
        return self.__iter__obj

    def __next__(self):
        return next(self.__iter__obj)

    def __str__(self):
        res = "vertices: "
        for i in self.gdict:
            res += str(i) + " "
        res += "\nedges: "
        for edge in self.findE():
            res += str(edge) + " "
        return res

    def getV(self):
        return list(self.gdict.keys())

    def getE(self):
        return self.findE()

    def findE(self):
        edge = []
        for v in self.gdict:
            for nv in self.gdict[v]:
                if {nv, v} not in edge:
                    edge.append({nv, v})
        return edge

    def addV(self, v):
        if v not in self.gdict:
            self.gdict[v] = []

    def addE(self, edge):
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1] = [v2]

    def find_path(self, start, end, path=None):
        if path == None:
            path = []
        path += [start]
        if start == end:
            return path
        if start not in self.gdict:
            return None
        for v in self.gdict[start]:
            if v not in path:
                ext_path = self.find_path(v, end, path)
                if ext_path:
                    return ext_path
        return None

    def find_all_paths(self, start, end, path=[]):
        path += [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for v in self.gdict[start]:
            if v not in path:
                ext_path = self.find_all_paths(v, end, path)
                for p in ext_path:
                    paths.append(p)
        return paths

def main():
    g = graph(gdict)
    print(g)

main()
