import pymysql
import pandas as pd

host_name = 'localhost'
host_port = 3306
username = 'root'
password = 'disappear1!'
database_name = 'student_mgmt'

db = pymysql.connect(
    host=host_name,     # MySQL Server Address
    port=host_port,          # MySQL Server Port
    user=username,      # MySQL username
    passwd=password,    # password for MySQL username
    db=database_name,   # Database name
    charset='utf8'
)


SQL = "SELECT * FROM students"
df = pd.read_sql(SQL, db)
df.to_csv('students.csv', sep=',', index=False, encoding='utf-8')

print(df)