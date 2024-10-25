class wascalled():

    def __init__ (self):
        self.called = False

    def __str__ (self):
        if self.called == False:
            print()
        elif self.called == True:
            print(wascalled)