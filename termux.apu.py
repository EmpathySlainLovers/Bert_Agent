import os

def execute_termux_command(cmd):
    try:
        result = os.popen(cmd).read()
        return f"[Termux] {result.strip()}"
    except Exception as e:
        return f"[Error] {str(e)}"
import subprocess

def tapi(cmd):
    try:
        return subprocess.check_output(["termux-" + cmd], stderr=subprocess.DEVNULL).decode().strip()
    except:
        return "API error or permission denied."
