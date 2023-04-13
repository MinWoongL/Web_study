SELECT country, avg(balance) FROM users
GROUP BY country;

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
('임서희', 24, '대전'),
('황상미', 28, '서울'),
('임병국', 28, '부산'),
('채가을', 27, '이천'),
('이민웅', 28, '수원');

UPDATE classmates
SET name='김철수한무두루미', address = '제주도'
WHERE rowid = 1;

DROP TABLE new_contacts;
DROP TABLE users;

-- power 테이블 생성

CREATE TABLE power (
    id INTEGER PRIMARY KEY,
    hero_id INTEGER,
    ability TEXT,
    -- 외래키 등록방법
    -- FOREIGN KEY (<필드명>) REFERENCES <테이블명>(<해당테이블PK>)
    -- 사실 지금은 hero 테이블이 없어서 외래키 등록 문장에 오류가 있음
    -- SQLITE
    FOREIGN KEY (hero_id) REFERENCES hero(id)
);

-- job 테이블 생성

CREATE TABLE job (
    id INTEGER PRIMARY KEY,
    job TEXT
);
-- country 테이블 생성

CREATE TABLE country (
    id INTEGER PRIMARY KEY,
    country TEXT
);
-- company 테이블 생성

CREATE TABLE company (
    id INTEGER PRIMARY KEY,
    company TEXT
);
-- hero 테이블 생성
CREATE TABLE hero (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    나이 INTEGER,
    가입날짜 DATE,
    job_id INTEGER,
    country_id INTEGER,
    company_id INTEGER,
    FOREIGN KEY (job_id) REFERENCES job(id),
    FOREIGN KEY (country_id) REFERENCES country(id),
    FOREIGN KEY (company_id) REFERENCES company(id)
);

-- 기존데이터를 새로운 테이블로 이동
-- 데이터 삽입
-- INSERT INTO 테이블(필드1, 필드2, ...)
-- VALUES(필드1, 필드2 ...)
INSERT INTO JOB(job)
SELECT DISTINCT job
FROM superheros;

INSERT INTO country(country)
SELECT DISTINCT country
FROM superheros;

INSERT INTO company(company)
SELECT DISTINCT company
FROM superheros;

INSERT INTO hero (id, name, 나이, 가입날짜,
                job_id, country_id, company_id)
SELECT sh.id, sh.name, sh.age, sh.date,
    CASE
        WHEN sh.job = '영웅' THEN 1 ELSE 2
    END AS job_id,
    CASE
        WHEN sh.country = '미국' THEN 1
        WHEN sh.country = '아스가르드' THEN 2
        WHEN sh.country = '러시아' THEN 3
        WHEN sh.country = '왜곡의 나라 와칸다' THEN 4
        WHEN sh.country = '아틀란티스' THEN 5
        WHEN sh.country = '아마조니아' THEN 6
        WHEN sh.country = '크립톤' THEN 7
        WHEN sh.country = '영국' THEN 8
        WHEN sh.country = '애포콜립스' THEN 9
        WHEN sh.country = '아즈라엘' THEN 10
        WHEN sh.country = '카하지아' THEN 11
        WHEN sh.country = '잉글랜드' THEN 12
        WHEN sh.country = '스페인' THEN 13
        WHEN sh.country = '독일' THEN 14
        WHEN sh.country = '캐나다' THEN 15
        WHEN sh.country = '완다' THEN 16
        WHEN sh.country = '그리스' THEN 17
        WHEN sh.country = '케냐' THEN 18
    END AS country_id,
    CASE
        WHEN sh.company = '마블' THEN 1
        WHEN sh.company = 'DC' THEN 2
        WHEN sh.company = '저스티스 리그' THEN 3
    END AS company_id
FROM superheros AS sh;

-- CROSS JOIN
-- 두 테이블 간 가능한 모든 조합을 선택
SELECT * FROM hero, job;

-- JOIN 을 테스트 하기 위해 랜덤으로 NULL 값을 넣음
UPDATE hero SET 가입날짜 = NULL WHERE id = 10;
UPDATE hero SET 가입날짜 = NULL WHERE id = 20;
UPDATE hero SET 가입날짜 = NULL WHERE id = 25;
UPDATE hero SET job_id = NULL WHERE id = 30;
UPDATE hero SET job_id = NULL WHERE id = 40;
UPDATE hero SET job_id = NULL WHERE id = 50;
UPDATE hero SET company_id = NULL WHERE id = 64;
UPDATE hero SET company_id = NULL WHERE id = 75;
UPDATE hero SET company_id = NULL WHERE id = 88;
UPDATE hero SET country_id = NULL WHERE id = 16;
UPDATE hero SET country_id = NULL WHERE id = 46;
UPDATE hero SET country_id = NULL WHERE id = 57;

-- INNER JOIN
-- 두 테이블에서 일치하는 값을 가진 행들만 선택
-- SELECT <필드> FROM 테이블1
-- INNER JOIN 테이블2
-- ON 조건
-- 전체 사람들의 id, 이름, 직업을 조회하여라

SELECT hero.id, hero.name, job.job
FROM hero
INNER JOIN job
ON hero.job_id = job.id;

-- LEFT JOIN
-- 왼쪽테이블의 모든 행과 오른쪽 테이블에서 일치하는 값을 가진 행을 선택
-- 일치하는 값이 없는 경우에는 NULL 값을 가짐

SELECT hero.id, hero.name, job.job
FROM hero
LEFT JOIN job
ON hero.job_id = job.id;

-- 똑같은 코드 다른 표현 방식
SELECT hero.id, 이름, 직업
FROM hero
LEFT JOIN job
ON hero.job_id = job.id;

-- 영웅들의 id, 이름, 능력조회
SELECT hero.id, hero.name, power.능력
FROM hero
LEFT JOIN power
ON hero.id = power.hero_id;

