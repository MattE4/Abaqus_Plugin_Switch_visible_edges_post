from abaqus import *
from abaqusConstants import *
from caeModules import visualization

def switchEdges():
	vps = session.viewports.keys()[0]
	co = session.viewports[vps].odbDisplay.commonOptions

	if co.visibleEdges == FEATURE:
		co.setValues(visibleEdges=EXTERIOR)
	#elif co.visibleEdges == EXTERIOR:
	else:
		co.setValues(visibleEdges=FEATURE)
		
if __name__ == '__main__':
	
	switchEdges()