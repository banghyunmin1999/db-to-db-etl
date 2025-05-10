# 🏗️ db-to-db-etl 프로젝트

**ETL(Extract, Transform, Load)** 파이프라인을 통해 고객의 금융 데이터를 집계하고,  
요약 테이블에 주기적으로 적재하는 자동화 시스템입니다.

---

## 📌 프로젝트 개요

- **목표**: MySQL에 저장된 원천 금융 데이터를 가공하여, 요약된 형태로 새로운 테이블에 적재
- **주요 기능**:
  - 원천 테이블 간 조인 및 집계 처리
  - 고객별 예금/대출 통합 요약
  - AWS EC2 서버에서 주기적 스케줄링 (Crontab 사용)

---


## ⚙️ 사용 기술

- Python (pandas, SQLAlchemy)
- MySQL
- Jupyter Notebook
- AWS EC2 (Ubuntu)
- Crontab

---


## 📎 참고 문서

- 프로젝트 설계 및 분석 자료는 `docs/` 폴더를 참고하세요.
    - `docs/ETL_패널_방현민.pptx`
    - `docs/01. ETL_분석모델정의서.pptx`

---

## 👤 작성자

- 방현민 

---

