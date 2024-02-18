# %%
import helper
import phase1Helper
excelname = "record"
fromworksheet = "newcandidate"
toworksheetname = "everyone"
# phase1 upadte to the new list and write down the list to sending mails
phase1Helper.copyfromtwotoone(excelname, fromworksheet, toworksheetname)

# %%
