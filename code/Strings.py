#Strings


#Multiplication Of String
print("Multiplication Of String")
s1="Vaibhav "
print(s1*4)

print("\n")

#len() of String - return the length of the string
print("len() of String")
s2="Vaibhav Mojidra" #return 15 including space 
s3="Vaibhav" #return 7
s4="Vaibhav " #return 8 including space after
print("Length of '"+s2+"': "+str(len(s2)))
print("Length of '"+s3+"': "+str(len(s3)))
print("Length of '"+s4+"': "+str(len(s4)))

print("\n")

#Indexing in String - syntax <string/string variable>[index]
print("Indexing in String")
s5="VaibhavM"
print("Index 0 of '"+s5+"': "+s5[0]) #returns V as its index starts from 0
print("Index 1 of '"+s5+"': "+s5[1]) #returns a (and not V) as its index starts from 0

print("\n")

#Negative indexing
print("Negative Indexing in String")
print("Index -1 of '"+s5+"': "+s5[-1])#returns M last letter 
print("Index -2 of '"+s5+"': "+s5[-2])#returns v second last letter

print("\n")

#Slicing in String - syntax <string/string variable>[startIndex:endIndex]
print("Slicing  in String")
s6="VaibhavMojidra"
print("[1:4] of '"+s6+"': "+s6[1:4]) #Prints substring including letter at index 1 but excluding letter at index 4
print("[0:4] of '"+s6+"': "+s6[0:4]) #Prints substring including letter at index 0 but excluding letter at index 4
print("[:4] of '"+s6+"': "+s6[:4]) #Prints substring from start to index 4 excluding letter at index 4
print("[4:] of '"+s6+"': "+s6[4:]) #Prints substring from index 4 including letter at index 4 till end

print("\n")

#Getting index of letter/word from String
print("Getting index of letter/word from String")
s7="Vaibhav Mojidra is a mobile app developer"
print("String : "+s7)
print("index('V'): "+str(s7.index('V'))) #prints first occurence of 'V' i.e 0
print("index('v'): "+str(s7.index('v'))) #prints first occurence of 'v' i.e 6 why 6 as its case sensitive V!=v
print("index('is'): "+str(s7.index('is'))) #prints first occurence of 'is' i.e 16 why 16 as its take return index of 'i' from is
print("index('a'): "+str(s7.index('a'))) #prints first occurrence of 'a' i.e 1
#print("index('x'): "+str(s7.index('x'))) #this will throw error as there is no x letter in string

print("\n")

#in operater in string to check if Strings contains a word
print("in operater in string to check if Strings contains a word")
print("String : "+s7)
print("'Vaibhav' in 'Vaibhav Mojidra is a mobile app developer': "+str('Vaibhav' in s7))#prints true
print("'vaibhav' in 'Vaibhav Mojidra is a mobile app developer': "+str('vaibhav' in s7))#prints false as case sensitive


#Practice
##email1="vaibhavmojidra@gmail.com"
##email2="vaibhavm@google.com"
##
##def replaceDomain(email):
##    if "@gmail.com" in email:
##        new_email=email[:email.index('@')]+"@google.com"
##        print('Email changed')
##        return new_email
##    print('No Email changed')
##    return email
##
##print(replaceDomain(email1))
##print(replaceDomain(email2))

#String Methods
s8=" Vaibhav Mojidra "
print("String - ' Vaibhav Mojidra '")
print("For upperCase .upper() "+s8.upper())
print("For lowerCase .lower() "+s8.lower())
print("For trim() .strip() "+s8.strip())
print("For left trim() .lstrip() "+s8.lstrip())
print("For right trim() .rstrip() "+s8.rstrip())
print("Method count returns how many time the letter/word repeated in string")
print(s8.count("a"))
print(s8.count("ai"))
print(s8.endswith("dra "))
print(s8.endswith("dra"))
print(s8.isnumeric())
print("111".isnumeric())
print(type("122"))
print(type(int("122")))
print(" ".join(["sa","sssa","as"]))
print("||".join(["sa","sssa","as"]))
print("Vaibhav Mojidra is a mobile app developer.".split())
print("Vaibhav,Mojidra is a mobile app developer.".split(","))

#String formating
print("Vaibhav Mojidra {} a {} app developer".format("is","mobile"))#parameters needs to be in  sequence
print("Vaibhav Mojidra {pre} a {domain} app developer".format(domain="mobile",pre="is"))#with variable parameters no need in seq
print("Decimals {:.2f} {:.2f} {:.2f}".format(2.3433,23.1,1))
print("0 {:>6}|".format(121))


