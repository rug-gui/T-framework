import sys
  
# setting path
sys.path.append('../T')
import main

if main.vmode[0][1]=='Light':
    from views import light as wndw
elif main.vmode[0][1]=='Dark':
    from views import dark as wndw
    
app = wndw.root