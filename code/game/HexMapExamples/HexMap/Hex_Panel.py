''' Module: Hex_Panel.py              2/16/2009
    Based on book: "wxPython in Action"

    Builds a Color Panel, which is currently an array of buttons. This is
    mainly as a experiment, to work out the bugs in having two panels
    side-by-side in the main window. Based on code from the book,
    "wxPython in Action" - you should run right out and buy a copy...'''
# pylint: disable-msg=import-error
import wx
from wx.lib import buttons

class ColorPanel(wx.Panel):
    ''' A panel containing a grid of color buttons.'''
    BMP_SIZE, BMP_BORDER = 16, 3
    NUM_COLS, SPACING = 1, 4
    colorList = ('Light Grey', 'Yellow', 'Goldenrod', 'gold', 'Orange',
            'Blue', 'Purple', 'Light Blue', 'Cyan', 'Light Steel Blue',
            'Cadet Blue', 'Aquamarine', 'pale green', 'Green', 'Forest Green')

    def __init__(self, parent, topFrame):
        wx.Panel.__init__(self, parent, -1, style=wx.RAISED_BORDER)
        self.topFrame = topFrame
        buttonSize = (self.BMP_SIZE + 2 * self.BMP_BORDER,
                      self.BMP_SIZE + 2 * self.BMP_BORDER)
        colorGrid = self.createColorGrid(parent, buttonSize)
        self.layout(colorGrid)

    def createColorGrid(self, parent, buttonSize):  #pylint: disable-msg=W0613
        ''' Creates a grid of color buttons.'''
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
        for eachColor in self.colorList:
            bmp = self.MakeBitmap(eachColor)
            bt = buttons.GenBitmapToggleButton(self, -1, bmp, size=buttonSize)
            bt.SetBezelWidth(1)
            bt.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetColor, bt)
            colorGrid.Add(bt, 0)
            self.colorMap[bt.GetId()] = eachColor
            self.colorButtons[eachColor] = bt
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid

    def layout(self, colorGrid):
        ''' Lays out the color buttons.'''
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(colorGrid, 0, wx.ALL, self.SPACING)
        self.SetSizer(box)
        box.Fit(self)

    def MakeBitmap(self, color):
        ''' Creates a bitmap of the given color.'''
        bmp = wx.Bitmap(16, 15)
        dc = wx.MemoryDC(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

    def OnSetColor(self, event):
        ''' Sets the color of the current pen.'''
        color = self.colorMap[event.GetId()]
        for bt in self.colorButtons.items():
            bt[1].SetValue(False)
        self.colorButtons[color].SetValue(True)
        self.topFrame.NewCPColor(color)
