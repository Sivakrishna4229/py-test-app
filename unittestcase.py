import unittest
from multiply import multiplication
class multiplytestcase(unittest.testcase):

  def test_1(self):

result=multiplication(3,4)
self.assertequal(result,12)

if_name_=='_main_':
unittest.main()
