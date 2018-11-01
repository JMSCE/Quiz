import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

def correct_answer_sound():
  GPIO.output(17, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(17,GPIO.LOW)

def good_news():
  for x in range (0,3):
    GPIO.output(17, GPIO.HIGH)
     time.sleep(0.5)
     GPIO.output(17,GPIO.LOW)
     time.sleep(0.5)

def bad_news():
  GPIO.output(18,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW)
  time.sleep(6)
  GPIO.output(18,GPIO.LOW)
  GPIO.output(23,GPIO.HIGH)

total_score = 0
name = input("Please enter your name")
print("Hello " + name + ". Welcome to the British Questions quiz. Please hit enter to begin.")
input()
#question 1
print("\n")
print("Who was the Prime Minister during the Falklands War?")
print("a. James Callaghan")
print("b. Margaret Thatcher")
print("c. Harold Wilson")
print("d. Edward Heath")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is Margaret Thatcher.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 2
print("\n")
print("Who was the British Prime Minister from 1945 - 1951?")
print("a. Clement Attlee")
print("b. William Beveridge")
print("c. Winston Churchill")
print("d. Neville Chamberlain")
answer = input ("Is it a, b, c or d?")
if answer == "a":
  print ("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print ("Incorrect. The correct answer is Clement Attlee. Thicko!")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 3
print("\n")
print("When was the Act of Union between England and Scotland?")
print("a. 1728")
print("b. 1707")
print("c. 1800")
print("d. 1812")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print ("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print ("Incorrect. The Act of Union between England and Scotland was in 1707. Don't get this confused with the Act of Union in 1800, which joined Scotland, England and Ireland.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 4
print("\n")
print("When did women get the right to vote on the same terms as men?")
print("a. 1906")
print("b. 1912")
print("c. 1918")
print("d. 1928")
answer = input ("Is it a, b, c or d?")
if answer == "d":
  print ("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print ("Incorrect. The correct answer is 1928. Women first got the right to vote in 1918 but it wasn't until 1928 that it was on the same terms as men (over 21)")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 5
print("\n")
print("When was Margaret Thatcher the British Prime Minister?")
print("a. 1980 - 1991")
print("b. 1979 - 1990")
print("c. 1973 - 1987")
print("d. 1978 - 1993")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is 1979 - 1990.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 6
print("\n")
print("What was the significance of D-Day during WWII?")
print("a. The allied invasion of Normandy to liberate France.")
print("b. When British fishermen had to rescue soldiers from Dunkirk.")
print("c. When the Soviet Union reached Berlin.")
print("d. The planned date for the dropping of first US atomic bomb against Japan.")
answer = input ("Is it a, b, c or d?")
if answer == "a":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print ("Incorrect. D-Day was the day when allied forces invaded Normandy in their successful attempt to liberate France from German occupation.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 7
print("\n")
print("What is the UK's second largest city?")
print("a. Manchester")
print("b. Liverpool.")
print("c. Birmingham.")
print("d. Glasgow.")
answer = input ("Is it a, b, c or d?")
if answer == "c":
  print ("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. Birmingham is the UK's second largest city.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 8
print("\n")
print("Which Cabinet position is described as the first among equals?")
print("a. Chancellor of the Exchequer")
print("b. Prime Minister.")
print("c. Foreign Secretary.")
print("d. Shadow Chancellor of the Exchequer.")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print ("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print ("Incorrect. The correct answer is the Prime Minister.") 
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 9
print("\n")
print("Which are considered the Great Offices of State?")
print("a. Prime Minister and Chancellor of Exchequer.")
print("b. Prime Minister, Chancellor of Exchequer and Lord Chancellor.")
print("c. Prime Minister, Chancellor of Exchequer and Foreign Secretary.")
print ("d. Prime Minister, Chancellor of Exchequer, Foreign Secretary and Home Secretary.")
answer = input ("Is it a, b, c or d?")
if answer == "d":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print ("Incorrect. The correct answer is the Prime Minister, Chancellor of Exchequer, Foreign Secretary and Home Secretary.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 10
print("\n")
print("True or false, Elizabeth I was the first Queen of England?")
print("a.True.")
print("b.False.")
answer = input ("Is it a or b?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print ("Incorrect. The first Queen of England was Mary I.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 11
print("\n")
print("True or false, it was a Briton who invented sonar?")
print("a.True.")
print("b.False.")
answer = input ("Is it a or b?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. Sonar was invented by American naval architect Lewis Nixon. You might have been thinking of radar, which was invented by the Briton, Sir Robert  Watson-Watt.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 12
print("\n")
print("When was the Scottish Parliament formed?")
print("a. 1881.")
print("b. 1987")
print("c. 1992")
print("d. 1999.")
answer = input ("Is it a, b, c or d?")
if answer == "d":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is 1999.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 13
print("\n")
print("Which one of the following is not a Commonwealth country?")
print("a. Senegal")
print("b. Canada")
print("c. Australia")
print("d. South Africa")
answer = input ("Is it a, b, c or d?")
if answer == "a":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. Senegal is not a member of the Commonwealth.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 14
print("\n")
print("What is the maximum claim that can be made using the small claims court in England and Wales?")
print("a. £5,000")
print("b. £10,000")
print("c. £15,0000")
print("d. £3,000")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The small claims court is for claims up to £10,000.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 15
print("\n")
print("In what part of the country can you see the Eden Project?")
print("a. Lake District.")
print("b. Cornwall")
print("c. Black Country")
print("d. Yorkshire")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The Eden Project is located in Cornwall.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 16
print("\n")
print("Under whose reign was the Bible first translated into English?")
print("a. Henry VII")
print("b. Henry VIII")
print("c. Elizabeth I")
print("d. James I")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is Henry VIII.")
  incorrect_answer_sound())
input("For the next question, hit enter.")
input("For the next question, hit enter.")
#question 17
print("\n")
print("In what country is the football team 'Celtic F.C.' based?")
print("a. England") 
print("b. Scotland")
print("c. Northern Ireland")
print("d. Wales")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is Scotland.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 18
print("\n")
print("What sport was Lord Coe best known for?")
print("a. Boxing") 
print("b. Tennis")
print("c. Running")
print("d. Cricket")
answer = input ("Is it a, b, c or d?")
if answer == "c":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is running.")
  incorrect_answer_sound())
input("For the next question, hit enter.")
#question 19
print("\n")
print("Who is the Patron Saint of Wales?")
print("a. Andrew") 
print("b. David")
print("c. Jacob")
print("d. John")
answer = input ("Is it a, b, c or d?")
if answer == "d":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is David.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#question 20
print("\n")
print("When was the last time that England won the Fifa World Cup?")
print("a. 1962") 
print("b. 1966")
print("c. 1974")
print("d. 1970")
answer = input ("Is it a, b, c or d?")
if answer == "b":
  print("Congratulations. You are correct.")
  total_score = total_score + 1
  correct_answer_sound()
else:
  print("Incorrect. The correct answer is 1966.")
  incorrect_answer_sound()
input("For the next question, hit enter.")
#########################
print("\n")
final_score = int(total_score/20*100)
print("You scored " + str(final_score) + "%")
if final_score >= 75 :
  print("Well done " + name + ". With this score you would pass the British Citizenship test.")
  good_news()
else:
  print("Hmmm. You need to do better " + name + ". With this score, you would fail the British Citizenship test.")
  bad_news()
