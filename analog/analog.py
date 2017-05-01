import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing()

rinputs = {
    'cnt':1,
    'labels':['port_3']
}
binputs = {'cnt':1,
    'labels':['GND']
}

linputs = {
    'cnt':2,
    'labels':['port_A5','port_5v']
}

d = schem.Drawing()
ARDUINO = e.blackbox(d.unit*1.3, d.unit*2.25,
rinputs=rinputs,
binputs=binputs,
linputs=linputs,
mainlabel='ARDUINO')
T = d.add(ARDUINO)
d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_3)
d.add(e.LED)
d.add(e.DOT)
d.add(e.GND)
d.pop()
l1 = d.add(e.LINE,xy=T.GND,tox=T.port_A5+[-1,0],d='left')
l2 = d.add(e.LINE,xy=T.port_5v,tox=T.port_5v+[-1,0],d='left')

POT = d.add(e.POT,endpts=[T.port_5v+[-1,0],l1.end],d="left")
p = d.add(e.DOT,xy=POT.tap+[0.5,0])
d.add(e.LINE,endpts=[T.port_A5,POT.tap+[0.5,0]])

d.draw()
d.save('source/analog.eps')
