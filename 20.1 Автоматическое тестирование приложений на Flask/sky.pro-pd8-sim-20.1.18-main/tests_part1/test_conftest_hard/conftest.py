import pytest

incoming_list = [7, "4", 15, "12", 95, 5, 3, 8]

@pytest.fixture()
def list_creator():
    return [int(num) for num in incoming_list]

