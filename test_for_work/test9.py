import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import keras
from keras import metrics
from keras import regularizers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D, Conv1D, MaxPooling1D
from keras.layers import LSTM, GRU
from keras.optimizers import Adam, RMSprop
from keras.layers.embeddings import Embedding
"""
0 смотрю визуально на данные +
1 создаю векторы/массивы из полей + 
2 сравню эти векторы по косинусному расстянию +
3 обучаю сеть -

"""

def get_g(data, to_fig):
    fig = plt.figure()
    for ix in range(len(to_fig)):
        ax = fig.add_subplot(len(to_fig), len(to_fig), ix+1)
        ax.set_title(f'Т{ix}')
        max_x = data[to_fig[ix][0]].max()
        #min_x = data[to_fig[ix][0]].min()
        max_y = data[to_fig[ix][1]].max()
        #min_y = data[to_fig[ix][0]].max()
        ax.set_xlim([0, max_x])
        ax.set_ylim([0, max_y])
        ax.set_xlabel(f'ось {to_fig[ix][0]}')
        ax.set_ylabel(f'ось {to_fig[ix][1]}')   
        ax.scatter(data[to_fig[ix][0]], data[to_fig[ix][1]], c = 'g', s = 14)
    fig.set_figwidth(20)
    fig.set_figheight(20)
    plt.show()


#def get_g(data, to_fig):
#    fig = plt.figure()
#    ax_ls = []
#    for i in range(len(to_fig)):
#        ax_ls.append(fig.add_subplot(len(to_fig), len(to_fig), i+1))
#    for ix, ax in enumerate(ax_ls):
#        #print (data[to_fig[ix][0]].idxmax(), data[to_fig[ix][1]].idxmin())
#        ax.set_title(f'Т{ix}')
#        max_x = data[to_fig[ix][0]].max()
#        #min_x = data[to_fig[ix][0]].min()
#        max_y = data[to_fig[ix][1]].max()
#        #min_y = data[to_fig[ix][0]].max()
#        ax.set_xlim([0, max_x])
#        ax.set_ylim([0, max_y])
#        ax.set_xlabel(f'ось {to_fig[ix][0]}')
#        ax.set_ylabel(f'ось {to_fig[ix][1]}')   
#        ax.scatter(data[to_fig[ix][0]], data[to_fig[ix][1]], c = 'g', s = 14)
#    fig.set_figwidth(20)
#    fig.set_figheight(20)
#    plt.show()




def similarity(vector1, vector2):
    return np.dot(vector1, vector2.T) / np.dot(np.linalg.norm(vector1, axis=0, keepdims=True), np.linalg.norm(vector2.T, axis=0, keepdims=True))

def func_sort(ID):
    if len(arr) != 0:
        for i in range(len(arr)):
            if ID not in G.keys():
                    preds0 = arr[i][0]
                    G[ID] = [[preds0, arr[i][1]]]
                    del arr[i]
            else:
                try:
                    preds1 = arr[i][0]
                    KEF = similarity(preds0, preds1)
                    if KEF>tresh:
                         G[ID].append([preds1, arr[i][1]])
                         del arr[i]
                except IndexError: 
                    if len(arr) == 0:
                         break
                    ID += 1
                    func_sort(ID)

def simple_crossing(a, b, x, y):
    #index = np.where(arr_v[:,0] == 0.0)[0]
    index_a = np.where(arr_v[:,a] >= x)[0] 
    index_b = np.where(arr_v[:,b] >= y)[0]
    new_a = arr_v[index_a]
    new_b = arr_v[index_b]
    #new_c = np.delete(arr_v, index_a, axis=0)
    t_list = []
    for t in index_a: 
        if t in index_b:
            t_list.append(arr_v[t])
    return t_list   



if __name__ == "__main__":
    f_open = pd.read_csv('data.csv', delimiter=',')

    # Смотрю на статистику данных
    for c in f_open.columns.tolist():
        print (f"###############\n{f_open[c].value_counts(dropna=False)}")

    # Убираю NaN
    f_open['transport_min_distance'] = f_open['transport_min_distance'].replace(np.nan, 0)
    f_open['parking_min_distance'] = f_open['parking_min_distance'].replace(np.nan, 0)
    f_open['price'] = f_open['price'].replace(np.nan, 0)
