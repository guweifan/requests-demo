import pytest
#from TestRunner import HTMLTestRunner,SMTP
import time 




now_time = time.strftime("%Y%m%d%H%M%S",time.localtime())

#discover = pytest.main([])
#生成测试报告
# report = "./test-report/"+now_time+"result.html"
# with (open(report,"wb")) as f:
#     runner = HTMLTestRunner(stream= f, title = '首贷分数查询接口', description = 'test')
#     runner.run("-v","-s","./test_case")


#pytest.main(["-v","./pytest_case","--html=./test-report/"+now_time+"report.html"])

pytest.main(["-vs","./pytest_case","--alluredir=./allure-report/"+now_time])


