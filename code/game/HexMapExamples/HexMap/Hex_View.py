''' Module: Hex_View.py           2/16/2009
    Author: John Crawford

    Contains the View component of the MVC pattern, more or less...
    I'm declaring the mapView window to be my basic View, but there are
    certainly display elements in the topFrame.

    Development Notes:
    Evolution of the DrawHex() function:
        Originally - hexes were not filled, and I used:
        dc.DrawLines(hex.point_list, hex.x_offset, hex.y_offset)
        to draw an empty hex. Then I added a filled Bitmap version of
        the hex, and drew it with dc.Blit() if the hex was intended
        to display as filled, or the Drawlines() if empty. Then I had
        to add code to draw a border (for Flashing) around a filled
        hex, and things got chaotic... The final design uses *only*
        Bitmaps for each possible hex state: filled/unfilled, active/
        inactive, flashed/unflashed, with the bitmaps being recreated
        each time there is a global change, such as the Active Color
        being changed. Possibly inefficient to keep rebuilding lots
        of different bitmaps, but cleaner and easier to manage here on
        the drawing side...
    The vHexGroup.SetActiveColor():
        Originally I called hex.SetupBitmaps() there, which remakes
        *all* of the bitmaps. However, that was noticeably slow,
        so I then changed to only make the two bitmaps that changed. Still
        wasn't instant, but much faster. Then, I remembered reading about
        the Memoization pattern: http://en.wikipedia.org/wiki/Memoization
        This was exactly what I needed. If the map has lots of active hexes,
        creating identical bitmaps for *all* of them is a massive waste of
        time. By adding a bitmap dictionary to the vHex Class, I only had
        to create *one* of each type of bitmap, and rebuilding the map is
        now instant, I say, *instant*!
        There is still some waste of memory, lots of identical bitmaps are
        stored (in the vHex object, not the Memo), but I'm currently
        less concerned about that (the bitmaps are small), than I was the
        slow response time to rebuilding a map. I may eventually recode it.
        [time passes] On further consideration, I *do* want every hex to have
        its own bitmap - although hexes are currently identical, my long-term
        plan is to make it a wargame map, so all the hexes would have their
        own distinct bitmap.
    The vHex.activeBitmap and other bitmaps:
        I started by having a vHex with several instance variables, all
        named *Bitmap. Also, I had several Boolean status variables, such as
        vHex.active, vHex.filled, etc. This made the function SetCurrentBitmap()
        start to get fairly involved, with lots of if/else lines to determine
        the hex status and which bitmap correctly mapped to that status.
        Then I realized that the bitmaps could be stored in a dictionary.
        So I considered how to build a key from the various status variables,
        and realized that if the *status* was stored in a single string
        (or possibly multiple strings), then I could build the key in one
        line of code.
    Properties - are cool, so I tried setting hex.currentBitmap to a
        property. That would mean I could delete all the calls to
        hex.SetCurrentBitmap(), since any time something access the current
        bitmap, it would be assigned the correct one. However, it slowed
        down the program drastically, once again taking several seconds to
        display a changed map. Oh well...
    Booleans:
        One thing that I have discovered, not sure how correct it is,
        but it seems that using Boolean variables is sometimes a bad idea,
        or at least suboptimal in some situations. Given how powerful
        Python dictionaries are, using strings instead of booleans,
        can make building dict keys much easier. Plus it's simply much
        *clearer* what you're referencing in the dictionary.
    Old Bugs:
        Great.. my first Heisenbug... my new bitmap handling code wasn't
        working with flashed hexes, so I put in a print statement - and
        it started working. Upon closer inspection, however, my print
        statement (which was supposed to print out the bitmap dictionary)
        was syntactically *wrong*. So the function was stopping at that
        point, which gave me a clue as to what was actually messing up.
        It actually turned out that I was setting hex.filled in the
        BuildHex() function, instead of the hex.init() function. Wups.
    Sliced Lists:
        So I was having every hex remove itself from vHexGroup.active_group,
        and it wasn't working right... Specifically:
            for hex in self.active_group:
                hex.SetInactive()
        and:
            self.parent.active_group.remove(self) (where self is hex)
        Now, I actually remember *reading* about problems
        sequentially removing items from a list, but I guess some
        things you just have to experience for yourself...
        Fortunately, using a sliced List, copies it - active_group[:]
        works nicely.
    Design question - who should tell the Game Model that a hex is active?
        My first thought is, the vHex itself, when it gets set active,
        should tell the Game Model. My second thought, is that the MapView
        function OnLeftMbDown(), which is the first point where a hex is
        set active, should do something different. Currently, it tells the
        vHex to activate itself. But I'm wondering, if instead, it should
        tell the Game Model *only*. And any time the vHex needs to know if
        it is active, query the Game Hex, rather than its own instance
        variable...
        I note in general, I have no communication between the Game hex,
        and the View vHex, or even a link. Maybe vHex should have a link
        back to the Game hex? Where should the linkages be, between the
        Model and the View?
    Current Bugs:
        If I switch windows/minimize, or something else I haven't figured
        out - I have had the mapView window permanently lose Focus, and
        thereby unable to receive keyboard events. No clue why.
        Running out of Device Contexts: I think this bug is fixed, but
        not entirely sure. Originally, after roughly 3 minutes of drawing
        hexes, the program crashed with an AssertionError on creating a
        new Device Context (DC). Although as far as I can tell, a DC is
        supposed to be destroyed when the variable goes out of scope, it
        didn't seem to be happening. At least, when I put in a 'del dc'
        statement, I haven't had the program crash since.
    '''
