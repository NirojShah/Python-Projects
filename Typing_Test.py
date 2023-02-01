
import time
import random 
import threading
import keyboard


Data = ["A random paragraph can also be an excellent way for a writer to tackle writers' block. Writing block can often happen due to being stuck with a current project that the writer is trying to complete. By inserting a completely random paragraph from which to begin, it can take down some of the issues that may have been causing the writers' block in the first place. ","Another productive way to use this tool to begin a daily writing routine. One way is to generate a random paragraph with the intention to try to rewrite it while still keeping the original meaning. The purpose here is to just get the writing started so that when the writer goes onto their day's writing projects, words are already flowing from their fingers.","It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test your programming and that the tool being created is working well.","Above are a few examples of how the random paragraph generator can be beneficial. The best way to see if this random paragraph picker will be useful for your intended purposes is to give it a try. Generate a number of paragraphs to see if they are beneficial to your current project.","Yes. We're always interested in improving this generator and one of the best ways to do that is to add new and interesting paragraphs to the generator. If you'd like to contribute some random paragraphs, please contact us."]


selected_para = random.choice(Data)

def timer():
    counter = 0
    print()
    print()
    print("Your time STARTS now >>>>")
    for i in range(1,61):
        time.sleep(1)
        counter+=1
        
        if counter == 60:
            print()
            print()
            print("Time is over...")
            return keyboard.press_and_release("enter")
        

def user_input(data):
    print()
    print()
    print(data)
    print()
    print()
    user_in = input("Start From Here :- \n")
    print()
    print()
    return [user_in,data]
    

def checker():

    right_word = 0
    wrong_word = 0
    main_inp = user_input(selected_para)
    data_main = main_inp[1]
    data_input = main_inp[0]

    list_convert_main = data_main.split(" ")
    list_convert_inpu = data_input.split(" ")

    for i in range(len(list_convert_inpu)):
        if list_convert_inpu[i] == list_convert_main[i]:
            right_word+=1

        elif list_convert_inpu[i] == list_convert_main[i]:
            wrong_word+=1

    percentage_of_correction = round(right_word/len(list_convert_main)*100)
    print("Wrong Spelled Word Percentage :- ",round(wrong_word/len(list_convert_main)*100)," %")
    print("Accuracy Percentage :- ",percentage_of_correction,"%")

    missed_word = 100-percentage_of_correction
    print("The Missed Percentage :- ",missed_word," %")
    print()
    print("Your Word Per Miniute is(WPM) :- ",len(list_convert_inpu))



if __name__ == "__main__":
    first = threading.Thread(target=timer)
    first.start() 

    second = threading.Thread(target=checker)
    second.start() 
