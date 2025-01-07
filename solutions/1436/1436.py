class Solution: 
    def destCity(self, paths: List[List[str]]) -> str:
        cities = dict()
        for path in paths:
            if path[0] in cities:
                cities[path[0]] += 1
            else:
                cities[path[0]] = 1
            
            if path[1] in cities:
                cities[path[1]] += 1
            else:
                cities[path[1]] = 0

        return(min(cities, key=cities.get))