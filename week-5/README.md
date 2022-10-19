## Assignment_-_Week_5
* #### **要求三：SQL CRUD**
  * **使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。**
    * *SQL指令*<br>
      `insert into member(id, name, username, password, follower_count) values(1, 'Amy', 'test', 'test',5);`
    * *指令執行畫面*
      > ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-1.png)
        ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-1-1.png)<br>
  * **使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。** 
    * *SQL指令*<br>
      `select * from member;`
    * *指令執行畫面*
      > ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-2.png)<br>
  * **使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。**
    * *SQL指令*<br>
      `select * from member order by time desc;`
    * *指令執行畫面*
      > ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-3.png)<br>
  * **使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )**
    * *SQL指令*<br>
      `select * from (select * from member order by time desc) as subtable order by time desc limit 1,3;`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-4.png)<br>
  * **⽤ SELECT 指令取得欄位 username 是 test 的會員資料。**
    * *SQL指令*<br>
      `select * from member where username='test';`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-5.png)<br>
  * **使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。**
    * *SQL指令*<br>
      `select * from member where username='test' and password='test';`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-6.png)<br>
  * **使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改 成 test2。**
    * *SQL指令*<br>
      `set sql_safe_updates=0;`<br>
      `update member set username='test2' where username='test';`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-7.png)<br>
* #### **要求四：SQL Aggregate Functions**
  * **取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。**
    * *SQL指令*<br>
      `select count(username) from member;`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/4-1.png)<br>
  * **取得 member 資料表中，所有會員 follower_count 欄位的總和。**
    * *SQL指令*<br>
      `select sum(follower_count) from member;`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/4-2.png)<br>
  * **取得 member 資料表中，所有會員 follower_count 欄位的平均數。**
    * *SQL指令*<br>
      `select avg(follower_count) from member;`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/4-3.png)<br>
* #### **要求五：SQL JOIN (Optional)**
  * **在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message。資料表中必須包含以下欄位設定：**
    * *SQL指令*<br>
      `create table message(id bigint primary key auto_increment, member_id bigint not null, content varchar(255) not null, like_count int unsigned not null default 0, time datetime not null default current_timestamp, foreign key (member_id) references member(id))`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/5-1.png)<br>
  * **使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。**
    * *SQL指令*<br>
      `select member.name, message.content from member inner join message on member.id = message.member_id;`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/5-2.png)<br>
  * **使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。**
    * *SQL指令*<br>
      `select member.name, member.username, message.content, message.like_count from member inner join message on member.id = message.member_id and member.username='test';`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/5-3.png)<br>
  * **使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中 欄位 username 是 test 的所有留⾔平均按讚數。**
    * *SQL指令*<br>
      `select avg(like_count) from (select member.username, message.like_count from member inner join message on member.id = message.member_id and member.username='test') as temptable;`
    * *指令執行畫面*
      >  ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/5-4.png)<br>
      
