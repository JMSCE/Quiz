import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)#red
GPIO.setup(17,GPIO.OUT)#green
GPIO.setup(23,GPIO.OUT)#buzzer
GPIO.output(23,GPIO.HIGH)#buzzer off
GPIO.setup(12,GPIO.OUT)#blue
GPIO.setup(16,GPIO.OUT)#yellow
GPIO.setup(26,GPIO.OUT)#white

def correct_answer_sound():
  GPIO.output(17, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(17,GPIO.LOW)

def incorrect_answer_sound():
  GPIO.output(18,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW)
  time.sleep(2)
  GPIO.output(18,GPIO.LOW)
  GPIO.output(23,GPIO.HIGH)

def good_news():
  for x in range (0,3):
    light_display()

def bad_news():
  GPIO.output(18,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW)
  time.sleep(10)
  GPIO.output(18,GPIO.LOW)
  GPIO.output(23,GPIO.HIGH)

def green_light():
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    time.sleep(1)

def red_light():
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)

def blue_light():
    GPIO.output(12,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12,GPIO.LOW)
    time.sleep(1)

def yellow_light():
    GPIO.output(16,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(16,GPIO.LOW)
    time.sleep(1)

def white_light():
    GPIO.output(26,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(26,GPIO.LOW)
    time.sleep(1)

def light_display():
  light_list = [green_light, blue_light, yellow_light, red_light, white_light]
  random.shuffle(light_list)
  for light_function in light_list:
    light_function()

questions = ["""When did the first farmers arrive in Britain?
a. 10,000 years ago b. 8,000 years ago c. 6,000 years ago d. 4,000 years ago""",
"""In what year did Emperor Claudius invade Britain?
a. 55 BC b. 12 BC c. 43 AD d. 65 AD""",
"""In what year did William, Duke of Normandy defeat Harold, the Saxon King?
a. 874 b. 1066 c. 955 d. 1166""",
"""In what year did Robert the Bruce defeat the English at the Battle of Bannockburn?
a. 1066 b. 1314 c. 1254 d. 1308""",
""" In what year did the Black Death begin in Britain?
a. 1302 b. 1484 c. 1508 d. 1348""",
"""When did Henry Tudor defeat Richard III at the Battle of Bosworth?
a. 1455 b. 1584 c. 1485 d. 1493""",
"""When did the English defeat the Spanish Armada?
a. 1384 b. 1473 c. 1512 d. 1588""",
"""When did the English civil war begin?
a. 1612 b. 1642 c. 1701 d. 1707""",
"""In what year did Parliament invite Chales II to come back from exile?
a. 1640 b. 1650 c. 1660 d. 1670""",
"""The first man to be called the Prime Minister was Sir Robert Walpole. When was he in power?
a. 1712 - 1720 b. 1721 - 1742 c. 1725 - 1730 d. 1717 - 1740""",
"""In what year did the 13 American colonies declare independence?
a. 1766 b. 1776 c. 1786 d. 1812""",
"""In what year did the British abolish slavery throughout the Empire?
a. 1807 b. 1822 c. 1828 d. 1833""",
"""When was the Act of Union between Great Britain and Ireland?
a. 1707 b. 1776 c. 1800 d. 1801""",
"""When was the Crimean War?
a. 1844 - 1848 b. 1853 - 1856 c. 1856 - 1858 d. 1860 - 1865""",
"""When did the Great War begin?
a. 1914 b. 1918 c. 1938 d. 1939""",
"""In what year was D-Day?
a. 1942 b. 1943 c. 1944 d. 1945""",
"""When did Margerat Thatcher become Prime Minister?
a. 1980 b. 1981 c. 1979 d. 1982""",
"""In what year did British combat troops leave Iraq?
a. 2003 b. 2007 c. 2009 d. They have not yet left""",
"""Since when has there been a Welsh Assembly and a Scottish Parliament?
a. 1998 b. 1999 c. 1992 d. 2000""",
"""When did the UK join the European Economic Community (EEC)?
a. 1970 b. 1973 c. 1976 d. 1979"""]

answers = ["c", "d", "b", "b", "d", "c", "d", "b", "c", "b", "b", "d", "c", "b", "a", "c", "c", "c", "c", "a", "b"]

total_score = 0
length = str(len(questions))
length_int = int(len(questions))

name = input("Please enter your name")
print("Hello " + name + ". Welcome to the British Questions quiz. There are " + length + " questions in this quiz. You need 75% to pass. Please hit enter to begin.")
input()
print(questions [0])
answer = input ("Is it a, b, c or d?")
if answer == answers[0]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[0]))
  incorrect_answer_sound()
