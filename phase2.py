import helper
import phase2Helper
excelname = "record"
# convert from tech_1_pass -> tech_2_pass, tks
tech1worksheet = "techpass1"
tech2worksheet = "techpass2"
phase2Helper.copyfromtwotoone(excelname, tech1worksheet, tech2worksheet, index=4)
# convert from nontech_1_pass -> nontech_2_pass, tks
nontech1worksheet = "nontechpass1"
nontech2worksheet = "nontechpass2"
phase2Helper.copyfromtwotoone(excelname, nontech1worksheet, nontech2worksheet, index=5)