'''
    sample game class
'''


class Game:
    '''
        game glass
    '''

    def __init__(self):
        '''
            init
        '''
        self.running = True

    def mainloop(self):
        '''
            main loop
        '''
        print("Starting")
        print("Finished")

    def game_running(self):
        '''
            is it running
        '''
        return self.running


if __name__ == '__main__':
    game = Game()
    game.mainloop()cd code
