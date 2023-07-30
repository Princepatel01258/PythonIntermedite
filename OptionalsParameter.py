#def func(word, add=5, freq=1):
 #   print(word*(freq+add))

#call = func('hello\n', 5, 3 )
#print(call)


class car(object):
    def __init__(self, make, model, year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showALL):
        if showALL:
            print("This Car is a %s %s from %s %s and has %s kms" %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This Car is a %s %s from %s." %(self.make, self.model, self.year))
whip = car('Ford', 'Fusion', 2012 ,'New', 0)
whip.display(True)
