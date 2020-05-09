# -*- coding=utf-8 -*-

# self          导值
# session       通信
# table_url     课表链接
# school_year   学年
# Semester_num  学期时间

import json
from flask import jsonify

class ImportTimeTable():
    def __init__(self, session, table_url, school_year, Semester_num):

        # 过滤教务处的系统
        if Semester_num == '春季第一学期':
            Semester_num = "12"
        else:
            Semester_num = "3"
        school_year = school_year[0:4]
        self.session = session
        self.table_url = table_url
        self.school_year = school_year
        self.Semester_num = Semester_num

        print("0")

    def Get_TimeTable(self):
        data = {"xnm":self.school_year,"xqm":self.Semester_num}
        table_info = self.session.post(self.table_url,data = data).json()
        ImportTimeTable_Data = {'CourseList': [],'Student':[]}
        for each in table_info["kbList"]:
            ImportTimeTable_Data["CourseList"].append(  {'Week':'{}'.format(each['xqjmc']) , 'ClassTime': each['jcs'], 'LengthOfClass':'','CourseInformation':each['kcmc'],'TeachingClassRoom':each['cdmc'],'WeekNumber':each['zcd'],'Teacher':each['xm'] }  )

        ImportTimeTable_Data["Student"].append({'StudentID':'{}'.format(table_info["xsxx"]['XH']),'StudentName':'{}'.format(table_info["xsxx"]['XM']) } )

        ImportTimeTable_Data = json.dumps(ImportTimeTable_Data, indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False)

        self.ImportTimeTable_Data = ImportTimeTable_Data

        return self.ImportTimeTable_Data










