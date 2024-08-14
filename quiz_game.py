print("Welcome to the Quiz game")

count = 0

def question():
    
    print("""
          What is the capital of Nigeria?
          \nA. Abuja
          \nB. Bauchi
          \nC. Calabar
          \nD. Damanturu
          """)
    question_1 = input("Pick option A, B, C or D").lower()
    
    if question_1 == "A".lower():
        global count
        count += 1
    else:
        print(f"You miss the question and your score is {count} you have 4 more to go.\n ")
    print("""
          What is the capital of Oyo State?
          \nA. Iseyin
          \nB. Oyo
          \nC. Ibadan
          \nD. Ogbomosho
          """)
    question_2 = input("Pick option A, B, C or D").lower()
    
    if question_2 == "C".lower():
        
        count += 1
    else:
        print(f"You miss the question and your score is {count} you have 3 more to go.\n ")
    print("""
          What is the longest river in the world?
          \nA. River Missisipi
          \nB. River Nile
          \nC. River Niger
          \nD. River Benue
          """)
    question_3 = input("Pick option A, B, C or D\n").lower()
    
    if question_3 == "A".lower():
        
        count += 1
    else:
        print(f"You miss the question and your score is {count} you have 2 more to go.\n ")
    
    print("""
          What is the name of the President of Nigeria?
          \nA. Mr Goodluck Jonathan
          \nB. Gen Muhamummed Buhari
          \nC. Sen Bola Ahmed Tinubu
          \nD. Gen Olusegun Obasanjo
          """)
    question_4 = input("Pick option A, B, C or D\n").lower()
    
    if question_4 == "C".lower():
        
        count += 1
    else:
        print(f"You miss the question and your score is {count} you have 1 more to go.\n ")
    
    print("""
          What is the name of the President of United States?
          \nA. Donald Trump
          \nB. Joe Biden
          \nC. Barrack Obama
          \nD. Bill Gate
          """)
    question_5 = input("Pick option A, B, C or D\n").lower()
    
    if question_5 == "B".lower():
        
        count += 1
    else:
        print(f"You miss the question and your score is {count} you have 0 more to go.\n ")
    
    
    print(f"You got {count} out of 5 correct!")
    
    return question
    
question()