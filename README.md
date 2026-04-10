# CI Failure Investigator

## 📌 Overview
This tool analyzes a provided GitHub workflow run to:
- Extract errors from CI logs  
- Classify and analyze those errors  
- Suggest possible fixes  

For better accuracy, the tool can also analyze the repository where the CI error occurred.

---

## 🧠 Enhanced Analysis (Optional)
To enable deeper analysis using an LLM with repository context:

1. Install the GitHub MCP server:  
   https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md  

2. Without this setup, the tool will still work, but it will rely on assumptions rather than full repository context.

---

## ⚙️ Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment variables

Update your `.env` file with your credentials:

```
GITHUB_TOKEN=your_github_token
CLAUDE_API_KEY=your_claude_api_key
```

## 🚀 Usage
### Run in IDE
1. Open app/main.py
2. Replace the hardcoded GitHub workflow run link with your own 
3. Run

### Run in Terminal

From the project root:

```
python -m app.main "https://github.com/{repo-owner}/{repo-name}/actions/runs/{run-id}/job/
```

## Result

The result of the analysis will be stored in a `response.md`

## Example
Example [CI failure](https://github.com/borodinaalena95/playwright-demo-tests/actions/runs/24028004677/job/70070588719)

And an example analysis result [file](./response_example.md)