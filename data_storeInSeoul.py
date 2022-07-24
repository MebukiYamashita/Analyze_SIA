import requests
import pandas as pd
sgg_pop_df = pd.read_csv('./files/report.txt', sep='\t', header=2)

columns = {
    '기간': 'period',
    '자치구': 'auto',
    '계': 'sum1',
    '계.1': 'sum2',
    '계.2': 'sum3',
    '남자': 'man1',
    '남자.1': 'man2',
    '남자.2': 'man3',
    '여자': 'woman1',
    '여자.1': 'woman2',
    '여자.2': 'woman3',
    '세대': 'house',
    '세대당인구': 'pop1',
    '65세이상고령자': 'pop_old'
}