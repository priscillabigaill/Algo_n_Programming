import os

def convertToSentence(fileName):
  # opening and reading the file
  readFile = open(os.getcwd() + "\\" + fileName, "r")
  # readFile = open(fileName, "r")
  stringValue = readFile.read()

  titles = ["Mr.", "Mrs.", "Dr."]
  data = stringValue.split()

  result = ""
  n = 0
  for i in data:
    temp = i + ""
    if (i.endswith(".") or i.endswith("?") or i.endswith("!")):
      if (n != len(data) - 1):
        if (i not in titles and str(data[n + 1][0]).isupper()):
          temp = temp + "\n"
      n = n + 1
      result = result + temp

  # Add a return statement to return the result
  return result


print(convertToSentence("text2.txt"))
