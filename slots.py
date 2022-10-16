import random;


ysiVoitot = 1;
kymppiVoitot = 1.5;
jatkaVoitot = 5;
akkaVoitot = 10;
kunkkuVoitot = 150;
assaVoitot = 300;

kokonaisVoittosumma = 0

#Syötetään lista jonka ensimmäisestä alkiosta tarkistetaan mikä merkki kyseessä. 
def addWin(column) : 

    global kokonaisVoittosumma
    if(column[0] == 9) : 
        kokonaisVoittosumma = kokonaisVoittosumma + ysiVoitot
    if(column[0] == 10) : 
        kokonaisVoittosumma = kokonaisVoittosumma + kymppiVoitot
    if(column[0] == "J") : 
        kokonaisVoittosumma = kokonaisVoittosumma + jatkaVoitot
    if(column[0] == "Q") : 
        kokonaisVoittosumma = kokonaisVoittosumma + akkaVoitot
    if(column[0] == "K") : 
        kokonaisVoittosumma = kokonaisVoittosumma + kunkkuVoitot
    if(column[0] == "A") : 
        kokonaisVoittosumma = kokonaisVoittosumma + assaVoitot
        print("JACKPOT!") 


for peli in range(100) :
    voittojenKa = 0; 
    peliKerrat = 1000;
    pelikerta = 0;
    voittojenLkm = 0;


    while pelikerta < peliKerrat: 
        voitto = True;

        lista = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9, 
                10,10,10,10,10,10,10,10,10,10,10,10,
                "J","J","J","J","J","J","J","J",
                "Q","Q","Q","Q","Q","Q","Q",
                "K","K","K","K","K", "K",
                "A","A","A"];

        column1 = [];
        column2 = [];
        column3 = [];


        listaPituus = len(lista);
        print(listaPituus)

        for x in range(3):
            randomNum = random.randint(0, len(lista)-1);

            column1.append(lista[randomNum])
            lista.pop(randomNum)

        for x in range(3):
            randomNum = random.randint(0, len(lista)-1);

            column2.append(lista[randomNum])
            lista.pop(randomNum)

        for x in range(3):
            randomNum = random.randint(0, len(lista)-1);

            column3.append(lista[randomNum])
            lista.pop(randomNum)



        while voitto:
            
            #Ylärivi
            if column1[0] == column1[1] and column1[0] == column1[2] :
                voittojenLkm = voittojenLkm + 1
                addWin(column1)
            #Keskimmäinen
            if column2[0] == column2[1] and column2[0] == column2[2] :
                voittojenLkm = voittojenLkm + 1
                addWin(column2);
            #Alarivi
            if column3[0] == column3[1] and column3[0] == column3[2] :
                voittojenLkm = voittojenLkm + 1
                addWin(column3);
            #Ylhäältä alas
            if column1[0] == column2[1] and column1[0] == column3[2]:
                voittojenLkm = voittojenLkm + 1
                addWin(column1)

            #Alhaalta ylös
            if column3[0] == column2[1] and column3[0] == column1[2]:
                voittojenLkm = voittojenLkm + 1
                addWin(column3)

            voitto = False;
        else:
            pelikerta = pelikerta+1

    
    else:
        print("Kiitos pelistä. Voitit", voittojenLkm, "kertaa. Voitit", kokonaisVoittosumma, "euroa");
    
    print("Kokonaispelikerta numero" , peli, "Yhteissumma tällä hetkellä: ", voittojenKa + kokonaisVoittosumma)
    voittojenKa = voittojenKa + kokonaisVoittosumma


print("Kokonaisvoittosummien keskiarvo on: ", (voittojenKa / 100))





        



