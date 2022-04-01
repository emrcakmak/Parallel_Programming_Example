import random
import time

class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindE:


    def __init__(self):

        self.listEnum = []

    def ChooseR(self, nn):
        total = 0
        count = 0

        for i in range(nn):
            while total < 1:
                count += 1
                number = round(random.uniform(0, 1), 3)

                total += number
            self.listEnum.append(count)

            count = 0
            total = 0

    def FindE_number(self):
        totaltop = 0
        sizlistenum = len(self.listEnum)
        for i in range(len(self.listEnum)):
            totaltop += self.listEnum[i]
        newtotal = totaltop / sizlistenum
        return newtotal