# pylint: disable-msg=import-error
import wx
from Hex_Game import ACROSS
from Hex_Math import ShortestDist, ComputeHexPoints

if __name__ == '__main__':
    print('Hex_View: starting Hex_Main')
    from Hex_Main import * #pylint: disable=W0401
    main()

HEX_SMALL = 41
HEX_LARGE = 53
HEX_DIAM = HEX_SMALL # default size

# images free for non-commercial use from http://www.oneodddude.net/
PIC1 = 'pic1.jpg'
PIC2 = 'pic2.jpg'
PIC3 = 'pic3.jpg'
def next_pic(x):
    ''' a generator function for cycling through background pictures,
        just to play around with generators... '''
    pic_list = (PIC1, PIC2, PIC3)
    while True:
        yield pic_list[x]
        x = x + 1 if x < len(pic_list) - 1 else 0
newpic = next_pic(0)

# keys that scroll the map around.
SCROLL_SML, SCROLL_BIG = 5, 50
thumb_dict = {wx.WXK_LEFT : (wx.HORIZONTAL, -SCROLL_SML, -SCROLL_BIG),
            wx.WXK_RIGHT : (wx.HORIZONTAL, SCROLL_SML, SCROLL_BIG),
            wx.WXK_UP : (wx.VERTICAL, -SCROLL_SML, -SCROLL_BIG),
            wx.WXK_DOWN : (wx.VERTICAL, SCROLL_SML, SCROLL_BIG),
            wx.WXK_PAGEUP : (wx.VERTICAL, -SCROLL_BIG, -SCROLL_BIG),
            wx.WXK_PAGEDOWN : (wx.VERTICAL, SCROLL_BIG, SCROLL_BIG),
            wx.WXK_HOME : (wx.HORIZONTAL, -SCROLL_BIG, -SCROLL_BIG),
            wx.WXK_END : (wx.HORIZONTAL, SCROLL_BIG, SCROLL_BIG), }