print("\n")
print(questions [1])
answer = input ("Is it a, b, c or d?")
if answer == answers[1]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[1]))
  incorrect_answer_sound()
print("\n")
print(questions [2])
answer = input ("Is it a, b, c or d?")
if answer == answers[2]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[2]))
  incorrect_answer_sound()
print("\n")
print(questions [3])
answer = input ("Is it a, b, c or d?")
if answer == answers[3]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[3]))
  incorrect_answer_sound()
print("\n")
print(questions [4])
answer = input ("Is it a, b, c or d?")
if answer == answers[4]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[4]))
  incorrect_answer_sound()
print("\n")
print(questions [5])
answer = input ("Is it a, b, c or d?")
if answer == answers[5]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[5]))
  incorrect_answer_sound()
print("\n")
print(questions [6])
answer = input ("Is it a, b, c or d?")
if answer == answers[6]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[6]))
  incorrect_answer_sound()
print("\n")
print(questions [7])
answer = input ("Is it a, b, c or d?")
if answer == answers[7]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[7]))
  incorrect_answer_sound()
print("\n")
print(questions [8])
answer = input ("Is it a, b, c or d?")
if answer == answers[8]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[8]))
  incorrect_answer_sound()
print("\n")
print(questions [9])
answer = input ("Is it a, b, c or d?")
if answer == answers[9]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[9]))
  incorrect_answer_sound()
print("\n")
print(questions [10])
answer = input ("Is it a, b, c or d?")
if answer == answers[10]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[10]))
  incorrect_answer_sound()
print("\n")
print(questions [11])
answer = input ("Is it a, b, c or d?")
if answer == answers[11]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[11]))
  incorrect_answer_sound()
print("\n")
print(questions [12])
answer = input ("Is it a, b, c or d?")
if answer == answers[12]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[12]))
  incorrect_answer_sound()
print("\n")
print(questions [13])
answer = input ("Is it a, b, c or d?")
if answer == answers[13]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[13]))
  incorrect_answer_sound()
print("\n")
print(questions [14])
answer = input ("Is it a, b, c or d?")
if answer == answers[14]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[14]))
  incorrect_answer_sound()
print("\n")
print(questions [15])
answer = input ("Is it a, b, c or d?")
if answer == answers[15]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[15]))
  incorrect_answer_sound()
print("\n")
print(questions [16])
answer = input ("Is it a, b, c or d?")
if answer == answers[16]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[16]))
  incorrect_answer_sound()
print("\n")
print(questions [17])
answer = input ("Is it a, b, c or d?")
if answer == answers[17]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[17]))
  incorrect_answer_sound()
print("\n")
print(questions [18])
answer = input ("Is it a, b, c or d?")
if answer == answers[18]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[18]))
  incorrect_answer_sound()
print("\n")
print(questions [19])
answer = input ("Is it a, b, c or d?")
if answer == answers[19]:
    print("Congratulations. You are correct.")
    total_score = total_score + 1
    correct_answer_sound()
else:
  print("Incorrect.The correct answer is " + (answers[19]))
  incorrect_answer_sound()
print("\n")
input("For your final score, hit enter.")
print("\n")
final_score = int(total_score/length_int*100)
print("You scored " + str(final_score) + "%")
if final_score >= 75 :
  print("Well done " + name + ". With this score you would pass the British Citizenship test.")
  good_news()
else:
  print("Hmmm. You need to do better " + name + ". With this score, you would fail the British Citizenship test.")
  bad_news()
