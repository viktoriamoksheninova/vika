import pandas as pd

df = pd.read_csv('train.csv')
print(df.info())


df.drop(['id','bdate','has_photo','has_mobile','followers_count',
'graduation','relation','life_main','people_main','city',
'last_seen','occupation_name','career_start','career_end'], axis=1, inplace=True)

def sex_apply(sex):
    if sex == 2:
        return 0 
    return 1
df['sex'] = df['sex'].apply(sex_apply)
df['education_form'].fillna('Full-time',inplace = True)
df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df['education_form'].value_counts())
df.drop(['education_form'],axis = 1,inplace = True)

def edu_statutus_apply(edu):
    if edu == 'Undergrduate applicant':
        return 1
    elif edu.find('Student')!= -1:
        return 2
    elif edu.find('Alumnus')!= -1:
        return 3
    else:
        return 4
df['education_status'] = df['education_status'].apply(edu_statutus_apply)
print(df['education_status'].value_counts())

def ocu_type_apply(ocu_type):
    if ocu_type == 'work':
        return 0 
    return 1
df['occupation_type'] = df['occupation_type'].apply(ocu_type_apply)
print(df['occupation_type'].value_counts())

def langs_apply(langs):
    if langs.find('Русский')!= -1:
        return 1
    return 0 
df['langs'] = df['langs'].apply(langs_apply)
df['occupation_type'].fillna('university', inplace = True)

df.info()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

x = df.drop('result', axis = 1)
y = df['result']
x_train, x_test, y_train, y_test = train_test_split(x,y,tast_size = 0.1)

sc = StandardScaler()
x_train = sc.fil_transform(x_train)
x_test = sc.transform(x_test)

classifier = KNeighborsClassifier(n_naighbors = 5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print(y_test)
print(y_pred)
print('Процент правильно предсказанных исходов:', round(accuracy_score(y_test, y_red) = 1))