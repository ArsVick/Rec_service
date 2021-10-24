# # импорты
# import pandas as pd
# import numpy as np
# from tqdm.notebook import tqdm
# from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
# from sklearn.neighbors import NearestNeighbors
# import pickle5 as pickle
# # import pickle
# import random
#
#
# def load_obj(name):
#     with open('obj/' + name + '.pkl', 'rb') as f:
#         return pickle.load(f)
#
#
# # загрузка модели и датасета
# best_books = [59539,
#               90136,
#               100198,
#               506885,
#               198185,
#               2507,
#               2120,
#               2098,
#               629210,
#               245280,
#               765117,
#               1294752,
#               79671,
#               1094723,
#               488269,
#               1271445,
#               1271448,
#               326819,
#               326736,
#               1,
#               9234,
#               2559,
#               2496,
#               408529,
#               1595987,
#               321164,
#               24189,
#               629185,
#               399501,
#               2846,
#               570219,
#               554713,
#               55357,
#               1698929,
#               3989,
#               3915,
#               87289,
#               258809,
#               83282,
#               232489,
#               256714,
#               432256,
#               1811765,
#               1180674,
#               702041,
#               958881,
#               1335388,
#               559117,
#               2114,
#               43531,
#               203212,
#               60804,
#               27939,
#               443769,
#               90303,
#               391825,
#               1404972,
#               854720,
#               452624,
#               816610,
#               576017,
#               2151,
#               576231,
#               780761,
#               1553823,
#               1426384,
#               252473,
#               1127207,
#               23700,
#               485633,
#               1757276,
#               786831,
#               1330514,
#               1636285,
#               92783,
#               6012,
#               277567,
#               550129,
#               75680,
#               254070,
#               26467,
#               1314611,
#               448519,
#               1645,
#               97439,
#               979786,
#               71181,
#               184743,
#               769937,
#               14898,
#               77803,
#               2169,
#               1961312,
#               41156,
#               817789,
#               843453,
#               80319,
#               32548,
#               615704,
#               210546,
#               185949,
#               125927,
#               25321,
#               1953,
#               181891,
#               245411,
#               1298731,
#               914797,
#               82951,
#               483727,
#               101546,
#               814608,
#               162657,
#               36736,
#               1368607,
#               1423910,
#               1180623,
#               2141,
#               1209762,
#               1042255]
#
# books = pd.read_csv('obj/books.csv')
# books_full_an = pd.read_csv('obj/books_full_an.csv')
# circulaton_full = pd.read_csv('obj/circulaton_full.csv')
# set_id = load_obj('set_id')
#
# neigh = load_obj('model')
# tfidf_transformer = load_obj('tfidf_transformer')
# count_vect = load_obj('count_vect')
# # Номер пользователя
# user = 1
#
#
# def pred_fun(user
#              # , books, books_full_an, circulaton_full, set_id, neigh, tfidf_transformer, count_vect,
#              ):
#     set_id = set(books_full_an.id.tolist())
#     # print(len(set_id))
#     print(circulaton_full['readerID'])
#     list_of_books = circulaton_full.loc[circulaton_full['readerID'] == user].catalogueRecordID.tolist() # History
#     print(list_of_books)
#     if len(list_of_books) > 0: # Проверка что пользователь брал хоть 1 книгу
#         test = ''
#         for x in list_of_books:
#             if x  in set_id:
#                 None
#             else:
#                 a = books_full_an.loc[books_full_an['id'] == x].iat[0, 3]
#                 test = test + ' ' + a
#         test = test.replace("  ", " ")
#         predict = count_vect.transform([test])
#         X_tfidf2 = tfidf_transformer.transform(predict)
#         res = neigh.kneighbors(X_tfidf2, return_distance=True)
#         return books.iloc[res[1][0]].id.tolist()
#     else:
#         print('I hate niggers')
#         return random.sample(best_books, 5)
#
#

# импорты
