import server

class jwtclient():
    # コンストラクタ
    def __init__(self):
        # JWT Server
        self.server = server.jwtserver()

    # 開始
    def start(self):
        self.accessToken = self.server.getAccessToken()
        return self.accessToken

    # 認証
    def auth(self):
        self.jwtdata = self.server.auth(self.accessToken)
        return self.jwtdata
    
    # データ取得
    def getData(self):
        return self.server.getData(self.jwtdata)
