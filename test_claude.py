from unittest.mock import patch, MagicMock
from agents.claude import call_claude_api

@patch('agents.claude.anthropic.Client')
def test_call_claude_api(mock_client_class):
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client

    mock_message = MagicMock()
    mock_message.content = [MagicMock()]
    mock_message.content[0].text = 'response text'
    mock_client.messages.create.return_value = mock_message

    result = call_claude_api('test prompt')
    assert result == 'response text'
    mock_client.messages.create.assert_called_once_with(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[{"role": "user", "content": [{"type": "text", "text": "test prompt"}]}]
    )
