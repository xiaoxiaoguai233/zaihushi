#encoding : UTF-8

from flask import Flask, request, jsonify
from login import *
from api.timetable import *

app = Flask(__name__)


######
#       部署测试
######
@app.route("/test",methods=["GET"])
def Test():
    return "项目部署成功"


######
#       欢迎页
######
@app.route("/",methods=["GET"])
def www_zaihushi_app_cn():
    page = open('index.html', encoding='utf-8'); #打开当前文件下的my_index.html(这个html是你自己写的)
    res = page.read()#读取页面内容，并转义后返回
    return res;


######
#       登录
######
@app.route("/api/Login",methods=["POST"])
def Login():
    my_data = request.get_json()
    studentID = my_data.get('studentID')
    Password = my_data.get('Password')
    zspt = Longin(studentID, Password, login_url, login_KeyUrl)
    response_cookies = zspt.Longin_Home()
    if response_cookies == "0":
        return jsonify(login_status="登录失败")
    else:
        return jsonify(login_status="登录成功")


######
#       获取课表
######
@app.route("/api/Timetable/ImportTimetable",methods=["POST"])
def ImportTimetable():
    #获取data数据
    my_data = request.get_json()
    studentID = my_data.get('studentID')
    Password = my_data.get('Password')
    school_year = my_data.get('school_year')
    Semester_num = my_data.get('Semester_num')

    zspt = Longin(studentID, Password, login_url, login_KeyUrl)
    response_cookies = zspt.Longin_Home()
    if response_cookies == "0":
        return jsonify(login_status="登录失败")
    else:
        t = ImportTimeTable(response_cookies, table_url,school_year,Semester_num)
        table = t.Get_TimeTable()
        table = json.loads(table)
        print(table)
        return jsonify(login_status="登录成功",CourseList=table["CourseList"],Student_Information=table["Student"])


######
#       获取学生个人信息
######
@app.route("/api/getStudentInformaction/getStudentInformaction",methods=["POST"])
def getStudentInformaction():
    my_data = request.get_json()
    studentID = my_data.get('studentID')
    Password = my_data.get('Password')
    school_year = my_data.get('school_year')
    Semester_num = my_data.get('Semester_num')

    zspt = Longin(studentID, Password, getStudentInformaction_url, login_KeyUrl)
    response_cookies = zspt.Longin_Home()
    if response_cookies == "0":
        return jsonify(login_status="登录失败")
    else:
        return 0


if __name__ == "__main__":
   app.run()
