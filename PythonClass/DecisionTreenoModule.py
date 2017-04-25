def entropy(class_probability):
    return sum(-p * math.log(p,2) for p in class_probabilities if p)
def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]
def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)
def partition_entropy(subsets):
    total_count = sum(len(subset) for subset in subsets)
    return sum( data_entropy(subset)*len(subset)/total_count for subset in subsets)

inputs = []

inputss=[['남','30대','no','yes','no','no'],
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

labelss = ['gender', 'age', 'job_yn', 'marry_yn', 'car_yn', 'coupon_yn']

for data in inputss:
    temp_dict = {}
    for i in range(len(labelss)):
        if i != 5:
            temp_dict[labelss[i]] = data[i]
    inputs.append(tuple((temp_dict, True if data[5] == 'yes' else False)))

def partition_by(inputs, attribute):
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][attribute]
        groups[key].append(input)
    return groups

def partition_entropy_by(inputs, attribute):
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())

for key in ['gender', 'age', 'job_yn', 'marry_yn', 'car_yn']:
    print(key, partition_entropy_by(inputs, key))

# senior_inputs = [(input, label) for input, label in inputs if input["level"] == ""]


def classify(tree, input): #분류기 선언, tree의 input값을 분류
    if tree in [True, False]: # 잎 노드면 값을 반환
        return tree

    attribute, subtree_dict = tree  # 위 경우가 아니면 키로 변수 값, 값으로 서브트리를 나타내는 딕셔너리로 파티션분할

    subtree_key = input.get(attribute) # 입력된 데이터 변수 중 하나가 기존에 관찰되지 않은 변수면 None을 입력

    if subtree_key not in subtree_dict: # 키에 해당하는 서브트리가 존재하지 않으면
        subtree = subtree_dict[subtree_key] # None 서브트리를 사용
    subtree = subtree_dict[subtree_key] # 서브트리를 선택
    return classify(subtree, input) # 이 과정을 재귀를 통해 잎 노드가 반환될 때까지 계속 수행

def build_tree_id3(inputs, split_candidates = None):

    if split_candidates is None: # 파티션이 첫 단계면 입력된 데이터의 모든 변수를 파티션 기준 후보로 설정
        split_candidates = inputs[0][0].keys()

    num_inputs = len(inputs) # 입력된 데이터에서 True, False 개수를 체크
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues

    if num_trues == 0:
        return False # true가 없다면 false 잎 노드를 반환
    if num_falses == 0:
        return True # false가 없다면 true 잎 노드를 반환

    if not split_candidates:
        return num_trues >= num_falses # 만약 사용할 변수가 없으면 많은 수를 반환

    best_attribute = min(split_candidates, key=partial(partition_entropy_by, inputs))
    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates
                      if a != best_attribute]
    subtrees = { attribute_value : build_tree_id3(subset, new_candidates) for attribute_value, subset in partitions.iteritems()}
    subtrees[None] = num_trues > num_falses # 기본값
    return (best_attribute, subtrees)

tree = build_tree_id3(inputs)
