
#fold 0
def fold0(json_positivo, json_negativo, quant):
    i = 0
    reviews_treino = []
    label_treino = []
    reviews_test = []
    label_test = []
    while(i<quant):
        
        if i<75:
            reviews_treino.append(json_positivo[i].get("review"))
            label_treino.append(json_positivo[i].get("voted_up"))
            reviews_treino.append(json_negativo[i].get("review"))
            label_treino.append(json_negativo[i].get("voted_up"))
        else:
            reviews_test.append(json_positivo[i].get("review"))
            label_test.append(json_positivo[i].get("voted_up"))
            reviews_test.append(json_negativo[i].get("review"))
            label_test.append(json_negativo[i].get("voted_up"))
            
        i+=1

    return reviews_treino, label_treino, reviews_test, label_test

#fold 1
def fold1(json_positivo, json_negativo, quant):
    i = 25
    reviews_treino = []
    label_treino = []
    reviews_test = []
    label_test = []
    while(i<quant):
        
        if i<100 and i>25:
            reviews_treino.append(json_positivo[i].get("review"))
            label_treino.append(json_positivo[i].get("voted_up"))
            reviews_treino.append(json_negativo[i].get("review"))
            label_treino.append(json_negativo[i].get("voted_up"))
        else:
            reviews_test.append(json_positivo[i].get("review"))
            label_test.append(json_positivo[i].get("voted_up"))
            reviews_test.append(json_negativo[i].get("review"))
            label_test.append(json_negativo[i].get("voted_up"))
            
        if i==99:
            i=0
        if i==24:
            break
        i+=1
        
    return reviews_treino, label_treino, reviews_test, label_test

#fold 2
def fold2(json_positivo, json_negativo, quant):
    i = 50
    reviews_treino = []
    label_treino = []
    reviews_test = []
    label_test = []
    while(i<quant):
        
        if (i<100 and i>49) or i<25:
            reviews_treino.append(json_positivo[i].get("review"))
            label_treino.append(json_positivo[i].get("voted_up"))
            reviews_treino.append(json_negativo[i].get("review"))
            label_treino.append(json_negativo[i].get("voted_up"))
        else:
            reviews_test.append(json_positivo[i].get("review"))
            label_test.append(json_positivo[i].get("voted_up"))
            reviews_test.append(json_negativo[i].get("review"))
            label_test.append(json_negativo[i].get("voted_up"))
        
        if i==99:
            i=0
        if i==49:
            break
        i+=1

    return reviews_treino, label_treino, reviews_test, label_test

#fold 3
def fold3(json_positivo, json_negativo, quant):
    i = 75
    reviews_treino = []
    label_treino = []
    reviews_test = []
    label_test = []
    while(i<quant):
        
        if (i<99 and i>74) or i<49:
            reviews_treino.append(json_positivo[i].get("review"))
            label_treino.append(json_positivo[i].get("voted_up"))
            reviews_treino.append(json_negativo[i].get("review"))
            label_treino.append(json_negativo[i].get("voted_up"))
        else:
            reviews_test.append(json_positivo[i].get("review"))
            label_test.append(json_positivo[i].get("voted_up"))
            reviews_test.append(json_negativo[i].get("review"))
            label_test.append(json_negativo[i].get("voted_up"))
        
        if i==99:
            i=0
        if i==74:
            break
        i+=1

    return reviews_treino, label_treino, reviews_test, label_test
    