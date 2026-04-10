import io
import requests
from app.config import GITHUB_TOKEN
from core.helper import process_zip_bytes
from models.data_models import CiData


def fetch_ci_data(repo_owner: str, repo_name: str, run_id: str):
    ci_data = CiData
    run_data = fetch_run(repo_owner, repo_name, run_id)
    ci_data.attempt_number = run_data["run_attempt"]
    ci_data.commit_sha = run_data["head_sha"]
    ci_data.branch = run_data["head_branch"]


    logs_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}/attempts/{ci_data.attempt_number}/logs"
    ci_data.run_url = logs_url
    response = requests.get(logs_url, headers={"Authorization": f"Bearer {GITHUB_TOKEN}"})

    if response.status_code == 200:
        zip_bytes = io.BytesIO(response.content)
        logs = process_zip_bytes(zip_bytes)
        ci_data.log = logs

    return ci_data

def fetch_run(repo_owner: str, repo_name: str, run_id: str):
    run_data = {}
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs/{run_id}"
    response = requests.get(url, headers={"Authorization": f"Bearer {GITHUB_TOKEN}"})

    if response.status_code == 200:
        run_data = response.json()

    return run_data
