from ai import call_ai
from parser import parse_log


def main():
    try:
        parseLog = parse_log()
        result = call_ai(parseLog)

        return result
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
