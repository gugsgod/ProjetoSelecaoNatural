CREATE DATABASE IF NOT EXISTS gamedb;

USE gamedb;

CREATE TABLE IF NOT EXISTS users(
	id_user INT,
    user VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_user)
    );

CREATE TABLE IF NOT EXISTS points(
	id_user INT,
    score INT,
    lap INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
); 

CREATE TABLE IF NOT EXISTS questions(
	id_question INT,
    question VARCHAR(120),
    alt_a VARCHAR(160),
    alt_b VARCHAR(160),
	alt_c VARCHAR(160),
	alt_d VARCHAR(160) 
);

INSERT INTO questions(id_question, question, alt_a, alt_b, alt_c, alt_d)
VALUES 
    (1, "Porque os tentilhões possuem diferentes formas de bico aqui nas ilhas de Galápagos?", 
    "Sob pressões seletivas diferentes, as condições ambientais nas ilhas levaram à seleção de diferentes características nos tentilhões.",
     "Os tentilhões fizeram cirurgias plásticas em seus bicos para se adaptarem.", 
     "Os tentilhões começaram a frequentar restaurantes diferentes na ilha, resultando em uma variedade de bicos.",
      "Para evitar brigas por comida, os tentilhões desenvolveram bicos especializados em tipos diferentes de alimento."),
    (2, "Por que alguns insetos parecem folhas ou ramos de plantas? E como isso os ajuda a escapar dos seus predadores?", 
    "Essa semelhança é resultado de mutações aleatórias que foram selecionadas ao longo do tempo devido à pressão seletiva dos predadores.", 
    "Os insetos desenvolveram essa semelhança para atrair mais facilmente suas presas.", 
    "Os insetos adotam essa camuflagem para se protegerem das mudanças climáticas.", 
    "A semelhança com folhas e ramos permite que os insetos se comuniquem de forma eficiente entre si."),
    (3, "Por que nesta região há um aumento das mariposas negras em comparação às brancas, que predominavam na região antes?", 
    "As mariposas brancas se tornaram presas fáceis nas árvores escuras, favorecendo a sobrevivência das mariposas negras.", 
    "As mariposas brancas aprenderam a se camuflar melhor.", 
    "A mudança na cor dos caules influenciou na coloração das mariposas.", 
    "As mariposas brancas mudaram de cor para se adaptar ao novo ambiente."),
    (4, "De que maneira o ambiente influencia na forma e organização dos animais?", 
    "Os animais se adaptam às mudanças ambientais ao longo do tempo.", 
    "A adaptação dos animais ao ambiente é um processo irrelevante.", 
    "As características dos animais são imutáveis, independentemente do ambiente.", 
    "Os animais são resistentes a qualquer alteração ambiental."),
    (5, "Qual dos seguintes exemplos melhor ilustra a seleção natural?", 
    "O aumento da resistência de uma população de bactérias a um antibiótico devido à mutação genética.", 
    "A mudança de cor da pele de um camaleão para se camuflar em diferentes ambientes.", 
    "A capacidade de um pássaro imitar sons para atrair parceiros.", 
    "O desenvolvimento de uma flor com aroma atraente para atrair polinizadores."),
    (6, "Assinale a alternativa que NÃO contém um mecanismo de evolução biológica segundo a teoria do neodarwinismo.", 
    "Mimetismo", 
    "Mutação", 
    "Deriva genética", 
    "Seleção natural"),
    (7, "Dois roedores divididos por um rio, os do norte ficam brancos e os do sul ficam castanhos, por que isso ocorre?", 
    "Estimula a sobrevivência de diferentes características fenotípicas, como a cor do pelo, adaptadas aos ambientes distintos ao norte e ao sul do rio.", 
    "Houve mutações específicas para os ambientes ao norte e ao sul do rio.", 
    "Promove a competição entre roedores brancos e castanhos.", 
    "Aumenta a probabilidade de sobrevivência apenas dos roedores brancos."),
    (8, "Quais são as características representativas dos anfíbios em relação à sua dependência da pele para atividades vitais?", 
    "seleção de adaptações em função do meio ambiente em que vivem.", 
    "lei do uso e desuso.", 
    "atrofia do pulmão devido ao uso contínuo da pele.", 
    "transmissão de caracteres adquiridos aos descendentes."),
    (9, "Quais características definem a maior adaptação entre indivíduos da mesma espécie?", 
    "Vivem mais e reproduzem mais", 
    "Comem mais e apresentam cores mais vibrantes", 
    "Apresentam mais membros como pernas e patas", 
    "São mais fortes"),
    (10, "Quais são as possíveis consequências da diminuição da variação genética nos guepardos devido à caça, seca e doenças?", 
    "Maior vulnerabilidade a doenças e condições ambientais adversas.", 
    "Aumento da adaptabilidade às mudanças ambientais.", 
    "Redução do risco de extinção em situações de crise ambiental.", 
    "Aumento da variabilidade fenotípica nas populações."),
    (11, "Por que o uso repetido de um único antibiótico contra as mesmas bactérias causa ineficácia no tratamento?", 
    "o antibiótico seleciona, na população bacteriana, as bactérias que já eram resistentes a ele.", 
    "o antibiótico induz modificações no metabolismo das bactérias.", 
    "as bactérias se adaptarem individualmente ao antibiótico.", 
    "o antibiótico induz diretamente nas bactérias uma resistência."),
    (12, "Por qual motivo as teorias darwinistas e neodarwinistas sugerem o surgimento da superbactéria KPC?", 
    "variações no material genético.", 
    "aumento da especiação.", 
    "crescimento populacional.", 
    "ampliação da irradiação adaptativa."),
    (13, "Como a adaptação pode levar a organismos não relacionados a desenvolver estruturas corporais semelhantes?", 
    "Seleção artificial.", 
    "Convergência evolutiva.", 
    "Divergência evolutiva.", 
    "Lei do uso e desuso."),
    (14, "Por que há predominância de girafas com pescoços maiores em ambientes escassos de alimentos e com comida em áreas altas?", 
    "De acordo com Darwin, a girafa com pescoço menor teria uma desvantagem competitiva e estaria em risco de ser eliminada pela seleção natural.", 
    "De acordo com Darwin, a girafa com pescoço menor teria uma vantagem competitiva e seria mais propensa a sobreviver", 
    "De acordo com Darwin, a girafa com pescoço menor teria a mesma probabilidade de sobreviver que a girafa com pescoço mais longo.", 
    "De acordo com Darwin, o tamanho do pescoço da girafa não teria nenhuma influência sobre sua sobrevivência e reprodução."),
    (15, "Qual declaração melhor destaca a importância da camuflagem na adaptação das espécies, considerando a seleção natural?", 
    "A camuflagem pode aumentar as chances de sobrevivência, permitindo que os organismos se ocultem no ambiente.", 
    "A camuflagem é uma estratégia que se limita a ambientes específicos, como florestas tropicais densas.", 
    "A camuflagem não é influenciada pela seleção natural, sendo uma característica aleatória.", 
    "A camuflagem geralmente resulta em comportamentos mais agressivos nos indivíduos."),
    (16, "De acordo com a teoria de Darwin, como esses anfíbios sobreviveram em ambientes tão hostis?", 
    "Modificou-se para se ajustar ao meio inóspito, tornando as gerações seguintes mais resistentes ao calor e aumentando a chance de sobrevivência das espécies.", 
    "Ele passou a produzir enzimas devido ao ambiente e essa característica foi transmitida aos descendentes.", 
    "Gerações recentes apresentam características cada vez melhores em relação aos antepassados devido à seleção do ambiente.", 
    "Nasceu com a capacidade de sobreviver nesse ambiente, selecionada e transmitida de geração em geração."),
    (17, "Qual das seguintes afirmações é verdadeira sobre a seleção natural?", 
    "Pode operar em diferentes níveis, desde o nível molecular até o nível das populações e espécies.", 
    "É o único mecanismo de evolução que causa mudanças na frequência alélica de uma população.", 
    "Sempre resulta na adaptação perfeita de um organismo ao seu ambiente.", 
    "É um processo que ocorre apenas em ambientes estáveis e não em ambientes em constante mudança."),
    (18, "Como as mudanças repentinas no ambiente podem explicar a origem de novas espécies, conforme a evolução?", 
    "As barreiras geográficas podem promover mecanismos de isolamento reprodutivo.", 
    "Quando as barreiras geográficas são pequenas e as áreas de sobrevivência são grandes, essas áreas recebem o nome de refúgio.", 
    "Quando o isolamento geográfico impede o cruzamento entre os indivíduos de duas populações, as espécies não são consideradas distintas.", 
    "Barreiras ecológicas não promovem especiação."),
    (19, "Que tipo de seleção é observada nos tentilhões africanos devido à redução de indivíduos com bicos de tamanho médio?", 
    "Disruptiva.", 
    "Direcional.", 
    "Destrutiva.", 
    "Estabilizadora.")
;
