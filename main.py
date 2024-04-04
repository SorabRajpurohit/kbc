questions = [
    ["Who is the prime minister of India?", "Manmohan Singh", "Arun Jetli", "LK Adwani", "Narendra Modi", 4],
    ["What is the  common name of NaCl?", "Salt", "Water", "Detergent", "Soda", 1],
    ["What is the capital of Cuba?", "Hevana", "Toranto", "Kabul", "Thimfu", 1],
    ["Who is president of Russia?", "Vladmir Putin", "Dimitri Vegas", "Rukhnich Sonkilov", "Youri Boyka", 1],
    ["Who won Grammy for year 2023 for best singer?", "Justin Biber", "Tylor Swift", "Adele", "The Weeknd", 2],
    ["In which continent Amazon forest is situated?", "Asia", "Africa", "S.Americla", "Autralia", 3],
    ["Which Country has biggest Diffence budget for 2023?", "USA", "India", "Pakista", "Russia",1],
    ["What type of script blind people use for reading a book?", "bile", "English", "Devnagari", "Brile",3],
    ["Who is the founder of Spacex?", "Ryan Parag", "Sundar Pichai", "Elon Musk", "Mahila Shinde",3],
    ["Which one of this car company is from Japan?" "Wolkswegon", "Lamborghini", "Ford", "Toyota", 4],
    ["Australian Captain Pet cummins plays from which team in ipl 2024?", "SRH", "CSK", "RR", "KKR",1 ],
    ["How many time India have won ICC mens odi wc?", 2, 1, 3, 0, 1],
    ["Gengeis Khan is from which country?", "China", "Kazkhastan", "Nepal", "Mangolia", 4],
    ["which enthenisity  do israel follow ?" "jewish", "christian", "islam", "Norwegin", 1],
    ["What Kind of snake gives with his tail before attaking?" "cobra", "python", "blackmamba", "rattle", 4]

    
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

for i in range(0,len(questions)):
    question = questions[i]
    money = 0
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(question[0])
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    reply = int(input("Enter your answer(1-4): "))
    print("Lock kar diya Jaye? (y/n)")
    A = input("y/n : ")
    if (A == "n"):
        break
    if (A == "y"):
        
        if reply == question[-1]:
            print(f"correct answer!!! You have won Rs. {levels[i]}")
            if(i==4):
                money = 10000
            elif(i==9):
                money = 320000
            elif(i==14):
                money = 10000000
        else:
            print("Wrong Answer!!")
            break
print(f"your take home money is {money}")