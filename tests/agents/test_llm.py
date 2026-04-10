import pytest
from unittest.mock import patch
from models.data_models import CiData
from agents.llm import build_prompt, analyze_ci, call_llm_api

def test_build_prompt():
    ci_data = CiData(
        repo_owner='owner',
        repo_name='repo',
        commit_sha='sha',
        branch='main',
        run_url='url',
        log='log content'
    )
    prompt = build_prompt(ci_data)
    assert 'repo": "owner/repo"' in prompt
    assert '"commit_sha": "sha"' in prompt
    assert '"log": "log content"' in prompt

@patch('agents.llm.call_llm_api')
def test_analyze_ci(mock_call):
    mock_call.return_value = 'response'
    ci_data = CiData('o','r','s','b','u','l')
    result = analyze_ci(ci_data)
    assert result == 'response'
    mock_call.assert_called_once()

@patch('agents.llm.call_claude_api')
@patch('agents.llm.CLAUDE_API_KEY', 'key')
def test_call_llm_api_with_key(mock_call_claude):
    mock_call_claude.return_value = 'response'
    result = call_llm_api('prompt')
    assert result == 'response'

@patch('agents.llm.CLAUDE_API_KEY', None)
def test_call_llm_api_no_key():
    with pytest.raises(ValueError, match="No API key found for Claude"):
        call_llm_api('prompt')
