from threading import Thread
from FindEnumberNumba import TicToc ,FindE

if __name__ == "__main__":
    spentTime = TicToc()
    spentTime.tic()
    k = 1000000
    FindEnum=[]
    threads =[]
    for i in range(3):
        FindEnum.append(FindE())
        threads.append(Thread(target=FindEnum[i].ChooseR, args=(k,)))
        print("Started thread number #%d" % i)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    totaltop = 0
    count = 0
    for findEnum in FindEnum:
        totaltop += findEnum.FindE_number()
        count += 1

    print("E = %12.8f | TİME = %.5f" %
          (totaltop / count, spentTime.toc()))