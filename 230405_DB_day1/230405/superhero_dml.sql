-- 전체조회
SELECT * FROM superhero;


-- 나이, 소속회사가 겹치지 않는 사람들 중
-- 소속회사, 나이 순으로 정렬
SELECT DISTINCT age, company FROM superhero
ORDER BY company, age;

-- 소속회사 별로 나이가 많은 순으로 조회하기
SELECT DISTINCT name, age, company FROM superhero
ORDER BY company, age DESC;

-- 가입날짜가 2000년 1월 1일
-- 이전인 사람 조회(DATE 필드)

SELECT name, date FROM superheros
WHERE date < '2000/01/01';

-- LIKE -> %, _
-- % : 글자수 제한없이 패턴을 만족
-- _ : 글자수를 제한
SELECT * FROM superheros
WHERE name LIKE '%맨' and LENGTH(name) == 3;

-- 소속회사가 마블이고 직업이 영웅인 사람들

SELECT * FROM superheros
WHERE company = '마블' AND job = '영웅';

-- 특정 데이터 포함여부(IN)
-- 마블, DC 소속의 사람들을 조회
SELECT * FROM superheros
WHERE company = '마블' OR company = 'DC';

SELECT * FROM superheros
WHERE company IN ('마블', 'DC');

-- 특정 조건 사이에 존재하는 데이터 조회(BETWEEN ... AND ...)
-- 나이가 100~500살 사이의 사람들을 조회
-- BETWEEN 은 이상, 이하를 사용함
SELECT * FROM superheros
WHERE age BETWEEN 100 AND 500;

-- 원하는 행 개수만큼만 조회(LIMIT)
SELECT * FROM superheros LIMIT 1;

-- 나이가 가장 적은 사람 1명
SELECT * FROM superheros
ORDER BY age LIMIT 1;

-- 나이가 가장 많은 사람 10명
SELECT * FROM superheros
WHERE company == '마블'
ORDER BY age DESC LIMIT 10;

-- N 번째 데이터부터 조회(OFFSET)
-- 나이가 10번째로 많은 사람
SELECT * FROM superheros
ORDER BY age DESC
LIMIT 1 OFFSET 9;

-- 전체 데이터 수를 구하여라
SELECT COUNT(*) AS COUNT
FROM superheros;

-- 조건문과 함께 활용
SELECT COUNT(*) AS COUNT
FROM superheros
WHERE job = '악당';

-- 전체 평균 나이
SELECT AVG(age) AS 평균나이
FROM superheros;

-- 마블 영웅들의 평균나이
SELECT AVG(age) AS 평균나이
FROM superheros
WHERE company = '마블';

-- 그룹 별 계산(GROUP BY)
-- 각 소속회사의 평균 나이를 구하여라
SELECT company, AVG(age) AS 평균나이
FROM superheros
GROUP BY company;