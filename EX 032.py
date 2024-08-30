from datetime import datetime
ano_atual = datetime.now().year
usr = int(input("Qual ano deseja analisar? Digite 0 para analisar o ano atual.\n"))
if usr == 0:
    usr_atual = ano_atual
    if usr_atual % 4 == 0 and usr_atual % 100 or usr_atual % 400 == 0:
        print(f"O ano atual ({usr_atual}) é bissexto.")
    else:
        print(f"O ano atual ({usr_atual}) não é bissexto.")
else:
    if usr % 4 == 0 and usr % 100 or usr % 400 == 0:
        print(f"O ano referido ({usr}) é bissexto.")
    else:
        print(f"O ano referido ({usr}) não é bissexto.")