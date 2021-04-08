#Explain your work

#Question 1
CV1 = dict() # Creating an empy dictionary.
CV1 = {"Name":"Yağızhann","Surname " : "Macuncu ", "University " : "METU"}
CV2 = {"Name":"HASAN ","Surname " : "KAYA ", "University " : "OXFORD"}
CV3 = {"Name":"MAHMUT ALİ ","Surname " : "ÇAKIR ", "University " : "ITU"}
CV4 = {"Name":"ABRAHAM ","Surname " : "LINCOLN ", "University " : "MIT"}
CV5 = {"Name":"FENERBAHÇELİ  ","Surname " : "CEMİL ", "University " : "FENERBAHCE"} # 5 CV'S with a couple of property.
cv = list()  # Creating an empty list so that we can store our CVi's such that i€{1,2,...,5}.
cv = [CV1, CV2, CV3, CV4, CV5] # Inserting CVi's into the list 'cv'.
for k in cv: # Printing the CVi's which are replaced in the list cv.
    print(k)
