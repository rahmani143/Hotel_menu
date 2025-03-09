import math
import pyttsx3       

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',170)
          

print("Welcome to RAHMANI'S Cafe")

pyttsx3.speak("Welcome to RAHMANI'S Cafe")

pyttsx3.speak("may i have your name ,please")

name = input("May i have your name ,please:")

pyttsx3.speak("Thank you for joining us today"+name)

menu2 = print("Dosa                :  10 SR\n"
                      "Coffee              :  02 SR\n"
                      "Bread               :  05 SR\n"
                      "Burger              :  05 SR\n"
                      "Cheese bread   :  05 SR\n"
                      "Cup cake          :  02SR\n"
                      "Pizza                 :  10 SR\n"
                      "Taco                 :  05 SR\n"
                      "Hot chocolate   :  05 SR\n"
                      "Broasted          :  18 SR\n"
                      "Madhbi             :   20 SR\n"
                      "Sprite                :  02.50 SR\n"
                      "Pepsi                :  02.50 SR\n"
                      "Mirinda            :  02.50 SR\n")


pyttsx3.speak("type how many orders u want to make from the menu")

num = int(input("enter the number of orders u want to make :"))

total = 0

pyttsx3.speak("enter the dish or beverage name from the menu without spaces in beginning or end")
pyttsx3.speak("then mention the quantity u want of the dish or beverage")

menu1={("dosa"):10,("coffee"):2,("bread"):5,("burger"):15,("cheese bread"):5,("cup cake"):2,
      ("pizza"):10,("taco"):5,("hot chocolate"):5,("broasted"):18,("madhbi"):20,("sprite"):2.50,
      ("pepsi"):2.50,("mirinda"):2.50}

wish = {}
for i in range (num) :
        dish = input ("enter the dish/beverage :")
        quantity = int (input("how many would u like to have:"))
        cost = menu1[dish] * quantity
        wish[dish] = [quantity,cost]
        total += cost

pyttsx3.speak("We will get you that right away "+name)

print("We will get you that right away ",name)

print("\nYour total will be=" + str(total) + "Saudi Riyal")

pyttsx3.speak("\nYour total will be=" + str(total) + "SR")

pyttsx3.speak("\nWe are happy to serve you " + name)

print("\nWe are happy to serve you " + name)

pyttsx3.speak("how would you like to pay Cash or Card")

print("how would you like to pay,Cash or card")



payment = input()

tax = total * 0.15

total_tax = str(tax + total)

if payment == "cash":
    print ("here is ur receipt:\n")
    print("dishes\t\tquantity\t\tsub_cost")
    for k in  wish:
               print(k,'\t\t ',wish[k][0],"\t\t",wish[k][1],"SR")

if payment == "card" :
    print ("successful transaction\n Here is your receipt :\n")
    print("dishes\t\tquantity\t\tsub_cost")
    for k in wish :
               print (k,'\t\t',wish[k][0],"\t\t",wish[k][1],"SR")
print("\t\t\t\ttotal = ",total,"SR")

print("total cost with vat = ",total_tax,"SR")

pyttsx3.speak("your total cost with vat will be  " + total_tax + "saudi riyal")

pyttsx3.speak("Enjoy and Hope to see you again")

print("Enjoy\n\nHope to see you again")


