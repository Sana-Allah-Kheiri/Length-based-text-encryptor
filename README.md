# Length-based-text-encryptor
Encryption key = { (a, b) ; s.t: a = cardinality of string containing only alphabetic characters,
 b = no. of Left Shifts with criteria mentioned in README file
switch (a) { //if a is 0 it means the word has more than four alphabets
  case(0):  b = 3   break;

  case(1):  b = 0   break;

  case(2):  b = 1   break;

  case(3):  b = 2   break;

  case(4):  b = 1   break;

}
}
