import sys
sys.path.append('..T')
import main
def SetMode(preference):
    main.c.execute("Update PREFERENCES SET VALUE='"+preference+"' WHERE OPTION='ViewMode'")