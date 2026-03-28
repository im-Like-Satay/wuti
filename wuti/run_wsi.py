import subprocess

from wuti.catch_input import catch_wsi


def run_wsi():
    """fungsi ini untuk menjalankan perinah dari fungsi catch_wsi"""
    inputWSIUser = catch_wsi()
    try:
        result = subprocess.run(
            inputWSIUser, shell=True, capture_output=True, text=True
        )
        output = result.stdout + result.stderr
        print(output)
        return output
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    run_wsi()
