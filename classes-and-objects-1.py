class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    
    print("Student Information:")

    def change_name(self, newName):
        self.name = newName
        print("Name: ", self.name)

    def change_age(self, newAge):
        self.age = newAge
        print("Age: ", self.age)

    def add_track(self, newTrack):
        self.tracks.append(newTrack)
        print("Track: ", self.tracks)

    def get_score(self, newScore):
        self.score = newScore
        print("Score: ", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Kate")
Bob.change_age(48)
Bob.add_track("UI/UX")
Bob.get_score(72.30)
