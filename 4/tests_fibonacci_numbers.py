import pytest
from fibonacci_numbers import fibonacci

class TestsFibonacciNumbers:
    
    @pytest.mark.parametrize("a,result", [(9,34) , (12,144)])
    def test_positiveint_posivitevalue(self,a,result):
        assert fibonacci(a) == result
        
    @pytest.mark.parametrize("a,result", [(0,0), (1,1), (2,1)])
    def test_zeroonetwo_zeroorone(self,a,result):
        assert fibonacci(a) == result
    
    @pytest.mark.parametrize("a,result", [(-1,ValueError) , (-12,ValueError)])
    def test_negativevalue_throwsexception(self,a,result):
        with pytest.raises(result):
            assert fibonacci(a)
            
    @pytest.mark.parametrize("a,result", [("txt",TypeError) , ("a",TypeError)])
    def test_textvalue_throwsexception(self,a,result):
        with pytest.raises(result):
            assert fibonacci(a)