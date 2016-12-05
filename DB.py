DB
I.MySQL:
        a)基本操作：
                1.mysql -h 主机名 -u 用户名 -p(栗子：mysql -uroot -p)
                                                h：后面接的是主机名，表示你要连接到哪台主机的MySQL数据库。
                                                u：后面接的是用户名，MySQL默认的就是root。
                                                p：指定需要使用密码登陆MySQL数据库，如果密码为空，该参数可以省略。

                2.mysql -h 192.168.1.105 -u root -p:远程连接主机并以root身份登录数据库
                3.show databases;                                       ->显示所有数据库
                4.create database [数据库名];                            ->创建数据库
                5.use [数据库名];                                        ->选择要操作的数据库
                6.create table [数据表名] (字段1 字段1类型 字段1属性,字段2 ...);
                7.describe [数据表名];
                8.update [数据库列名] set [字段名]=[新value] where 更新条件;
                9.drop table table_name;
                8.alter table [数据表名] ADD column_name datatype                   ->为表添加新字段
                  alter table [数据表名] DROP column_name                           ->删除表字段
                  alter table [数据表名] CHANGE column_name new_colum_name datatype ->改表字段
                  alter table [数据表名] RENAME new_table_name                      ->重命名表

or
ALTER TABLE table_name
DROP COLUMN column_name
                                                  ->查看表结构
        b)重要的SQL命令：
                1.SELECT语句----->  SELECT column_name,column_name FROM table_name
                                    &&
                                    SELECT * FROM table_name;
                2.DISTINCK语句----->SELECT DISTINCT column_name,column_name
                                    FROM table_name;
                3.WHERE语句-------->SELECT column_name,column_name
                                    FROM table_name WHERE column_name operator value;
                4.GROUP BY语句----->SELECT column_name,column_name
                                     FROM table_name ORDER BY column_name,column_name
                                     ASC|DESC;(ASC为默认排序方式)
                5.INSERT INTO语句---->INSERT INTO table_name
                                      VALUES (value1,value2,value3,...);
                                      &&
                                      INSERT INTO table_name (column1,column2,column3,...)
                                      VALUES (value1,value2,value3,...);
                6.UPDATE语句------->UPDATE table_name
                                    SET column1=value1,column2=value2,...
                                    WHERE some_column=some_value;
                                    一定要写where语句，不然该表的所有数据都将被更新！！！！
                7.DELETE语句-------->DELETE FROM table_name
                                     WHERE some_column=some_value;
                                     ***同样要写where语句，不然该表的所有数据都将被删除！！！！
                                     (DELETE FROM table_name;
                                     or
                                     DELETE * FROM table_name;)
                8.LIMIT语句--------->SELECT column_name(s)
                                     FROM table_name
                                     LIMIT number;
                9.LIKE语句---------->SELECT column_name(s)
                                     FROM table_name
                                     WHERE column_name LIKE pattern;
                10.SQL通配符------->
                                    % 替代 0 个或多个字符
                                    _ 替代一个字符
                                    [charlist] 字符列中的任何单一字符
                                    [^charlist] or [!charlist] 不在字符列中的任何单一字符
                11.IN操作符-------->
                                    SELECT column_name(s)
                                    FROM table_name
                                    WHERE column_name IN (value1,value2,...);
                                    &&
                                    SELECT column_name(s)
                                    FROM table_name
                                    WHERE column_name IN (select column from table_w3c where ...);
                12.BETWEEN操作符----->
                                    SELECT column_name(s)
                                    FROM table_name
                                    WHERE column_name BETWEEN value1 AND value2;
                13.Join连接--------->
                    13.1 INNER JOIN关键字>
                                        /***
                                            INNER JOIN 与JOIN相同
                                            关键字在表中存在至少一个匹配时返回行
                                        ***/
                                        SELECT column_name(s)
                                        FROM table1
                                        INNER JOIN table2
                                        ON table1.column_name=table2.column_name;
                                        or
                                        SELECT column_name(s)
                                        FROM table1
                                        JOIN table2
                                        ON table1.column_name=table2.column_name;


                    13.2 LEFT JOIN关键字>
                                        /***
                                            LEFT JOIN 关键字从左表（table1）返回所有的行，
                                            即使右表（table2）中没有匹配。
                                            如果右表中没有匹配，则结果为 NULL。
                                        ***/
                                        SELECT column_name(s)
                                        FROM table1
                                        LEFT JOIN table2
                                        ON table1.column_name=table2.column_name;
                                        or
                                        SELECT column_name(s)
                                        FROM table1
                                        LEFT OUTER JOIN table2
                                        ON table1.column_name=table2.column_name;

                    13.3 RIGHT JOIN关键字>
                                        /***
                                            RIGHT JOIN 关键字从右表（table2）返回所有的行，
                                            即使左表（table1）中没有匹配。
                                            如果左表中没有匹配，则结果为 NULL。
                                        ***/
                                        SELECT column_name(s)
                                        FROM table1
                                        ON table1.column_name=table2.column_name;
                                        RIGHT JOIN table2
                                        or
                                        SELECT column_name(s)
                                        FROM table1
                                        RIGHT OUTER JOIN table2
                                        ON table1.column_name=table2.column_name;
                    13.4 FULL OUTER JOIN 关键字>
                                            /***
                                                FULL OUTER JOIN 关键字只要左表（table1）
                                                和右表（table2）其中一个表中存在匹配，则返回行.
                                                FULL OUTER JOIN 关键字结合了
                                                LEFT JOIN 和 RIGHT JOIN 的结果。
                                            ***/
                                            SELECT column_name(s)
                                            FULL OUTER JOIN table2
                                            ON table1.column_name=table2.column_name;
                14.UNION 操作符-------->
                                        /***
                                            UNION 操作符用于合并两个或多个 SELECT 语句的结果集。
                                            UNION 内部的每个 SELECT 语句必须拥有相同数量的列。
                                            列也必须拥有相似的数据类型。
                                            同时，每个 SELECT 语句中的列的顺序必须相同。
                                            UNION 结果集中的列名总是等于-->
                                            <---UNION 中第一个 SELECT 语句中的列名。
                                        ***/

                                        SELECT column_name(s) FROM table1
                                        UNION
                                        SELECT column_name(s) FROM table2;

                                        aadsf
                                            默认地，UNION 操作符选取不同的值。
                                            如果允许重复的值，请使用 UNION ALL。
                                        ***/

                                        SELECT column_name(s) FROM table1
                                        UNION ALL
                                        SELECT column_name(s) FROM table2;

                    15.聚合函数：
                            AVG():
                                  --->SELECT AVG(column_name) FROM table_name;

                            COUNT():
                                  --->SELECT COUNT(column_name) FROM table_name;
                                      SELECT COUNT(*) FROM table_name;
                            FIRST():
                            LAST():
                            SUM():
                            MIN():
                            MAX():


















II.mongodb:

III.redis:

IV.优化：
