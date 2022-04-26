# import os
import os


class GetExcelpath:
    absolute_path = ''
    def testcasesheet(self,ExcelName):
        self.absolute_path = os.path.dirname(__file__)+"/"+ExcelName+".xlsx"
        #print(absolute_path)
        return self.absolute_path


