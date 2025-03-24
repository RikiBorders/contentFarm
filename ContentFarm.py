from YoutubeClient import YoutubeClient

class ContentFarm():

    def __init__(self):
        self.youtubeClient = YoutubeClient()
        self.uploadIntervalInSeconds = 60

        self.youtubeClient.downloadUrls()


if __name__ == '__main__':
    ContentFarm()