import subprocess

from catch_input import catch_wsi


def run_wsi():
    """fungsi ini untuk menjalankan perinah dari fungsi catch_wsi"""
    inputWSIUser = catch_wsi()
    try:
        runWSIProcess = subprocess.run(
            inputWSIUser, shell=True, capture_output=True, text=True
        )
        return str(runWSIProcess)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run_wsi()
