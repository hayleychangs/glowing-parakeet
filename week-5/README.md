## Assignment_-_Week_5
* **要求三：SQL CRUD**
  * **使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。**
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
  * **使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由 近到遠排序。**
    * *SQL指令*<br>
      `select * from member order by time desc;`
    * *指令執行畫面*
      > ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-3.png)<br>
  * **使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位， 由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )**
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
      
