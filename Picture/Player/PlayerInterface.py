import nsii
from mainPlayer import *

# Nsii setup
nsii = nsii.Nsii()

nsii.fps_target = 'max'
nsii.font = ('Consolas', (16, 8))

# mainPlayer setup
player = Player()


def resizeX(val):
    return int(val / 189 * nsii.size[0])


def resizeY(val):
    return int(val / 100 * nsii.size[1])


def isClicked(iPosX, iPosY, iSizeX=14, iSizeY=14):
    mPosX, mPosY = nsii.m_pos
    iSizeX = resizeX(iSizeX)
    iSizeY = resizeY(iSizeY)
    iPosX = resizeX(iPosX)
    iPosY = resizeY(iPosY)
    return iPosX <= mPosX < iPosX + iSizeX and iPosY <= mPosY < iPosY + iSizeY


class PlayerInterface:
    def __init__(self):
        self.menuState = 0
        self.pageId = 0
        self.musicList = player.musicList
        self.numPage = len(self.musicList) // 3
        self.numOfMusicsInLastPage = len(self.musicList) % 3
        self.isCreatingPlaylist = False
        self.CPName = ""  # Name of the playlist the user is creating

        """
        Possible states :
        0 - Music choice
        1 - Queue
        2 - Playlist
        """
        # Images
        # loop
        self.loopButtonOff = nsii.new_image('image/LoopOffButton.ppm')
        self.loopButtonOn = nsii.new_image('image/LoopOnButton.ppm')

        self.loopButton = self.loopButtonOff

        # Time indicator - red line on the time bar
        self.timeIndicator = nsii.new_image('image/TimeIndicator.ppm')

        # Playlist name giver window - Shows when the user wants to create a playlist
        self.playlistNameGiver = nsii.new_image('image/PlaylistNameGiver.ppm')

        # Pages / Tabs
        # Music Tab
        # tab 3 - 3 musics available
        self.musicTab3 = nsii.new_image('image/MusicPage3.ppm')
        # tab 2 - 2 musics available
        self.musicTab2 = nsii.new_image('image/MusicPage2.ppm')
        # tab 1 - 1 music available
        self.musicTab1 = nsii.new_image('image/MusicPage1.ppm')

        # Queue Tab
        # tab 3 - 3 musics available
        self.queueTab3 = nsii.new_image('image/QueuePage3.ppm')
        # tab 2 - 2 musics available
        self.queueTab2 = nsii.new_image('image/QueuePage2.ppm')
        # tab 1 - 1 music available
        self.queueTab1 = nsii.new_image('image/QueuePage1.ppm')
        # The queue is empty
        self.queueTab0 = nsii.new_image('image/QueuePage0.ppm')

        # Playlist Tab
        # tab 3 - 3 playlists available
        self.playlistTab3 = nsii.new_image('image/PlaylistPage3.ppm')
        # tab 2 - 2 playlists available
        self.playlistTab2 = nsii.new_image('image/PlaylistPage2.ppm')
        # tab 1 - 1 playlist available
        self.playlistTab1 = nsii.new_image('image/PlaylistPage1.ppm')
        # The playlist folder is empty
        self.playlistTab0 = nsii.new_image('image/PlaylistPage0.ppm')

    def showInterface(self):
        # Music Tab
        if self.menuState == 0:
            if self.pageId < self.numPage:  # 3 musics are available in this page
                self.musicTab3.size = nsii.size
                self.musicTab3.show()
            elif self.numOfMusicsInLastPage == 2:  # 2 musics are available in this page
                self.musicTab2.size = nsii.size
                self.musicTab2.show()
            else:  # 1 music is available in this page
                self.musicTab1.size = nsii.size
                self.musicTab1.show()

        # Queue Tab
        elif self.menuState == 1:
            if self.pageId < len(player.queue) // 3:  # 3 musics are available in this page
                self.queueTab3.size = nsii.size
                self.queueTab3.show()
            elif len(player.queue) % 3 == 2:  # 2 musics are available in this page
                self.queueTab2.size = nsii.size
                self.queueTab2.show()
            elif len(player.queue) % 3 == 1:  # 1 music is available in this page
                self.queueTab1.size = nsii.size
                self.queueTab1.show()
            else:  # The queue is empty
                self.queueTab0.size = nsii.size
                self.queueTab0.show()

        # Playlist tab
        else:
            if self.pageId < len(player.playlistsList) // 3:  # 3 playlists are available in this page
                self.playlistTab3.size = nsii.size
                self.playlistTab3.show()
            elif len(player.playlistsList) % 3 == 2:  # 2 playlists are available in this page
                self.playlistTab2.size = nsii.size
                self.playlistTab2.show()
            elif len(player.playlistsList) % 3 == 1:  # 1 playlist is available in this page
                self.playlistTab1.size = nsii.size
                self.playlistTab1.show()
            else:  # The playlist folder is empty
                self.playlistTab0.size = nsii.size
                self.playlistTab0.show()

        # Loop Button
        self.loopButton.pos = (resizeX(72), resizeY(81))
        self.loopButton.size = (resizeX(14), resizeY(14))
        self.loopButton.show()

        if player.soundDuration != 0:
            pos = 54 + int((player.soundTime / player.soundDuration) * 124)
            self.timeIndicator.pos = (resizeX(pos), resizeY(72))
        else:
            self.timeIndicator.pos = (resizeX(54), resizeY(72))
        self.timeIndicator.size = (1, resizeY(4))
        self.timeIndicator.show()

        if self.isCreatingPlaylist:
            self.playlistNameGiver.pos = (resizeX(47), resizeY(15))
            self.playlistNameGiver.size = (resizeX(110), resizeY(50))
            self.playlistNameGiver.show()

        nsii.draw()

    def buttonManagement(self):
        if nsii.m_click('right'):
            time.sleep(0.1)  # Protection against long mouse press
            if not nsii.m_click('right'):
                if self.isCreatingPlaylist:
                    if isClicked(81, 49, 13, 13):  # Cancel
                        self.isCreatingPlaylist = False
                    elif isClicked(111, 49, 13, 13):  # Validate
                        if self.CPName != "":
                            player.createPlaylist(self.CPName)
                            self.isCreatingPlaylist = False
                    elif isClicked(56, 38, 90, 8):  # Name modifier
                        self.CPName = nsii.input((resizeX(57), resizeY(39))).strip("\n")
                else:
                    # Player tab buttons
                    if isClicked(100, 81):  # Play button
                        player.play()

                    elif isClicked(118, 81):  # Stop button
                        player.stop()

                    elif isClicked(164, 81):  # Next music button
                        player.next()

                    elif isClicked(54, 81):  # Shuffle queue button
                        player.shuffleQueue()

                    elif isClicked(72, 81):  # Loop button
                        player.changeLoop()
                        if player.isLoop:
                            self.loopButton = self.loopButtonOn
                        else:
                            self.loopButton = self.loopButtonOff

                    # Pages buttons
                    elif isClicked(178, 5, 7, 7):  # Next page button
                        if self.menuState == 0:
                            if self.pageId < self.numPage:
                                self.pageId += 1

                        elif self.menuState == 1:
                            if self.pageId < len(player.queue) // 3:
                                self.pageId += 1

                        elif self.menuState == 2:
                            if self.pageId < len(player.playlistsList) // 3:
                                self.pageId += 1

                    elif isClicked(48, 5, 7, 7):  # Previous page button
                        if self.pageId != 0:
                            self.pageId -= 1

                    elif isClicked(169, 5, 7, 7):  # Add playlist button
                        if self.menuState == 2:
                            if player.queue:
                                self.CPName = ""
                                self.isCreatingPlaylist = True

                    elif isClicked(2, 26, 42, 23):  # Menu set to music tab
                        self.menuState = 0
                        self.pageId = 0

                    elif isClicked(2, 50, 42, 23):  # Menu set to queue tab
                        self.menuState = 1
                        self.pageId = 0

                    elif isClicked(2, 74, 42, 24):  # Menu set to playlist tab
                        self.menuState = 2
                        self.pageId = 0

                    # Tab 1 buttons
                    elif isClicked(158, 16, 12, 12):
                        if self.menuState == 0:  # Play button / Music menu
                            if self.pageId < self.numPage or self.numOfMusicsInLastPage >= 1:
                                player.insertMusic(1 + self.pageId * 3)
                                if player.isPlaying:
                                    player.next()
                                else:
                                    player.play()
                        elif self.menuState == 1:  # Play button / Queue menu
                            if self.pageId < len(player.queue) // 3 or len(player.queue) % 3 >= 1:
                                player.queue.insert(0, player.queue.pop(self.pageId * 3))
                                if player.isPlaying:
                                    player.next()
                                else:
                                    player.play()
                        else:
                            if self.pageId < len(player.playlistsList) // 3 or len(player.playlistsList) % 3 >= 1:
                                if player.isPlaying:
                                    player.stop()
                                player.getPlaylist(1 + self.pageId * 3)
                                player.play()

                    elif isClicked(172, 16, 12, 12):
                        if self.menuState == 0:  # Add music button / Music menu
                            if self.pageId < self.numPage or self.numOfMusicsInLastPage >= 1:
                                player.addMusic(1 + self.pageId * 3)
                        elif self.menuState == 1:
                            if self.pageId < len(player.queue) // 3 or len(player.queue) % 3 >= 1:
                                player.removeMusic(1 + self.pageId * 3)
                        else:
                            if self.pageId < len(player.playlistsList) // 3 or len(player.playlistsList) % 3 >= 1:
                                player.removePlaylist(1 + self.pageId * 3)

                    # Tab 2 buttons
                    elif isClicked(158, 34, 12, 12):
                        if self.menuState == 0:  # Play button / Music menu
                            if self.pageId < self.numPage or self.numOfMusicsInLastPage == 2:  # Test if the tab 2 is shown
                                player.insertMusic(2 + self.pageId * 3)
                                if player.isPlaying:
                                    player.next()
                                else:
                                    player.play()
                        elif self.menuState == 1:
                            if self.pageId < len(player.queue) // 3 or len(player.queue) % 3 == 2:
                                player.queue.insert(0, player.queue.pop(1 + self.pageId * 3))
                                if player.isPlaying:
                                    player.next()
                                else:
                                    player.play()
                        else:
                            if self.pageId < len(player.playlistsList) // 3 or len(player.playlistsList) % 3 == 2:
                                if player.isPlaying:
                                    player.stop()
                                player.getPlaylist(2 + self.pageId * 3)
                                player.play()

                    elif isClicked(172, 34, 12, 12):
                        if self.menuState == 0:  # Add music button / Music menu
                            if self.pageId < self.numPage or self.numOfMusicsInLastPage == 2:  # Test if the tab 2 is shown
                                player.addMusic(2 + self.pageId * 3)
                        elif self.menuState == 1:
                            if self.pageId < len(player.queue) // 3 or len(player.queue) % 3 == 2:
                                player.removeMusic(2 + self.pageId * 3)
                        else:
                            if self.pageId < len(player.playlistsList) // 3 or len(player.playlistsList) % 3 == 2:
                                player.removePlaylist(2 + self.pageId * 3)

                    # Tab 3 buttons
                    elif isClicked(158, 52, 12, 12):
                        if self.menuState == 0:  # Play button / Music menu
                            if self.pageId < self.numPage:  # Test if the tab 3 is shown
                                player.insertMusic(3 + self.pageId * 3)
                                if player.isPlaying:
                                    player.next()
                                else:
                                    player.play()
                        elif self.menuState == 1:
                            if self.pageId < len(player.queue) // 3:
                                player.queue.insert(0, player.queue.pop(2 + self.pageId * 3))
                                if player.isPlaying:
                                    player.next()
                                else:
                                    player.play()
                        else:
                            if self.pageId < len(player.playlistsList) // 3:
                                if player.isPlaying:
                                    player.stop()
                                player.getPlaylist(3 + self.pageId * 3)
                                player.play()

                    elif isClicked(172, 52, 12, 12):
                        if self.menuState == 0:  # Add music button / Music menu
                            if self.pageId < self.numPage:  # Test if the tab 3 is shown
                                player.addMusic(3 + self.pageId * 3)
                        elif self.menuState == 1:
                            if self.pageId < len(player.queue) // 3:
                                player.removeMusic(3 + self.pageId * 3)
                        else:
                            if self.pageId < len(player.playlistsList) // 3:
                                player.removePlaylist(3 + self.pageId * 3)


if __name__ == '__main__':
    p = PlayerInterface()
    while True:
        p.showInterface()
        p.buttonManagement()
        nsii.name = f"{player.queue}"
