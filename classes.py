class Television:
    MIN_ChANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.__CHANNEL = 0
        self.__VOLUME = 0
        self.__STATUS = False
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """

    def power(self):
        if self.__STATUS == False:
            self.__STATUS = True
        else:
            self.__STATUS = False
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """

    def channel_up(self):
        if self.__STATUS == True:
            if self.__CHANNEL == 3:
                self.__CHANNEL = 0
            else:
                self.__CHANNEL += 1
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """

    def channel_down(self):
        if self.__STATUS == True:
            if self.__CHANNEL == 0:
                self.__CHANNEL = 3
            else:
                self.__CHANNEL -= 1
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """

    def volume_up(self):
        if self.__STATUS == True:
            if self.__VOLUME == 2:
                pass
            else:
                self.__VOLUME += 1
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """

    def volume_down(self):
        if self.__STATUS == True:
            if self.__VOLUME == 0:
                pass
            else:
                self.__VOLUME -= 1
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """

    def __str__(self):
        return f"TV status: Is on = {self.__STATUS}, Channel = {self.__CHANNEL}, Volume = {self.__VOLUME}"
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """