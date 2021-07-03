from scripts.generate_training_data import main_refer_gen_data
from scripts.gen_adj_mx import main_refer_gen_adj_mx
from dcrnn_train import main_refer_train
from scripts.eval_baseline_methods import main_refer_eval
import argparse
import os

# 파일이름은 Seoul_all 로 함


name_list=['virtual_1220024600','virtual_1220025200','virtual_1220026100','virtual_1220027500',
           'virtual_1220029600','virtual_1220030400','virtual_1220031300','virtual_1220032300']

file = name_list[3]
path = f'./data/{file}'


try:
    os.mkdir(path)
except:
    True


#데이터 준비하기 - train, test, valivalidation 나누기


main_refer_gen_data(file)
print("\n\n\n\n@@@@@Data generated@@@@@\n\n\n\n")
#그래프 구성
main_refer_gen_adj_mx(file)
print("\n\n\n\n@@@@@Graph generated@@@@@\n\n\n\n")
#트레이닝
main_refer_train(file)
print("\n\n\n\n@@@@@Model generated@@@@@\n\n\n\n")


print(f"{file} @@@@@@@@@@@@@@@@@@완료")


#
#
# file = 'virtual_1220025200'
# path = f'./data/{file}'
#
#
# try:
#     os.mkdir(path)
# except:
#     True
#
#
# #데이터 준비하기 - train, test, valivalidation 나누기
#
#
# main_refer_gen_data(file)
# print("\n\n\n\n@@@@@Data generated@@@@@\n\n\n\n")
# #그래프 구성
# main_refer_gen_adj_mx(file)
# print("\n\n\n\n@@@@@Graph generated@@@@@\n\n\n\n")
# #트레이닝
# main_refer_train(file)
# print("\n\n\n\n@@@@@Model generated@@@@@\n\n\n\n")
#
#
# print(f"{file} @@@@@@@@@@@@@@@@@@완료")



#
# file = 'virtual_1220026100'
# path = f'./data/{file}'
#
#
# try:
#     os.mkdir(path)
# except:
#     True
#
#
# #데이터 준비하기 - train, test, valivalidation 나누기
#
#
# main_refer_gen_data(file)
# print("\n\n\n\n@@@@@Data generated@@@@@\n\n\n\n")
# #그래프 구성
# main_refer_gen_adj_mx(file)
# print("\n\n\n\n@@@@@Graph generated@@@@@\n\n\n\n")
# #트레이닝
# main_refer_train(file)
# print("\n\n\n\n@@@@@Model generated@@@@@\n\n\n\n")
#
#
# print(f"{file} @@@@@@@@@@@@@@@@@@완료")
#



# file = 'virtual_1220027500'
# path = f'./data/{file}'
#
#
# try:
#     os.mkdir(path)
# except:
#     True
#
#
# #데이터 준비하기 - train, test, valivalidation 나누기
#
#
# main_refer_gen_data(file)
# print("\n\n\n\n@@@@@Data generated@@@@@\n\n\n\n")
# #그래프 구성
# main_refer_gen_adj_mx(file)
# print("\n\n\n\n@@@@@Graph generated@@@@@\n\n\n\n")
# #트레이닝
# main_refer_train(file)
# print("\n\n\n\n@@@@@Model generated@@@@@\n\n\n\n")
#
#
#
#
# print(f"{file} @@@@@@@@@@@@@@@@@@완료")
#
#
#
# file = 'virtual_1220029600'
# path = f'./data/{file}'
#
#
# try:
#     os.mkdir(path)
# except:
#     True
#
#
# #데이터 준비하기 - train, test, valivalidation 나누기
#
#
# main_refer_gen_data(file)
# print("\n\n\n\n@@@@@Data generated@@@@@\n\n\n\n")
# #그래프 구성
# main_refer_gen_adj_mx(file)
# print("\n\n\n\n@@@@@Graph generated@@@@@\n\n\n\n")
# #트레이닝
# main_refer_train(file)
# print("\n\n\n\n@@@@@Model generated@@@@@\n\n\n\n")
#
# print(f"{file} @@@@@@@@@@@@@@@@@@완료")
# #

#
# file = 'virtual_1220030400'
# path = f'./data/{file}'
#
#
# try:
#     os.mkdir(path)
# except:
#     True
#
#
# #데이터 준비하기 - train, test, valivalidation 나누기
#
#
# main_refer_gen_data(file)
# print("\n\n\n\n@@@@@Data generated@@@@@\n\n\n\n")
# #그래프 구성
# main_refer_gen_adj_mx(file)
# print("\n\n\n\n@@@@@Graph generated@@@@@\n\n\n\n")
# #트레이닝
# main_refer_train(file)
# print("\n\n\n\n@@@@@Model generated@@@@@\n\n\n\n")
#
#
# print(f"{file} @@@@@@@@@@@@@@@@@@완료")
#
#
#
# file = 'virtual_1220031300'
# path = f'./data/{file}'
#
#
# try:
#     os.mkdir(path)
# except:
#     True
#
#
# #데이터 준비하기 - train, test, valivalidation 나누기
#
#
# main_refer_gen_data(file)
# print("\n\n\n\n@@@@@Data generated@@@@@\n\n\n\n")
# #그래프 구성
# main_refer_gen_adj_mx(file)
# print("\n\n\n\n@@@@@Graph generated@@@@@\n\n\n\n")
# #트레이닝
# main_refer_train(file)
# print("\n\n\n\n@@@@@Model generated@@@@@\n\n\n\n")
#
#
# print(f"{file} @@@@@@@@@@@@@@@@@@완료")