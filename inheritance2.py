# multiple inheritance
class father():
    def outputmom(self):
        print('father')
class mom():
    def outputfa(self):
        print('mom')
class child(father,mom):
    def outputc(self):
        print('son')
c=child()
c.outputmom()
c.outputfa()
c.outputc()
# heritance inheritance


class mom():
    def outputmom(self):
        print()
class father():
    def outputfa(self):
        print('fa')
class child():
    def outputc(self):
        print('child')
c=child()
c.outputmom()
c.outputfa()
c.output()