#####################################################
class mapView(wx.ScrolledWindow):  #pylint: disable-msg=C0103
    ''' Builds three bitmap objects:
        mapBackground - original image from file, used to erase window.
        mapBuffer - where the hex map is drawn, in-memory.
        mapVisible - the actual on-screen bitmap, only one that is visible.
        Also builds a list of vHexes, which contain the point coordinates
        needed to draw a hex map, based on information from the hex list
        returned by the Game Model object.'''
    def __init__(self, parent, statusBar):
        wx.ScrolledWindow.__init__(self, parent, wx.ID_ANY, size=(900, 700), style=wx.HSCROLL | wx.VSCROLL)
        self.Status = statusBar # passed in from topFrame.
        self.gameModel = None # link back to the game Model object.
        self.hex_group = None # list of viewHexes.

        ''' Originally I used a single flash_hex to hold the current hex being
            flashed - then when the mouse moved over a new hex, cleared the
            current flash_hex and set it to the new hex.
            However, if I moved the mouse fast enough, multiple hexes
            could be flashed without being unflashed, leaving a chain of
            hexes improperly flashed, so I made a list, which gets cleared
            every time a new hex (or no hex) is mouse-moved over.
            Then, I realized that the list really should be part of the class
            vHexGroup itself, so I moved it down there... '''
        pic = next(newpic)
        self.mapBackground = wx.Image(pic, type=wx.BITMAP_TYPE_JPEG)
        width = self.mapBackground.GetWidth()
        height = self.mapBackground.GetHeight()
        self.mapBuffer = wx.Bitmap(width, height)
        self.mapVisible = wx.StaticBitmap(self, \
                bitmap = wx.Bitmap(width, height),\
                style = wx.RAISED_BORDER)
        self.SetScrollbars(1, 1, width, height)
        self.EraseHexMap()
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.mapVisible.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.mapVisible.Bind(wx.EVT_LEFT_DOWN, self.OnLeftMbDown)

    def OnPaint(self, event):  #pylint: disable-msg=C0103
        ''' Creating a second DC for the top window is *required* to
            clear the OnPaint event, since the event is generated by
            that window. Otherwise, hello Infinite Loop... '''
        try:
            dc = wx.BufferedPaintDC(self)
            del dc
            dc2 = wx.PaintDC(self)
            del dc2
        except AssertionError:
            print(f' Problems opening DC. Should not happen...{event}')

    def OnMouseMove(self, event):
        ''' As mouse is moved over the map:
                Flash any hexes the mouse passes over.
                De-flash any hex when the mouse leaves it.
                Set as Active any hexes that mouse is Dragged over. '''
        event.Skip()
        pt = event.GetPosition()
        self.Status.SetStatusText(f'Mouse Coords = {str(pt)}', 1)
        new_hex = self.GetValidHex(pt)
        # case 1: mouse has been moved OFF of any hexes, so clear flash.
        if not new_hex:
            if self.hex_group:
                self.hex_group.DeFlashHexes()
            return
        # case 2: mouse is being dragged, AND there is a valid hex under mouse.
        # make selected hexes active, not flashed.
        if event.Dragging():
            new_hex.SetNewColor()
            return
        # case 3: mouse has been moved onto a valid hex, so flash it.
        self.hex_group.DeFlashHexes()
        new_hex.SetFlash()

    def OnLeftMbDown(self, event):
        ''' Change the color of any hex that is left-clicked.
            Originally I made this on mouse-UP, but combined with the
            mouse-dragging function, it was a bit glitchy, wouldn't
            activate the last hex in the mouse-drag. '''
        event.Skip()
        pt = event.GetPosition()
        onldhex = self.GetValidHex(pt)
        if not onldhex:
            return
        hex.SetNewColor()
        msg = f'Hex col/row = [{onldhex.col}][{onldhex.row}]'
        self.Status.SetStatusText(msg, 0)
        self.Refresh()

    def GetValidHex(self, pt):
        ''' Returns a valid hex object, or None if no hex is found.'''
        if self.hex_group:
            return self.hex_group.FindHex(pt[0], pt[1])
        return None

    def DrawHex(self, dhhex, text=False): # Needs Work!
        ''' See Developer notes.'''
        try:
            dc = wx.MemoryDC(self.mapBuffer)
            dc2 = wx.MemoryDC(hex.currentBitmap)
            dc.Blit(dhhex.x_offset, dhhex.y_offset, dhhex.width, dhhex.height,\
                dc2, 0, 0, useMask=True)
            del dc
            del dc2
            if text:
                print("Text not implemented yet.")
        except AssertionError:
            print('Problems opening DC. Should not happen...')

        #if text: # refactor
            #dc.SetTextForeground('white')
            #coords = '%d/%d' % (hex.col, hex.row)
            #dc.DrawText(coords, hex.x_offset + 10, hex.y_offset + 10)
        self.Refresh()

    def DrawHexMap(self):
        ''' Draw the entire hex map.'''
        self.EraseHexMap()
        if self.hex_group:
            for dhmhex in self.hex_group:
                hex.parent.draw_f(dhmhex, True)

    def BuildNewMap(self, game=None):
        ''' Build a new hex map, using the gameModel passed in.'''
        if game:
            self.gameModel = game
        self.hex_group = vHexGroup(self.gameModel, HEX_DIAM, self.DrawHex)
        self.DrawHexMap()

    def EraseHexMap(self):
        ''' Erase the entire hex map.'''
        tmp = wx.Bitmap(self.mapBackground)
        width, height = tmp.GetWidth(), tmp.GetHeight()
        try:
            dc = wx.MemoryDC(tmp)
            dc2 = wx.MemoryDC(self.mapBuffer)
            dc2.Blit(0, 0, width, height, dc, 0, 0)
            del dc
            del dc2
        except AssertionError:
            print('Problems opening DC. Should not happen...')
        self.Refresh()

    def MoveMapView(self, key, shift=False):
        ''' move the scrolling window and the scrollbar thumbs in parallel,
            either small or large increments, if shift key is down. '''
        old_x = self.GetScrollPos(wx.HORIZONTAL)
        old_y = self.GetScrollPos(wx.VERTICAL)

        thumbdir = thumb_dict[key][0] # determines if Horizontal or Vertical.
        newpos = thumb_dict[key][1] if not shift else thumb_dict[key][2]

        new_x = newpos if thumbdir == wx.HORIZONTAL else 0
        new_y = newpos if thumbdir == wx.VERTICAL else 0

        self.Scroll(old_x + new_x, old_y + new_y)

    def ChangeBackground(self):
        ''' Change the background image of the map.'''
        pic = next(newpic)
        self.mapBackground = wx.Image(pic)
        self.DrawHexMap()

    def RotateMap(self):
        ''' Rotate the map 60 degrees.'''
        if self.hex_group:
            self.hex_group.BuildHexes()
            self.DrawHexMap()

    def ClearActiveColors(self):
        ''' Reset all hexes to their original colors.'''
        if self.hex_group:
            self.hex_group.ResetHexColors()

    def ChangeActiveColor(self, color):
        ''' Change the color of all active hexes.'''
        if self.hex_group:
            self.hex_group.activeColor = color

    def ChangeHexFill(self, fill):
        ''' Change the fill of all hexes.'''
        if self.hex_group:
            self.hex_group.SetHexFill(fill)
            self.DrawHexMap()

    def ChangeHexSize(self, size):
        ''' Change the size of all hexes.'''
        if self.hex_group:
            diam = HEX_SMALL if size == 'small' else HEX_LARGE
            self.hex_group.SetHexSize(diam)
            self.DrawHexMap()

