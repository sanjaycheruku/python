'''
single inheritance
multilevel inheritance
multiple inheritance
hierachical inheritance
'''
# single inheritance
'''
class parent():
    def output(self):
        print('parent')
class child(parent):
    def outputc(self):
        print('child')
c=child()
c.outputc()
c.output()
  '''
  # multilevel inheritance
  """
class grand():
    def outputhi(self):
        print('grand father') 
class father(grand):
    def output(self):
        print('father')
class child(father):
    def outputc(self):
        print("ther")
c=child()
c.outputhi()
c.output()
c.outputc()
c=child()
"""
#multiple inheritance

class father():
    def outputmo(self):
        print('father')
class mo():
    def outputfa(self):
        print('mo')
class child(father,mo):
    def outputc(self):
        print('son')
c=child()
c.outputmo()
c.outputfa()
c.outputc()
