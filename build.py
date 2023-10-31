#!/usr/bin/env python

import subprocess

def build_project():
    try:
        # Add your build commands here
        subprocess.run(["python", "setup.py", "build"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        exit(1)

if __name__ == "__main__":
    build_project()
