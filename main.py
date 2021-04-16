'''=============== APPLICATION (FIRSTSURVEY) ==============='''

#IMPORT OF LIBRARIES REQUIRED FOR THE CONSTRUCTION OF ALGORITHM
from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
import mysql.connector


#CONNECTION TO THE MYSQL DATABASE 
#FOR VALIDATION AND INSERTING OF APPLICATION DATA.
banco = mysql.connector.connect(
        host = "HOSTNAME",
        port="PORTNAME",
        user="USERNAME",
        passwd="PASSWORD",
        database="DATABASE"
    )

'''=============== DEVELOPING THE ALGORITHM ==============='''
# VALIDATING IN THE DATABASE
def accessing_registration():
    cpf = security_screen.lineEdit.text()
    passw = security_screen.lineEdit_2.text()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM baseA WHERE CPF = '{}' and SENHA = '{}'".format(cpf, passw))
    checking = cursor.fetchone()
    try:
        if (cpf in checking and passw in checking):
            security_screen.close()
            information_screen.show()
            information_screen.label_7.setText('{}'.format(cpf))
            cursor.execute("SELECT NOME FROM baseA WHERE CPF = '{}'".format(cpf))
            connect = cursor.fetchall()
            information_screen.label_8.setText(str(connect[0][0]))
            cursor.execute("SELECT ENDEREÇO FROM baseA WHERE CPF = '{}'".format(cpf))
            connect2 = cursor.fetchall()
            information_screen.label_11.setText(str(connect2[0][0]))
        def close_info():
            information_screen.close()
        information_screen.pushButton_6.clicked.connect(close_info)

    except:
        security_screen.label_8.setText("Por favor, confira os dados do CPF e da senha!")
        security_screen.lineEdit.setText("")
        security_screen.lineEdit_2.setText("")


#ACCESSING THE DEBTS PAGE
def acessing_debts():
    screen_debt.show()
    def reporting_debts():
        cpf = screen_debt.lineEdit.text()
        passw = screen_debt.lineEdit_2.text()
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM baseA WHERE CPF = '{}' and SENHA = '{}'".format(cpf, passw))
        checking = cursor.fetchone()
        try:
            if (cpf in checking and passw in checking):
                debt_logg.show()
                screen_debt.lineEdit.setText("")
                screen_debt.lineEdit_2.setText("")
                screen_debt.close()
                debt_logg.label_7.setText('{}'.format(cpf))
                cursor.execute("SELECT NOME FROM baseA WHERE CPF = '{}'".format(cpf))
                connect = cursor.fetchall()
                debt_logg.label_10.setText(str(connect[0][0]))
                def debts_report():
                    cursor = banco.cursor()
                    cursor.execute(
                        "SELECT dividas.INFO_COMPRA, dividas.VALOR_COMPRA, dividas.VALOR_ATUALIZADO, dividas.DATA_COMPRA FROM baseA JOIN dividas ON baseA.CPF = dividas.CPF_DEVEDOR WHERE CPF = '{}';".format(cpf))
                    reading = cursor.fetchall()
                    debt_logg.tableWidget.setRowCount(len(reading))
                    debt_logg.tableWidget.setColumnCount(4)

                    for request in range(0, len(reading)):
                        for query in range(0, 4):
                            debt_logg.tableWidget.setItem(request, query, QtWidgets.QTableWidgetItem
                            (str(reading[request][query])))

                    banco.close()
                debts_report()

        #APPLYING EXCEPT (ERROR CPF OR PASSW)
        except:
            screen_debt.label_8.setText("Por favor, confira os dados do CPF e da senha!")
            screen_debt.lineEdit.setText("")
            screen_debt.lineEdit_2.setText("")

    #CLOSE SCREEN
    def close_debt():
        screen_debt.label_8.setText("")
        screen_debt.close()
    screen_debt.pushButton_6.clicked.connect(close_debt)

    #LOGAR FUNCTION
    screen_debt.pushButton.clicked.connect(reporting_debts)


#ACCESS TO REGISTRATION
def securityscreen():
        security_screen.show()
        security_screen.pushButton.clicked.connect(accessing_registration)
        def close():
            security_screen.close()
        security_screen.pushButton_6.clicked.connect(close)


#ENDING THE APPLICATION BY CONNECTING THE FUNCTION
def closing_application():
    firstsurvey_screen.close()


'''===================== CONNECTIONS TO PYQT5 ====================='''

#READING THE SCREEN FILES IN UI FORMAT
app = QtWidgets.QApplication([])
firstsurvey_screen = uic.loadUi("screens/firstsurvey_screen.ui")
security_screen = uic.loadUi("screens/security_screen.ui")
information_screen = uic.loadUi("screens/information_screen.ui")
screen_debt = uic.loadUi("screens/screen_debt.ui")
debt_logg = uic.loadUi("screens/screen_debt_logg.ui")


#ADDING FUNCTIONALITY TO THE SCREEN BUTTONS
firstsurvey_screen.pushButton.clicked.connect(securityscreen)
firstsurvey_screen.pushButton_2.clicked.connect(acessing_debts)
firstsurvey_screen.pushButton_6.clicked.connect(closing_application)


#INSERTING IMAGES ON SCREENS
icon=QtGui.QPixmap([])
firstsurvey_screen.label_11.setPixmap(QtGui.QPixmap('img\image_firstsurvey.png'))


#INITIALIZING THE APPLICATION
firstsurvey_screen.show()
app.exec()