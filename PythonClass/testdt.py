from collections import Counter, defaultdict
from functools import partial
import math, random

def entropy(class_probabilities):
    """given a list of class probabilities, compute the entropy"""
    return sum(-p * math.log(p, 2) for p in class_probabilities if p)

def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count
            for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    """find the entropy from this partition of data into subsets"""
    total_count = sum(len(subset) for subset in subsets)

    return sum( data_entropy(subset) * len(subset) / total_count
                for subset in subsets )

def group_by(items, key_fn):
    """returns a defaultdict(list), where each input item
    is in the list whose key is key_fn(item)"""
    groups = defaultdict(list)
    for item in items:
        key = key_fn(item)
        groups[key].append(item)
    return groups

def partition_by(inputs, attribute):
    """returns a dict of inputs partitioned by the attribute
    each input is a pair (attribute_dict, label)"""
    return group_by(inputs, lambda x: x[0][attribute])

def partition_entropy_by(inputs,attribute):
    """computes the entropy corresponding to the given partition"""
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())

def classify(tree, input):
    """classify the input using the given decision tree"""

    # if this is a leaf node, return its value
    if tree in [True, False]:
        return tree

    # otherwise find the correct subtree
    attribute, subtree_dict = tree

    subtree_key = input.get(attribute)  # None if input is missing attribute

    if subtree_key not in subtree_dict: # if no subtree for key,
        subtree_key = None              # we'll use the None subtree

    subtree = subtree_dict[subtree_key] # choose the appropriate subtree
    return classify(subtree, input)     # and use it to classify the input

def build_tree_id3(inputs, split_candidates=None):

    # if this is our first pass,
    # all keys of the first input are split candidates
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()

    # count Trues and Falses in the inputs
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues

    if num_trues == 0:                  # if only Falses are left
        return False                    # return a "False" leaf

    if num_falses == 0:                 # if only Trues are left
        return True                     # return a "True" leaf

    if not split_candidates:            # if no split candidates left
        return num_trues >= num_falses  # return the majority leaf

    # otherwise, split on the best attribute
    best_attribute = min(split_candidates,
        key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates
                      if a != best_attribute]

    # recursively build the subtrees
    subtrees = { attribute : build_tree_id3(subset, new_candidates)
                 for attribute, subset in partitions.items() }

    subtrees[None] = num_trues > num_falses # default case

    return (best_attribute, subtrees)

if __name__ == "__main__":

    inputs = []  # 최종적으로 사용할 데이터셋의 형태가 리스트여야 하기 때문에 빈 리스트를 생성합니다.

    inputss = [['남', '30대', 'no', 'yes', 'no', 'no'],
               ['여', '20대', 'yes', 'yes', 'yes', 'no'],
               ['여', '20대', 'yes', 'yes', 'no', 'no'],
               ['여', '40대', 'no', 'no', 'no', 'no'],
               ['여', '30대', 'no', 'yes', 'no', 'no'],
               ['여', '30대', 'no', 'no', 'yes', 'no'],
               ['여', '20대', 'no', 'yes', 'no', 'no'],
               ['여', '20대', 'no', 'yes', 'yes', 'yes'],
               ['여', '30대', 'yes', 'yes', 'no', 'yes'],
               ['남', '40대', 'yes', 'no', 'yes', 'no'],
               ['남', '20대', 'no', 'no', 'no', 'no'],
               ['남', '30대', 'no', 'yes', 'yes', 'no'],
               ['남', '20대', 'yes', 'no', 'no', 'no'],
               ['여', '30대', 'yes', 'yes', 'no', 'yes'],
               ['남', '30대', 'yes', 'yes', 'yes', 'yes'],
               ['여', '30대', 'yes', 'no', 'no', 'no'],
               ['여', '30대', 'no', 'yes', 'yes', 'yes'],
               ['남', '20대', 'yes', 'yes', 'no', 'no'],
               ['남', '40대', 'yes', 'no', 'yes', 'no'],
               ['남', '30대', 'no', 'no', 'no', 'no'],
               ['여', '30대', 'yes', 'yes', 'no', 'yes'],
               ['남', '30대', 'yes', 'no', 'yes', 'no'],
               ['여', '40대', 'no', 'yes', 'yes', 'yes'],
               ['남', '30대', 'no', 'yes', 'no', 'no'],
               ['여', '30대', 'yes', 'yes', 'yes', 'yes'],
               ['여', '40대', 'yes', 'no', 'yes', 'no'],
               ['남', '40대', 'yes', 'yes', 'no', 'yes'],
               ['여', '40대', 'yes', 'yes', 'no', 'yes']]  # 데이터 값

    labelss = ['gender', 'age', 'job_yn', 'marry_yn', 'car_yn', 'coupon_yn']  # 데이터의 라벨(컬럼명)
    alabel = ['gender', 'age', 'job_yn', 'marry_yn', 'car_yn']
    for data in inputss:  # 위처럼 리스트로 된 데이터값과 리스트로된 라벨(컬럼명)을 분석에 맞는 데이터형태로 바꾸는 과정.
        temp_dict = {}  # 데이터셋 = [ ( {데이터가 되는 컬럼의 키와 값으로 구성된 딕셔너리}, 분석타겟컬럼의 값  ) , ..... ] 의 형태로 되어있어야 분석할 수 있다.
        for i in range(len(labelss)):
            if i != 5:
                temp_dict[labelss[i]] = data[i]
        inputs.append(tuple((temp_dict, True if data[5] == 'yes' else False)))

    print("building the tree")
    tree = build_tree_id3(inputs)
    print(tree)


print(classify(tree,{ "gender" : "여"}))