class LogAnalyzer:
    wasLastFileNameValid: bool = False
    def __init__(self, log_filename: str) -> None:
        self.lfn = log_filename
    def isValid_log_filename(self) -> bool:
        if self.lfn is None or not self.lfn:
            raise ValueError('No filename provided!') 
        if self.lfn.lower().endswith('.slf'):
            self.wasLastFileNameValid = False
            return False
        self.wasLastFileNameValid = True
        return True