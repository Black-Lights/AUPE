import subprocess
import webbrowser
from time import sleep

def run_script(script_path):
    """Run a Python script and wait until it's done."""
    cmd = f"python {script_path}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return process

def main():
    # Step 1: Run the webserver script
    print("Running webserver script...")
    webserver_process = run_script('notebooks/Webserver-Merged.py')

    # Step 2: Wait for the webserver to start up
    sleep(10)  # Give the server a few seconds to start

    # Step 3: Start the Dash app
    print("Starting Dash app...")
    app_process = run_script('notebooks/Dashboard-Merged.py')  # Your Dash app script

    # Step 4: Open the browser
    sleep(5)  # Give the server a few seconds to start
    webbrowser.open('http://127.0.0.1:8050')

    # Step 5: Keep the script running to keep the Dash app alive
    try:
        # Output from the processes is captured and displayed
        for line in iter(webserver_process.stdout.readline, ''):
            print(line, end='')
        for line in iter(app_process.stdout.readline, ''):
            print(line, end='')
    except KeyboardInterrupt:
        webserver_process.terminate()
        app_process.terminate()
        print("Processes terminated.")

if __name__ == '__main__':
    main()