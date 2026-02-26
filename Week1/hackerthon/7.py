#7.System "Snapshot" Comparison Tool
import os, sys
import subprocess, difflib

def snap():
    txt  = "\nPACKAGES:\n" + subprocess.getoutput("pip freeze")
    txt += "\nENV:\n" + "\n".join(f"{k}={v}" for k,v in os.environ.items())
    txt += "\nUSERS:\n" + subprocess.getoutput("who")
    return txt

if sys.argv[1] == "snap":
    open(sys.argv[2], "w").write(snap())
    print("Snapshot is saved!")

elif sys.argv[1] == "diff":
    a = open(sys.argv[2]).read().splitlines()
    b = open(sys.argv[3]).read().splitlines()
    print("\n".join(difflib.unified_diff(a, b)))