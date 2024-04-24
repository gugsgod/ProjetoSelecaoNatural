class TextFormat:
    def FormatText(listaSep, respostaDesejada, tamanhoLista):
        quantidadeChar = len(respostaDesejada)
        if quantidadeChar <= 40:
            listaSep.append(respostaDesejada)
            tamanhoLista = 1
            
        if 40 < quantidadeChar <= 60:
            for i in range(int(quantidadeChar/2)+5):
                i = int(quantidadeChar/2)+5-i
                if respostaDesejada[i] == " ":
                    listaSep.append(respostaDesejada[0:i])
                    listaSep.append(respostaDesejada[i+1:quantidadeChar])
                    tamanhoLista = 2
                    break
                    
        if 60 < quantidadeChar<= 80:
            for i in range (40):
                i = 43-i
                if respostaDesejada[i] == " ":
                    listaSep.append(respostaDesejada[0:i])
                    listaSep.append(respostaDesejada[i+1:quantidadeChar])
                    tamanhoLista = 2
                    
                    break
                
        if 80 < quantidadeChar <= 100:
            for i in range(int(quantidadeChar/3)+5):
                i =  35 - i
                if respostaDesejada[i] == " ":
                    listaSep.append(respostaDesejada[0:i])
                    for j in range(int(quantidadeChar/3)):
                        j = 62 - j
                        if respostaDesejada[j] == " ":
                            listaSep.append(respostaDesejada[i+1:j])
                            listaSep.append(respostaDesejada[j+1:quantidadeChar])
                            tamanhoLista = 3
                            break
                            
        if 100 < quantidadeChar <= 120:
            for i in range(int(quantidadeChar/3)+5):
                i =  44 - i
                if respostaDesejada[i] == " ":
                    listaSep.append(respostaDesejada[0:i])
                    for j in range(int(quantidadeChar/3)):
                        j = 82 - j
                        if respostaDesejada[j] == " ":
                            listaSep.append(respostaDesejada[i+1:j])
                            listaSep.append(respostaDesejada[j+1:quantidadeChar])
                            tamanhoLista = 3
                            break
                    
        if 120 < quantidadeChar <= 140:
            for i in range(int(quantidadeChar/3)+5):
                i = 40 - i
                if respostaDesejada[i] == " ":
                    listaSep.append(respostaDesejada[0:i])
                    for j in range(int(quantidadeChar/3)):
                        j = 80 - j
                        if respostaDesejada[j] == " ":
                            listaSep.append(respostaDesejada[i+1:j])
                            for g in range(int(quantidadeChar/3)):
                                g = 120 - g
                                if respostaDesejada[g] == " ":
                                    listaSep.append(respostaDesejada[j+1:g])
                                    listaSep.append(respostaDesejada[g+1:quantidadeChar])
                                    tamanhoLista = 4
                                    break
                                    
        if 140 < quantidadeChar <= 160:
            for i in range(int(quantidadeChar/3)+5):
                i = 40 - i
                if respostaDesejada[i] == " ":
                    listaSep.append(respostaDesejada[0:i])
                    for j in range(int(quantidadeChar/3)):
                        j = 80 - j
                        if respostaDesejada[j] == " ":
                            listaSep.append(respostaDesejada[i+1:j])
                            for g in range(int(quantidadeChar/3)):
                                g = 120 - g
                                if respostaDesejada[g] == " ":
                                    listaSep.append(respostaDesejada[j+1:g])
                                    listaSep.append(respostaDesejada[g+1:quantidadeChar])
                                    tamanhoLista = 4
                                    break
    
        return tamanhoLista
    
    def posicaoNoBotao(self, tamanho, lista, superficie):
        if tamanho == 1:
            pass
        if tamanho == 2:
            pass
        if tamanho == 3:
            pass
        if tamanho == 4:
            pass
        
    