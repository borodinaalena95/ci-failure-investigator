from app.config import CLAUDE_API_KEY
from agents.claude import call_claude_api
from models.data_models import CiData

def build_prompt(ci_data: CiData):
    return f"""
        Analyze this failed CI run.
    
        Tasks:
        
        1. Parse the log and identify all distinct failures.
        2. Classify each as:
           * server bug
           * frontend/product bug
           * test automation flaw
           * environment/infrastructure issue
           * unknown
        3. For each failure, provide:
           * evidence
           * confidence
           * explanation
           * likely impacted file(s) if inferable
           * proposed next step
        4. If mcp-github is available, inspect the repo and propose the smallest safe code fix.
        5. If mcp-github is unavailable, do not invent repo details; propose only a likely fix based on the log.
        
        Return in .md friendly format:
        
        - if mcp-github is unavailable add a NOTE: LLM doesn't have direct access to the repository. 
        The following analysis is based on assumptions  
        - if mcp-github is available add a NOTE: LLM performed the analysis based on the repository content.
        
        * failure summary
        * failed test names related to this failure
        * final assessment
        * proposed fix (only for automation bugs. for application bugs suggest to verify the application logic) 
        * whether this is mainly a product defect or automation defect
        
        Context:
        {{
        "repo": "{ci_data.repo_owner}/{ci_data.repo_name}",
        "commit_sha": "{ci_data.commit_sha}",
        "branch": "{ci_data.branch}",
        "run_url": "{ci_data.run_url}",
        "log": "{ci_data.log}"
        }}
    """


def analyze_ci(ci_data: CiData):
    return call_llm_api(
        prompt=build_prompt(ci_data),
    )


def call_llm_api(prompt: str) -> str:
    if CLAUDE_API_KEY:
        response = call_claude_api(prompt)
        return response
    else:
        raise ValueError("No API key found for Claude")