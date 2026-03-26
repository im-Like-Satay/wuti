import argparse as arg


def catch_wsi():
    """Fungsi ini untuk menangkap input user menggunakan lib bawaan python argeparse dan diteruskan ke fungsi `run_wsi'"""

    parser = arg.ArgumentParser(description="Alat utilitas wsi canggih")
    parser.add_argument(
        "command", nargs=arg.REMAINDER, type=str, help="Masukkan sebuah input"
    )
    args = parser.parse_args()

    return args.command


if __name__ == "__main__":
    catch_wsi()
