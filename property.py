
# %% 

class Student3:
    def __init__(self, count: int):
        print('मान्छे हुँ मान्छे तर तँ जस्तो असुरको लागि शंकर, शंकर हु। नरपिसाचको लागि नरसिंह र तँ जस्तोको लागि नरदेवी, उग्रचंदी, भद्रकालीको छोरा शंकर हुँ शंकर।')
        self.__count = count

    @property
    def count(self):        #   Getter
        print('\nसाथीहरुको लागि यो हात सलाम हो, दुश्मनको लागि यो हात फलाम हो।')
        return f'{self.__count}'

    @count.setter           #   Setter
    def count(self, value):
        print('\nआगोलाई छुने प्रयास नगर, टाढैबाट हेर, पोल्न सक्छ।')
        self.__count = value

class_1 = Student3(10)
print(class_1.count)
class_1.count = 111
print(class_1.count)

# %%

