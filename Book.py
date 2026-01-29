class Book:
    def __init__(self, title : str, checked_out : bool = False):
        self.title = title
        self.checked_out = checked_out
        
    def check_out(self):
        self.checked_out = True