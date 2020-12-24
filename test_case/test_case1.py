import unittest
import requests
import sys
sys.path.append("..")
from seq_data.firstLoanScore import seq_firstLoanScore
from ddt import data, ddt,unpack

@ddt
class tongdun_api_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_url = "http://22.144.101.183:13010/bpmService"

    def test_paras_bishu_normal(self):
        ''' 正常返回'''
        self.payload = seq_firstLoanScore.firstLoanScore_payload('BO20191108000039')
        self.response = requests.post(self.test_url, json = self.payload)
        self.assertEqual(self.response.json()['ServiceResponse']['resCode'],'0000')
        print(self.response.json())
    
    @data([{"ServiceRequest": {"serviceType": "firstLoanScore","reqTime": "2019-11-04 09:30:21","data": {"appNum": "","prodCode": "01G213"}}},"appNum为空"],
          [{"ServiceRequest": {"serviceType": "firstLoanScore","reqTime": "2019-11-04 09:30:21","data": {"appNum": "BO20191108000039","prodCode": ""}}},"prodCode为空"],
          [{"ServiceRequest": {"serviceType": "","reqTime": "2019-11-04 09:30:21","data": {"appNum": "BO20191108000039","prodCode": "01G213"}}},"serviceType为空"])
    @unpack    
    def test_paras_bishu_null(self,payload,note):
        '''ddt'''
        print(note)
        self.payload = payload
        self.response = requests.post(self.test_url, json = self.payload)
        self.assertEqual(self.response.json()['ServiceResponse']['resCode'],'9999')
        print(self.response.json())
        

if __name__ == "__main__":
    unittest.main() 