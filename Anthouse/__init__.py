import win32com.client
import pythoncom

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

    nCount = inXASession.GetAccountListCount()
    print("The number of account: ", nCount)

    #--------------------------------------------------------------------------
    # Get single data
    #--------------------------------------------------------------------------
    inXAQuery = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
    inXAQuery.LoadFromResFile("C:\\eBEST\\xingAPI\\Res\\t8413.res")
    inXAQuery.SetFieldData('t8413InBlock', 'shcode', 0, '099220')
    inXAQuery.SetFieldData('t8413InBlock', 'gubun', 0, '2')
    inXAQuery.SetFieldData('t8413InBlock', 'sdate', 0, '20140101')
    inXAQuery.SetFieldData('t8413InBlock', 'edate', 0, '20160118')
    inXAQuery.SetFieldData('t8413InBlock', 'comp_yn', 0, 'N')

    inXAQuery.Request(0)

    while XAQueryEvents.queryState == 0:
        pythoncom.PumpWaitingMessages()


    # Get FieldData
    nCount = inXAQuery.GetBlockCount('t8413OutBlock1')
    for i in range(nCount):
        print(inXAQuery.GetFieldData('t8413OutBlock1', 'date', i), ":", inXAQuery.GetFieldData('t8413OutBlock1', 'close', i))

    XAQueryEvents.queryState = 0


