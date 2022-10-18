## Assignment_-_Week_5
* **要求三：SQL CRUD**
  * **使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。**
    * *SQL指令*<br>
      `insert into member(id, name, username, password, follower_count)values(1, 'Amy', 'test', 'test',5);`
    * *指令執行畫面*
      > ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-1.png)
        ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-1-1.png)<br>
  * **使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。** 
    * *SQL指令*<br>
      `select * from member;`
    * *指令執行畫面*
      > ![](https://github.com/hayleychangs/glowing-parakeet/blob/main/week-5/pics/3-2.png)<br>
