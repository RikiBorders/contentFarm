from YoutubeDLClient import YoutubeDLClient

class ContentFarm():

    def __init__(self):
        self.youtubeClient = YoutubeDLClient(preferredcodec='mp4')
        self.uploadIntervalInSeconds = 60

if __name__ == '__main__':
    ContentFarm()