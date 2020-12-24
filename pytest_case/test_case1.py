import pytest
import requests
import sys

from requests.models import codes
sys.path.append("..")
from seq_data.firstLoanScore import seq_firstLoanScore
from common.common import read_csv,read_excl




class Test_tongdun_api():

    def test_data_bishu_normal(self,get_base_url):
        ''' 正常返回'''
        self.payload = seq_firstLoanScore.firstLoanScore_payload('BO20201009000066')
        self.response = requests.post(get_base_url, json = self.payload)
        assert (self.response.json()['ServiceResponse']['resCode'] == '0000')
        #print(self.response.json())


    def get_url(self,get_base_url):
        get_url = get_base_url
        return get_url
   
    
    @pytest.mark.parametrize("data,code",read_csv())
    def test_data_bishu_csv_null(self,get_base_url,data,code):
        '''pytest参数化'''
        #print(data)
        self.payload = data
        self.response = requests.post(get_base_url, json = self.payload)
        assert (self.response.json()['ServiceResponse']['resCode'] == code)
        print("---------------------------------------------------------------------->"+self.response.json()['ServiceResponse']['resCode'])
        print("------------------------------>"+code)
        print(self.response.json())
        

    @pytest.mark.parametrize("data,code",read_excl())
    def test_data_bishu_excl_null(self,get_base_url,data,code):
        '''pytest参数化'''
        #print(data)
        self.payload = data
        self.response = requests.post(get_base_url, json = self.payload)
        assert (self.response.json()['ServiceResponse']['resCode'] == code)
        print("---------------------------------------------------------------------->"+self.response.json()['ServiceResponse']['resCode'])
        print("------------------------------>"+code)
        print(self.response.json())
        
    



if __name__ == "__main__":
    pytest.main(['-sv','./test_case1.py'])