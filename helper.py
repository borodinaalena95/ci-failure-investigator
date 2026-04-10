import zipfile

def parse_link(link: str):
    parts = link.split("/")
    if len(parts) < 9:
        raise ValueError("Invalid link format")
    repo_owner = parts[3]
    repo_name = parts[4]
    run_id = parts[7]
    return repo_owner, repo_name, run_id

def process_zip_bytes(zip_bytes):
    logs = ""
    with zipfile.ZipFile(zip_bytes, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.txt'):
                with zip_ref.open(file_name) as log_file:
                    logs += log_file.read().decode('utf-8')

    return logs