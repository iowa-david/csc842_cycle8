import os
import psutil
import re

ROOT_DIR = "C:/Users/davemc/OneDrive - Default Directory/Training"
KEYLOGGER_FILES = ["keylogger.exe", "logger.exe", "kl.exe"]
PROCESS_NAMES = ["keylogger", "keylg", "textinputhost"]
# stack overflow ssn validation https://stackoverflow.com/questions/4087468/ssn-regex-for-123-45-6789-or-xxx-xx-xxxx
SSN_REGEX = r'^(?!(000|666|9))\d{3}-(?!00)\d{2}-(?!0000)\d{4}$|^(?!(000|666|9))\d{3}(?!00)\d{2}(?!0000)\d{4}$'


def search_file_for_pattern(file_path, pattern):

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    results = re.findall(pattern, content)
    return results

def check_files_for_pii():
    found_files = []
    cnt = 0
    for root_dir, _, files in os.walk(ROOT_DIR):
        for file in files:
            cnt += 1

            result = search_file_for_pattern(os.path.join(root_dir, file), SSN_REGEX)
            if(len(result) > 0):
                found_files.append(os.path.join(root_dir, file))

    print(f"{cnt} files checked")
    return found_files


def detect_keylogger_files():
    found_files = []
    cnt = 0
    for root_dir, _, files in os.walk(ROOT_DIR):
        for file in files:
            cnt += 1
            if any(name in str(file) for name in PROCESS_NAMES):
                found_files.append(os.path.join(root_dir, file))

    print(f"{cnt} files checked")
    return found_files


def identify_matching_processes(target_process_names):
    lower_target_names = [name.lower() for name in target_process_names]
    matching_processes = [process.info for process in psutil.process_iter(['pid', 'name'])
                          if process.info['name'].lower() in lower_target_names]
    return matching_processes


def main():
    suspicious_files = detect_keylogger_files()
    suspicious_processes = identify_matching_processes(PROCESS_NAMES)
    pii_files = check_files_for_pii()

    if (pii_files):
        print("Found possible pii in files")
        for file in pii_files:
            print(f"File found: {file}")
    else:
        print("No identified pii files found")


    if (suspicious_files):
        print("Found possible keylogger files")
        for file in suspicious_files:
            print(f"File found: {file}")
    else:
        print("No identified keylogger files found")

    if (suspicious_processes):
        print("Found possible keylogger process")
        for process in suspicious_processes:
            print(f"PID: {process['pid']}, Name: {process['name']}")
    else:
        print("No identified keylogger processes found")


main()
