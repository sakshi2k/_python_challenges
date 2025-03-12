You are given a string containing a detailed list of files. Your task is to evaluate a simple query on a certain subset of these files.
The string consists of N lines separated by end-of-line characters (ASCII code 10). Each line contains information about one file, grouped in three columns: date, size and name (in that order). The columns (except for the last one) have fixed lengths and are separated by one space. They have the following formats and meanings:
• Column size has length 10 and contains the size of the file in bytes. The size is less than 231 bytes and is aligned to the right.
• Column date has length 10 and contains the last modification date of the file in the format "yyyy-mm-dd".
• Column name is of variable length and contains the name of the file. The name of the file consists of at most 255 printable ASCIl characters and contains at least one dot character. The part of the name after the last dot is called the extension. File names are case-sensitive.

We are only interested in files that satisfy the following criteria:
• They contain archive data. We say that a file contain archive data if its extension is either "zip", "rar" or "tgz".
• Their size is less than 240 * 210 bytes.
• They were last modified before 1995-10-13.
Calculate the quantity of these files.

Write a function:
def solution(S)
that, given a string S describing the file list, returns the answer to the query, encoded as a string. If there are no files satisfying the criteria listed above, the function should return "NO FILES".

For example, given string S with N = 9 lines (enclosed between """):
"""
1988-08-29 956 system.zip
1976-09-16 126976 old-photos.tgz
1987-02-03 118784 logs. rar
1961-12-04 703594496 very-long-filename. rar
1980-08-03 2 DELETE-THIS. TXT
2014-08-23 138 important.rar
2001-08-26 595968 MOONLIGHT-SONATA.FLAC
1967-11-30 245760 archive.rar
1995-10-13 731 file.tgz
"""
the function should return "3".
Assume that:
• N is an integer within the range [1..100];
• string S consists only of printable ASCII characters and end-of-line characters;
• string S is a correct list of files according to the specification above. Files can have the same names.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
