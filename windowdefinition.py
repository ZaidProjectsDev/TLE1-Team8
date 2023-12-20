
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


active_window = WindowDefinition('', '')


def update_active_window(new_window):
    global active_window
    active_window = WindowDefinition(new_window.getPid(),new_window.getTitle())

def get_active_window():
    global active_window
    return active_window

def get_updated_window_status():
    print(get_active_window().title + " x " + get_active_window().pid)

