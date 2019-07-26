# project object to be used with tracker.py
import datetime

class Project:
    def __init__(self, name):
        self.name = name
        self.workseconds = 0 

        try:
            self.read_data()
        except:
            pass

    def start_timer(self):
        self.start_time = datetime.datetime.now()

    def stop_timer(self):
        self.stop_time = datetime.datetime.now()
        self.workseconds = self.workseconds + (self.stop_time - self.start_time).seconds

    def write_data(self):
        with open(self.name + ".txt", "w+") as f:
            f.write(self.name + "\n")
            f.write(str(self.workseconds))

    def read_data(self):
        with open(self.name + ".txt", "r") as f:
            self.name = f.readline().strip("\n")
            self.workseconds = int(f.readline())

if __name__ == "__main__":
    x = Project("first")
    x.start_timer()
    time.sleep(1)
    x.stop_timer()
    x.write_data()
    print(x.workseconds)
    
    x.start_timer()
    time.sleep(1)
    x.stop_timer()
    x.write_data()
    print(x.workseconds)
