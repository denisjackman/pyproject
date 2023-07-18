''' Module: Hex_Main.py  2/16/2009
    Author: John Crawford

    Written using: Python 2.5 and wxPython 2.8.9.1

    Functions MakeMenuBar(), CreateMenu(), CreateMenuItem()
    based on book: "wxPython in Action"

    Basic Hex-Board Drawing program
    Uses the Model-View-Controller pattern. In my original Pygame
    implementation, I used a Mediator (event manager) to handle
    communication between the main MVC objects. This version used wxPython,
    in which an event manager is built into the package. Also, the View and
    Controller objects are deeply intertwingled in wxPython.

    The View object (mapView) has a link to the Game Model object, and
    calls the Game functions for information about the Model - currently
    only how many cols/rows of hexes, and what direction the hexes point.

    The Game Model object has a link to a wxPython Event Handler function
    (which is gotten from the topFrame.GetEventHandler()), which is *only*
    used to generates Events. The Game Model does not have any access to
    any of the View object's data or function. However, in order to generate
    Events in wxPython, an object must either be of type EvtHandler, or
    have a link to that function.

    The Controller object, I'm going to call the topFrame, in this module.
    It handles the keyboard/menu options, etc.

    Main Objects:
        Game - creates 2d map and loads it with hexes. Abstract data model,
            does not contain any interface/view data.
        View - creates sprite list corresponding to each game hex. Handles
            all displaying of map/hexes using wxPython widgets.
    Current features:
        Creates a window (now a subclassed ScrollingWindow, with a
        background bitmap larger than the window display, which
        scrolls around with arrow keys.
        Draws a single hex, and array of hexes from Game Model map.
        Displays hex coordinates roughly in center of hex.
        Flips hex direction to either across or down the screen.
        Locate specific hex that mouse is clicked on, toggles color.
        Flash specific hex that mouse moves over with third color.
        Selects specific hex with mouse-click, toggles border of hex
        with another color. Much cleaner than my code in Pygame.
        Shift-drag mouse to multi-select hexes.
        Has Menu bar - the Quit options works at least...
        Has additional Color panel window besides the map window,
        which can be toggled on/off. CP is mainly an experiment, to
        test out having two windows side-by-side. And sure enough, I ran
        into problems with Focus and keyboard events not being trapped.
        Hexes can be filled or empty.
        Change colors of individual hexes.
        Fill color can be selected via the Color Panel.
        When vHex changes color, it sets the associated Game Model hex to
        new color - not that the game does anything with it yet...
        Can select number of hexes per col/row when creating new Game.
    ToDo:
        Map background does not resize to fit maximum large-hexes.
        Generates multi-sized hexes.
        Load image files per hex type.
        Fix the hex-finding algorithm. Currently if the mouse is too close
        to one corner, it sometimes finds the wrong hex. Oh well...
        Fix the flash-bordering code, which actually will require fixing
        the polygon drawing/dithering code...
    Someday:
        Replace the wxPython polygon/hex drawing algorithm with my own for
        dithering the edges, so they are more compatible. Currently there
        are some displaying artifacts on one hex edge. If I put two hexes
        side-by-side on one of the angled sided, the pixels making up the
        opposite sides don't quite line up right. I put a one-pixel gap
        between hexes, but the mismatched edges means there are some slight
        Moire patterns showing up in big maps. Oh well...
    Removed:
        Originally - a vHex had three states, plain, Active, or Flashed.
        Active was semi-permanent, after being mouse-clicked, whereas
        Flashed was transient, only while the mouse was *directly* over
        a hex. However, the Active state only had one color. I changed the
        design (such as it is) to allow every hex to have a different color,
        so the Active state, although useful as a learning tool (this
        whole project is to learn Python and wxPython), has been changed
        to allow a multi-colored hex map.
    '''

import wx
from Hex_Game import Game, EVT_MAP_ROT
from Hex_View import mapView, thumb_dict
from Hex_Panel import ColorPanel

# event binder, the event declared in the hex_Game module.
HDL_MAP_ROT = wx.PyEventBinder(EVT_MAP_ROT, 1)

MAP_TITLE = 'Basic Hex Map Version 0.1'
SCR_SIZE = (800, 600)

