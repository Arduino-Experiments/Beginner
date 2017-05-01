import SchemDraw as schem
import SchemDraw.elements as e

d = schem.Drawing()

rinputs = {
'cnt':6,
'labels':['port_2','port_3','port_4','port_5','port_6','port_7']}
binputs = {'cnt':1,
       'labels':['GND']
        }
d = schem.Drawing()
ARDUINO = e.blackbox(d.unit*1.3, d.unit*2.25,rinputs=rinputs,binputs=binputs,mainlabel='ARDUINO')
T = d.add(ARDUINO)
d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_2)
d.add(e.LED)
d.add(e.DOT)
d.add(e.GND)
d.pop()

d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_3)
d.add(e.LED)
d.add(e.DOT)
d.add(e.GND)
d.pop()

d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_4)
d.add(e.LED)
d.add(e.DOT)
d.add(e.GND)
d.pop()

d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_5)
d.add(e.LED)
d.add(e.DOT)
d.add(e.GND)
d.pop()

d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_6)
d.add(e.LED)
d.add(e.DOT)
d.add(e.GND)
d.pop()

d.push()
d.add(e.RBOX,label='1000$\Omega$',xy=T.port_7)
d.add(e.LED)
d.add(e.DOT)
d.add(e.GND)
d.pop()

d.draw()
d.save('source/Marquee-LED-Banner.eps')
