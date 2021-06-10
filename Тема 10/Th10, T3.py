# =============================================================================
# TV controller
# 
# Create a simple prototype of a TV controller in Python. It’ll use the following 
# commands:
# 
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() -‎ вмикає попередній канал‎. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# ‎is_exist(N/'name') - отримує 1 аргумент - число N або рядок 'name' і повертає "Так", якщо канал N або 'name' існує в списку, або "Ні" - в іншому випадку.‎
#  
# 
# The default channel turned on before all commands is №1.
# 
# Your task is to create the TVController class and methods described above.
# 
# ```
# 
# CHANNELS = ["BBC", "Discovery", "TV1000"]
# 
#  class TVController:
# 
# pass
# 
#  controller = TVController(CHANNELS)
# 
# controller.first_channel() == "BBC"
# 
# controller.last_channel() == "TV1000"
# 
# controller.turn_channel(1) == "BBC"
# 
# controller.next_channel() == "Discovery"
# 
# controller.previous_channel() == "BBC"
# 
# controller.current_channel() == "BBC"
# 
# controller.is_exist(4) == "No"
# 
# controller.is_exist("BBC") == "Yes"
# 
# =============================================================================

def current_numb_ch(N):
    TVController.N = N

def check_number_ch(N):
    if N > len(CHANNELS):
        N -= (len(CHANNELS)-1)
        TVController.N = N
    elif N < 1:
        while N not in range(1, len(CHANNELS)+1):
            N += len(CHANNELS)
        else: TVController.N = N
    else: TVController.N = N 

class TVController():
    N = 1   
    
    def __init__(self, list):
        self.list = list
    
    
    def first_channel(self):
        N = 1
        current_numb_ch(N)
        channel = self.list[0]
        print(channel)
    
    def last_channel(self):
        N = len(self.list)
        current_numb_ch(N)
        channel = self.list[-1]
        print(channel)
        
    def turn_channel(self, N):
        current_numb_ch(N)
        channel = self.list[N-1]
        print(channel)

    def next_channel(self):
        N = TVController.N+1
        check_number_ch(N)        
        channel = self.list[TVController.N-1]
        print(channel)
    
    def previous_channel(self):
        N = TVController.N-1
        check_number_ch(N)
        channel = self.list[TVController.N-1]
        print(channel)

    def current_channel(self):
        channel = self.list[TVController.N-1]
        print(channel)
    
    def is_exist(self, *args):
        for arg in args:
            if type(arg) == int:
                N = arg
                if N in range(1, len(self.list)+1):
                    print('Даний номер каналу є.')
                else:
                    print('Даного номера каналу немає.')
            elif type(arg) == str:
                name = arg
                if name in self.list:
                    print('Даний канал є.')
                else:
                    print('Даного каналу немає.')


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(4)
controller.is_exist("BBC")
        
    
        
        

