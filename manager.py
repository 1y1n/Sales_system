# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.template
import torndb
import os.path
import time,datetime
#import pygal
#import json
#from echarts import Echart, Legend, Bar, Axis
import calendar



from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)
define("hostaddress", default='127.0.0.1:3306', help="sql host", type=str)
define("dbname", default="kucun", help="database name", type=str)#kucun
define("username", default="root", help="db username", type=str)
define("password", default="KUCUN123456", help="db password", type=str)#KUCUN123456




'''
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
'''

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        #self.set_secure_cookie('username','value',expires_days=1)
        return self.get_secure_cookie("username")
    def get_power(self):
        sql='select power from user where username="%s"' %(tornado.escape.xhtml_escape(self.current_user))
        res = self.application.db.get(sql)
        return res['power']

class Login_in_Handler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect('login_success')
        else:
            self.render('index.html')
    def post(self):
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        # match sql data
        if username and pwd and self.application.db.query('select id from user where username="%s" and password="%s"' %(username,pwd)):
            self.set_secure_cookie("username", self.get_argument("username"))
            #sql = 'select power from user where id=%d' % (int(id[0]['id']))
            #res = self.application.db.query(sql)
            #power = res[0]['power']
            self.redirect("/login_success")

        else:
            self.write('Warmning.')


class Login_success(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        default_end_time = (datetime.datetime.now()).strftime('%Y-%m-%d')
        default_end_time_sql = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        user = tornado.escape.xhtml_escape(self.current_user)#获取登陆用户名

        mobile_sql = 'select * from mobile where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                     'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' % (self.default_end_time, self.default_end_time_sql)
        parts_sql = 'select * from parts where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                    'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' % (self.default_end_time, self.default_end_time_sql)
        card_sql = 'select * from mobile_card where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                   'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' % (self.default_end_time, self.default_end_time_sql)
        gift_sql = 'select * from gift where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                   'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' % (self.default_end_time, self.default_end_time_sql)
        mobile_res = self.application.db.query(mobile_sql)
        parts_res = self.application.db.query(parts_sql)
        card_res = self.application.db.query(card_sql)
        gift_res = self.application.db.query(gift_sql)

        self.render('login_success.html', user=self.get_power(),
                    mobile_res=mobile_res,parts_res=parts_res,card_res=card_res,gift_res=gift_res)


class Logout(BaseHandler):
    def get(self):
        #if (self.get_argument("logout", None)):
        self.clear_cookie("username")
        self.redirect("/")


#账单
class Count(BaseHandler):
    
    @tornado.web.authenticated
    def get(self):
        default_end_time = (datetime.datetime.now()).strftime('%Y-%m-%d')
        default_end_time_sql = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        default_begin_time = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        mobile_a_keys, mobile_b, mobile_c = self.chart('Day', 'mobile')
        parts_a_keys, parts_b, parts_c = self.chart('Day', 'parts')
        card_a_keys, card_b, card_c, = self.chart('Day', 'card')  # 以上为手机数量和品牌  ,按　天　计算
        all_data = self.list_add(self.list_add(mobile_c, parts_c), card_c)  # 所有总收入
        mobile_sql = 'select * from mobile where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                   'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' %(self.default_begin_time,self.default_end_time_sql)
        parts_sql = 'select * from parts where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                   'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' %(self.default_begin_time,self.default_end_time_sql)
        card_sql = 'select * from mobile_card where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                   'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' %(self.default_begin_time,self.default_end_time_sql)
        gift_sql = 'select * from gift where ckrq between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                   'and  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d")' %(self.default_begin_time,self.default_end_time_sql)
        mobile_res = self.application.db.query(mobile_sql)
        parts_res = self.application.db.query(parts_sql)
        card_res = self.application.db.query(card_sql)
        gift_res = self.application.db.query(gift_sql)
        self.render("count.html", user=self.get_power(),
                    mobile_a_keys=mobile_a_keys, mobile_b=mobile_b, mobile_c=mobile_c,
                    parts_a_keys=parts_a_keys, parts_b=parts_b, parts_c=parts_c,
                    card_a_keys=card_a_keys, card_b=card_b, card_c=card_c,
                    all_data=all_data, mobile_res=mobile_res, parts_res=parts_res, card_res=card_res,gift_res=gift_res,
                    date=self.getEveryDay(self.default_begin_time,
                                          self.default_end_time))  # (self.default_time,self.default_time)

    @tornado.web.authenticated
    def post(self):
        begin_date = self.get_argument('begin_date', None)
        end_date = self.get_argument('end_date', None)
        begin_month = self.get_argument('begin_month', None)
        end_month = self.get_argument('end_month', None)
        # print begin_date,end_date,begin_month,end_month
        if begin_date != '' and end_date != '':
            mobile_a_keys, mobile_b, mobile_c= self.chart('Day', 'mobile', begin_date, end_date)
            parts_a_keys, parts_b, parts_c = self.chart('Day', 'parts', begin_date, end_date)
            card_a_keys, card_b, card_c = self.chart('Day', 'card', begin_date, end_date)
            all_data = self.list_add(self.list_add(mobile_c, parts_c), card_c)
            mobile_sql = 'select * from mobile where DATE_FORMAT(ckrq, "%%%%Y-%%%%m-%%%%d") between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                         'and  DATE_FORMAT("%s 23:59:59","%%%%Y-%%%%m-%%%%d  %%%%H:%%%%M:%%%%S")' % (
                begin_date, end_date)
            parts_sql = 'select * from parts where DATE_FORMAT(ckrq, "%%%%Y-%%%%m-%%%%d") between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                        'and  DATE_FORMAT("%s 23:59:59","%%%%Y-%%%%m-%%%%d  %%%%H:%%%%M:%%%%S")' % (
                begin_date, end_date)
            card_sql = 'select * from mobile_card where DATE_FORMAT(ckrq, "%%%%Y-%%%%m-%%%%d") between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                       'and  DATE_FORMAT("%s 23:59:59","%%%%Y-%%%%m-%%%%d  %%%%H:%%%%M:%%%%S")' % (
                begin_date, end_date)
            gift_sql = 'select * from gift where DATE_FORMAT(ckrq, "%%%%Y-%%%%m-%%%%d") between  DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") ' \
                       'and  DATE_FORMAT("%s 23:59:59","%%%%Y-%%%%m-%%%%d  %%%%H:%%%%M:%%%%S")' % (
                begin_date, end_date)
            mobile_res = self.application.db.query(mobile_sql)
            parts_res = self.application.db.query(parts_sql)
            card_res = self.application.db.query(card_sql)
            gift_res = self.application.db.query(gift_sql)
            self.render("count.html", user=self.get_power(),
                        mobile_a_keys=mobile_a_keys, mobile_b=mobile_b, mobile_c=mobile_c,
                        parts_a_keys=parts_a_keys, parts_b=parts_b, parts_c=parts_c,
                        card_a_keys=card_a_keys, card_b=card_b, card_c=card_c,
                        all_data=all_data, mobile_res=mobile_res, parts_res=parts_res, card_res=card_res,gift_res=gift_res,
                        date=self.getEveryDay(begin_date, end_date))
        elif begin_month != '' and end_month != '':
            mobile_a_keys, mobile_b, mobile_c = self.chart('Month', 'mobile', begin_month, end_month)  # 以月份计算
            parts_a_keys, parts_b, parts_c = self.chart('Month', 'parts', begin_month, end_month)
            card_a_keys, card_b, card_c = self.chart('Month', 'card', begin_month, end_month)
            all_data = self.list_add(self.list_add(mobile_c, parts_c), card_c)
            mobile_sql = 'select * from mobile where DATE_FORMAT(ckrq, "%%%%Y-%%%%m") between  DATE_FORMAT("%s-01","%%%%Y-%%%%m") ' \
                         'and  DATE_FORMAT("%s-01","%%%%Y-%%%%m")' % (
                begin_month, end_month)
            parts_sql = 'select * from parts where DATE_FORMAT(ckrq, "%%%%Y-%%%%m") between  DATE_FORMAT("%s-01","%%%%Y-%%%%m") ' \
                        'and  DATE_FORMAT("%s-01","%%%%Y-%%%%m")' % (
                begin_month, end_month)
            card_sql = 'select * from mobile_card where DATE_FORMAT(ckrq, "%%%%Y-%%%%m") between  DATE_FORMAT("%s-01","%%%%Y-%%%%m") ' \
                       'and  DATE_FORMAT("%s-01","%%%%Y-%%%%m")' % (
                begin_month, end_month)
            gift_sql = 'select * from gift where DATE_FORMAT(ckrq, "%%%%Y-%%%%m") between  DATE_FORMAT("%s-01","%%%%Y-%%%%m") ' \
                       'and  DATE_FORMAT("%s-01","%%%%Y-%%%%m")' % (
                begin_month, end_month)
            mobile_res = self.application.db.query(mobile_sql)
            parts_res = self.application.db.query(parts_sql)
            card_res = self.application.db.query(card_sql)
            gift_res = self.application.db.query(gift_sql)
            self.render("count.html", user=self.get_power(),
                        mobile_a_keys=mobile_a_keys, mobile_b=mobile_b, mobile_c=mobile_c,
                        parts_a_keys=parts_a_keys, parts_b=parts_b, parts_c=parts_c,
                        card_a_keys=card_a_keys, card_b=card_b, card_c=card_c,
                        all_data=all_data, mobile_res=mobile_res, parts_res=parts_res, card_res=card_res,gift_res=gift_res,
                        date=self.getBetweenMonth(begin_month, end_month))
        else:
            self.write('error')

    def chart(self, date_style, style, date_1=default_begin_time, date_2=default_end_time):  # 指定日期内，每一天销售的商品+数量
        if date_style == 'Day':
            date = self.getEveryDay(date_1, date_2)
        elif date_style == 'Month':
            date = self.getBetweenMonth(date_1, date_2)
        date_len = len(date)
        data = {}
        shouru_data = [0 for i in range(date_len)]
        for i, j in zip(date, range(date_len)):
            if style == 'mobile' or style == 'parts':
                if date_style == 'Day':
                    sql = 'select pp,count(pp) as shuliang,sum(shoujia) as shouru from %s where DATE_FORMAT(ckrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") group by pp ' % (
                    style, i)
                elif date_style == 'Month':
                    sql = 'select pp,count(pp) as shuliang,sum(shoujia) as shouru from %s where DATE_FORMAT(ckrq,"%%%%Y-%%%%m") = DATE_FORMAT("%s-01","%%%%Y-%%%%m") group by pp ' % (
                    style, i)
            elif style == 'card':
                if date_style == 'Day':
                    sql = 'select lx as pp,count(lx) as shuliang,sum(shoujia) as shouru from mobile_card where DATE_FORMAT(ckrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") group by lx ' % (
                    i)
                elif date_style == 'Month':
                    sql = 'select lx as pp,count(lx) as shuliang,sum(shoujia) as shouru from mobile_card where DATE_FORMAT(ckrq,"%%%%Y-%%%%m") = DATE_FORMAT("%s-01","%%%%Y-%%%%m") group by lx ' % (
                    i)
            res = self.application.db.query(sql)
            data_title = ''
            data_data = [0 for l in range(date_len)]
            if res:
                for r in res:
                    # print r
                    data_title = r['pp']
                    data_data[j] = int(r['shuliang'])
                    shouru_data[j] += int(r['shouru'])
                    if data.has_key(data_title):
                        data[data_title] = self.list_add(data[data_title], data_data)
                    else:
                        data[data_title] = data_data
        insert_data = data.items()  # 把dict转为list
        data_keys = data.keys()
        data_keys.append(u'\u6536\u5165')  # 图表上面那行 legend（图例） 添加了　‘收入’的unicode　编码
        data_keys = str(data_keys).replace('u\'', '\'')
        data_keys.encode("unicode-escape")
        return data_keys, insert_data, shouru_data

        # select ckrq from mobile where ckrq is not null;     map(format('%Y-'%m-%d'),res_sql)
        # select pp from mobile where ckrq is not null ;
        # select pp from mobile where DATE_FORMAT(rkrq,"%Y-%m-%d") = DATE_FORMAT("%s","%Y-%m-%d")
        # select pp,count(pp) as shuliang from mobile where DATE_FORMAT(ckrq,"%Y-%m-%d") = DATE_FORMAT("%s","%Y-%m-%d") group by pp ;  # 算出指定日期出库的商品名称及数量
        # select pp,count(pp) as shuliang from mobile where ckrq between '2017-09-15' and '2017-09-25' group by pp ;  #　算出指定日期范围内出库的商品名称及数量
        # select pp,count(pp) as shuliang from mobile where to_days(ckrq)=to_days(now()) group by pp; # 查询当天出库的商品及数量
        # select * from mobile where date_sub(curdate(),interval 7 day) <= date(ckrq); # 计算最近７天

    def getEveryDay(self, begin_date, end_date):  # 获取指定两个日期内的所有日期
        date_list = []
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        return date_list

    def list_add(self, a, b):  # 两个列表值相加
        c = []
        for i, j in zip(a, b):
            c.append(i + j)
        return c

    def getBetweenMonth(self, begin_date, end_date):
        date_list = []
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m")
            date_list.append(date_str)
            begin_date = self.add_months(begin_date, 1)
        return date_list

    def add_months(self, dt, months):
        month = dt.month - 1 + months
        year = dt.year + month / 12
        month = month % 12 + 1
        day = min(dt.day, calendar.monthrange(year, month)[1])
        return dt.replace(year=year, month=month, day=day)


