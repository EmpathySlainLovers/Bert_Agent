import subprocess

def tapi(cmd):
    try:
        return subprocess.check_output(["termux-" + cmd], stderr=subprocess.DEVNULL).decode().strip()
    except:
        return "API error or permission denied."