#################################################################
STANDARD_COLOR = 'light grey'
FLASH_COLOR = 'red'

class vHexGroup(list):  # pylint: disable=C0103
    ''' Composed of a list of viewHexes. The vHexes have three sets of
        information:
        Col/Row - from Game Model, won't change for life of vHexGroup
        Width/Height - same for every vHex, can be changed for group.
        Filled - currently same for every vHex, I might alter this.
        Active, Flashed - may be different for each vHex.
        Also contains some sublists, of hexes with the properties that
        can vary per hex, such as active/flashed.
        Hexes can add themselves to the subgroups, or be added.  They
        are only cleared by the HexGroup object, as a group. '''
    def __init__(self, game, hex_diameter, draw_f):
        ''' not entirely sure this class should have a Drawing function
            here, may change it. [time passes...] After much thought
            and code, the function stays here - there are many times
            where I want a  single vHex to draw itself, so it's very
            convenient being here...'''
        self.draw_f = draw_f # drawing function in parent window mapView
        self.gameModel = game
        self.cols = game.cols
        self.rows = game.rows
        self.hex_d = hex_diameter
        self.hex_filled = False
        self.activeColor = STANDARD_COLOR
        self.flash_group = []
        for inithex in game.hex_list: # build a list of empty vHexes.
            self.append(vHex(self, inithex))
        self.BuildHexes()

    def BuildHexes(self):
        ''' Sets up all the visual elements for displaying a hex, such
            as size, direction, color, filled. '''
        self.dir = self.gameModel.hex_dir
        width = self.hex_d * .93 if self.dir == ACROSS else self.hex_d
        height = self.hex_d if self.dir == ACROSS else self.hex_d * .93
        self.x_gap = 1 if self.dir == ACROSS else 2
        self.y_gap = 2 if self.dir == ACROSS else 1
        for bhhex in self:
            bhhex.SetupCoords(self.dir, width, height, self.x_gap, self.y_gap)
            bhhex.SetupBitmaps()

    def ResetHexColors(self):
        ''' Reset all hexes to their original colors.'''
        self.activeColor = STANDARD_COLOR
        for rhchex in self:
            rhchex.color = STANDARD_COLOR
            rhchex.SetupBitmaps()
            self.draw_f(rhchex)

    def DeFlashHexes(self):
        ''' Remove all hexes from the flash group.'''
        for dfhhex in self.flash_group[:]:
            dfhhex.SetNonFlash()

    def SetHexSize(self, size):
        ''' Change the size of all hexes.'''
        self.hex_d = size
        self.BuildHexes()

    def SetHexFill(self, fill):
        ''' Change the fill of all hexes.'''
        self.hex_filled = fill
        stat = 'filled' if fill else 'empty'
        for shfhex in self:
            shfhex.FillStatus = stat

    def FindHex(self, m_x, m_y):
        ''' I thought that locating the hex where the mouse is over/clicked
        was going to be much harder. However, one of the benefits of making
        the map window a Scrollable window - the mouse event position is
        relative to the entire window/bitmap, even if it's scrolled. So I
        don't need to take into account where the scrollbars are, and I have
        the actual pixel on the bitmap where the mouse is.
        Note: because hexes are offset, there can be up to two (but no more)
        hexes that the IsInRect() function might be true for, so I only
        have to check at most two hexes in the entire list, to find the
        correct one. '''

        close_hex = None
        for cur_hex in self: # wow... I'm a... LIST...
            if cur_hex.IsInRect(m_x, m_y):
                cur_dist = ShortestDist(cur_hex.GetRect(), (m_x, m_y))
                if close_hex is None:
                    close_hex = cur_hex
                else:
                    close_dist = ShortestDist(close_hex.GetRect(), (m_x, m_y))
                    if close_dist < cur_dist:
                        return cur_hex
        return close_hex

