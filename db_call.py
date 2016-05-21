import psycopg2
import win32com.client
import pythoncom
import sqlite3

#================== Database Connection =================== st
# conn_string = "host='localhost' dbname ='Anthouse' user='' password=''"
try:
        conn = sqlite3.connect("db.sqlite3")
except:
        print("error database connection")
curs = conn.cursor()
#
# curs.execute("TRUNCATE TABLE sdata_stock")
# conn.commit()




class XASessionEvents:
    logInState = 0
    def OnLogin(self, code, msg):
        print("OnLogin method is called")
        print(str(code))
        print(str(msg))
        if str(code) == '0000':
            XASessionEvents.logInState = 1

    def OnLogout(self):
        print("OnLogout method is called")

    def OnDisconnect(self):
        print("OnDisconnect method is called")

class XAQueryEvents:
    queryState = 0
    def OnReceiveData(self,szTrCode):
        print("ReceiveData")
        XAQueryEvents.queryState = 1
    def OnReceiveMessage(self, systemError, messageCode, message):
        print("ReceiveMessage")

if __name__ == "__main__":
    server_addr = "hts.ebestsec.co.kr"
    server_port = 20001
    server_type = 0
    user_id = "songdh10"
    user_pass ="gusdl57"
    user_certificate_pass="gusdlsla57"

    inXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
    inXASession.ConnectServer(server_addr, server_port)
    inXASession.Login(user_id, user_pass, user_certificate_pass, server_type, 0)

    while XASessionEvents.logInState == 0:
        pythoncom.PumpWaitingMessages()

    inXAQuery = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
    inXAQuery.LoadFromResFile("C:\\eBEST\\xingAPI\\Res\\t8430.res")
    inXAQuery.SetFieldData('t8430InBlock', 'gubun', 0, 0)
    inXAQuery.Request(0)

    while XAQueryEvents.queryState == 0:
        pythoncom.PumpWaitingMessages()

    # Get FieldData
    nCount = inXAQuery.GetBlockCount('t8430OutBlock')
    print(nCount)
    for i in range(nCount):
        print(i, ":", inXAQuery.GetFieldData('t8430OutBlock', 'hname', i), ":", inXAQuery.GetFieldData('t8430OutBlock', 'shcode', i), inXAQuery.GetFieldData('t8430OutBlock','uplmtprice',i))
        a = inXAQuery.GetFieldData('t8430OutBlock', 'hname', i)
        b = inXAQuery.GetFieldData('t8430OutBlock', 'shcode', i)

        #================== Database Connection ===================
        curs.execute("INSERT INTO sdata_stock2 (s_name,s_code) VALUES ('%s', '%s')"%(a,b))
        conn.commit()
    XAQueryEvents.queryState = 0


# sql_string = "SELECT * FROM blog_post"
#
# sql_string = 'INSERT INTO stockdata_stock2(s_name,s_code,s_open,s_close,s_date) VALUES("sdn","099220","%s","%s","%s")'%(a,b,c)
# print(inXAQuery.GetFieldData('t8413OutBlock1', 'close', 1))




# #================== Database Connection =================== ed
#
# # sql_string = "SELECT * FROM blog_post"
# sql_string = "INSERT into stockdata_stock values('sdn','099220','')"
# curs.execute(sql_string)
# result = curs.fetchall()
# print(result)
# conn.commit()

