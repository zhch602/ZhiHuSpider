# -*- coding: utf-8 -*-

from __future__ import division
from zhihu import *
from collections import Counter
import operator


class Analysisrespondent():
    url = ""
    residence = []
    occupation1 = 0
    occupation2 = 0
    occupation3 = 0
    occupation4 = 0
    occupation5 = 0
    occupation6 = 0
    occupation7 = 0
    occupation8 = 0
    occupation9 = 0
    occupation10 = 0
    occupation11 = 0
    occupation12 = 0
    occupation13 = 0
    occupation = [occupation1, occupation2, occupation3, occupation4, occupation5, occupation6, occupation7,
                  occupation8,
                  occupation9, occupation10, occupation11, occupation12, occupation13]
    undergraduate = 0
    highschool = 0
    education = [undergraduate, highschool]
    agree_num = 0
    answers_num = 0
    occupations_list = []
    residence_list = []
    unknown = 0
    female = 0
    male = 0
    sex = [male,female,unknown]
    proportions_list = []

    def __init__(self, url):

        self.url = url

    def display(self):
        print "female:"+str(self.female)+" "+"male:"+str(self.male)

    def analysis(self):
        question = Question(self.url)
        answers = question.get_all_answers()

        for answer in answers:
            author = answer.get_author()
            author_id = author.get_user_id()
            if (author_id.decode('GBK') == "匿名用户"):
                continue
            author_url = author.user_url
            sex = author.get_gender()
            agree_num = author.get_agree_num()
            answers_num = author.get_answers_num()
            agree_answers = agree_num/answers_num
            print agree_answers
            #proportion = [author.get_user_id(),author.user_url,agree_num/answers_num]
            #self.proportions_list.append(proportion)
            if (sex == 'unknown'):
                self.unknown += 1
            elif (sex == 'female'):
                self.female += 1
            else:
                self.male += 1
            #occupation = author.get_occupation
            #if (occupation != 0):
            #    self.occupations_list.append(occupation)
            #residence = author.get_residence()
            #if (residence != 0):
            #    self.residence_list.append(residence)
            #education = author.get_education()
            #if (education != 0):
            #    self.undergraduate += 1
            #else:
            #    self.highschool += 1


# class Analysisfollower():

#    url = ""

#    def __init__(self,url):

#        self.url = url

#    def analysis(self):
#        question = Question(self.url)
#        followers_num = question.get_answers_num()
#        answers = question.get_all_answers()

