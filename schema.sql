'''#mobile table
create table mobile(
id integer primary key autoincrement,
pp varchar(20) charset utf8,
xh varchar(20) charset utf8,
ch varchar(20),
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
shoujia smallint,
fkfs varchar(10) charset utf8,
bz varchar(50) charset utf8
);

insert into mobile(pp,xh,ch,jinjia)
values('vivo','x7','2134567890',1234);

UPDATE mobile SET xx=xx where id=xx;

'''
'''#parts table
create table parts(
id integer primary key autoincrement,
mc varchar(20) charset utf8,
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
shoujia smallint,
fkfs varchar(10) charset utf8,
bz varchar(50) charset utf8
);

'''


'''# mobile_card table
create table mobile_card(
id integer primary key autoincrement,
lx varchar(20) charset utf8,
haoma varchar(20),
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
shoujia smallint,
fkfs varchar(10) charset utf8,
bz varchar(50) charset utf8
);
'''

'''# gift table
create table gift(
id integer primary key autoincrement,
mc varchar(20) charset utf8,
rkrq datetime DEFAULT CURRENT_TIMESTAMP,
ckrq datetime,
jinjia smallint,
bz varchar(50) charset utf8
);
'''