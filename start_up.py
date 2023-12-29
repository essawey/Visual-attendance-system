import subprocess

def install_dependencies():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
