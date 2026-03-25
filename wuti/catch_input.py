import argparse


def catch_wsi(inputData: str | None = None) -> str:
    """Fungsi ini untuk menangkap input user dan diteruskan ke fungsi `run_wsi'"""

    parser = argparse.ArgumentParser(description="Alat utilitas wsi canggih")
    parser.add_argument("command", type=str, help="Masukkan sebuah input")
    args = parser.parse_args()

    print(args.command)

    return args.command


if __name__ == "__main__":
    catch_wsi()
