import pytest
from square_function import calculate_roots


class TestsSquareFunction:
    @pytest.mark.parametrize("a,b,c,result", [(3,6,2,(-0.42, -1.58)) , (2,4,1,(-0.29, -1.71))])
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