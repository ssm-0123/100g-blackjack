#!python3



def value(hand):
  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''
  result = 0
  switch = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13}
  Ace = 0
  for a in hand:
    if "A" == a[0]:
      Ace = Ace + 1
  if Ace == 0:
    for b in hand:
      result = result + switch[b[0]]
    return result
  elif Ace >= 1:
    final = []
    result = 0
    for b in hand:
      if b[0] != "A":
        result = result + switch[b[0]]
      else :
        result = result + 1
    final.append(result)
    if Ace == 1:
      final.append(result+10)
    elif Ace == 2:
      final.append(result+10)
      final.append(result+20)
    elif Ace == 3:
      final.append(result+10)
      final.append(result+20)
      final.append(result+30)
    elif Ace == 4:
      final.append(result+10)
      final.append(result+20)
      final.append(result+30)
      final.append(result+40)
    return final

          




      
  
      
"""

def main():
  assert value(['AH','3D','4S']) == [8,18]
  assert value(['KH','TD']) == 23
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 31

if __name__ == "__name__":
  main()
"""