class vHex():  # pylint: disable=C0103
    ''' Aka viewHex - this is a semi-Sprite type object, which keeps the
        coordinate information about the on-screen hexes, to simplify
        finding which hex is mouse-touched.  A hex is Flashed when the
        mouse moves over it, changing either color or border. '''

    bmp_dict = {} # take a Memo. See Notes. A Class attribute, not instance.

    def __init__(self, parent, ghhex):
        self.parent = parent
        self.gameHex = ghhex # link back to Game Model hex
        self.col, self.row = ghhex.col, ghhex.row
        self.color = STANDARD_COLOR
        self.FillStatus = 'empty'       # or 'filled'
        self.FlashStatus = 'nonflashed' # or 'flashed
        self.bitmap_dict = {'standard': None}
        self.currentBitmap = None
        self.x_offset = 0
        self.y_offset = 0
        self.width = 0
        self.height = 0
        self.point_list = []
        self.border_list = []
        self.filled = False

    def SetupCoords(self, scdir, width, height, x_gap, y_gap):
        ''' Sets up the coordinates for the hex, based on the direction'''
        if dir == ACROSS:
            self.x_offset = self.col * (width + x_gap) + \
                            (width/2) * (self.row % 2)
            self.y_offset = self.row * (height + y_gap) * .75
        else:
            self.x_offset = self.col * (width + x_gap) * .75
            self.y_offset = self.row * (height + y_gap) + \
                            (height/2) * (self.col %2)
        self.width, self.height = width, height
        self.point_list = ComputeHexPoints(width, height, scdir, True)
        self.border_list = ComputeHexPoints(width, height, scdir, True, True)
        self.filled = self.parent.hex_filled

    def SetupBitmaps(self):
        ''' Sets up the bitmaps for the hex, based on the color and fill'''
        self.bitmap_dict['standard'] = self.MakeBitmap(self.color, self.color)
        self.bitmap_dict['flashed_border'] = self.MakeBitmap(self.color, FLASH_COLOR, True)
        self.bitmap_dict['flashed_fill'] = self.MakeBitmap(FLASH_COLOR, FLASH_COLOR)
        self.SetCurrentBitmap()

    def SetCurrentBitmap(self):
        ''' Sets the current bitmap, based on the fill and flash status'''
        if self.FlashStatus == 'nonflashed':
            self.currentBitmap = self.bitmap_dict['standard']
        elif self.FillStatus == 'empty':
            self.currentBitmap = self.bitmap_dict['flashed_border']
        else:
            self.currentBitmap = self.bitmap_dict['flashed_fill']

    def MakeBitmap(self, fill_color, border_color, border=False):
        ''' the full key consists of everything that makes a bitmap unique.
            Uses a Memo for speed, see Notes. '''
        size_k = self.parent.hex_d
        dir_k = self.parent.dir
        full_key = f'{size_k}_{dir_k}_{fill_color}_{border_color}'
        if full_key in vHex.bmp_dict:
            return vHex.bmp_dict[full_key] # Yes! instant gratification.

        bmp = wx.Bitmap(self.width, self.height)
        try:
            dc = wx.MemoryDC(bmp)
            dc.SetBackground(wx.Brush('Black'))
            dc.Clear()
            dc.SetBrush(wx.Brush(fill_color))
            # need to also set Pen before DrawPolygon - turns out that DrawPolygon
            # does *not* draw a border, the hex is actually one pixel smaller
            # than expected otherwise.
            dc.SetPen(wx.Pen(fill_color, 0))
            dc.DrawPolygon(self.point_list, 0, 0) # fill the hex
            if border:
                dc.SetPen(wx.Pen(border_color, 3))
                dc.DrawLines(self.border_list, 0, 0) # put border around hex
            del dc
            bmp.SetMaskColour('Black')
        except AssertionError:
            print('Problems opening DC. Should not happen...')

        vHex.bmp_dict[full_key] = bmp # add to Memo
        return bmp

    def SetNewColor(self):
        ''' Sets the color of the hex, and tells the Game Model hex the new'''
        self.color = self.parent.activeColor
        self.gameHex.color = self.color # tell Game Model hex the new color.
        self.SetupBitmaps()
        self.parent.draw_f(self)

    def SetFlash(self):
        ''' Sets the hex to Flash status, and adds it to the flash group.'''
        self.FlashStatus = 'flashed'
        self.SetCurrentBitmap()
        if not self in self.parent.flash_group:
            self.parent.flash_group.append(self)
        self.parent.draw_f(self)

    def SetNonFlash(self):
        ''' Sets the hex to non-Flash status, and removes it from the flash group.'''
        self.FlashStatus = 'nonflashed'
        self.SetCurrentBitmap()
        if self in self.parent.flash_group:
            self.parent.flash_group.remove(self)
        self.parent.draw_f(self)

    def IsInRect(self, x, y):
        ''' Returns True if the point (x,y) is in the hex's rectangle.'''
        if self.x_offset <= x <= self.x_offset + self.width:
            if self.y_offset <= y <= self.y_offset + self.height:
                return True
        return False

    def GetRect(self):
        ''' Returns the rectangle of the hex.'''
        topleft = (self.x_offset, self.y_offset)
        topright = (self.x_offset + self.width, self.y_offset)
        botleft = (self.x_offset, self.y_offset + self.height)
        botright = (self.x_offset + self.width, self.y_offset + self.height)
        return (topleft, topright, botleft, botright)
