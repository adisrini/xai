from explanation import Explanation

if __name__ == '__main__':
    shifts = {"hello": 3, "goodbye": 4, "my": 10, "name": 6, "is": 2, "aditya": 5}
    explanation = Explanation(shifts)
    print explanation.top_k(5)