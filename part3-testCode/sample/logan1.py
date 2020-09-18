class LogAnalyzer:
    def isValid_log_filename(self, filename: str) -> bool:
        """file exist?
        
        NOTE: injects "seams"
        """
        # return pathlib.Path(filename).exists
        fmgr = FileExtensionManager()
        return fmgr.isValid(filename)

class FileExtensionManager:
    def isValid(self, filename: str) -> bool:
        """
        wait a sec, i wanna know difference btwn FileNotFoundError and FileExsitsError
        
        oh, ez af

        link: https://docs.python.org/3/library/exceptions.html

        +-------------------+-----------------------------------------------------------------------+
        | exception         | explanation                                                           |
        +===================+=======================================================================+
        | FileExistsError   | raised when trying to create a file or directory which alrdy exists.  |
        +-------------------+-----------------------------------------------------------------------+
        | FileNotFoundError | raised when a file or directory is requested but doesn't exist.       |
        +-------------------+-----------------------------------------------------------------------+

        """
        try:
            with open(filename) as _:
                return True
        except:
            return False