################################################################
## modules
##
################################################################


class SearchModule(tornado.web.UIModule):
    def render(self):
        return ""




class Entry_mobile(tornado.web.UIModule):
    def render(self,options):
        if options=='mobile':#手机
            return "<tr>\
                    <th>id</th>\
                    <th>品牌</th>\
                    <th>型号</th>\
                    <th>串号</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>售价</th>\
                    <th>付款方式</th>\
                    <th>备注</th>\
                    <th> 操作 </th>\
                 </tr>"
        elif options=='parts':# 配件
            return "<tr>\
                    <th>id</th>\
                    <th>品牌</th>\
                    <th>名称</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>售价</th>\
                    <th>付款方式</th>\
                    <th>备注</th>\
                    <th> 操作 </th>\
                 </tr>"
        elif options=='card':
            return "<tr>\
                    <th>id</th>\
                    <th>类型</th>\
                    <th>号码</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>售价</th>\
                    <th>付款方式</th>\
                    <th>备注</th>\
                    <th> 操作 </th>\
                 </tr>"
        elif options=='gift':
            return "<tr>\
                    <th>id</th>\
                    <th>名称</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>备注</th>\
                    <th> 操作 </th>\
                 </tr>"
        elif options=='count_card':
            return "<tr>\
                    <th>id</th>\
                    <th>类型</th>\
                    <th>号码</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>售价</th>\
                    <th>付款方式</th>\
                    <th>备注</th>\
                 </tr>"
        elif options=='count_mobile':
            return"<tr>\
                    <th>id</th>\
                    <th>品牌</th>\
                    <th>型号</th>\
                    <th>串号</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>售价</th>\
                    <th>付款方式</th>\
                    <th>备注</th>\
                 </tr>"
        elif options=="count_parts":
            return "<tr>\
                    <th>id</th>\
                    <th>品牌</th>\
                    <th>名称</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>售价</th>\
                    <th>付款方式</th>\
                    <th>备注</th>\
                 </tr>"
        elif options=="count_gift":
            return "<tr>\
                    <th>id</th>\
                    <th>名称</th>\
                    <th>入库日期</th>\
                    <th>出库日期</th>\
                    <th>进价</th>\
                    <th>备注</th>\
                 </tr>"

