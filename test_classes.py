import pytest
from classes import *

class Test:
    def setup_method(self):
        self.tv = Television()
        
    def tearrdown_method(self):
        del self.tv
    
    def test__init(self):
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

    def test_power(self):
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
    
    def test_channel_up(self):
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0"
        
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 2, Volume = 0"
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
    
    def test_channel_down(self):
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
        
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 2, Volume = 0"
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0"
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
    def test_volume_up(self):
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
        
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
    def test_volume_down(self):
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        
    def test__str(self):
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"