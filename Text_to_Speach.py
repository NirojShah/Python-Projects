import gtts

# my_text = taking input of the text which you want to convert to speach. 

my_text = input("Enter the text here :- ")

# language = en = selecting language is english
language = "en"

# conversion = giving the predefined function of gtts.
conversion = gtts.gTTS(text=my_text, lang=language, slow=False)

# loction = Enter the where you want to save the file by coping the location.
location = input("Enter the save file destination :- ")
# file_name = enter the file name 
file_name = input("Enter the name of the File :- ")
# Adding the extention of mp3
file_name=file_name+".mp3"

location = location.split("\\")

main_Location = "\\\\".join(location)

try:
    conversion.save(main_Location+"\\\\"+file_name)
except Exception as error:
    print("This task is not successfull due to ---> "+error)

print("The task has been completed...")


