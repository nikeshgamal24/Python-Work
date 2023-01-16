# # blurprint --> certain features fix (common to all object)--> class


# # scorpio-->size , addd ---> individually feature add unique--> object
# # BMW-->size , addd ---> individually feature add unique--object


# #class create
#   #--> variable , function (method)
#   #inheritance 

# # funciton --> call
# #class

# class College:
#     def __init__(self,name,location): #constructor --> function --> is called automatically whenever the object is formed/created
#         self.name = name #self--> points to the object that is created at present 
#         #kun object banauda yo constructor call bhayeko ho tyo object lai point garxa
#         self.location = location
    
#     def display_details(self): #operation ko lagi hamile function banauuni ho 
#         print(self.name)
#         print(self.location)
#         return 0  

#     def __str__(self):
#         return  f"My college name is {self.name} and it is located at {self.location}"

# #data security--> class bhitra data function---> outside accesss garna mildaiina (outsider restrict)

# college1 = College("NCIT","BALKUMARI")  #object create -> __init__()
# print(college1.display_details())
# # print(name)

# college2 = College("COSMOS","Satdobato")  #object create -> __init__()
# print(college2)




# # #scenario:
# 1. Student ko marks calcualte garnu paryo total 
# 2. NIeksh , Mini , sudesh ---> Student

class Student:
    full_marks = 500

    def __init__(self,snm_marks,sp_marks,onm_marks,ai_marks):
        self.snm_marks = snm_marks
        self.sp_marks = sp_marks
        self.onm_marks = onm_marks
        self.ai_marks = ai_marks

    def total_marks(self):
        return self.snm_marks+self.sp_marks+self.onm_marks+self.ai_marks

    def calcuate_percentage(self,obtained_marks):
        percentage = (obtained_marks/Student.full_marks)*100
        return percentage

    def display_details(self):
        ...

nikesh = Student(40,45,42,35)
total_marks_nikesh = nikesh.total_marks()  #--> object.funciton_name()
# print(total_marks_nikesh)

percentage = nikesh.calcuate_percentage(total_marks_nikesh)
print(percentage)

print('*'*100)
mini = Student(47,42,44,40)
total_marks_mini = mini.total_marks()  #--> object.funciton_name()
# print(total_marks_nikesh)

percentage = mini.calcuate_percentage(total_marks_mini)
print(percentage)


#Car--->BMW--details, Audi-details , mercedes-detaisl

# car--> price return ---> outside of class store ani kun car chai expensive   #maxm of three numbers