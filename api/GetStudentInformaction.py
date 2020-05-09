# -*- coding=utf-8 -*-

# self          导值
# session       通信
# table_url     课表链接
# school_year   学年
# Semester_num  学期时间

import json
from flask import jsonify

class ImportTimeTable():
    def __init__(self, session, getStudentInformaction_url, school_year, Semester_num):

        # 过滤教务处的系统
        if Semester_num == '春季第一学期':
            Semester_num = "12"
        else:
            Semester_num = "3"
        school_year = school_year[0:4]
        self.session = session
        self.getStudentInformaction_url = getStudentInformaction_url
        self.school_year = school_year
        self.Semester_num = Semester_num

        print("0")

    def Get_TimeTable(self):
        data = {"xnm":self.school_year,"xqm":self.Semester_num}
        table_info = self.session.post(self.getStudentInformaction_url,data = data).json()












