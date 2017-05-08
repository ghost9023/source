#데이터셋 생성

import operator
from math import log
import time
def createdataset():
    dataset=[['남','30대','no','yes','no','no'],
            ['여','20대','yes','yes','yes','no'],
            ['여','20대','yes','yes','no','no'],
            ['여','40대','no','no','no','no'],
            ['여','30대','no','yes','no','no'],
            ['여','30대','no','no','yes','no'],
            ['여','20대','no','yes','no','no'],
            ['여','20대','no','yes','yes','yes'],
            ['여','30대','yes','yes','no','yes'],
            ['남','40대','yes','no','yes','no'],
            ['남','20대','no','no','no','no'],
            ['남','30대','no','yes','yes','no'],
            ['남','20대','yes','no','no','no'],
            ['여','30대','yes','yes','no','yes'],
            ['남','30대','yes','yes','yes','yes'],
            ['여','30대','yes','no','no','no'],
            ['여','30대','no','yes','yes','yes'],
            ['남','20대','yes','yes','no','no'],
            ['남','40대','yes','no','yes','no'],
            ['남','30대','no','no','no','no'],
            ['여','30대','yes','yes','no','yes'],
            ['남','30대','yes','no','yes','no'],
            ['여','40대','no','yes','yes','yes'],
            ['남','30대','no','yes','no','no'],
            ['여','30대','yes','yes','yes','yes'],
            ['여','40대','yes','no','yes','no'],
            ['남','40대','yes','yes','no','yes'],
            ['여','40대','yes','yes','no','yes']]
    labels=['gender','age','job_yn','marry_yn','car_yn','coupon_yn']
    return dataset, labels

# DT 생성

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0] # 모든 클래스가 한쪽으로 몰려있을 경우 트리분할노드를 종료
    if len(dataSet[0]) == 1: # 더 이상 나눌 값이 데이터셋에 없을 때 트리분할노드를 종료
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet) # 정보획득량을 통해 최적의 분할 적합상태를 설정
    bestFeatLabel = labels[bestFeat]

    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][Value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabel)
    return myTree

# 엔트로피 계산

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2) # 엔트로피 계산식
    return shannonEnt

# 분류기

def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]  # 첫 번째 구분 노드
    secondDict = inputTree[firstStr] # 첫 노드에 의해 분류된 이후 딕셔너리
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): # 아래가 딕셔너리면 재귀적으로 classify(분류기)를 재귀적으로 계속 돌려서 분류를 계속 진행된다.
        classLabel = classify(valueOfFeat, featLabels, testVec) # 리프 노드 일땐 yes or no를 넣고 나머지 경우는 딕셔너리 상태일때니까 위 조건에 의해 재귀하서 재분류를 한다.
    else:
        classLabel = valueOfFeat # 최종 리프 노드는 yes, no로 구분되기 때문에 string이기 때문에 결과값이 출력 됐을 땐 classLabel을 리턴한다
    return classLabel



























