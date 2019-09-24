import hashlib
import base64
import jwt
import datetime
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class jwtserver():
    # コンストラクタ
    def __init__(self):
        # ハッシュ値を生成する
        self.passphrase = 'pitadigi'

        # 鍵情報をロードする
        self.loadKeys()

    # 秘密鍵、公開鍵をロードする
    def loadKeys(self):
        # 秘密鍵をロードする
        self.loadPrivateKey()
        # 公開鍵を生成する
        self.createPublicKey()
    
    # 公開鍵を生成する
    def createPublicKey(self):
        self.publickey = self.privatekey.publickey()

    # 秘密鍵をロードする
    def loadPrivateKey(self):
        self.privatekey = RSA.importKey(self.loadFile('keys/privateKey.pem'))

    # 指定されたファイルの内容をロードする
    def loadFile(self, fileName):
        f = open(fileName, 'r')
        data = f.read()
        f.close()

        return(data)

    # ハッシュ値を公開鍵で暗号化しアクセストークンを作成する
    def getAccessToken(self):
        cipher = PKCS1_OAEP.new(self.publickey)
        cipherText = cipher.encrypt(self.passphrase.encode())
        
        return base64.b64encode(cipherText)

    # アクセストークンを認証してJWTを返す
    def auth(self, accessToken):
        retJwt = None

        # アクセストークンをbase64でデコードする
        cipherText = base64.b64decode(accessToken)
        # 秘密鍵で復号化する
        cipher = PKCS1_OAEP.new(self.privatekey)
        decryptPassPhrase = cipher.decrypt(cipherText)

        # 復号化したものがパスフレーズと同じかをチェックする
        if(decryptPassPhrase.decode() == self.passphrase):
            # JWTを生成する
            retJwt = self.createJWT()
        else:
            print(decryptPassPhrase.decode())

        return retJwt

    # JWTを生成する
    def createJWT(self):
        # 秘密鍵でJWTを生成する
        # JWTの有効期限(exp)は1時間
        # 1時間経過後に同じJWTでアクセスするとエラーになる
        return jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1 * 60 * 60)}, self.privatekey.exportKey(format='PEM'), algorithm='RS256')

    # データを取得する
    def getData(self, jwtdata):
        data = None
        # 秘密鍵でJWTを検証する
        try:
            payload = jwt.decode(jwtdata, self.publickey.exportKey(format='PEM'), algorithms=['RS256'])
            data = 'Welcome to pitadigi'
        except jwt.ExpiredSignatureError:
            data = 'jwt error'
        
        return data

