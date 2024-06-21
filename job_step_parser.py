import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON from file '{file_path}'.")
        return None

def extract_job_steps(data):
    if data is None:
        return None

    job_steps = []
    for step_name, num_steps in data.items():
        job_steps.append({"step_name": step_name, "num_steps": num_steps})
    return job_steps

def main():
    file_path = input("Enter the path to the JSON file: ")

    # Read JSON file
    json_data = read_json_file(file_path)

    # Extract job steps
    job_steps = extract_job_steps(json_data)

    if job_steps:
        print("Job steps extracted successfully:")
        for step in job_steps:
            print(f"Step Name: {step['step_name']}, Number of Steps: {step['num_steps']}")
    else:
        print("No job steps extracted.")

if __name__ == "__main__":
    main()