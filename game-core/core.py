

# Numero di righe nella griglia
rowLenght = 9

# Numero di colonne nella griglia
columnLenght = 9

# Numero massimo di navi: 6 [prima avevo scelto 5 con 1 sola da due]
# Orgnizzate come segue:
#   2 navi da 2 celle
#   1 nave da 3 celle
#   1 nave da 4 celle
#   1 nave da 5 celle
#
# GUARDARE es.jpg

# Variabile che indica di chi è il turno corrente
# Può assumere i vaoli 1 o 2 
# rispettivamente al turno del player corrente
currentTurn = 1

callbackPlayer1
callbackPlayer2

def setPlayer1Callback(_callback):
  global callbackPlayer1
  callbackPlayer1 = _callback

def setPlayer2Callback(_callback):
  global callbackPlayer2
  callbackPlayer2 = _callback

def setNextTurn():
  global currentTurn
  currentTurn = ((currentTurn + 1) % 2) + 1
