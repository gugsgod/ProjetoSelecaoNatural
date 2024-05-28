class TextFormat:
    
    def format_text(wished_str):
        run = True
        list_sep = []
        amount_char = len(wished_str)
        if amount_char <= 40:
            list_sep.append(wished_str)

        if 40 < amount_char <= 60:
            for i in range(int(amount_char/2)+5):
                i = int(amount_char/2)+5-i
                if wished_str[i] == " ":
                    list_sep.append(wished_str[0:i])
                    list_sep.append(wished_str[i+1:amount_char])
                    break
                    
        elif 60 < amount_char<= 80:
            for i in range (40):
                i = 43-i
                if wished_str[i] == " ":
                    list_sep.append(wished_str[0:i])
                    list_sep.append(wished_str[i+1:amount_char])                    
                    break
                
        elif 80 < amount_char <= 100:
            list_1 = []
            for i in range(int(amount_char/3)+5):
                i =  35 - i
                if wished_str[i] == " ":
                    list_1.append(wished_str[0:i])
                    list_1.append(wished_str[i+1:amount_char])
                    break
            for j in range(int(amount_char/3)):
                j = 62 - j
                if wished_str[j] == " ":
                    list_sep.append(list_1[0])
                    list_sep.append(wished_str[i+1:j])
                    list_sep.append(wished_str[j+1:amount_char])
                    break
                            
        elif 100 < amount_char <= 120:
            list_1 = []
            for i in range(int(amount_char/3)+5):
                i =  44 - i
                if wished_str[i] == " ":
                    list_1.append(wished_str[0:i])
                    list_1.append(wished_str[i+1:amount_char])
                    break
            for j in range(int(amount_char/3)):
                j = 82 - j
                if wished_str[j] == " ":
                    list_sep.append(list_1[0])
                    list_sep.append(wished_str[i+1:j])
                    list_sep.append(wished_str[j+1:amount_char])
                    break
                    
        elif 120 < amount_char <= 140:
            list_1 = []
            list_2 = []
            
            for i in range(int(amount_char/3)+5):
                i = 44 - i
                if wished_str[i] == " ":
                    list_1.append(wished_str[0:i])
                    break
            
            for j in range(int(amount_char/3)):
                j = 82 - j
                if wished_str[j] == " ":
                    list_2.append(list_1[0])
                    list_2.append(wished_str[i+1:j])
                    break
            
            for g in range(int(amount_char/3)):
                g = 120 - g
                if wished_str[g] == " ":
                    list_sep.append(list_2[0])
                    list_sep.append(list_2[1])
                    list_sep.append(wished_str[j+1:g])
                    list_sep.append(wished_str[g+1:amount_char])
                    break
                
                                                        
        elif 140 < amount_char <= 160:
            list_1 = []
            list_2 = []
            
            for i in range(int(amount_char/3)+5):
                i = 44 - i
                if wished_str[i] == " ":
                    list_1.append(wished_str[0:i])
                    break
            
            for j in range(int(amount_char/3)):
                j = 82 - j
                if wished_str[j] == " ":
                    list_2.append(list_1[0])
                    list_2.append(wished_str[i+1:j])
                    break
            
            for g in range(int(amount_char/3)):
                g = 120 - g
                if wished_str[g] == " ":
                    list_sep.append(list_2[0])
                    list_sep.append(list_2[1])
                    list_sep.append(wished_str[j+1:g])
                    list_sep.append(wished_str[g+1:amount_char])
                    break
        return list_sep
        
    def format_question (question):
        separete_list = []
        qtdChar = len(question)
        if qtdChar <= 60:
            question = question
    
        if 60 < qtdChar <=90:
            for i in range(int(qtdChar/2)+5):
                i = int(qtdChar/2)+5-i
                if question[i] == " ":
                    separete_list.append(question[0:i])
                    separete_list.append(question[i+1:qtdChar])
                    break

        if 90 < qtdChar <= 120:
            for i in range(int(qtdChar/2)):
                i = 61-i
                if question[i] == " ":
                    separete_list.append(question[0:i])
                    separete_list.append(question[i+1:qtdChar])
                    break
            
        return separete_list