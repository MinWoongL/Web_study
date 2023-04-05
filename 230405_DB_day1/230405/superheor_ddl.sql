-- id, 이름, 직업, 능력, 국적, 소속회사, 나이, 가입날짜

-- 새로운 테이블을 생성하기

CREATE TABLE superheros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    job TEXT NOT NULL,
    ability TEXT NOT NULL,
    country TEXT NOT NULL,
    company TEXT NOT NULL,
    age INTEGER NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE superheros2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    job TEXT NOT NULL,
    ability TEXT NOT NULL,
    country TEXT NOT NULL,
    company TEXT NOT NULL,
    age INTEGER NOT NULL
);

-- 테이블 수정
ALTER TABLE superheros2 RENAME TO superhero2;

-- 컬럼추가
ALTER TABLE superhero2 ADD COLUMN 가입날짜 DATE;
ALTER TABLE superhero2 ADD COLUMN 임시 TEXT;

-- 컬럼지우기
-- extension 은 sqlite3 버전 관계로 실행이 안된다. 쉘에서 실행해야 함
ALTER TABLE superhero2 DROP COLUMN 임시;

DROP TABLE superhero;