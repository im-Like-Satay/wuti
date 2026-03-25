import subprocess

from catch_input import catch_wsi


def run_wsi(perintah: str):
    """fungsi ini untuk menjalankan perinah dari fungsi catch_wsi"""
    inputWSIUser = catch_wsi()
    runWSIProcess = subprocess.run(
        inputWSIUser, shell=True, capture_output=True, text=True
    )

    print("[INFO] funct `run_wsi' running", runWSIProcess)
    return runWSIProcess


if __name__ == "__main__":
    run_wsi()
