import pathlib

class LogAnalyzer:
    def isValid_log_filename(self, filename: str) -> bool:
        """file exist?
        
        NOTE: ofc, using os.path.exist() or pathlib.Path().exist
        but, be aware that its "filesystem". it may hurt u when u do unittest.
        """
        return pathlib.Path(filename).exists