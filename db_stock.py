import psycopg2
import win32com.client
import pythoncom
import time
import sqlite3

#================== Database Connection =================== st
# conn_string = "host='localhost' dbname ='Anthouse' user='' password=''"
try:
        conn = sqlite3.connect("db.sqlite3")
except:
        print("error database connection")
curs = conn.cursor()




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



    inXAQuery2 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
    inXAQuery2.LoadFromResFile("C:\\eBEST\\xingAPI\\Res\\t1102.res")

    curs.execute("SELECT s_code FROM sdata_stock2")
    result = curs.fetchall()
    print(result)
    for i in result:
        s_codelist = list(i)
        print(s_codelist[0])

        inXAQuery2.SetFieldData('t1102InBlock', 'shcode', 0 , "%s"%(s_codelist[0]))
        inXAQuery2.Request(0)



        while XAQueryEvents.queryState == 0:
            pythoncom.PumpWaitingMessages()
            time.sleep(0.03)


        hname = inXAQuery2.GetFieldData('t1102OutBlock','hname',0)
        price = inXAQuery2.GetFieldData('t1102OutBlock','price',0)
        sign = inXAQuery2.GetFieldData('t1102OutBlock','sign',0)
        change = inXAQuery2.GetFieldData('t1102OutBlock','change',0)
        diff = inXAQuery2.GetFieldData('t1102OutBlock','diff',0)
        volume = inXAQuery2.GetFieldData('t1102OutBlock','volume',0)
        recprice = inXAQuery2.GetFieldData('t1102OutBlock','recprice',0)
        avgp = inXAQuery2.GetFieldData('t1102OutBlock','avg',0)
        uplmtprice = inXAQuery2.GetFieldData('t1102OutBlock','uplmtprice',0)
        dnlmtprice = inXAQuery2.GetFieldData('t1102OutBlock','dnlmtprice',0)
        jnilvolume = inXAQuery2.GetFieldData('t1102OutBlock','jnilvolume',0)
        volumediff = inXAQuery2.GetFieldData('t1102OutBlock','volumediff',0)
        openp = inXAQuery2.GetFieldData('t1102OutBlock','open',0)
        opentime = inXAQuery2.GetFieldData('t1102OutBlock','opentime',0)
        high = inXAQuery2.GetFieldData('t1102OutBlock','high',0)
        hightime = inXAQuery2.GetFieldData('t1102OutBlock','hightime',0)
        low = inXAQuery2.GetFieldData('t1102OutBlock','low',0)
        lowtime = inXAQuery2.GetFieldData('t1102OutBlock','lowtime',0)
        high52w = inXAQuery2.GetFieldData('t1102OutBlock','high52w',0)
        high52wdate = inXAQuery2.GetFieldData('t1102OutBlock','high52wdate',0)
        low52w = inXAQuery2.GetFieldData('t1102OutBlock','low52w',0)
        low52wdate = inXAQuery2.GetFieldData('t1102OutBlock','low52wdate',0)
        exhratio = inXAQuery2.GetFieldData('t1102OutBlock','exhratio',0)
        per = inXAQuery2.GetFieldData('t1102OutBlock','per',0)
        pbrx = inXAQuery2.GetFieldData('t1102OutBlock','pbrx',0)
        listing = inXAQuery2.GetFieldData('t1102OutBlock','listing',0)
        jkrate = inXAQuery2.GetFieldData('t1102OutBlock','jkrate',0)
        memedan = inXAQuery2.GetFieldData('t1102OutBlock','memedan',0)
        vol = inXAQuery2.GetFieldData('t1102OutBlock','vol',0)
        shcode = inXAQuery2.GetFieldData('t1102OutBlock','shcode',0)
        valuep = inXAQuery2.GetFieldData('t1102OutBlock','value',0)
        highyear = inXAQuery2.GetFieldData('t1102OutBlock','highyear',0)
        highyeardate = inXAQuery2.GetFieldData('t1102OutBlock','highyeardate',0)
        lowyear = inXAQuery2.GetFieldData('t1102OutBlock','lowyear',0)
        lowyeardate = inXAQuery2.GetFieldData('t1102OutBlock','lowyeardate',0)


        print(hname)
        print(shcode)

        curs.execute("INSERT INTO sdata_stock_current (hname,price,sign,change,diff,volume,recprice,avgp,uplmtprice,dnlmtprice,jnilvolume,volumediff,openp,opentime,high,hightime,low,lowtime,high52w,high52wdate,low52w,low52wdate,exhratio,per,pbrx,listing,jkrate,memedan,vol,shcode,valuep,highyear,highyeardate,lowyear,lowyeardate) VALUES ('%s','%s', '%s', '%s','%s', '%s','%s','%s', '%s','%s','%s', '%s','%s','%s', '%s','%s','%s', '%s', '%s','%s', '%s','%s','%s', '%s','%s','%s','%s', '%s','%s','%s', '%s','%s','%s', '%s','%s')"%(hname,price,sign,change,diff,volume,recprice,avgp,uplmtprice,dnlmtprice,jnilvolume,volumediff,openp,opentime,high,hightime,low,lowtime,high52w,high52wdate,low52w,low52wdate,exhratio,per,pbrx,listing,jkrate,memedan,vol,shcode,valuep,highyear,highyeardate,lowyear,lowyeardate))

        print(XAQueryEvents.queryState)
        XAQueryEvents.queryState = 0
        conn.commit()