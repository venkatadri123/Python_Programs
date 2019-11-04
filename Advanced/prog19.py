# Interface to connect to any database.
from abc import*
class MyInter(ABC):
    @abstractmethod
    def connect(self):
        pass
class Oracle(MyInter):
    def connect(self):
        print('connecting to Oracle...')
class Sybase(MyInter):
    def connect(self):
        print('connecting to Sybase...')

dbname=input('enter database name:')
classname=globals()[dbname]
c=classname()
c.connect()
