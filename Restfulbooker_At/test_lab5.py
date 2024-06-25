#fixtures
#Pass some of  the data to another testcase we use fixture
import pytest


@pytest.fixture
def test_case1():
    data1=[1,2,3,4,5]  #type List
    return data1

@pytest.fixture()
def sample_data1():
    return True

def test_case2(test_case1,sample_data1):
     assert len(test_case1) == 5
     assert sample_data1 == True