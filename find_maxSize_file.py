import os

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size
path="D:\\"
print ("Size: " + str(getFolderSize(path)))

def largest_file(p):

    max_file=""
    max_size=0
    size=0
    d=[]
    for folder, subfolders, files in os.walk(p):

        # checking the size of each file
        for file in files:
            size = os.stat(os.path.join(folder, file)).st_size
            #print("File {}-->size {}".format(os.path.join(folder, file),size))
            key=os.path.join(folder, file)
            value=size
            d.append((key,file,value))



    #print("The largest file is: " + max_file)
    #print('Size: ' + str(max_size) + ' bytes')
    #print(d)
    return (sorted(d, key=lambda x: x[2], reverse=True)[:10])


    #file_size=sorted(file_size,reverse=True)
    #print(file_size)





print(largest_file('D:\\'))


#t=[('D:\\Aricent\\Personal\\7987-FBAPS9437R-Form 16 (Part-A).pdf', '7987-FBAPS9437R-Form 16 (Part-A).pdf', 53131), ('D:\\Aricent\\Personal\\Appraisal_2019.pdf', 'Appraisal_2019.pdf', 69931), ('D:\\Aricent\\Personal\\displayCertificate.pdf', 'displayCertificate.pdf', 491311), ('D:\\Aricent\\Personal\\ITR_Altran_2018.PDF', 'ITR_Altran_2018.PDF', 137724), ('D:\\Aricent\\Personal\\ITR_Aricent_2019.PDF', 'ITR_Aricent_2019.PDF', 163789), ('D:\\Aricent\\Personal\\ITR_Rsystem_2018.PDF', 'ITR_Rsystem_2018.PDF', 130220), ('D:\\Aricent\\Personal\\Tax_computation_2020.pdf', 'Tax_computation_2020.pdf', 96738), ('D:\\Aricent\\Personal\\Your Resignation has been accepted.eml', 'Your Resignation has been accepted.eml', 12043), ('D:\\Aricent\\Personal\\Home Loan\\HomeLoanStatement.pdf', 'HomeLoanStatement.pdf', 18576), ('D:\\Aricent\\Personal\\Home Loan\\Insurance_homeloan.pdf', 'Insurance_homeloan.pdf', 142001), ('D:\\Aricent\\Personal\\Home Loan\\Insurance_loan.pdf', 'Insurance_loan.pdf', 954125), ('D:\\Aricent\\Personal\\Home Loan\\ITCertificate.pdf', 'ITCertificate.pdf', 32290), ('D:\\Aricent\\Personal\\Home Loan\\LBALXXXXXXXX4584-WLH2574526.pdf', 'LBALXXXXXXXX4584-WLH2574526.pdf', 33463), ('D:\\Aricent\\Personal\\Home Loan\\LBXXXXXXXXXXXX84.pdf', 'LBXXXXXXXXXXXX84.pdf', 19160), ('D:\\Aricent\\Personal\\Home Loan\\loanStatement.xps', 'loanStatement.xps', 60383), ('D:\\Aricent\\Personal\\Home Loan\\PPF_statement.pdf', 'PPF_statement.pdf', 62602), ('D:\\Aricent\\Personal\\Home Loan\\Premium paid.pdf', 'Premium paid.pdf', 194400), ('D:\\Aricent\\Personal\\Home Loan\\Registry.pdf', 'Registry.pdf', 3112051), ('D:\\Aricent\\Personal\\Home Loan\\RegistryReciept.jpg', 'RegistryReciept.jpg', 45797), ('D:\\Aricent\\Personal\\HRA\\3457_001.pdf', '3457_001.pdf', 163294), ('D:\\Aricent\\Personal\\HRA\\Q1.pdf', 'Q1.pdf', 180200), ('D:\\Aricent\\Personal\\HRA\\Q2.pdf', 'Q2.pdf', 160628), ('D:\\Aricent\\Personal\\HRA\\Q3.pdf', 'Q3.pdf', 161634), ('D:\\Aricent\\Personal\\HRA\\Q4.pdf', 'Q4.pdf', 168755), ('D:\\Aricent\\Personal\\ITR tax 2019\\19212599076_FBAxxxxx7R_A1.pdf', '19212599076_FBAxxxxx7R_A1.pdf', 107262), ('D:\\Aricent\\Personal\\ITR tax 2019\\19218541361_FBAxxxxx7R_U1.pdf', '19218541361_FBAxxxxx7R_U1.pdf', 95690), ('D:\\Aricent\\Personal\\ITR tax 2019\\2020-02-13-10-22-13-857_-1722389123_.pdf', '2020-02-13-10-22-13-857_-1722389123_.pdf', 26723), ('D:\\Aricent\\Personal\\ITR tax 2019\\FBAPS9437R_639034013022000201_ITNS280_13022020_SAQXXX.pdf', 'FBAPS9437R_639034013022000201_ITNS280_13022020_SAQXXX.pdf', 11583), ('D:\\Aricent\\Personal\\ITR tax 2019\\ITR_2018-19_FBAPS9437R.PDF', 'ITR_2018-19_FBAPS9437R.PDF', 137724), ('D:\\Aricent\\Personal\\LIC\\BillDesk - All Your Payments. Single Location.pdf', 'BillDesk - All Your Payments. Single Location.pdf', 95088), ('D:\\Aricent\\Personal\\LIC\\LIC_Halfyearly.pdf', 'LIC_Halfyearly.pdf', 95467), ('D:\\Aricent\\Personal\\LIC\\LIC_Premium statement.pdf', 'LIC_Premium statement.pdf', 24496), ('D:\\Aricent\\Personal\\LIC\\LIC_Premium_2020_21.pdf', 'LIC_Premium_2020_21.pdf', 23950), ('D:\\Aricent\\Personal\\MC2 Bills\\invoice_mobile.pdf', 'invoice_mobile.pdf', 34550), ('D:\\Aricent\\Personal\\Proof2019\\FinalInvestmentProof_FY 2019-20.pdf', 'FinalInvestmentProof_FY 2019-20.pdf', 32124), ('D:\\Aricent\\Personal\\Proof2019\\LIC.pdf', 'LIC.pdf', 24101), ('D:\\Aricent\\Personal\\Salary Slip\\April_2020.pdf', 'April_2020.pdf', 32964), ('D:\\Aricent\\Personal\\Salary Slip\\Aug2019.pdf', 'Aug2019.pdf', 46632), ('D:\\Aricent\\Personal\\Salary Slip\\Aug_2020.pdf', 'Aug_2020.pdf', 34036), ('D:\\Aricent\\Personal\\Salary Slip\\July2019.pdf', 'July2019.pdf', 46632), ('D:\\Aricent\\Personal\\Salary Slip\\July_2020.pdf', 'July_2020.pdf', 34304), ('D:\\Aricent\\Personal\\Salary Slip\\June2019.pdf', 'June2019.pdf', 46632), ('D:\\Aricent\\Personal\\Salary Slip\\June_2020.pdf', 'June_2020.pdf', 34304), ('D:\\Aricent\\Personal\\Salary Slip\\March_2020.pdf', 'March_2020.pdf', 34304), ('D:\\Aricent\\Personal\\Salary Slip\\May_2020.pdf', 'May_2020.pdf', 34304), ('D:\\Aricent\\Personal\\Salary Slip\\Sept2019.pdf', 'Sept2019.pdf', 46632), ('D:\\Aricent\\Personal\\Salary Slip\\Sep_2020.pdf', 'Sep_2020.pdf', 34036), ('D:\\Aricent\\Personal\\UDemy\\DataScience.pdf', 'DataScience.pdf', 76175), ('D:\\Aricent\\Personal\\UDemy\\Django.pdf', 'Django.pdf', 76385), ('D:\\Aricent\\Personal\\UDemy\\ISTQBFoundationLevel.pdf', 'ISTQBFoundationLevel.pdf', 79341), ('D:\\Aricent\\Personal\\UDemy\\Online Courses - Anytime, Anywhere _ Udemy.pdf', 'Online Courses - Anytime, Anywhere _ Udemy.pdf', 88440), ('D:\\Aricent\\Personal\\UDemy\\PythonCourse.pdf', 'PythonCourse.pdf', 76522), ('D:\\Aricent\\Personal\\UDemy\\RobotFramework.pdf', 'RobotFramework.pdf', 91772), ('D:\\Aricent\\Personal\\UDemy\\SoftwareTesting.pdf', 'SoftwareTesting.pdf', 91804), ('D:\\Aricent\\Personal\\UDemy\\SparkPython.pdf', 'SparkPython.pdf', 75593)]

