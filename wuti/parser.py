import re

from wuti.run_wsi import run_wsi


def parse_log():
    """fungsi ini untuk memparse log menggunakan regex"""

    logData = str(run_wsi())
    regexPattern = r"'^(?:.*?(?P<error_type>[A-Z][a-zA-Z0-9_]*(?:Error|Exception|Warning|Exit|Interrupt|Stop|NotFound|Failure))\s*:\s*(?P<error_msg>.*))$"

    try:
        resultParserLog = str(re.findall(regexPattern, logData))
        print(resultParserLog)
        return resultParserLog
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    parse_log()
