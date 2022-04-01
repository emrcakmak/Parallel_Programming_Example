from threading import Thread
from FindEnumber import TicToc ,FindE

if __name__ == "__main__":
    spentTime = TicToc()
    spentTime.tic()
    k = 1000000
    FindEnum=FindE()
    FindEnum.ChooseR(k)
    findEnumber =FindEnum.FindE_number()
    print("E = %12.8f | TİME = %.5f" %
          (findEnumber, spentTime.toc()))