class TextFormat:
    def FormatText(stringDesejada):
        run = True
        list_sep = []
        quantidadeChar = len(stringDesejada)
        if quantidadeChar <= 40:
            list_sep.append(stringDesejada)

        if 40 < quantidadeChar <= 60:
            for i in range(int(quantidadeChar/2)+5):
                i = int(quantidadeChar/2)+5-i
                if stringDesejada[i] == " ":
                    list_sep.append(stringDesejada[0:i])
                    list_sep.append(stringDesejada[i+1:quantidadeChar])
                    break
                    
        elif 60 < quantidadeChar<= 80:
            for i in range (40):
                i = 43-i
                if stringDesejada[i] == " ":
                    list_sep.append(stringDesejada[0:i])
                    list_sep.append(stringDesejada[i+1:quantidadeChar])                    
                    break
                
        elif 80 < quantidadeChar <= 100:
            list_1 = []
            for i in range(int(quantidadeChar/3)+5):
                i =  35 - i
                if stringDesejada[i] == " ":
                    list_1.append(stringDesejada[0:i])
                    list_1.append(stringDesejada[i+1:quantidadeChar])
                    break
            for j in range(int(quantidadeChar/3)):
                j = 62 - j
                if stringDesejada[j] == " ":
                    list_sep.append(list_1[0])
                    list_sep.append(stringDesejada[i+1:j])
                    list_sep.append(stringDesejada[j+1:quantidadeChar])
                    break
                            
        elif 100 < quantidadeChar <= 120:
            list_1 = []
            for i in range(int(quantidadeChar/3)+5):
                i =  44 - i
                if stringDesejada[i] == " ":
                    list_1.append(stringDesejada[0:i])
                    list_1.append(stringDesejada[i+1:quantidadeChar])
                    break
            for j in range(int(quantidadeChar/3)):
                j = 82 - j
                if stringDesejada[j] == " ":
                    list_sep.append(list_1[0])
                    list_sep.append(stringDesejada[i+1:j])
                    list_sep.append(stringDesejada[j+1:quantidadeChar])
                    break
                    
        elif 120 < quantidadeChar <= 140:
            list_1 = []
            list_2 = []
            
            for i in range(int(quantidadeChar/3)+5):
                i = 44 - i
                if stringDesejada[i] == " ":
                    list_1.append(stringDesejada[0:i])
                    break
            
            for j in range(int(quantidadeChar/3)):
                j = 82 - j
                if stringDesejada[j] == " ":
                    list_2.append(list_1[0])
                    list_2.append(stringDesejada[i+1:j])
                    break
            
            for g in range(int(quantidadeChar/3)):
                g = 120 - g
                if stringDesejada[g] == " ":
                    list_sep.append(list_2[0])
                    list_sep.append(list_2[1])
                    list_sep.append(stringDesejada[j+1:g])
                    list_sep.append(stringDesejada[g+1:quantidadeChar])
                    break
                
                                                        
        elif 140 < quantidadeChar <= 160:
            list_1 = []
            list_2 = []
            
            for i in range(int(quantidadeChar/3)+5):
                i = 44 - i
                if stringDesejada[i] == " ":
                    list_1.append(stringDesejada[0:i])
                    break
            
            for j in range(int(quantidadeChar/3)):
                j = 82 - j
                if stringDesejada[j] == " ":
                    list_2.append(list_1[0])
                    list_2.append(stringDesejada[i+1:j])
                    break
            
            for g in range(int(quantidadeChar/3)):
                g = 120 - g
                if stringDesejada[g] == " ":
                    list_sep.append(list_2[0])
                    list_sep.append(list_2[1])
                    list_sep.append(stringDesejada[j+1:g])
                    list_sep.append(stringDesejada[g+1:quantidadeChar])
                    break
        
        return list_sep
    