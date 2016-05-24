# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from operate import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class MainDialog(QTabWidget):
    def __init__(self, parent=None):

        self.residence = 0
        self.sex = 0
        self.occupation = 0
        self.education = 0
        self.praise = 0

        super(MainDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("知乎通"))
        self.setMaximumSize(400, 300)
        self.setMinimumSize(400, 300)

        label0 = QLabel(self.tr(""))
        label1 = QLabel(self.tr("问题URL:"))
        label2 = QLabel(self.tr("问题URL:"))
        label3 = QLabel(self.tr("问题URL:"))
        label4 = QLabel(self.tr("性别:"))
        label5 = QLabel(self.tr("行业:"))
        label6 = QLabel(self.tr("居住地:"))
        label7 = QLabel(self.tr("教育水平:"))
        label8 = QLabel(self.tr("得赞比:"))

        self.questionEdit1 = QLineEdit()
        self.questionEdit2 = QLineEdit()
        self.questionEdit3 = QLineEdit()

        analysisrespondentPushButton = QPushButton(self.tr("分析答题者"))
        analysisfollowerPushButton = QPushButton(self.tr("分析关注者"))
        findanswerPushButton = QPushButton(self.tr("查找答案"))
        findquestionPushButton = QPushButton(self.tr("查找问题"))

        self.sexComboBox = QComboBox()
        self.occupationComboBox = QComboBox()
        self.sexComboBox.insertItem(0, self.tr("请选择"))
        self.sexComboBox.insertItem(1, self.tr("男"))
        self.sexComboBox.insertItem(2, self.tr("女"))
        self.occupationComboBox.insertItem(0, self.tr("请选择"))
        self.occupationComboBox.insertItem(1, self.tr("高新科技"))
        self.occupationComboBox.insertItem(2, self.tr("信息传媒"))
        self.occupationComboBox.insertItem(3, self.tr("服务业"))
        self.occupationComboBox.insertItem(4, self.tr("金融"))
        self.occupationComboBox.insertItem(5, self.tr("教育"))
        self.occupationComboBox.insertItem(6, self.tr("医疗服务"))
        self.occupationComboBox.insertItem(7, self.tr("艺术娱乐"))
        self.occupationComboBox.insertItem(8, self.tr("制造加工"))
        self.occupationComboBox.insertItem(9, self.tr("地产建筑"))
        self.occupationComboBox.insertItem(10, self.tr("贸易零售"))
        self.occupationComboBox.insertItem(11, self.tr("公共服务"))
        self.occupationComboBox.insertItem(12, self.tr("开采冶金"))
        self.occupationComboBox.insertItem(13, self.tr("交通仓储"))
        self.occupationComboBox.insertItem(14, self.tr("农林牧渔"))

        self.residenceCheckBox = QCheckBox()
        self.residenceCheckBox.setText(self.tr("比例最高"))
        self.educationCheckboBox = QCheckBox()
        self.educationCheckboBox.setText(self.tr("本科及以上"))
        self.praiseCheckboBox = QCheckBox()
        self.praiseCheckboBox.setText(self.tr("排名前5"))

        firstLayout = QGridLayout()
        firstLayout.addWidget(label1, 0, 0)
        firstLayout.addWidget(self.questionEdit1, 0, 1, 1, 3)
        firstLayout.addWidget(analysisrespondentPushButton, 1, 3)

        secondLayout = QGridLayout()
        secondLayout.addWidget(label2, 0, 0)
        secondLayout.addWidget(self.questionEdit2, 0, 1, 1, 3)
        secondLayout.addWidget(analysisfollowerPushButton, 1, 3)

        thirdLayout = QGridLayout()
        thirdLayout.addWidget(label3, 0, 0)
        thirdLayout.addWidget(self.questionEdit3, 0, 1, 1, 4)
        thirdLayout.addWidget(label4, 1, 0)
        thirdLayout.addWidget(self.sexComboBox, 1, 1)
        thirdLayout.addWidget(label5, 2, 0)
        thirdLayout.addWidget(self.occupationComboBox, 2, 1)
        thirdLayout.addWidget(label6, 3, 0)
        thirdLayout.addWidget(self.residenceCheckBox, 3, 1)
        thirdLayout.addWidget(label7, 1, 3)
        thirdLayout.addWidget(self.educationCheckboBox, 1, 4)
        thirdLayout.addWidget(label8, 2, 3)
        thirdLayout.addWidget(self.praiseCheckboBox, 2, 4)
        thirdLayout.addWidget(findanswerPushButton, 4, 4)

        forthLayout = QGridLayout()
        forthLayout.addWidget(label0, 0, 0)
        forthLayout.addWidget(label0, 0, 2)
        forthLayout.addWidget(findquestionPushButton, 0, 1)

        tab1 = QWidget()
        #        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        self.addTab(tab1, self.tr("答题者分析"))
        #       self.addTab(tab2,self.tr("关注者分析"))
        self.addTab(tab3, self.tr("答案查找"))
        self.addTab(tab4, self.tr("问题查找"))
        tab1.setLayout(firstLayout)
        #        tab2.setLayout(secondLayout)
        tab3.setLayout(thirdLayout)
        tab4.setLayout(forthLayout)

        self.residenceCheckBox.stateChanged.connect(self.chageResidence)

        self.connect(analysisrespondentPushButton, SIGNAL("clicked()"), self.soltAnalysisrespondent)
        #        self.connect(analysisfollowerPushButton, SIGNAL("clicked()"), self.soltAnalysisfollower)
        self.connect(findanswerPushButton, SIGNAL("clicked()"), self.soltFindanswer)
        self.connect(findquestionPushButton, SIGNAL("clicked()"), self.soltFindquestion)

        self.connect(self.occupationComboBox, SIGNAL("activated(int)"), self.changeOccupation)
        self.connect(self.sexComboBox, SIGNAL("activated(int)"), self.changeSex)

    def soltAnalysisrespondent(self):
        question = self.questionEdit1.text()
        ar = Analysisrespondent(question)
        ar.analysis()
        analysisrespondentDialog = AnalysisrespondentDispaly()
        analysisrespondentDialog.exec_()

    #    def soltAnalysisfollower(self):
    #        question = self.questionEdit2.text()
    #        af = Analysisfollower(question)
    #        af.analysis()
    #        analysisfollowerDialog =AnalysisfollowerDispaly()
    #        analysisfollowerDialog.exec_()

    def soltFindanswer(self):
        question = self.questionEdit3.text()
        fa = Findanswer(self.sex, self.residence, self.occupation, self.education, self.praise, question)
        fa.find()
        findanswerDispaly = FindanswerDispaly()
        findanswerDispaly.exec_()

    def soltFindquestion(self):
        fq = Findquestion()
        fq.find()
        findquestionDispaly = FindquestionDispaly()
        findquestionDispaly.exec_()

    def changeSex(self):
        self.sex = self.sexComboBox.currentIndex()

    def changeOccupation(self):
        self.occupation = self.occupationComboBox.currentIndex()

    def chageResidence(self, state):
        if state == Qt.Checked:
            self.residence = 1
        else:
            self.residence = 0

    def changeEducation(self, state):
        if state == Qt.Checked:
            self.education = 1
        else:
            self.education = 0

    def changePraise(self, state):
        if state == Qt.Checked:
            self.praise = 1
        else:
            self.praise = 0


class AnalysisrespondentDispaly(QDialog):
    def __init__(self, parent=None):
        super(AnalysisrespondentDispaly, self).__init__(parent)
        self.setWindowTitle(self.tr("分析结果"))
        self.setMaximumSize(400, 600)
        self.setMinimumSize(400, 600)


class AnalysisfollowerDispaly(QDialog):
    def __init__(self, parent=None):
        super(AnalysisfollowerDispaly, self).__init__(parent)
        self.setWindowTitle(self.tr("分析结果"))
        self.setMaximumSize(400, 600)
        self.setMinimumSize(400, 600)


class FindanswerDispaly(QDialog):
    def __init__(self, parent=None):
        super(FindanswerDispaly, self).__init__(parent)
        self.setWindowTitle(self.tr("查找结果"))
        self.setMaximumSize(400, 600)
        self.setMinimumSize(400, 600)


class FindquestionDispaly(QDialog):
    def __init__(self, parent=None):
        super(FindquestionDispaly, self).__init__(parent)
        self.setWindowTitle(self.tr("查找结果"))
        self.setMaximumSize(400, 600)
        self.setMinimumSize(400, 600)


def main():
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    mainDialog.show()
    app.exec_()


if __name__ == '__main__':
    main()
