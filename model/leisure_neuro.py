import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

df = pd.read_csv('leisure2.csv')
#df = df.drop_duplicates()

X = df[['area', 'duration', 'budget', 'time', 'type']].values
y = df['place'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 1) #random_state = 2

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'derevo.pkl')
print("Модель сохранена в файл derevo.pkl")

y_pred = model.predict(X_test)
print("accuracy:", accuracy_score(y_test, y_pred))

area = int(input("Введите, где бы Вы хотели отдохнуть: улица - 1, помещение - 2 "))
duration = int(input("Введите время отдыха: 1 час = 1, 3 часа = 3, 6 часов = 6"))
budget = int(input("Введите ваш бюджет: до 1000 рублей = 1000, больше 1000 = 10000"))
time = int(input("Введите время суток: утро = 1, день = 2, вечер = 3, ночь = 4"))
type_l = int(input("Введите тип отдыха: активный = 1, пассивный = 2"))
answer = model.predict([[area, duration, budget, time, type_l]])
if answer == 1:
    print("Прогулка в парке или на набережной.")
elif answer == 2:
    print("Велосипед, самокат или лыжи, если лежит снег.")
elif answer == 3:
    print("Экскурсия или городской квест.")
elif answer == 4:
    print("Пикник или шашлыки.")
elif answer == 5:
    print("Кинотеатр.")
elif answer == 6:
    print("Музей, выставка или галерея.")
elif answer == 7:
    print("Тир или боулинг.")
elif answer == 8:
    print("Тренажёрный зал или фитнес-клуб.")
elif answer == 9:
    print("Бар или кафе.")
    
