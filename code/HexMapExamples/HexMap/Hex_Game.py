''' Module: Hex_Game.py   2/16/2009
    Author: John Crawford

    Contains the Game Model part of an MVC model. Builds a simple hex map,
    which can currently only be rotated. Has a link back to the Event
    Handler from the wxPython top Frame, used to generate events.
    Events Generated: MapRotateEvent.
    
    '''
import wx
from Hex_Math import *

# this Event is technically unnecessary, as the top frame receives the
# keypress which initiates a MapRotate. The top frame *could* also tell
# its own mapView to rotate, rather than having the Game Model send back
# an event saying the map changed. But what would be the fun in that???
class MapRotatedEvent(wx.PyEvent):
    def __init__(self, evtType, id):
        wx.PyEvent.__init__(self, id, evtType)
EVT_MAP_ROT = wx.NewEventType()

class Game(object):
    ''' Builds a 2d hex map. Contains purely abstract Game Model data,
        such as hexes and their rows/columns. Does not contain any visual
        interface information, all of which is under the View Model element.
        Does have a link to a function in the
        top Frame that can generate events.'''
    def __init__(self, map_cols, map_rows, event_mgr, id):
        self._map = gMap(map_cols, map_rows)
        self._eventMgr = event_mgr
        # top frame id - so all events appear to originate from that frame.
        self._eventId = id

    def RotateMap(self):
        self._map.RotateMap()
        evt = MapRotatedEvent(EVT_MAP_ROT, self._eventId)
        self._eventMgr.ProcessEvent(evt)

    hex_dir = property(lambda self : self._map.hex_dir)
    hex_list = property(lambda self : self._map.ListHexes())
    
    cols = property(lambda self : self._map.hex_cols)
    rows = property(lambda self : self._map.hex_rows)
    
    Boardwalk = property(lambda : True) # what's a game without the properties
    Park_Place = property(lambda : True) # Boardwalk and Park Place?

class gMap(object):
    ''' builds a dictionary/2D array of hex objects. '''
    def __init__(self, map_cols, map_rows):
        self.mapname = 'standard hex map'
        self.hex_cols = map_cols
        self.hex_rows = map_rows
        self.hex_dir = ACROSS # default, can be changed in-game.
        self.hex_dict = {}
        ''' dictionary key is (col, row) of each hex. So far I don't
            reference hexes by row/col, but that might change... Or
            possibly I should change the dictionaries to Lists.'''
        for x in range(self.hex_cols):
            for y in range(self.hex_rows):
                self.hex_dict[(x, y)] = gHex(x, y, self.hex_dir)

    def ListHexes(self):
        hex_list = []
        for hex in self.hex_dict.itervalues():
            hex_list.append(hex)
        return hex_list

    def RotateMap(self):
        self.hex_dir = ACROSS if self.hex_dir == DOWN else DOWN
        for hex in self.hex_dict.itervalues():
            hex.hex_dir = self.hex_dir

class gHex(object):
    def __init__(self, x, y, hex_dir):
        # needs more cowb... ah, Variables...
        self.col = x
        self.row = y
        self.color = None # set by the View component, vHex
        self.hex_dir = hex_dir
