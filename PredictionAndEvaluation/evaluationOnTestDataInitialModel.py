from ultralytics import YOLO
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

dataset = pd.read_csv("../ModelsAndResults/initialModelTrain/results.csv", delimiter=",")

print(dataset.head())
print(dataset.columns)
sns.pairplot(dataset, x_vars="epoch", y_vars="val/cls_loss")
plt.show()

print(dataset["val/cls_loss"].min())
print(dataset["val/box_loss"].min())

