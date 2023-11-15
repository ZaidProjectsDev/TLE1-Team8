class WindowDefinition:
    pid = ''
    title = ''

    def __init__(self, process_id='', title=''):
        self.pid = process_id
        self.title = title


    def getTitle(self):
        return self.title

    def getPid(self):
        return self.pid

activeWindow = WindowDefinition()