import pyttsx3
user = pyttsx3.init()
""" RATE"""
rate = user.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
user.setProperty('rate', 170)     # setting up new voice rate
"""VOLUME"""
volume = user.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
user.setProperty('volume',2.0)    # setting up volume level  between 0 and 1

def fun(txt):
   print("speaking......")
   print("")
   user.say(txt)
   user.runAndWait()

txt="hey friend iam your talking friend"
fun(txt)


while txt != "bye":
    txt = input("EM matladali :")
    txt= txt.lower()
    fun(txt)

