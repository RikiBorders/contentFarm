class BatchDownloadLimitExceededException(Exception):
    def __init__(self, batchDownloadLimit: int, requestedDownloads: int):
        self.message=f'Exceeded self-defined batch download limit of {batchDownloadLimit}. Number of requested downloads: {requestedDownloads}'
        super().__init__(self.message)