import yt_dlp as ytdl

from Logger import Logger
from Exceptions import BatchDownloadLimitExceededException

class YoutubeDLClient():
    def __init__(self):
        self.config = {
            'batchDownloadLimit': 3
        }
        self.youtubedlOptions = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        self.logger = Logger('dummyLoggerFilePath')
        
        self.logger.log('YoutubeDL Client started')

    def downloadWithUrl(self, url: str, withMetaData: bool=False):
        '''
        Raises: ytdl.DownloadError: failed to download from url
        '''
        # Download videos in .mp4 format
        try:
            with ytdl.YoutubeDL(self.youtubedlOptions) as youtubedl:
                if withMetaData:
                    return youtubedl.extract_info(url, download=False)
                else:
                    return youtubedl.download(url)
                    
        except Exception as exception:
            self.logger.logError(f'Caught an exception when downloading URL: {url}. Exception: {exception}')
        
    def downloadUrls(self, urls: list, withMetaData: bool=False):
        '''
        Raises: BatchDownloadLimitExceededException: if number of urls exceed the batch download limit
        '''
        print(urls)
        if len(urls) > self.config['batchDownloadLimit']:
            raise BatchDownloadLimitExceededException(self.config['batchDownloadLimit'], len(urls))
        
        downloads: list[dict] = []

        for url in urls:
            downloads.append(self.downloadWithUrl(url, withMetaData))
        
        return downloads