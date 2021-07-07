# hondana SQLの作成コマンド

#sqliteの起動方法
sqlite3 データベース名.sqlite3   # データベースに接続する（同名ファイルがなければ作成して接続する）　テーブル名前とは別

#sqlliteのテーブル作成
CREATE TABLE book ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT , title TEXT NOT NULL , publisher TEXT NOT NULL  ,author TEXT NOT NULL , price INT NOT NULL ,ISBN INT NOT NULL , date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP );

#sqliteのデータ挿入の基本構文　valueの後の括弧の中に題名等を入れていく
INSERT INTO book ( title, publisher, author, price, ISBN, date) VALUES ('サンプルタイトル', 'サンプル出版', 'サンプルAUTHOR', '1000', '123456789', CURRENT_TIMESTAMP);

#sqlliteの閉じる方法
.quit
