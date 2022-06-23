-- personテーブルにデータを追加
INSERT INTO person (id, name, size) VALUES (10, 'A', 11.1);
INSERT INTO person (id, name, size) VALUES (11, 'B', 22.2);
INSERT INTO person (id, name, size) VALUES (12, 'C', 33.3);

-- humanテーブルを作成
CREATE TABLE human (id INTEGER PRIMARY KEY, name TEXT NOT NULL, height REAL, weight REAL);

-- humanテーブルにデータを追加
INSERT INTO human (id, name, height, weight) VALUES (100, 'A', 160.1, 80.2);
INSERT INTO human (id, name, height, weight) VALUES (101, 'B', 170.2, 70.4);
INSERT INTO human (id, name, height, weight) VALUES (102, 'D', 180.3, 60.1);

-- person, humanテーブルの確認
SELECT * FROM person;
SELECT * FROM human;

-- 内部結合SQL
SELECT a.name, a.size, b.height, b.weight FROM person AS a INNER JOIN human AS b ON a.name = b.name;
SELECT a.name, a.size, b.height, b.weight FROM person AS a, human AS b WHERE a.name = b.name;

-- 外部結合SQL
SELECT a.name, a.size, b.height, b.weight FROM person AS a LEFT JOIN human AS b ON a.name = b.name;
