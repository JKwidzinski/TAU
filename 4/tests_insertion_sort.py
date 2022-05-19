import pytest
from insertion_sort import insertionsort

class TestsInsertionSort:
    
    @pytest.mark.parametrize("arr,result", [([7,3,5],[3,5,7]) , ([151,12,15,111],[12,15,111,151])])
    def test_intvalues_sortedarray(self,arr,result):
        assert insertionsort(arr) == result
        
    @pytest.mark.parametrize("arr,result", [([4.5,3.1,4.2],[3.1,4.2,4.5]) , ([1.25,1.21,5.123,5.122],[1.21,1.25,5.122,5.123])])
    def test_doublevalues_sortedarray(self,arr,result):
        assert insertionsort(arr) == result
    
    @pytest.mark.parametrize("arr,result", [(['z', 'a', 'c'],['a','c','z']) , (['b','x','d','y'],['b','d','x','y'])])
    def test_charvalues_sortedarray(self,arr,result):
        assert insertionsort(arr) == result
        
    @pytest.mark.parametrize("arr,result", [(['badf', 'adfh', 'cljhk'],['adfh','badf','cljhk']) , (['aac','aab','dfg','den'],['aab','aac','den','dfg'])])
    def test_stringvalues_sortedarray(self,arr,result):
        assert insertionsort(arr) == result