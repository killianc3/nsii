# Sound
import contextlib
# General
import os
# Shuffle the queue
import random
# Threads
import threading
import time
# Sound duration
import wave
import winsound


class Player:
    def __init__(self):
        # Get filenames  & path from the music folder
        self.musicPath = os.path.abspath('./Player/music')
        self.musicList = os.listdir(self.musicPath)

        self.playlistsPath = os.path.abspath("./Player/playlists")
        self.playlistsList = os.listdir(self.playlistsPath)

        self.currentMusic = None

        # Loop the musics, (add the finished music at the end of the queue)
        self.isLoop = False
        self.isPlaying = False

        # User commands self.stop() & self.next()
        self.stopMusic = False
        self.nextMusic = False

        # Queue management
        self.queue = []
        self.player = None

        self.soundDuration = 0
        self.soundTime = 0

    # Queue Manager
    def queueManager(self):
        """Manage the queue, start the musics one by one"""
        while True:
            if not self.queue:
                break
            # Get the music path
            self.currentMusic = self.queue.pop(0)
            self.isPlaying = True

            # If the loop mode is activated, add the current music at the end of the queue
            if self.isLoop:
                self.queue.append(self.currentMusic)

            # Start the music
            winsound.PlaySound(self.currentMusic, winsound.SND_FILENAME + winsound.SND_ASYNC)

            # Start a timer equal to the music duration
            with contextlib.closing(wave.open(self.currentMusic, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
            self.soundDuration = int(duration) + 1

            # Wait until music finishes + self.stop() & self.next()
            for _time in range(self.soundDuration * 2):
                time.sleep(0.5)
                self.soundTime = _time // 2
                if self.stopMusic:
                    break
                if self.nextMusic:
                    self.nextMusic = False
                    break

            # If we called self.stop(), stop the queue
            if self.stopMusic:
                self.stopMusic = False
                break

            # Transition
            time.sleep(1)

        # When we self.stop(), we clear the current music
        winsound.PlaySound(None, winsound.SND_PURGE)
        self.soundDuration = 0
        self.soundTime = 0
        self.currentMusic = None
        self.isPlaying = False

    # Getters
    def getMusic(self, musicId):
        return self.musicList[musicId]

    def getAllInfos(self):
        print("\nInfos :")
        print("Current music : {}\nMusic duration : {}\n".format(self.currentMusic, self.soundDuration))
        print("Music list : {}".format(self.musicList))
        print("Queue list : {}".format(self.queue))
        print("\nLoop : {}".format(self.isLoop))
        print("MusicPath : {}".format(self.musicPath))
        print("PlaylistsPath : {}".format(self.playlistsPath))

    # User commands
    def stop(self):
        """Stop the queue"""
        if self.isPlaying:
            self.stopMusic = True

    def play(self):
        """Play the queue"""
        if not self.isPlaying:
            self.player = threading.Thread(target=self.queueManager)
            self.player.start()

    def next(self):
        """Play the next music in the queue"""
        if self.queue:
            self.nextMusic = True

    def changeLoop(self):
        """Add / Remove the play mode  -Loop- of the PlayModes list"""
        self.isLoop = not self.isLoop

    def addMusic(self, MusicId):
        """Add a music into the queue"""
        if self.musicPath + "\\" + self.getMusic(MusicId - 1) not in self.queue:
            self.queue.append(self.musicPath + "\\" + self.getMusic(MusicId - 1))

    def insertMusic(self, MusicId):
        """Insert a music into the queue"""
        self.queue.insert(0, self.musicPath + "\\" + self.getMusic(MusicId - 1))

    def removeMusic(self, userChoice):
        """Remove a music from the queue"""
        self.queue.pop(userChoice - 1)

    def shuffleQueue(self):
        """Shuffle the queue"""
        random.shuffle(self.queue)

    def createPlaylist(self, playlistName):
        """
        Create a file with all the musics in the queue, the file name is the name of the playlist
        :param playlistName: Name of the playlist
        """
        with open(self.playlistsPath + '/' + playlistName + '.txt', "w") as nPlaylist:
            if self.isPlaying:
                if not self.isLoop:
                    nPlaylist.write(self.currentMusic.strip(self.musicPath) + '\n')
            for music in self.queue:
                nPlaylist.write(music.strip(self.musicPath) + '\n')
        self.playlistsList.append(playlistName + '.txt')

    def getPlaylist(self, userChoice):
        """Add all the musics of the selected playlist into the queue"""
        with open(self.playlistsPath + '/' + self.playlistsList[userChoice - 1], 'r') as gPlaylist:
            musicList = gPlaylist.readlines()
            for music in musicList:
                self.queue.append(self.musicPath + "\\" + music.strip("\n"))

    def removePlaylist(self, userChoice):
        """ Delete the selected playlist file"""
        playlistName = self.playlistsList.pop(userChoice - 1)
        os.remove(os.path.join(self.playlistsPath, playlistName))
