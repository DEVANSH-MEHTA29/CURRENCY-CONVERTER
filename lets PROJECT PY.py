print("Welcome to Currency Converter!!!")
print( )
value = float(input("AMOUNT:  "))
print( )

A=['INR','USD','EUR','CAND','RUBL','GBP','YEN']
print("From currency : ")
in_c = input("(INR/USD/EUR/CAND/RUBL/GBP/YEN)  :")

if in_c  in A:
        print( )
        print( )
        print("To Currency  ")
        out_c = input("(INR/USD/EUR/CAND/RUBL/GBP/YEN) : ")
        if out_c not in A:
            print( )
            print( )
            
            print(" Invalid!! ")
            print("Kindly enter only mentioned units keeping in mind CASE SENSITIVITY")
            print("Run the program again!!!")
            
else:
        print( )
        print( )
        print("Invalid!!")
        print("Kindly enter only mentioned units keeping in mind CASE SENSITIVITY")

        print("Run the program again!!!")
        

       # Managed
#Inverted

dict = {'INR': 1, 'USD': 0.0123, 'EUR': 0.0115, 'GBP': 0.0102,'YEN':1.7001,"RUBL":0.7408,"CAND":0.0163}

def currency_converter (value,in_c,out_c):
    print( )
    print( )
    print("1",in_c,"=","%.4f"%(dict[out_c] / dict[in_c]),out_c," (as of 25 NOV.2022)")
    print()
    return(print(" CONVERTED AMOUNT :  ","%.4f"%((dict[out_c] / dict[in_c]) * value),out_c))
    
currency_converter(value,in_c,out_c)

           
            





 

