class Logger():
    def __init__(self, log_file):
        #TODO: Upload log files to a particular location at a regular interval
        self.log_file = log_file
        print(f'Logger started with "{self.log_file}" log file')

    def log(self, message):
        print(message)

    def logError(self, message):
        print(message)

    def uploadLog(self):
        #TODO: upload logs
        print('fooBar')