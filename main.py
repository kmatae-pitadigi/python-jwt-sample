import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QLabel, QTextEdit, QGridLayout, QPushButton)

class App(QWidget):

    # コンストラクタ
    def __init__(self):
        super().__init__()
        self.title ='Python JWT Sample'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 400
        self.initUI()
    
    # 画面初期化、表示
    def initUI(self):
        # データをロードする
        self.loadData()

        # 画面を中央に表示
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.frameGeometry() \
            .moveCenter(
                QDesktopWidget()
                .availableGeometry()
                .center()
            )
        
        # コントロールの配置
        self.initControl()

        self.show()

    # データのロード
    def loadData(self):
        # base64でエンコードした公開鍵を読み込む
        file_pubkey64 = open('keys/publicKey.base64')
        self.pubkey64 = file_pubkey64.read()
        file_pubkey64.close()

    # コントロール配置
    def initControl(self):
        # コントロールの作成
        lblPublicKey = QLabel('公開鍵(base64)')
        txtPublicKey = QTextEdit(self.pubkey64)
        cmdSubmit = QPushButton('実行')

        # コントロールをグリッドに表示
        grid = QGridLayout()

        # コントロール間のスペースを設定
        grid.setSpacing(10)

        # コントロールの配置
        grid.addWidget(lblPublicKey, 1, 0)
        grid.addWidget(txtPublicKey, 1, 1)
        grid.addWidget(cmdSubmit, 2, 1)

        self.setLayout(grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

