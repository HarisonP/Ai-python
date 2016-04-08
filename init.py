from sklearn import svm
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB


import json
import numpy as np
import random
import features as translators
import data_operations as dataAPI


def train_tree_name_classifier():
    with open('femaleTrain.txt') as data_female:
        data_female = data_female.readlines();
    with open('maleTrain.txt') as data_male:
        data_male = data_male.readlines()

    data = data_male + data_female
    translated_data = [translators.translate_name_in_array(name.lower()) for name in data]
    translated_data_output = [1] * len(data_male) + [0] * len(data_female)

    # max_depth=11
    clf = tree.DecisionTreeClassifier(max_depth=9,random_state=3)
    clf = clf.fit(translated_data, translated_data_output)

    with open('femaleTest.txt') as data_female:
        test_data_female = data_female.readlines();
    with open('maleTest.txt') as data_male:
        test_data_male = data_male.readlines()


    female_succes_rate = 0;
    for female_name in test_data_female:
        if clf.predict([translators.translate_name_in_array(female_name)])[0] == 0:
            female_succes_rate += 1

    print(female_succes_rate, len(test_data_female))
    female_succes_rate = float(female_succes_rate) / len(test_data_female)
    print(female_succes_rate)


    male_succes_rate = 0;
    for male_name in test_data_male:
        if clf.predict([translators.translate_name_in_array(male_name)])[0] == 1:
            male_succes_rate += 1

    print(male_succes_rate, len(test_data_male))
    male_succes_rate = float(male_succes_rate) / len(test_data_male)
    print(male_succes_rate)

    print((male_succes_rate + female_succes_rate) / 2)

def train_knn_name_classifier():
    with open('femaleTrain.txt') as data_female:
        data_female = data_female.readlines();
    with open('maleTrain.txt') as data_male:
        data_male = data_male.readlines()

    data = data_male + data_female
    translated_data = [translators.translate_name_in_array(name) for name in data]
    translated_data_output = [1] * len(data_male) + [0] * len(data_female)

    print(data[0], translated_data[0], translated_data_output[0])

    # n = 3
    clf = KNeighborsClassifier(n_neighbors=15, p = 1)
    clf.fit(translated_data, translated_data_output)

    with open('femaleTest.txt') as data_female:
        test_data_female = data_female.readlines();
    with open('maleTest.txt') as data_male:
        test_data_male = data_male.readlines()


    female_succes_rate = 0;
    for female_name in test_data_female:
        if clf.predict([translators.translate_name_in_array(female_name)])[0] == 0:
            female_succes_rate += 1

    print(female_succes_rate, len(test_data_female))
    female_succes_rate = float(female_succes_rate) / len(test_data_female)
    print(female_succes_rate)


    male_succes_rate = 0;
    for male_name in test_data_male:
        if clf.predict([translators.translate_name_in_array(male_name)])[0] == 1:
            male_succes_rate += 1

    print(male_succes_rate, len(test_data_male))
    male_succes_rate = float(male_succes_rate) / len(test_data_male)
    print(male_succes_rate)
    print((male_succes_rate + female_succes_rate) / 2)

dataAPI.generate_train_and_test_files()

# 0.786247086247
train_tree_name_classifier()

# 70% k = 15 p = 1 0.744522144522
# train_knn_name_classifier()
