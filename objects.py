# objects.py


class Task:
    def __init__(self, project):
        self.type = "Task"
        self.project = project
        self.complete = False
        self.description = ""

    def __repr__(self):
        string =  (self.type + "\nProject: " + self.project +
               "\nComplete: " + str(self.complete) +
               "\nDescription: " + self.description)
        return string

    def setComplete(self):
        self.complete = True

    def setIncomplete(self):
        self.complete = False

    def setDescription(self, text):
        self.description = text

    def setProject(self, project):
        self.project = project

    def getComplete(self):
        return self.complete

    def getDescription(self):
        return self.description

    def getProject(self):
        return self.Project

class Bug(Task):
    def __init__(self, project):
        Task.__init__(self, project)
        self.type = "Bug"
        self.lines = []

    def setLines(self, lines):
        self.lines = lines

    def getLines(self):
        return self.lines

