import operator

class Explanation:
    
    def __init__(self, shifts):
        """
        Initializes an explanation with a dictionary from features to their shifts.
        """
        self.shifts = shifts
        
    def top_k(self, k):
        """
        Returns the top k features ranked by amount shifted.
        """
        return sorted(self.shifts.items(), key = operator.itemgetter(1), reverse = True)[:k]

if __name__ == '__main__':
    shifts = {"hello": 3, "goodbye": 4, "my": 10, "name": 6, "is": 2, "aditya": 5}
    explanation = Explanation(shifts)
    print explanation.top_k(5)
