class Student:


    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores


    def add_score(self, score):
        self.scores.append(score)


    def mean_score(self):
        return sum(self.scores) / len(self.scores)


