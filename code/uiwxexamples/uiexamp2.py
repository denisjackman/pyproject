'''ui example'''
# sample_three.py
# pylint: disable-msg=import-error
import wx


class MyFrame(wx.Frame):
    """
        wxframe class
    """
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        pnl = wx.Panel(self, -1)
        self.rb1 = wx.RadioButton(pnl,
                                  label='Button 1',
                                  pos=(30, 10))
        self.rb2 = wx.RadioButton(pnl,
                                  label='Button 2',
                                  pos=(30, 30))
        self.rb3 = wx.RadioButton(pnl,
                                  label='Button 3',
                                  pos=(30, 50))
        # set value for the second radio button as true(checked)
        self.rb2.SetValue(True)
        self.title = "Hello World"

    def isName(self):
        """
            isname function
        """
        return self.title

    def isTitle(self):
        """
            istitle function
        """
        return self.title


def main():
    """
        main function
    """
    app = wx.App()
    frame = MyFrame(None, title="Hello World")
    frame.Show()
    app.MainLoop()
    print(f"Title is : {frame.isName()}")


if __name__ == '__main__':
    main()
