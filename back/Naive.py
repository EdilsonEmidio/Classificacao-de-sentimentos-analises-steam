from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn.naive_bayes import MultinomialNB
import Folds 

def organizar_dataset(json_positivo, json_negativo, quant, fold):
    i = 0
    if fold==0:
        reviews_treino, label_treino, reviews_test, label_test = Folds.fold0(json_positivo, json_negativo, quant)
    elif fold==1:
        reviews_treino, label_treino, reviews_test, label_test = Folds.fold1(json_positivo, json_negativo, quant)
    elif fold==2:
        reviews_treino, label_treino, reviews_test, label_test = Folds.fold2(json_positivo, json_negativo, quant)
    elif fold==3:
        reviews_treino, label_treino, reviews_test, label_test = Folds.fold3(json_positivo, json_negativo, quant)
    else:
        reviews_treino, label_treino, reviews_test, label_test = Folds.fold0(json_positivo, json_negativo, quant)
        
    #treinando aqui abaixo
    vectorizer = CountVectorizer()
    X_treino = vectorizer.fit_transform(reviews_treino)
    X_treino = TfidfTransformer().fit_transform(X_treino)

    model = MultinomialNB().fit(X_treino, label_treino)

    X_test = vectorizer.transform(reviews_test)
    X_test = TfidfTransformer().fit_transform(X_test)

    predito = model.predict(X_test)
    retorno = {}
    
    accuracy = accuracy_score(label_test, predito)
    precision = precision_score(label_test, predito)
    recall = recall_score(label_test, predito)
    fscore = f1_score(label_test, predito)
    retorno = {
        "acuracia":accuracy,
        "precisao":precision,
        "recall":recall,
        "fscore":fscore,
        "reviews":[]
    }
    i=0
    
    while(i<30):
        retorno["reviews"].append(
            {
                "review":reviews_test[i],
                "saida":bool(predito[i]),
                "esperado":label_test[i]
            }
        )
        i+=1

    return retorno
