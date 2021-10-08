-- - ------------------------------------------
# blog项目
create database blog;
use blog;
create table users(
    uid int auto_increment primary key not null ,
    username varchar(50) not null,
    password varchar(50) not null ,
    name varchar(50) not null,
    phone varchar(11),
    email varchar(50),
    time timestamp not null
)default charset = utf8;

create table brief(
    bid int auto_increment primary key not null ,
    title text not null ,
    writer_id int not null ,
    time timestamp not null ,
    read_num int not null default 0,
    comment_num int not null default 0,
    recommend_num int not null default 0,
    up_num int not null default 0,
    down_num int not null default 0,
    constraint fk_brief_wid foreign key brief(writer_id) references users(uid)
)default charset = utf8;

create table contents(
    cid int auto_increment primary key not null ,
    title_id int not null ,
    content text not null ,
    time timestamp not null ,
    constraint fk_contents_tid foreign key contents(title_id) references brief(bid)
)default charset = utf8;

create table comments(
    cmid int auto_increment primary key not null ,
    time timestamp not null ,
    title_id int not null ,
    user_id int not null ,
    comment text not null ,
    constraint fk_comments_uid foreign key comments(user_id) references users(uid)
)default charset = utf8;


# 创建唯一索引
create unique index balabala on users(username,password); -- 创建索引
create unique index babala on users(phone);  -- 手机号唯一索引
create unique index balala on users(email);  -- 邮箱唯一索引



insert into users(username, password, name, phone, email, time) values ('zhangsan', 666, '张三', 1111111, 'dasda@adw.com', '2017-08-15 14:38:46');
insert into users(username, password, name, phone, email, time) values ('lisi', 666, '李四', 12431414, 'd231da@adw.com', '2019-08-15 16:58:42');
insert into users(username, password, name, phone, email, time) values ('wangwu', 666, '王五', 31241124, 'd42341da@adw.com', '2020-09-16 5:28:16');


insert into brief(title, writer_id, time, read_num, comment_num, recommend_num, up_num, down_num)
values ('震惊1', '1', '2018-10-25 14:22:32', 10000, 1, 456, 555, 10);
insert into brief(title, writer_id, time, read_num, comment_num, recommend_num, up_num, down_num)
values ('震惊2', '1', '2019-10-25 15:22:32', 1000, 2, 456, 555, 10);
insert into brief(title, writer_id, time, read_num, comment_num, recommend_num, up_num, down_num)
values ('震惊3', '2', '2018-9-25 16:22:32', 1000, 1, 46, 55, 1);
insert into brief(title, writer_id, time, read_num, comment_num, recommend_num, up_num, down_num)
values ('震惊4', '2', '2020-10-25 11:22:32', 10000, 2, 456, 555, 1000);
insert into brief(title, writer_id, time, read_num, comment_num, recommend_num, up_num, down_num)
values ('震惊5', '3', '2019-8-25 10:22:32', 1000, 1, 56, 55, 100);
insert into brief(title, writer_id, time, read_num, comment_num, recommend_num, up_num, down_num)
values ('震惊6', '3', '2021-01-15 15:22:32', 100, 1, 6, 5, 10);
insert into brief(title, writer_id, time, read_num, comment_num, recommend_num, up_num, down_num)
values ('震惊7', '3', '2018-1-15 14:32:32', 300, 1, 56, 55, 60);


insert into contents(title_id, content, time) values(1,'卧槽，震惊1啊', '2018-10-25 14:22:32');
insert into contents(title_id, content, time) values(2,'卧槽，震惊2啊', '2019-10-25 15:22:32');
insert into contents(title_id, content, time) values(3,'卧槽，震惊3啊', '2018-9-25 16:22:32');
insert into contents(title_id, content, time) values(4,'卧槽，震惊4啊', '2020-10-25 11:22:32');
insert into contents(title_id, content, time) values(5,'卧槽，震惊5啊', '2019-8-25 10:22:32');
insert into contents(title_id, content, time) values(6,'卧槽，震惊6啊', '2021-01-15 15:22:32');
insert into contents(title_id, content, time) values(7,'卧槽，震惊7啊', '2018-1-15 14:32:32');


insert into comments(time, user_id, title_id, comment) values('2018-10-25 14:22:33', 2, 1, '真厉害啊');
insert into comments(time, user_id, title_id, comment) values('2019-10-25 15:22:33', 3, 2, '真水啊');
insert into comments(time, user_id, title_id, comment) values('2019-10-25 19:22:32', 2, 2, '真丘比啊');
insert into comments(time, user_id, title_id, comment) values('2018-9-25 16:22:42', 1, 3, '白金之星啊');
insert into comments(time, user_id, title_id, comment) values('2020-10-25 15:22:32', 3, 4, '急速猎杀啊');
insert into comments(time, user_id, title_id, comment) values('2020-10-25 13:22:32', 3, 4, '真写不出来');
insert into comments(time, user_id, title_id, comment) values('2019-8-26 10:22:32', 1, 5, '真sss啊');
insert into comments(time, user_id, title_id, comment) values('2021-01-15 15:25:32', 3, 6, '真asfasfd啊');
insert into comments(time, user_id, title_id, comment) values('2018-1-16 14:32:32', 1, 7, '真厉affasfaf');