class List_mobile(tornado.web.UIModule):
    def render(self, list, user):
        return self.render_string('list_mobile.html', list=list, user=user)

class List_parts(tornado.web.UIModule):
    def render(self, list, user):
        return self.render_string('list_parts.html', list=list, user=user)

class List_card(tornado.web.UIModule):
    def render(self, list, user):
        return self.render_string('list_card.html', list=list, user=user)

class List_gift(tornado.web.UIModule):
    def render(self, list, user):
        return self.render_string('list_gift.html', list=list, user=user)
################################################################


################################################################
## Add function
##
################################################################


class Add_mobile(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("add-mobile.html",res='', user=self.get_power())

    @tornado.web.authenticated
    def post(self):
        pp = self.get_argument('pp')
        xh = self.get_argument('xh')
        ch = self.get_argument('ch')
        jinjia = self.get_argument('jinjia')
        bz = self.get_argument('bz',None)
        try:
            if pp!='' and xh!='' and ch!='' and jinjia!='':
                sql="insert into mobile(pp,xh,ch,jinjia,bz) \
                            values('%s','%s','%s',%d,'%s');" %(pp,xh,ch,int(jinjia),bz)
                res = self.application.db.execute(sql)
                if res=='':res=None
                # self.render("add-mobile.html",res=res, user=self.get_power())
                self.finish({'message': 'ok'})
        except:
            self.finish({'message': 'failed'})


class Add_parts(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("add-parts.html", res='', user=self.get_power())

    @tornado.web.authenticated
    def post(self):
        pp = self.get_argument('pp')
        mc = self.get_argument('mc')
        sl = self.get_argument('sl')
        jinjia = self.get_argument('jinjia')
        bz = self.get_argument('bz')
        try:
            for i in range(int(sl)):
                sql="insert into parts(pp,mc,jinjia,bz) \
                    values('%s','%s',%d,'%s');" %(pp,mc,int(jinjia),bz)
                res = self.application.db.execute(sql)
                time.sleep(0.1)
            # self.render("add-parts.html",res=res, user=self.get_power())
            self.finish({'message': 'ok'})
        except:
            self.finish({'message': 'failed'})

class Add_card(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("add-card.html", res='', user=self.get_power())

    @tornado.web.authenticated
    def post(self):
        lx = self.get_argument('lx')
        haoma = self.get_argument('haoma')
        jinjia = self.get_argument('jinjia')
        bz = self.get_argument('bz',None)
        try:
            if lx!='' and haoma!='' and jinjia!='':
                sql="insert into mobile_card(lx,haoma,jinjia,bz) \
                            values('%s',%d, %d, '%s');" %(lx,int(haoma),int(jinjia),bz)
                res = self.application.db.execute(sql)
                if res=='':
                    res=None
                    self.finish({'message': 'cha ru shi bai'})
                # self.render("add-card.html",res=res, user=self.get_power())
                self.finish({'message': 'ok'})
        except:
            self.finish({'message': 'failed'})



class Add_gift(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("add-gift.html", res='', user=self.get_power())

    @tornado.web.authenticated
    def post(self):
        mc = self.get_argument('mc')
        sl = self.get_argument('sl')
        jinjia = self.get_argument('jinjia')
        bz = self.get_argument('bz')
        try:
            for i in range(int(sl)):
                sql = "insert into gift(mc,jinjia,bz) \
                            values('%s',%d,'%s');" % (mc, int(jinjia), bz)
                res = self.application.db.execute(sql)
                time.sleep(0.1)
            # self.render("add-gift.html", res=res, user=self.get_power())
            self.finish({'message': 'ok'})
        except:
            self.finish({'message': 'failed'})
###########################################################


################################################################
## Inventory function
##
################################################################

class Inventory_mobile(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        sql = 'select * from mobile'
        res = self.application.db.query(sql)
        self.render("inventory-mobile.html", res=res, user=self.get_power())

    @tornado.web.authenticated
    def post(self):
        try:
            value = self.get_argument('caozuo',None)
            id = self.get_argument('id',None)
            shoujia = self.get_argument('shoujia',None)
            fkfs = unicode(self.get_argument('fkfs',None))
            bz  = unicode(self.get_argument('bz',None))
            # 出库
            if value == u'出库' and id:
                sql='update mobile SET ckrq=now(),shoujia=%d,fkfs="%s",bz="%s" where id=%d' %(int(shoujia),fkfs,bz,int(id))
                res=self.application.db.execute(sql)
                self.redirect('/inventory-mobile')
            #删除
            elif value == u'删除' and id:
                sql='delete from mobile where id=%d' %(int(id))
                res=self.application.db.execute(sql)
                if res!='' or res != None:
                    self.redirect('/inventory-mobile')
                else:
                    self.write('删除出错')
            else:
                self.write('出错')
        except  ValueError:
            self.write('售价或付款方式未填写')

class Inventory_parts(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        sql='select * from parts'
        res = self.application.db.query(sql)
        self.render("inventory-parts.html", res=res, user=self.get_power())

    @tornado.web.authenticated
    def post(self):
        try:
            value = self.get_argument('caozuo', None)
            id = self.get_argument('id', None)
            shoujia = self.get_argument('shoujia', None)
            fkfs = unicode(self.get_argument('fkfs', None))
            bz = unicode(self.get_argument('bz', None))
            # 出库
            if value == u'出库' and id:
                sql = 'update parts SET ckrq=now(),shoujia=%d,fkfs="%s",bz="%s" where id=%d' % (
                int(shoujia), fkfs, bz, int(id))
                res = self.application.db.execute(sql)
                self.redirect('/inventory-parts')
            # 删除
            elif value == u'删除' and id:
                sql = 'delete from parts where id=%d' % (int(id))
                res = self.application.db.execute(sql)
                if res != '' or res != None:
                    self.redirect('/inventory-parts')
                else:
                    self.write('删除出错')
            else:
                self.write('出错')
        except  ValueError:
            self.write('售价或付款方式未填写')

class Inventory_card(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        sql='select * from mobile_card'
        res = self.application.db.query(sql)
        self.render("inventory-card.html", res=res, user=self.get_power())


    @tornado.web.authenticated
    def post(self):
        try:
            value = self.get_argument('caozuo', None)
            id = self.get_argument('id', None)
            shoujia = self.get_argument('shoujia', None)
            fkfs = unicode(self.get_argument('fkfs', None))
            bz = unicode(self.get_argument('bz', None))
            # 出库
            if value == u'出库' and id:
                sql = 'update mobile_card SET ckrq=now(),shoujia=%d,fkfs="%s",bz="%s" where id=%d' % (
                int(shoujia), fkfs, bz, int(id))
                res = self.application.db.execute(sql)
                self.redirect('/inventory-card')
            # 删除
            elif value == u'删除' and id:
                sql = 'delete from mobile_card where id=%d' % (int(id))
                res = self.application.db.execute(sql)
                if res != '' or res != None:
                    self.redirect('/inventory-card')
                else:
                    self.write('删除出错')
            else:
                self.write('出错')
        except  ValueError:
            self.write('售价或付款方式未填写')

class Inventory_gift(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        sql='select * from gift'
        res = self.application.db.query(sql)
        self.render("inventory-gift.html", res=res, user=self.get_power())


    @tornado.web.authenticated
    def post(self):
        try:
            value = self.get_argument('caozuo', None)
            id = self.get_argument('id', None)
            bz = unicode(self.get_argument('bz', None))
            # 出库
            if value == u'出库' and id:
                sql = 'update gift SET ckrq=current_timestamp,bz="%s" where id=%d' % (
                bz, int(id))
                res = self.application.db.execute(sql)
                self.redirect('/inventory-gift')
            # 删除
            elif value == u'删除' and id:
                sql = 'delete from gift where id=%d' % (int(id))
                res = self.application.db.execute(sql)
                if res != '' or res != None:
                    self.redirect('/inventory-gift')
                else:
                    self.write('删除出错')
            else:
                self.write('出错')
        except  ValueError:
            self.write('售价或付款方式未填写')

class Search(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        # 搜索
        search_mobile = self.get_argument('search-mobile', None)
        search_parts = self.get_argument('search-parts', None)
        search_card = self.get_argument('search-card', None)
        search_gift = self.get_argument('search-gift', None)
        if search_mobile != None:
            str = ''
            pp = self.get_argument('pp', None)
            xh = self.get_argument('xh', None)
            rkrq = self.get_argument('rkrq', None)
            ckrq = self.get_argument('ckrq', None)
            fkfs = self.get_argument('fkfs', None)
            ch = self.get_argument('ch', None)
            if pp!='':
                str = str + 'pp="%s" and ' %(pp)
            if xh!='':
                str = str + 'xh="%s" and ' % (xh)
            if rkrq !='':
                str = str + 'DATE_FORMAT(rkrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' % (rkrq)
            if ckrq !='':
                str = str + 'DATE_FORMAT(ckrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' % (ckrq)
            if fkfs !='':
                str = str + 'fkfs="%s" and ' % (fkfs)
            if ch !='':
                str = str + 'ch="%s" and ' % (ch)
            if str !='':
                str = str[:-5]
                sql='select * from mobile where %s' %(str)
                res = self.application.db.query(sql)
                self.render("inventory-mobile.html", res=res, user=self.get_power())
            else:
                self.redirect('/inventory-mobile')
        elif search_parts != None:
            str = ''
            pp = self.get_argument('pp', None)
            mc = self.get_argument('mc', None)
            rkrq = self.get_argument('rkrq', None)
            ckrq = self.get_argument('ckrq', None)
            fkfs = self.get_argument('fkfs', None)
            if pp!='':
                str = str + 'pp="%s" and ' %(pp)
            if mc!='':
                str = str + 'mc="%s" and ' % (mc)
            if rkrq!='':
                str = str + 'DATE_FORMAT(rkrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' % (rkrq)
            if ckrq!='':
                str = str + 'DATE_FORMAT(ckrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' % (ckrq)
            if fkfs!='':
                str = str + 'fkfs="%s" and ' % (fkfs)
            if str != '':
                str = str[:-5]
                sql='select * from parts where %s' %(str)
                res = self.application.db.query(sql)
                self.render("inventory-parts.html", res=res, user=self.get_power())
            else:
                self.redirect("/inventory-parts")
        elif search_card != None:
            str = ''
            lx = self.get_argument('lx', None)
            haoma = self.get_argument('haoma', None)
            rkrq = self.get_argument('rkrq', None)
            ckrq = self.get_argument('ckrq', None)
            fkfs = self.get_argument('fkfs', None)
            if lx!='':
                str = str + 'lx="%s" and ' %(lx)
            if haoma!='':
                str = str + 'haoma=%d and ' %(int(haoma))
            if rkrq!='':
                str = str + 'DATE_FORMAT(rkrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' %(rkrq)
            if ckrq!='':
                str = str + 'DATE_FORMAT(ckrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' %(ckrq)
            if fkfs!='':
                str = str + 'fkfs="%s" and ' %(fkfs)
            if str != '':
                str = str[:-5]
                sql='select * from mobile_card where %s' %(str)
                res = self.application.db.query(sql)
                self.render("inventory-card.html", res=res, user=self.get_power())
            else:
                self.redirect("/inventory-card")
        elif search_gift != None:
            str = ''
            mc = self.get_argument('mc', None)
            rkrq = self.get_argument('rkrq', None)
            ckrq = self.get_argument('ckrq', None)
            if mc!='':
                str = str + 'mc="%s" and ' %(mc)
            if rkrq!='':
                str = str + 'DATE_FORMAT(rkrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' % (rkrq)
            if ckrq!='':
                str = str + 'DATE_FORMAT(ckrq,"%%%%Y-%%%%m-%%%%d") = DATE_FORMAT("%s","%%%%Y-%%%%m-%%%%d") and ' % (ckrq)
            if str != '':
                str = str[:-5]
                sql='select * from gift where %s' %(str)
                res = self.application.db.query(sql)
                self.render("inventory-gift.html", res=res, user=self.get_power())
            else:
                self.redirect("/inventory-gift")

        else:
            self.write('222')

        #########################################################
        #### Make Chart
        ####
        #########################################################

class Test(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('test.html', user=self.get_power())

    @tornado.web.authenticated
    def post(self):
        # print self.data_received('data')
        lx = self.get_argument('lx')
        haoma = self.get_argument('haoma')
        jinjia = self.get_argument('jinjia')
        bz = self.get_argument('bz', None)
        print(lx,haoma,jinjia,bz)
        self.finish({'message': 'ok'})


#########################################################

###########################################################
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/', Login_in_Handler),
                    (r'/login_success', Login_success),
                    (r'/login', Login_in_Handler),
                    (r'/logout', Logout),
                    (r'/add-mobile', Add_mobile),
                    (r'/inventory-mobile', Inventory_mobile),
                    (r'/add-parts', Add_parts),
                    (r'/inventory-parts', Inventory_parts),
                    (r'/add-card', Add_card),
                    (r'/inventory-card', Inventory_card),
                    (r'/add-gift', Add_gift),
                    (r'/inventory-gift', Inventory_gift),
                    (r'/count', Count),
                    (r'/search', Search),
                    (r'/test', Test)
                    ]
        settings = {
            'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
            'static_path' : os.path.join(os.path.dirname(__file__), "static"),
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            "xsrf_cookies": True,
            "login_url": "/login",
            "ui_modules" : {
                            'Entry_mobile': Entry_mobile,
                            'List_mobile': List_mobile,
                            'List_parts': List_parts,
                            'List_card': List_card,
                            'List_gift': List_gift,
                            }#  init modules
        }


        self.init_db()

        tornado.web.Application.__init__(self, handlers, debug=True,**settings)

    # create db .
    def init_db(self):
        try:
            self.db = torndb.Connection(options.hostaddress, options.dbname,options.username, options.password)
            self.db.update("set time_zone = '+8:00'")

        #sql = 'select * from user'
            #sql = 'drop table test if exists;' \
            #      'create table user(id int not null auto_increment,username varchar(10) not null,password varchar(50) not null, primary key(id));'
        except:
            'db connect error'






if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

'''# msg table
create table msg
(id int not null auto_increment,
pp varchar(10) not null,
xh varchar(50) not null,
ch varchar(50) not null,
rkrq varchar(10) not null,
ckrq varchar(10) not null,
je varchar(10) not null,
fkfs varchar(10) not null,
bz varchar(10) not null,
primary key(id));
'''


'''#mobile table
create table mobile(
id int not null auto_increment,
pp varchar(20) charset utf8,
xh varchar(20) charset utf8,
ch varchar(20),
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
shoujia smallint,
fkfs varchar(10) charset utf8,
bz varchar(50) charset utf8,
primary key(id)
);

insert into mobile(pp,xh,ch,jinjia)
values('vivo','x7','2134567890',1234);

UPDATE mobile SET xx=xx where id=xx;

'''
'''#parts table
create table parts(
id int not null auto_increment,
pp varchar(20) charset utf8,
mc varchar(20) charset utf8,
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
shoujia smallint,
fkfs varchar(10) charset utf8,
bz varchar(50) charset utf8,
primary key(id)
);

'''


'''# mobile_card table
create table mobile_card(
id int not null auto_increment,
lx varchar(20) charset utf8,
haoma varchar(20),
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
shoujia smallint,
fkfs varchar(10) charset utf8,
bz varchar(50) charset utf8,
primary key(id)
);
'''

'''# gift table
create table gift(
id int not null auto_increment,
mc varchar(20) charset utf8,
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
bz varchar(50) charset utf8,
primary key(id)
);
'''
'''
create table user(
id int not null auto_increment,
username varchar(10),
password varchar(20),
power varchar(10),
primary key(id)
);
'''
