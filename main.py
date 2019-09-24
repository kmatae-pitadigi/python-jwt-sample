import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QLabel, QTextEdit, QGridLayout, QPushButton)
import client

class App(QWidget):

    # コンストラクタ
    def __init__(self):
        super().__init__()
        self.client = client.jwtclient()

        self.title ='Python JWT Sample'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 400
        self.initUI()
    
    # 画面初期化、表示
    def initUI(self):
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

    # コントロール配置
    def initControl(self):
        # コントロールの作成
        lblAccessToken = QLabel('アクセストークン')
        self.txtAccessToken = QTextEdit()
        lblJwt = QLabel('JWT')
        self.txtJwt = QTextEdit()
        cmdSubmit = QPushButton('実行')
        self.lblData = QLabel()

        # コントロールをグリッドに表示
        grid = QGridLayout()

        # コントロール間のスペースを設定
        grid.setSpacing(10)

        # コントロールの配置
        grid.addWidget(lblAccessToken, 1, 0)
        grid.addWidget(self.txtAccessToken, 1, 1)
        grid.addWidget(lblJwt, 2, 0)
        grid.addWidget(self.txtJwt, 2, 1)
        grid.addWidget(cmdSubmit, 3, 1)
        grid.addWidget(self.lblData, 4, 1)

        # 実行ボタンにイベントを設定する
        cmdSubmit.clicked.connect(self.handleSubmitClicked)

        self.setLayout(grid)

    # 実行ボタンクリック時の処理
    def handleSubmitClicked(self):
        accessToken = self.client.start()
        self.txtAccessToken.setText(accessToken.decode())

        jwt = self.client.auth()

        self.txtJwt.setText(jwt.decode())

        data = self.client.getData()

        self.lblData.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

