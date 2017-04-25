# 의사결정나무를 만들고 시각화 하기 위한 패키지가 몇가지 있다.
# 1. GraphViz : 노드를 다이어그램형태로 시각화
# 2. pydot : 트리를 시각화
# 3. Numpy : 수학적 계산을 위한 모듈
# 3. IPython
# 4. scipy : 과학적 계산을 위한 모듈
# 5. sklearn : 머신러닝, 데이터마이닝을 위한 모듈
#  우선 패키지를 설치하고 시작하자.
#
# references
# https://www.datascienceschool.net/view-notebook/583f056ecca24bf78e6850af1439a104/
# https://www.datascienceschool.net/view-notebook/d3ecf5cc7027441c8509c0cae7fea088/
# https://www.datascienceschool.net/view-notebook/16c28c8c192147bfb3d4059474209e0a/
#
# numpy.distutils.system_info.NotFoundError: no lapack/blas resources found
#

import io
import pydot
from IPython.core.display import Image
from sklearn.tree import export_graphviz
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

def draw_decision_tree(classifier):
    dot_buf = io.StringIO()
    export_graphviz(classifier, out_file=dot_buf, feature_names=iris.feature_names)
    graph = pydot.graph_from_dot_data(dot_buf.getvalue())[0]
    image = graph.create_png()
    return Image(image)


def plot_decision_regions(X, y, classifier, title):
    resolution = 0.01
    markers = ('s', '^', 'o')
    colors = ('red', 'blue', 'lightgreen')
    cmap = mpl.colors.ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T).reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], s=80, label=cl)

    plt.xlabel('sepal length [cm]')
    plt.ylabel('sepal width [cm]')
    plt.legend(loc='upper left')
    plt.title(title)
    plt.show()

from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

from sklearn.tree import DecisionTreeClassifier

tree5 = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=0).fit(X, y)

draw_decision_tree(tree5)

