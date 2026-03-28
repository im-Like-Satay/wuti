from wuti.ai import call_ai
from wuti.parser import parse_log


def main():
    try:
        error = parse_log()
        if error is None:
            return
        result = call_ai(error)

        print(result)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
