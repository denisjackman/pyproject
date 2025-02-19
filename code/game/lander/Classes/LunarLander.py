'''
    lunarlander
'''


class LunarLander():
    '''
        Lunar lander object
    '''

    def __init__(self):
        self.altitude = 1000
        self.velocity = 0
        self.fuel = 100
        self.start = True

    def getVelocity(self):
        '''
            VELOCITY
        '''
        return self.velocity

    def getAltitude(self):
        '''
            ALTITUDE
        '''
        return self.altitude

    def getFuel(self):
        '''
            FUEL
        '''
        return self.fuel

    def thrust(self, fuel):
        '''
            THRUST
        '''
        if fuel > self.fuel:
            self.velocity -= fuel * 4
            self.fuel = 0
        self.velocity -= fuel * 4
        self.fuel -= fuel

    def tick(self, fuel):
        '''
            TICK
        '''
        self.thrust(fuel)
        self.velocity += 2
        self.altitude -= self .velocity
        # check for landing or crash
        if self.altitude <= 0 and self.velocity < 5:
            print('skrrttt~ Houston, we have '
                  'landed. ~skrrtt~ Victory! '
                  '\'Murica! Fuck yeah!')
            self.restart()
        elif self.altitude <= 0 and self.velocity > 4:
            print('Oh no, you crashed!')
            self.restart()

    def report(self):
        '''
            REPORT
        '''
        print(f'\nAlt = {self.getAltitude()}'
              f' Vel = {self.getVelocity()}'
              f' Fuel = {self.getFuel()}')

    def restart(self):
        '''
            restart
        '''
        self.start = False
        restart = input('Replay? Y/N >')
        if restart.lower() == 'y':
            self.start = True
