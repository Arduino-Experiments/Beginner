import SchemDraw as schem
import SchemDraw.elements as e
rinputs = {
'cnt':1,
'labels':['port_5']}
binputs = {'cnt':1,
       'labels':['GND']
        }
d = schem.Drawing()
ARDUINO = e.blackbox(d.unit, d.unit,rinputs=rinputs,binputs=binputs,mainlabel='ARDUINO')
T = d.add(ARDUINO)
BOT = d.add(e.GND,xy=T.GND)
d.add(e.DOT)
d.add(e.RBOX, d='right',xy=T.port_5, label='220$\Omega$')
d.add(e.LED,flip=True, d='down',toy=BOT.start)

d.add(e.LINE, d='left', tox=BOT.start)
d.draw()
d.save('source/Blink.eps')
