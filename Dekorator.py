class Man(object):
    def __init__(self, name):
        self._name = name

    def say(self):
        print ('Привет! Меня зовут %s!' % self._name)


class Jetpack(object):
    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        print ('%s летит на реактивном ранце!' % self._man._name)


man = Man('Петр')

man_jetpack = Jetpack(man)
man_jetpack.say()
man_jetpack.fly()

#Привет! Меня зовут Петр!
#Петр летит на реактивном ранце!