import pytest
from square_function import calculate_roots
from get_data import getdata

data = getdata('../data.json', "square")

class TestsSquareFunction:
    @classmethod
    def setup(cls):
        print('\nsetup squarefunction tests')

    @classmethod
    def teardown(cls):
        print('\nteardown squarefunction tests')
    
    @pytest.mark.parametrize("a,b,c,result", data)
    def test_normalvalues_tworoots(self,a,b,c,result):
        assert calculate_roots(a,b,c) == result

    @pytest.mark.parametrize("a,b,c,result", [(4,4,1,-0.5) , (3,6,3,-1.0)])
    def test_deltaequalszero_oneroot(self,a,b,c,result):
        assert calculate_roots(a,b,c) == result
        
    @pytest.mark.parametrize("a,b,c,result", [(4,4,"txt",TypeError) , ("asdf",6,3,TypeError)])
    def test_wrongtype_throwsexception(self,a,b,c,result):
        with pytest.raises(result):
            assert calculate_roots(a,b,c)
            
    @pytest.mark.parametrize("a,b,c,result", [(0,4,1,ValueError) , (4,0,3,ValueError), (0,0,1,ValueError)])
    def test_wrongtype_throwsexception(self,a,b,c,result):
        with pytest.raises(result):
            assert calculate_roots(a,b,c)