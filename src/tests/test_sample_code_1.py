from app.sample_code_1 import handler
from collections import namedtuple


def test_get_user_api(mocker):
    a = namedtuple('User', 'id fname lname')
    a.id = 1
    a.fname = 'Tommy'
    a.lname = 'Truong'
    request_data = {
        'id': 1
    }
    context = {}
    mocker.patch(
        'app.sample_code_1.function_to_db',
        return_value=a
    )
    expected = a
    actual = handler(request_data, context)
    assert expected == actual
