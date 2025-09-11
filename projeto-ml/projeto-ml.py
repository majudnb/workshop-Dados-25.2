#https://colab.research.google.com/drive/1Ksr7LepcNIs8HeX-Ma-euLHsilrEP-L_#scrollTo=PFTvOoL4irDb

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

data = {
    'titulo': ['Livro 1', 'Livro 2', 'Livro 3', 'Livro 4', 'Livro 5',
               'Livro 6', 'Livro 7', 'Livro 8', 'Livro 9', 'Livro 10'],
    'ano': [2020, 2019, 2021, 2018, 2022, 2021, 2020, 2019, 2022, 2021],
    'paginas': [250, 300, 150, 500, 400, 320, 280, 360, 420, 310],
    'autor': ['Autor 1', 'Autor 2', 'Autor 1', 'Autor 3', 'Autor 4',
              'Autor 2', 'Autor 1', 'Autor 3', 'Autor 4', 'Autor 2'],
    'genero': ['Ficção', 'Não-ficção', 'Ficção', 'Ficção', 'Não-ficção',
               'Ficção', 'Não-ficção', 'Ficção', 'Ficção', 'Não-ficção'],
    'reviews': [150, 200, 50, 500, 300, 120, 180, 220, 400, 160],
    'nota': [4.5, 3.8, 4.2, 3.5, 4.8, 4.1, 3.9, 4.0, 4.6, 3.7]
}

df = pd.DataFrame(data)

df['sucesso'] = (df['nota'] >= 4.0).astype(int)

features = ['ano', 'paginas', 'autor', 'genero', 'reviews']
X = df[features]
y = df['sucesso']

num_features = ['ano', 'paginas', 'reviews']
cat_features = ['autor', 'genero']

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

models = {
    "LogisticRegression": LogisticRegression(max_iter=500),
    "RandomForest": RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=3)
}

pipelines = {name: Pipeline([
    ('preprocessor', preprocessor),
    ('model', model)
]) for name, model in models.items()}

for name, pipe in pipelines.items():
    pipe.fit(X_train, y_train)
    print(f"{name} treinado com sucesso.")

results = {}
for name, pipe in pipelines.items():
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n{name} - Acurácia: {acc:.4f}")
    print(classification_report(y_test, y_pred))
    
    cv_scores = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')
    print(f"{name} - CV accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
    
    results[name] = acc

best_model_name = max(results, key=results.get)
best_model = pipelines[best_model_name]
print("\nMelhor modelo:", best_model_name)

joblib.dump(best_model, "best_model_livros.pkl")
print("Modelo salvo em best_model_livros.pkl")

novos_livros = pd.DataFrame({
    'ano': [2023, 2022],
    'paginas': [320, 400],
    'autor': ['Autor 1', 'Autor 4'],
    'genero': ['Ficção', 'Não-ficção'],
    'reviews': [150, 220]
})

previsoes = best_model.predict(novos_livros)
print("\nPrevisões de sucesso dos novos livros:", previsoes)
