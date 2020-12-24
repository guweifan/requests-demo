import unittest
from test_case import test_case1
from TestRunner import HTMLTestRunner,SMTP
import time 


suite = unittest.TestSuite()
suite.addTest(test_case1.tongdun_api_test("test_paras_bishu_normal"))
#suite.addTest(test_case1.tongdun_api_test("test_paras_bishu_null"))

test_dir = './test_case/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

# runner = unittest.TextTestRunner()
# runner.run(discover)

#now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
now_time = time.strftime("%Y%m%d%H%M%S",time.localtime())


#生成测试报告
report = "./test-report/"+now_time+"result.html"
with (open(report,"wb")) as f:
    runner = HTMLTestRunner(stream= f, title = '首贷分数查询接口', description = 'test')
    runner.run(discover)

# #发送邮件
# smtp = SMTP(user= "weifan.gu@dhc.com.cn", password= "19930206", host= "smtp.dhc.com.cn")
# smtp.sender(to="357409858@qq.com", subject="20201209测试报告",  attachments=report)