#    print (f_open[f_open['price'] == 352119.0])
#    # данные на 2 группы Москва/Не Москва
#    data_moscow = f_open.loc[f_open["is_moscow"] == True]
#    not_moscow = f_open.loc[f_open["is_moscow"] == False]

#    # Простая визуалтзация
#    get_g(data_moscow, "finance_count", "distance_100")
#    get_g(not_moscow, "finance_count", "distance_100")
    get_g(f_open, [["distance_100", "parking_min_distance"],
                   ["cafe_count", "distance_100"],
                   ["distance_100", "finance_count"],
                   ["price", "parking_min_distance"],
                   ["price", "distance_100"],
                   ["finance_count", "distance_100"]])



    # Решил не учитывать culture_count
    att_col = ["price", "finance_count", "shop_count", "distance_100", "distance_500", "cafe_count", "culture_count", "job_gov_count", 
               "parking_min_distance", "parking_count", "transport_min_distance", "transport_count", "cafe_count", "shop_count",
               "place_type", "lat", "lon"] 

    coding_vec = ["ОПС Б1_2", "ОПС Б1", "ТП", "КЦ", "other"]   
    
    #f_open = data_moscow[att_col]
    print (f_open["price"].describe())
    print (f_open["distance_100"].describe())
    f_open = f_open[att_col]
    arr_v = f_open.to_numpy()
    print (len(simple_crossing(0, 3, 300000, 1)), simple_crossing(0, 3, 300000, 1))
    
    for d in range(arr_v.shape[1]):
        for r in range(arr_v.shape[0]):
            try: 
                arr_v[r,d] = coding_vec.index(arr_v[r,d])
            except ValueError:
                pass

    # Простая кластеризация
    min_max_scalar = preprocessing.MinMaxScaler()#feature_range=(0,1)
    data_scale = min_max_scalar.fit_transform(arr_v)
    tresh = .96
    G = {}
    arr = []
    for l in range(data_scale.shape[0]):
        arr.append([data_scale[l,:], arr_v[l,:]])
    func_sort(0)

    for k in list(G.keys()):
        #print (len(G[k])) 
        if len(G[k]) > 8:
           print (G[k][0][1]) 
     
#Уже не успею доделать, пора отдыхать, описание внутри файла.

    """
    К сожалению эти данные и мои знания не позволяют мне оценить прибыльность, предпологаю нужно знать:   
        1 - полная стоимости аренды если она есть (почта гос учереждение)
        2 - кол-во сотрудников
        3 - зп сотрудников
        4 - цена комунальных услуг
        5 - прибыл/убыток отделения
        6 - кол-во человек побывавших в отделении
    Из имеющихся данных мои наблюдения:
        - высокая цена на площадь при низких distance, 
        - так же в ценовом диапазоне 200000 - 250000, 37% имеет низкую distance
        - очень странно, при близкой паркове низкая distance
        Некоторые данные похожи на синтезированные, возможно из за моего недостаточного опыта.
    ** distance - надеюсь чам выше тем лучше:)
    Что можно сделать.
        Обучить сеть рекомендовать цену:
            0 - цена ниже рынка с "приемлимой пропускной способностью"
            1 - цена средняя
            2 - цена завышена "низкая пропускная способность"
        Обучить сеть предсказывать кол-во людей - не получилось
           
        Статьи которые прочитал для анализа этих данных
           
    """

# data.sort_values(by=name_x, ascending=True, inplace=True)
# f_open.pivot_table("id", "finance_count", "shop_count").plot(kind='bar', stacked=True)
# pd.get_dummies(f_open[name])
# (f_open[name]==True).sum() 
# f_open.nunique()
# f_open[name].nunique()
# f_open.columns.tolist()
# f_open.info()
# f_open.describe()
# np.isnan(arr[r,d])

# https://habr.com/ru/post/196980/
# https://medium.com/@bigdataschool/4-шага-к-моделированию-machine-learning-практические-примеры-на-python-caee5f123873 
# https://konstantinklepikov.github.io/2019/10/08/scikit-learn-preprocessing.html
# http://blog.datalytica.ru/2018/04/blog-post.html   
# https://habr.com/ru/post/491552/    
# https://habr.com/ru/post/202090/
# https://www.kaggle.com/rohitanil/keras-cnn-lstm-lb-0-059
# https://habr.com/ru/post/468295/
