from datetime import datetime as dt
import pytest


def checkFileType(file_name):
    return "zip" in file_name or "rar" in file_name or "tgz" in file_name

def checkDate(date_str):
    b = dt.strptime(date_str.replace("-","/"), "%Y/%m/%d")
    a = dt.strptime('1995/10/13', "%Y/%m/%d")
    return a > b

def checkSize(size_: str):
    x = 240 * pow(2,10)
    return int(size_) < 240 * pow(2,10)

def check_condition_match(line: str):
    date_in_line = line[0:10]
    size_in_line = line[10:20]
    file_name_in_line = line[20:]
    return checkDate(date_in_line) and checkSize(size_in_line) and checkFileType(file_name_in_line)


def solution(textData):
    count = 0

    lines = textData.splitlines()
    for each_line in lines:
        line = each_line.lstrip()
        
        if check_condition_match(line):
            print(line)
            count += 1
    
    return str(count)
        

# main()
def main():
    text_1 = """\
        1988-08-29       956 system.zip
        1976-09-16    126976 old-photos.tgz
        1987-02-03    118784 logs.rar
        1961-12-04 703594496 very-long-filename.rar
        1980-08-03         2 DELETE-THIS.TXT
        2014-08-23       138 important.rar
        2001-08-26    595968 MOONLIGHT-SONATA.FLAC
        1967-11-30    245760 archive.rar
        1995-10-13       731 file.tgz\
        """
    assert solution(text_1) == "3" 