#导入Flask对象。
from flask import Flask,render_template,request,redirect

#使用Flask对象创建一个app对象。
app = Flask(__name__)

students = [
    {'name': 'dustfree', 'chinese': '65', 'math': '65', 'english': '65'},
    {'name': '小白狼', 'chinese': '65', 'math': '65', 'english': '65'},
    {'name': '绯夜', 'chinese': '65', 'math': '65', 'english': '65'},
    {'name': '棒棒', 'chinese': '65', 'math': '65', 'english': '65'},
]

@app.route('/')
def welcome():
    return render_template('/welcome.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #此处需要连接数据库进行账号密码校验。
        print('从服务器接收到的数据：',username,password)
        #登录成功之后，应该跳转到管理页面。
        return redirect('/admin')
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html',students=students)

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == 'POST':
        username = request.form.get('username')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')
        print('获取的学员信息:',username,math,chinese,english)
        students.append({'name':username, 'chinese': chinese, 'math': math, 'english': english})
        return redirect('/admin')
    return render_template('add.html')

@app.route('/delete')
def delete_student():
    #在后台拿到学员的名字
    print(request.method)
    username = request.args.get('name')
    #找到学员并删除信息
    for stu in students:
        if  stu['name'] == username:
            students.remove(stu)
    return redirect('/admin')

@app.route('/change',methods=["GET","POST"])
def change_student():
    username = request.args.get('name')
    if  request.method == "POST":
        username = request.form.get('username')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')
        for stu in students:
            if  stu['name'] == username:
                stu['chinese'] = chinese
                stu['math'] = math
                stu['english'] = english
        return redirect('/admin')
    for  stu in students:
        if stu['name'] == username:
            #需要在页面中渲染学生的成绩数据
            return render_template('change.html',students=stu)

if __name__ == '__main__':
    app.run(debug=True)
