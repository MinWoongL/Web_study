import re
from flask import Flask
from flask import render_template, request, url_for, redirect, flash
from werkzeug.utils import redirect
import pymysql
import pymysql.cursors

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user='root',
    passwd='disappear1!',
    db='market',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)

app.secret_key = 'my_secret'

@app.route("/")
def hello():
    return "<h1>Hello World</h1><h3>MinWoong</h3>"

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html",title="Sign up Page")
    else:
        user_id = request.form.get("user_id")
        user_password = request.form.get("user_password")
        user_name = request.form.get("user_name")
        user_email = request.form.get("user_email")
        user_hp = request.form.get("user_hp")
        
        if (user_id == '' or user_password == '' or name == '' or user_email == '' or user_hp == ''):
            return render_template("register.html", message = "입력되지 않은정보가 있습니다", title="Sign up Page")
        
        cursor = db.cursor()
        sql = """
            insert into users values ('{}','{}','{}','{}','{}');
        """.format(user_id,user_password,user_name,user_email,user_hp)
        
        rst = cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        if rst == 1 :
            db.commit()
            flash('회원가입 완료, 로그인 해주세요')
            return redirect(url_for('login'))
        else:
            print('error')
        return redirect(url_for('register'), message="정확한 정보를 다시 입력해주세요")

@app.route('/pagetest', methods = ["GET","POST"])
def pagetest():
    if request.method == "GET":
        return render_template("pagetest.html", title = "회원가입")
    else:
        user_id = request.form.get("user_id")
        user_password = request.form.get("user_password")
        user_name = request.form.get("user_name")
        user_email = request.form.get("user_email")
        user_hp = request.form.get("user_hp")
        
        if (user_id == '' or user_password == '' or name == '' or user_email == '' or user_hp == ''):
            return render_template("pagetest.html", message = "입력되지 않은정보가 있습니다", title ="회원가입")
        
        
        cursor = db.cursor()
        sql = """
            insert into users values ('{}','{}','{}','{}','{}');
        """.format(user_id,user_password,user_name,user_email,user_hp)
        
        rst = cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        if rst == 1 :
            db.commit()
            flash('회원가입 완료, 로그인 해주세요')
            return redirect(url_for('login'))
        else:
            print('error')
        return redirect(url_for('pagetest'), message="정확한 정보를 다시 입력해주세요",title="회원가입")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", title ="Login")
    else:
        user_id = request.form.get("user_id")
        user_password = request.form.get("user_password")
        
        cursor = db.cursor()
        sql = """
            select user_id,user_password from users where user_id = '{}';
        """.format(user_id)
        
        rst = cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        if rst != 1:
            return "아이디가 존재하지않습니다."
        else:
            if result[0]['user_password'] == user_password:
                flash("로그인이 정상적입니다.")
                return redirect(url_for('product'))
            else:
                return render_template('login.html', message = "비밀번호가 일치하지 않습니다.", title ="Login")
            

@app.route('/logintest', methods = ["GET","POST"])
def logintest_post_get():
    if request.method == "POST":
        print(request.form.get("userid"))
        print(request.form.get("password"))
        return "{ userid } 로그인 처리완료"
    else:
        return render_template("index.html", template="parameter")

@app.route('/logintest2', methods = ["POST"])
def login_post():
    return render_template(
        "index0.html",
        title = 'Flask Template Test',
        home_str = "Hello Flask",
        home_list = [1,2,3,4,5]
        )

@app.route('/html')
def html():
    return render_template('2.html')

@app.route('/Tim')
def Tim():
    return render_template("text.html")

@app.route('/user')
def user():
    return f'<h1>user info page</h1>'

@app.route('/user/<user>')
def userinfo(user):
    return f'<h1>{user}</h1>' + '사용자정보입니다.'

@app.route('/product')
def product():
    cursor = db.cursor()

    sql = """
        select * from goods;
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return render_template("product.html", rows = result, title ="제품정보조회")

@app.route('/product/<product>')
def productinfo(product):
    cursor = db.cursor()

    sql = """
        select * from goods where goodsno = {};
    """.format(product)
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    return render_template("product_detail.html", item = result, title="제품상세정보")


@app.route('/<name>')
def name(name):
    return f"name page, {name}"






if __name__ == "__main__":
    app.run(debug=True, host ="127.0.0.1", port = 3300)

