import pytest
from unittest.mock import patch, MagicMock
from integrations.git.git import fetch_ci_data, fetch_run

@patch('integrations.git.git.requests.get')
def test_fetch_run(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'run_attempt': 1, 'head_sha': 'abc', 'head_branch': 'main'}
    mock_get.return_value = mock_response

    result = fetch_run('owner', 'repo', '123')
    assert result == {'run_attempt': 1, 'head_sha': 'abc', 'head_branch': 'main'}
    mock_get.assert_called_once()

@patch('integrations.git.git.fetch_run')
@patch('integrations.git.git.requests.get')
@patch('integrations.git.git.CiData')
def test_fetch_ci_data(mock_cidataclass, mock_get, mock_fetch_run):
    mock_fetch_run.return_value = {'run_attempt': 1, 'head_sha': 'abc', 'head_branch': 'main'}
    # Since code does ci_data = CiData (assign class), result is the mock class
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = b'zipdata'
    mock_get.return_value = mock_response

    with patch('integrations.git.git.process_zip_bytes', return_value='logs'):
        result = fetch_ci_data('owner', 'repo', '123')
        assert result is mock_cidataclass
        assert result.attempt_number == 1
        assert result.commit_sha == 'abc'
        assert result.branch == 'main'
        assert result.run_url == 'https://api.github.com/repos/owner/repo/actions/runs/123/attempts/1/logs'
        assert result.log == 'logs'