class Findanswer():
    sex = 0
    sex_text = ""
    residence = 0
    residence_list = []
    occupation = 0
    occupations_list = []
    education = 0
    praise = 0
    url = ""
    answers_list = []
    undergraduate = 0
    highschool = 0

    def __init__(self, sex, residence, occupation, education, praise, url):

        self.sex = sex
        if (sex == 1):
            self.sex_text = 'male'
        else:
            self.sex_text = 'female'
        self.residence = residence
        self.occupation = occupation
        if (occupation == 1):
            self.occupations_list.append('高新科技')
            self.occupations_list.append('互联网')
            self.occupations_list.append('电子商务')
            self.occupations_list.append('电子游戏')
            self.occupations_list.append('计算机软件')
            self.occupations_list.append('计算机硬件')
        elif (occupation == 2):
            self.occupations_list.append('信息传媒')
            self.occupations_list.append('出版社')
            self.occupations_list.append('电影录音')
            self.occupations_list.append('广播电视')
            self.occupations_list.append('通信')
        elif (occupation == 3):
            self.occupations_list.append('金融')
            self.occupations_list.append('银行')
            self.occupations_list.append('资本投资')
            self.occupations_list.append('证券投资')
            self.occupations_list.append('保险')
            self.occupations_list.append('信贷')
            self.occupations_list.append('财务')
            self.occupations_list.append('审计')
            self.occupations_list.append('信息传媒')
            self.occupations_list.append('信息传媒')
        elif (occupation == 4):
            self.occupations_list.append('服务业')
            self.occupations_list.append('法律')
            self.occupations_list.append('餐饮')
            self.occupations_list.append('酒店')
            self.occupations_list.append('旅游')
            self.occupations_list.append('广告')
            self.occupations_list.append('公关')
            self.occupations_list.append('景观')
            self.occupations_list.append('咨询分析')
            self.occupations_list.append('市场推广')
            self.occupations_list.append('人力资源')
            self.occupations_list.append('社工服务')
            self.occupations_list.append('养老服务')
        elif (occupation == 5):
            self.occupations_list.append('教育')
            self.occupations_list.append('高等教育')
            self.occupations_list.append('基础教育')
            self.occupations_list.append('职业教育')
            self.occupations_list.append('幼儿教育')
            self.occupations_list.append('特殊教育')
            self.occupations_list.append('培训')
        elif (occupation == 6):
            self.occupations_list.append('医疗服务')
            self.occupations_list.append('临床医疗')
            self.occupations_list.append('制药')
            self.occupations_list.append('保健')
            self.occupations_list.append('美容')
            self.occupations_list.append('医疗器材')
            self.occupations_list.append('生物工程')
            self.occupations_list.append('疗养服务')
            self.occupations_list.append('护理服务')
        elif (occupation == 7):
            self.occupations_list.append('艺术娱乐')
            self.occupations_list.append('创意艺术')
            self.occupations_list.append('体育健身')
            self.occupations_list.append('娱乐休闲')
            self.occupations_list.append('图书馆')
            self.occupations_list.append('博物馆')
            self.occupations_list.append('策展')
            self.occupations_list.append('博彩')
        elif (occupation == 8):
            self.occupations_list.append('制造加工')
            self.occupations_list.append('食品饮料业')
            self.occupations_list.append('纺织皮革业')
            self.occupations_list.append('服装业')
            self.occupations_list.append('烟草业')
            self.occupations_list.append('造纸业')
            self.occupations_list.append('印刷业')
            self.occupations_list.append('化工业')
            self.occupations_list.append('汽车')
            self.occupations_list.append('家具')
            self.occupations_list.append('电子电器')
            self.occupations_list.append('机械设备')
            self.occupations_list.append('塑料工业')
            self.occupations_list.append('金属加工')
            self.occupations_list.append('军火')
        elif (occupation == 9):
            self.occupations_list.append('地产建筑')
            self.occupations_list.append('房地产')
            self.occupations_list.append('装饰装潢')
            self.occupations_list.append('物业服务')
            self.occupations_list.append('特殊建造')
            self.occupations_list.append('建筑设备')
        elif (occupation == 10):
            self.occupations_list.append('贸易零售')
            self.occupations_list.append('零售')
            self.occupations_list.append('大宗交易')
            self.occupations_list.append('进出口贸易')
        elif (occupation == 11):
            self.occupations_list.append('公共服务')
            self.occupations_list.append('政府')
            self.occupations_list.append('国防军事')
            self.occupations_list.append('航天')
            self.occupations_list.append('科研')
            self.occupations_list.append('给排水')
            self.occupations_list.append('水利能源')
            self.occupations_list.append('电力电网')
            self.occupations_list.append('公共管理')
            self.occupations_list.append('环境保护')
            self.occupations_list.append('非营利组织')
        elif (occupation == 12):
            self.occupations_list.append('开采冶金')
            self.occupations_list.append('煤炭工业')
            self.occupations_list.append('石油工业')
            self.occupations_list.append('黑色金属')
            self.occupations_list.append('有色金属')
            self.occupations_list.append('土砂石开采')
            self.occupations_list.append('地热开采')
        elif (occupation == 13):
            self.occupations_list.append('交通仓储')
            self.occupations_list.append('邮政')
            self.occupations_list.append('物流递送')
            self.occupations_list.append('地面运输')
            self.occupations_list.append('铁路运输')
            self.occupations_list.append('管线运输')
            self.occupations_list.append('航运业')
            self.occupations_list.append('民用航空业')
        else:
            self.occupations_list.append('农林牧渔')
            self.occupations_list.append('种植业')
            self.occupations_list.append('畜牧养殖业')
            self.occupations_list.append('林业')
            self.occupations_list.append('渔业')
        self.education = education
        self.praise = praise
        self.url = url

    def find(self):
        question = Question(self.url)
        answers = question.get_all_answers()

        for answer in answers:
            author = answer.get_author()
            if (self.sex != 0):
                if (self.sex_text == author.get_gender()):
                    self.answers_list.append(author)
                else:
                    continue
            if (self.occupation != 0):
                for occupation in self.occupations_list:
                    if (occupation == author.get_reoccupation()):
                        break
                    self.answers_list.pop()
            if (self.residence == 1):
                self.residence_list.append(author.get_residence())
            if (self.education == 1):
                education = author.get_education()
                if (education != 0):
                    self.undergraduate += 1
                else:
                    self.highschool += 1
            if (self.praise == 1):
                agree_num = author.get_agree_num()
                answers_num = author.get_answers_num()


        residence_count = Counter(self.residence_list)
        sorted_residence = sorted(residence_count.iteritems(), key=operator.itemgetter(1), reverse=True)
        print sorted_residence[0][0]


class Findquestion():
    def find(self):
        print 1
