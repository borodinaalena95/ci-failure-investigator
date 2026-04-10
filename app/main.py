import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from core.helper import parse_link
from integrations.git.git import fetch_ci_data
from agents.llm import build_prompt, call_llm_api

if __name__=="__main__":
    if len(sys.argv) >= 2:
        link = sys.argv[1]
    else:
        # replace link to run in IDE
        link = "https://github.com/{repo-owner}/{repo-name}/actions/runs/{run-id}/job/{job-id}"

    repo_owner, repo_name, run_id = parse_link(link)
    ci_data = fetch_ci_data(repo_owner, repo_name, run_id)
    ci_data.repo_owner = repo_owner
    ci_data.repo_name = repo_name
    prompt = build_prompt(ci_data)
    response = call_llm_api(prompt)

    with open("response.md", "w") as f:
        f.write(response)
        f.close()
