import importlib
import filechanges1

def changes():
    try:
        importlib.reload(filechanges1)
        filechanges1.print_changes()
    except:
        pass
for i in range(5):
    changes()
    input("Hit Enter to update ")
