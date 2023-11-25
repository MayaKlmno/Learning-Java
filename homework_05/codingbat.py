def count_code(str):
  code = 0
  for i in range(len(str)-3):
    if str[i:i+2].lower() == "co" and str[i+3].lower() == "e":
      code += 1
  return code

def xyz_there(str):
  for i in range(len(str)):
    if str[i:i+3] == "xyz" and str[i-1] != ".":
      return True
  return False

count = count_code('corexxcone=n')
count = xyz_there('corexxxyzne=n')
