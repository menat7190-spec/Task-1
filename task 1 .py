from sklearn.datasets import load_iris
iris = load_iris()
print("Number of Samples:", iris.data.shape[0])
print("Number of Features:", iris.data.shape[1])
print("Classes:", iris.target_names)
