from lib.userInterface import userInterface

if __name__ == '__main__':
    ui = userInterface()

    if ui.yesNoQuery("Input from file? [y/n]"):
        path = input("Please input path of your file: ")
        ui.fileInput(path)
    else:
        ui.userInput()

    ui.quantize().predict()
    print ("The predicted price is : %f\n" % ui.getPredictedPrice())

    if ui.yesNoQuery("Print regression report? [y/n]"):
        ui.printReport()
