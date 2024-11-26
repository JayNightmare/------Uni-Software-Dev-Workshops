from unittest.mock import patch
from Epic_4.Workshop_8.Exercises.Exercise_4.Exercise4 import shorten_url

@patch("Exercise4.Exercise4.requests.post")
def test_shorten_url(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "data": {"tiny_url": "https://tiny.one/test123"}
    }
    result = shorten_url("https://example.com")
    assert result == "https://tiny.one/test123", "Shortened URL is incorrect."
    assert mock_post.called, "API call for URL shortening was not made."
