# Money Visual :) (six day basis)
# By Brandon Salazar
# made on 12/23/23

print("""                                     Welcome to Money Visual
   A simple program that calculates an individuals pay for the span of six days in a visually appealing way. 
                  Programmed using python math operators and if else statements. """)
print("""
Money Visual is simple to use.
Run the code.
Enter the hours worked using a whole number for each day then press enter.
If the hours worked for that day is zero simply enter zero.
When Hourly Pay is asked simply type your hourly pay as a whole number and press enter.
 """)

dayOne =  int(input("Enter Hours Day 1: "));
dayTwo =  int(input("Enter Hours Day 2: "));
dayThree = int(input("Enter Hours Day 3: "));
dayFour = int(input("Enter Hours Day 4: "));
dayFive = int(input("Enter Hours Day 5: "));
daySix = int(input("Enter Hours Day 6: "));

hoursOfWork=(dayOne+ dayTwo+ dayThree+ dayFour + dayFive + daySix)

payRate = int(input("Hourly Pay: $ "));
if hoursOfWork > 0 and payRate > 0 :
  print("Total amount due: $", payRate * hoursOfWork)  # this will print/display the total amount of money made if hours are more than zero
  print("Thank you for using Money Visual by Brandon Salazar")
elif payRate == 0 and hoursOfWork == 0:
  print("Well this is awkward because why are you entering only zeros hahahah please try again !")
elif payRate <= 0:
    print("The pay rate per hour must be greater than zero to work. Try again !")
elif hoursOfWork <= 0:
  print("The amount of hours worked must be greater than zero to work. Try again !")
  
