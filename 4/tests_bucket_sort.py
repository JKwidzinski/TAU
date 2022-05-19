import pytest
from bucket_sort import bucketsort

class TestsBucketSort:
    @pytest.mark.parametrize("arr,n,result", [([7,3,5],3,[3,5,7]) , ([151,12,15,111],3,[12,15,111,151])])
    def test_intvalues_sortedarray(self,arr,n,result):
        assert bucketsort(arr,n) == result
        
    @pytest.mark.parametrize("arr,n,result", [([4.5,3.1,4.2],3,[3.1,4.2,4.5]) , ([1.25,1.21,5.123,5.122],3,[1.21,1.25,5.122,5.123])])
    def test_doublevalues_sortedarray(self,arr,n,result):
        assert bucketsort(arr,n) == result
    
    @pytest.mark.parametrize("arr,n,result", [(['z', 'a', 'c'],3,TypeError) , (['b','x','d','y'],3,TypeError)])
    def test_charvalues_sortedarray(self,arr,n,result):
        with pytest.raises(result):
            assert bucketsort(arr,n)
        
    @pytest.mark.parametrize("arr,n,result", [(['badf', 'adfh', 'cljhk'],3,TypeError) , (['aac','aab','dfg','den'],3,TypeError)])
    def test_stringvalues_sortedarray(self,arr,n,result):
        with pytest.raises(result):
            assert bucketsort(arr,n)