#######################################################################
class topFrame(wx.Frame):  #pylint: disable-msg=C0103
    ''' Main Frame for the Hex Map program. '''
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=SCR_SIZE)
        self.topPanel = wx.Panel(self, -1)
        self.gameModel = None # link back to Game Model object.

        self.MakeStatusBar()

        self.mapView = mapView(self.topPanel, self.StatusBar)
        self.CP = ColorPanel(self.topPanel, self)

        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(self.CP, 0, wx.EXPAND)
        box.Add(self.mapView, 1, wx.EXPAND)
        self.topPanel.SetSizer(box)
        self.MakeMenuBar() # great - this is order-dependent - fails earlier.

        self.mapView.SetFocus()
        self.mapView.Bind(wx.EVT_CHAR, self.OnKeyPress)
        self.mapView.Bind(wx.EVT_KILL_FOCUS, self.OnLostFocus)

        self.Bind(HDL_MAP_ROT, self.OnMapRotated)

    def MakeMenuBar(self):
        ''' Create the menu bar. '''
        menuBar = wx.MenuBar()
        for eachMenuData in self.MenuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        ''' Create a menu from a menu description.'''
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2: # then this is a sub-menu, with items.
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu)
            else: # then this is a menu item
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        ''' Create a menu item.'''
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def MakeStatusBar(self):
        ''' Create the status bar.'''
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-4, -2, -2])

    def NewCPColor(self, color):
        ''' Received message from Color Panel that a new color has been'''
        self.mapView.ChangeActiveColor(color)

    def OnNewGame(self, event):  #pylint: disable-msg=W0613
        ''' Create a new game. '''
        dlg = SliderDialog(self, -1, 'New Map: Set Columns and Rows')
        result = dlg.ShowModal()
        if result == wx.ID_CANCEL:
            return
        cols = dlg.colSlider.GetValue()
        rows = dlg.rowSlider.GetValue()
        dlg.Destroy()
        self.gameModel = Game(cols, rows, self.GetEventHandler(), self.GetId())
        self.mapView.BuildNewMap(self.gameModel)


    def OnMapRotated(self, event):  #pylint: disable-msg=W0613
        ''' Received message from Game Model that map has been rotated. '''
        self.mapView.RotateMap()


    def OnRotateMap(self, event):  #pylint: disable-msg=W0613
        ''' tell Game Model to rotate the map. '''
        self.gameModel.RotateMap()


    def OnKeyPress(self, event):
        ''' Handle key presses. '''
        if event.GetKeyCode() in (ord('r'), ord('R')):
            self.gameModel.RotateMap()
        elif event.GetKeyCode() in (ord('c'), ord('C')):
            self.mapView.ClearActive()
        elif event.GetKeyCode() in (ord('b'), ord('B')):
            self.mapView.ChangeBackground()
        elif event.GetKeyCode() in thumb_dict.items():
            self.mapView.MoveMapView(event.GetKeyCode(), event.ShiftDown())
        elif event.GetKeyCode() in (ord('q'), ord('Q')):
            self.Close()

    def OnCloseWindow(self, event):  #pylint: disable-msg=W0613
        ''' Close the window. '''
        self.Close()


    def OnChangeBG(self, event):  #pylint: disable-msg=W0613
        ''' Change the background color.'''
        self.mapView.ChangeBackground()


    def OnToggleCP(self, event):
        ''' Show or hide the color panel.'''
        self.CP.Show(not event.IsChecked())

    def OnClearMap(self, event):  #pylint: disable-msg=W0613
        ''' Clear the map. '''
        self.mapView.ClearActiveColors()


    def OnHexFill(self, event):
        ''' Toggle hex fill.'''
        self.mapView.ChangeHexFill(event.IsChecked())

    def OnHexSize(self, event):
        ''' Change the hex size.'''
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        if item:
            size = item.GetLabel().split()[0].lower()
            self.mapView.ChangeHexSize(size)

    # required to keep the mapView receiving keyboard events... KLUDGY
    def OnLostFocus(self, event):
        ''' Set focus back to the mapView. '''
        self.mapView.SetFocus()
        event.Skip()

    def MenuData(self):
        ''' Create the menu data.'''
        menu_list = (
            ('&File', (
                ('&New', 'New Background', self.OnChangeBG),
                ('', '', ''),
                ('&Quit', 'Quit', self.OnCloseWindow))),
            ('&Game', (
                ('&New Game', 'Make New Game', self.OnNewGame),
                ('&Clear All', 'Clear Hex Map', self.OnClearMap),
                ('&Rotate Map', 'Rotate Hex Map', self.OnRotateMap),
                ('&Flash Border', 'Flash Cursor or Border', self.OnHexFill, wx.ITEM_CHECK),
                ('', '', '', wx.ITEM_SEPARATOR),
                ('&Toggle CP Off', 'Set CP On', self.OnToggleCP, wx.ITEM_CHECK),
                ('', '', '', wx.ITEM_SEPARATOR),
                ('&Small Hexes', 'Small Hexes', self.OnHexSize, wx.ITEM_RADIO),
                ('&Large Hexes', 'Large Hexes', self.OnHexSize, wx.ITEM_RADIO)
                )
            ) # end of Game
        ) # end of entire menu_list

        return menu_list
#pylint: disable-msg=W0613
class SliderDialog(wx.Dialog):
    ''' Enter the number of columns/rows in a map, using slider widgets. '''
    def __init__(self, parent, ID, title, \
                 pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):
        wx.Dialog.__init__(self, parent, ID, title, size=(400, 400))
        self.SetBackgroundColour('light steel blue')
        okButton = wx.Button(self, wx.ID_OK, 'OK', pos=(50, 340))
        okButton.SetDefault()
        cancelButton = wx.Button(self, wx.ID_CANCEL, 'Cancel', pos=(150, 340))
        self.rowSlider = wx.Slider(self, -1, 1, 1, 30, pos=(10, 5), size=(-1, 300), \
            style=wx.SL_VERTICAL | wx.SL_AUTOTICKS | wx.SL_LABELS | wx.SL_RIGHT)
        self.rowSlider.SetTickFreq(1)
        self.colSlider = wx.Slider(self, -1, 1, 1, 30, pos=(90, 260), size=(300, -1), \
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS | wx.SL_TOP)
        self.colSlider.SetTickFreq(1)

    def isName(self):
        ''' isname function '''
        return self.title
    
    def isTitle(self):
        ''' istitle function '''
        return self.title

########################################################################
class cApp(wx.App):  #pylint: disable-msg=C0103
    ''' this is the Controller part of the MVC model. The App component
        of wxPython runs an application loop that handles events. '''
    def __init__(self):
##        wx.App.__init__(self, redirect=True, filename='errlog.txt')
        wx.App.__init__(self) # toggle these lines for error logging.
        self.topFrame = None

    def OnInit(self):
        ''' Initialize the application. '''
        self.topFrame = topFrame(None, MAP_TITLE)
        self.SetTopWindow(self.topFrame)
        self.topFrame.Show()
        return True

    def isName(self):
        ''' isname function '''
        return self.title
    
    def isTitle(self):
        ''' istitle function '''
        return self.title

def main():
    ''' main function. '''
    my_app = cApp()
    my_app.MainLoop()

if __name__ == '__main__':
    main()
