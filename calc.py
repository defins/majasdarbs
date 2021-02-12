#programma bus primitivs kalkulators
def saskaitit(a,b):
    return a + b
def atnemt (a,b):
    return a - b
def reizinat (a,b):
    return a * b
def dalit (a,b):
    return a / b

print("Sis ir loti primitivs kalkulators.")
print ("izvelies kadu darbibu veiksi:")
print ("1. saskaitit")
print ("2. atnetm")
print ("3. reizinat")
print ("4. dalit")
print ("q - lai izlegtu programmu")

while True:
    izvele = input ("Ievadi izveli: ")

    if izvele in ('1','2','3','4'):
        sk1 = float(input("Ievadi pirmo skaitli: "))
        sk2 = float(input("ievadi otro skaitli: "))

        if izvele  == '1':
            print (sk1, "+", sk2, "=", saskaitit(sk1,sk2))
        elif izvele == '2':
            print (sk1, "-", sk2, "=", atnemt(sk1,sk2))
        elif izvele == '3':
            print (sk1, "*", sk2, "=", reizinat(sk1,sk2))
        elif izvele == '4':
            print (sk1, "/", sk2, "=", dalit(sk1,sk2))
        elif izvele == 'q':
            print ("sledzam ara")
        break
    else :
        print("nepareizs ievads")
    


