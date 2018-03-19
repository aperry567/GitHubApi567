# Standard Library imports
from unittest.mock import Mock, patch

# Third Party imports
from nose.tools import assert_true

# Local imports
from HW04aperry567 import github_id
from HW04aperry567 import github_repo


@patch('HW04aperry567.requests.get')
def test_github_id(mock_get):
    mock_get.return_value.ok = True

    response = github_id()

    assert_true(response)

