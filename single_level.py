'''single leve inheritance'''

'''parent class'''
class animal:
    livingthing=True
    def eat ():
        print('eanting')
    def sleep():
        print('sleeping')
    def ntg():
        print('eating,sleeping,going')
    def name():
        print('goutham')
'''child class'''
class goat(animal):
    def grass():
        print('eat')
    def rice():
        print('not eat')
    def sleep():
        print('daily')
goat.sleep()
animal.sleep()
print(goat.livingthing)
print(animal.livingthing)
animal.ntg()
goat.ntg()
goat.name()
animal.name()
animal.rice()  # AttributeError:type object 'animal' has no attribute 'rice'
