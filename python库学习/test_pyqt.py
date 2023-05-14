
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox,QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets
import pymysql

class Status:
    def __init__(self):
        self.ui = QUiLoader().load(r'D:\xzc\学习\python库\pyqt5_test.ui')
        # self.table=QtWidgets.QTableWidget()
        # self.ui.button.clicked.connect(self.handleCalc)
        # self.name = self.Text_info.toPlainText()
        # self.ui.comboBox.addItem('pig')

        '''
        表格操作
        '''
        # #表格中插入内容
        # self.ui.sumtable.insertRow(1)
        # #对表格中未设置内容的单元赋值
        # self.ui.sumtable.setItem(1,0,QTableWidgetItem('666'))
        # #对已设置内容的单元重新赋值
        # self.ui.sumtable.item(0,0).setText('100')
        #获取表格列数
        rowcount=self.ui.sumtable.rowCount()
        print(rowcount)
        self.show_info()

        '''
        捕捉相应行为，跳转到def的位置
        '''
        self.ui.button.clicked.connect(self.handleCalc)
        self.ui.comboBox.currentIndexChanged.connect(self.handlecbox)
        self.ui.Text_info.textChanged.connect(self.handletext)
        #登录后进入Calculate新界面
        self.ui.login_Button.clicked.connect(self.handle_login)
        #捕捉表格变动信息
        self.ui.sumtable.cellChanged.connect(self.handletablechanged)

        # self.ui.Text_info.textChanged.connect(self.handletext)

    def show_info(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', charset='utf8', db='exercise1')
        cursor = conn.cursor()
        cursor.execute('select name,password from L1')
        data = cursor.fetchall()
        self.ui.sumtable.insertRow(0)
        for row,info in enumerate(data):
            for colunm,item in enumerate(info):
                self.ui.sumtable.setItem(row,colunm,QTableWidgetItem(str(item)))
            row_position = self.ui.sumtable.rowCount()
            self.ui.sumtable.insertRow(row_position)

    def handle_login(self):
        print('enter success')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', charset='utf8', db='exercise1')
        cursor = conn.cursor()
        cursor.execute('select name,password from L1')
        data = cursor.fetchall()
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        for row in data:
            print(row)
            if username == row[0] and password == row[1]:
                print('login success')
                self.ui.Text_info.setPlainText(str(data))
                QMessageBox.about(self.ui,'登录结果','login success')
                self.ui2 = Calculate()
                #进入新窗口
                self.ui2.ui2.show()
                self.ui.close()


    def handletablechanged(self,row,column):
        print(self.ui.sumtable.item(0, 0).text())
        print(row)
        print('vhanede')
        name = self.ui.sumtable.item(row,0).text()
        value = self.ui.sumtable.item(row, column).text()
        print(name)
        print(value)

    def handlecbox(self):
        type = self.ui.comboBox.currentText()
        print(type)

    def handleCalc(self):
        print('button clicked')
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',charset='utf8',db='exercise1')
        cursor = conn.cursor()
        cursor.execute('update L1 set amount=amount+1000')
        cursor.execute("select * from L1")
        data = cursor.fetchall()
        self.ui.Text_info.setPlainText(str(data))

    def handletext(self):
        print('text input')
        text = self.ui.Text_info.toPlainText()
        QMessageBox.about(self.ui,'结果',text)
        print(text)

class Calculate:
    def __init__(self):
        self.ui2 = QUiLoader().load(r'D:\xzc\学习\python库\pyqt5_system.ui')
        self.table_init()
        self.catch_movement()

    def catch_movement(self):
        self.ui2.add_button.clicked.connect(self.handleadd_button)
        self.ui2.save_button.clicked.connect(self.handlesave_button)
        self.ui2.stu_table.cellChanged.connect(self.handletableChanged)

    #用于显示数据库中每一行
    def table_init(self):
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',charset='utf8',db='exercise1')
        cursor = conn.cursor()
        cursor.execute('select id,name,gender,amount from L1')
        data = cursor.fetchall()
        for row,info in enumerate(data):
            print(row)
            #将数据库中每一行打印
            self.ui2.stu_table.insertRow(row)
            self.ui2.stu_table.setItem(row, 0,QTableWidgetItem(str(info[0])))
            self.ui2.stu_table.setItem(row, 1, QTableWidgetItem(info[1]))
            self.ui2.stu_table.setItem(row, 2, QTableWidgetItem(info[2]))
            self.ui2.stu_table.setItem(row, 3, QTableWidgetItem(str(info[3])))
            #用于显示
            # self.ui2.stu_table.item(row, 1).text() = info[1]
            # self.ui2.stu_table.item(row, 2).text() = info[2]
            # self.ui2.stu_table.item(row, 3).text() = info[3]

    def handletableChanged(self,row,column):
        info = self.ui2.stu_table.item(row,column).text()
        QMessageBox.about(self.ui2, 'info_changed 结果', info)

    def handleadd_button(self):
        print('add success')
        max_row = self.ui2.stu_table.rowCount()
        self.ui2.stu_table.insertRow(int(max_row))

    def handlesave_button(self):
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',charset='utf8',db='exercise1')
        cursor = conn.cursor()
        #遍历表格，进行保存,若表中结果与数据库中一致，则跳过，不一致则修改保存
        cursor.execute('select id,name,gender,amount from L1')
        data=cursor.fetchall()
        for row,info in enumerate(data):
            #print('first cir {} {}'.format(row,info))
            for column,result in enumerate(info):
                #print(column,result)
                #print('location {} {}'.format(row,column))
                table_info = self.ui2.stu_table.item(row,column).text()
                print('table result {0}'.format(self.ui2.stu_table.item(row,column).text()))
                print('data result {0}'.format(result))
                if str(result) != str(table_info):
                    print('data not match')
                    cursor.execute('update L1 set id=%s where id=%s;',[str(table_info),str(result)])
                    print('update L1 set id=\'{}\' where id=\'{}\''.format(str(table_info),str(result)))
        print('save success')


    def handleform(self):
        pass

app = QApplication()
status = Status()
status.ui.show()
app.exec_()

    # app = QApplication()
    # window = QMainWindow()
    # window.setWindowTitle('统计薪资')
    # window.resize(640,480)
    # text = QPlainTextEdit('edit',window)
    # text.setPlaceholderText('please input')
    # text.resize(300,400)
    # button = QPushButton('test',window)
    # button.move(400,50)
    # button.show()
    # button.clicked.connect(handleCalc)
    # text.move(10,10)
    # text.show()
    # window.show()
    # app.exec_()
#
#
# # app = QApplication([])  #其他控件调用时必须先创建
# #
# # window = QMainWindow()  #主窗口对象
# # window.resize(500, 400)
# # window.move(300, 310)
# # window.setWindowTitle('薪资统计')
# #
# # textEdit = QPlainTextEdit(window)
# # textEdit.setPlaceholderText("请输入薪资表")
# # textEdit.move(10,25)
# # textEdit.resize(300,350)
# #
# # button = QPushButton('统计', window)
# # button.move(380,80)
# #
# # window.show()
# #
# # app.exec_() #死循环