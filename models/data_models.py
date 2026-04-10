from dataclasses import dataclass

@dataclass
class CiData:
    repo_owner: str
    repo_name: str
    commit_sha: str
    branch: str
    run_url: str
    log: str

