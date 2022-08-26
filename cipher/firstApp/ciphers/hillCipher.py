import numpy as np
chars = "abcdefghijklmnopqrstuvwxyz"

def split(chars):
    return [char for char in chars]


# Encode given char with a key
def encode(str, key):

  str = str.replace(" ", "").lower()

  # Add arbitrary letters if necessary
  if(len(str) % len(key) != 0):
    for i in range(len(key) - len(str) % len(key)): str += "x"

  # Transform the word into a matrix of numbers
  wordMatrix = np.array([[split(chars).index(char.lower())+1 for char in str]])

  res = ""
  for i in range(0, len(split(str)), len(key)):
    if(str[i] not in split(chars)):
      print("Illegal character found: " + str[i])
      return False

    # Get group of letters
    tmpM = np.array([wordMatrix[0][i+j] for j in range(len(key))])

    # Multiply group with key
    multM = np.matmul(key, tmpM)

    # Add encoded chars
    for j in range(len(key)):
      res += chars[int(round(multM[j]%26-1))]

  return(res.upper())

# Decode given char with a key
def decode(str, key):

  # Get determinant of the key matrix
  A = round(np.linalg.det(key))
  if(A == 0):
    print("Invalid determinant")
    return False

  # Get the inverse matrix
  invKey = np.linalg.inv(key) * A

  # Find k^-1 (mod26)
  def bruteKMod26(k):
    primeNumbers = [1,3,5,7,9,11,15,17,19,21,23,25]
    for m in primeNumbers:
      if (k * m) % 26 == 1:
        return m
  invA = bruteKMod26(A)
  if not invA:
    print("Invalid key matrix")
    return False

  decodeKey = (np.round(invKey) * invA) % 26
  wordMatrix = np.array([[split(chars).index(char.lower())+1 for char in str]])
  str = str.replace(" ", "").lower()

  res = ""
  for i in range(0, len(split(str)), len(decodeKey)):
    tmpM = np.array([wordMatrix[0][i+j] for j in range(len(decodeKey))])
    multM = np.matmul(decodeKey, tmpM)
    for j in range(len(decodeKey)):
      res += chars[int(round(multM[j]%26-1))]
  return(res.upper())




# key = np.array([[9, 4], [5, 7]])
# key = np.array([[1, 3, -1], [6, 1, 1], [-5, 4, -3]])
# key = np.array([[6, 1, 3, 5], [2, 9, 0, 9], [8, 0, 1, 9], [7, 8, 0, 8]])
# # key = np.round(np.random.rand(10, 10) * 10) # Key can be invalid

# toEncode = "The quick brown fox jumps over the lazy dog"

# print("Encoding:", toEncode)
# encoded = encode(toEncode, key)
# print("Encoded: ", encoded)
# print("Decoded: ", decode(encoded, key))
