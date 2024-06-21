import subprocess

def launch_shell_job(command):
    # Launch the command in a shell
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for the command to complete and capture output
    stdout, stderr = process.communicate()
    
    # Print the output
    print("Standard Output:")
    print(stdout.decode())
    print("Standard Error:")
    print(stderr.decode())

# Example command: echo "Hello, World!" in the shell
command = 'echo "Hello, World!"'

# Launch the shell job
launch_shell_job(command)