import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

user = 'kopouser'
password = 'kopouser'
host = '52.78.189.121'  
port = '3306'  
database = 'kopo'
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')
engine


def makeData():
    sqlSelect = """
    SELECT NOW() AS time_tag, C.CUSTOMER_ID, C.NAME , COALESCE(C.TOTAL_BALANCE,0) AS total_balance , COALESCE(D.TOTAL_LOAN_AMOUNT,0) AS total_loan_amount
    FROM 
    (
    	SELECT  A.CUSTOMER_ID  , B.NAME , SUM(A.BALANCE) AS total_balance
    	FROM account_info A 
    	INNER JOIN customer_info B
    	ON A.CUSTOMER_ID = B.CUSTOMER_ID
    	GROUP BY   A.CUSTOMER_ID , B.NAME
    ) C
    LEFT JOIN 
    (
    	SELECT A.CUSTOMER_ID , SUM(B.loan_amount) AS total_loan_amount
    	FROM customer_info A
    	LEFT JOIN loan_info B
    	ON A.CUSTOMER_ID = B.CUSTOMER_ID
    	GROUP BY A.CUSTOMER_ID
    ) D
    ON C.CUSTOMER_ID = D.CUSTOMER_ID
    """
    selloutDf = pd.read_sql_query(sqlSelect, con=engine)
    selloutDf.to_sql(
    'customer_finance_summary',
    con=engine,
    if_exists='append',  # 기존 테이블에 추가
    index=False
    )

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    makeData()
    print(f"{now} : customer_finance_summary 테이블에 데이터 추가 완료")
except Exception as e: 
    print(f"오류 발생 : {e}")