# objects.py


class task:
    def __init__(self, project):
        self.project = project
        self.complete = False
        self.description = ""

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

class bug(task):
    def __init__(self, project):
        task.__init__(self, project)
        self.lines = []

    def setLines(self, lines):
        self.lines = lines

    def getLines(self):
        return self.lines

