"""
날짜 : 2020/07/22
이름 : 권기민
내용 : 파이썬 Hadoop 실습하기
"""

import os
from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop

# Hadoop 접속
hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')

# local의 /home/bigdata/naver/naver-20-xx-xx를 하둡 /naver/ 복사
old_naver = os.dir = '/home/bigdata/naver'
new_naver = hdfs.destination_dir = '/naver'
hdfs.rename_file_dir(dir, destination_dir)

print('폴더 이동 완료')

# local의 /home/bigdata/naver/naver-20-xx-xx를 삭제

# 프로그램 종료