# %%
import helper
import phase1Helper
excelname = "record"
fromworksheet = "newcandidate"
toworksheetname = "everyone"
thankssheetname = "ThanksList"
# phase1 upadte to the new list and write down the list to sending mails
# try:
phase1Helper.copyfromtwotoone(excelname, fromworksheet, toworksheetname)
print("phase1 end Successfully!")
# except:
#     print('something went wrong!!')