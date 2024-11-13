#Maisha Tapia Paredes, proficieny test secret cypher
def my_function():
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  new_alphabet = ""
  secret_code = str(input("Type in what you want translated: "))
  for char in secret_code:
      char = ord(char)+5
      new_alphabet = new_alphabet+(chr(char))
  print("original code:",secret_code)
  print("cyphered code:", new_alphabet)
my_function()