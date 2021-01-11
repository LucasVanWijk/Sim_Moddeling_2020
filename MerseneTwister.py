from warnings import warn


class Mersenne:
    """Pseudorandom number generater"""

    def __init__(self, seed=1234):
        """
        Initialize pseudorandom number generator. Accepts an
        integer or floating-point seed, which is used in
        conjunction with an integer multiplier, k, and the
        Mersenne prime, j, to "twist" pseudorandom numbers out
        of the latter. This member also initializes the order
        of the generator's period, so that members floating and
        integer can emit a warning when generation is about to
        cycle and thus become not so pseudorandom.
        """
        self.seed = seed
        self.j = 2 ** 31 - 1
        self.k = 16807
        self.period = 2 ** 30
  
    def randomNumber(self, interval=None, count=1, typeNb="int"):
        """
        Return a pseudorandom float or int. Default is one floating or integer number between zero and one. 
        Pass in a tuple or list, (a,b), to return a floating-point number on [a,b]. 
        If count is 1, a single number is returned, otherwise a list of numbers is returned.
        """
        
        randFloat = lambda i, randomness: (i[1] - i[0]) * randomness + i[0] if i is not None else randomness
        randInt = lambda i, randomness: int((i[1] - i[0] + 1) * randomness + i[0]) if i is not None else int(randomness<0.50)
        exactuables = {"int": randInt, "float": randFloat}
        relevantExactuable = exactuables[typeNb]
        results = []
        
        for i in range(count):
            self.seed = (self.k * self.seed) % self.j
            randomNess = (self.seed / self.j)
            results.append(relevantExactuable(interval, randomNess))    
            self.period -= 1
            if self.period == 0: warn("Pseudorandom period nearing!!", category=ResourceWarning)
        
        if count == 1:
            return results.pop()
        else:
            return results



