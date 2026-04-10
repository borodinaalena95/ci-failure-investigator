import pytest
import zipfile
import io
from core.helper import parse_link, process_zip_bytes

def test_parse_link_valid():
    link = "https://github.com/owner/repo/actions/runs/1234567890/job/987"
    assert parse_link(link) == ("owner", "repo", "1234567890")

def test_parse_link_invalid():
    with pytest.raises(ValueError, match="Invalid link format"):
        parse_link("invalid")

def test_process_zip_bytes():
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zf:
        zf.writestr('log1.txt', 'content1')
        zf.writestr('log2.txt', 'content2')
        zf.writestr('notlog.txt', 'ignore')
    zip_buffer.seek(0)
    result = process_zip_bytes(zip_buffer)
    assert result == 'content1content2ignore'
