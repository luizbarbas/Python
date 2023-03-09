import yfinance
import matplotlib.pyplot as plt
import pyautogui
import pyperclip
import time
ticker = input("digite a ação desejada: ")
dados = yfinance.Ticker(ticker).history("6mo")
fechamento = dados.Close
grafico = fechamento.plot()
máxima = fechamento.max()
mínima = fechamento.min()
atual = fechamento[-1]
print(fechamento)
print(grafico)
print(máxima)
print(mínima)
print(atual)

pyautogui.PAUSE=2
pyautogui.hotkey("alt","tab")
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://mail.yahoo.com/d/folders/1?.intl=br&.lang=pt-BR")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")
pyautogui.click(x=135, y=302)

pyperclip.copy("luizclaudiomachado@yahoo.com.br")
pyautogui.hotkey("ctrl","v")
pyautogui.click(x=370, y=361)
pyperclip.copy("cotação solicitada")
pyautogui.hotkey("ctrl","v")
pyautogui.click(x=363, y=442)

mensagem = f"""
Prezado,
Seguem análises dos últimos 6 meses da ação {ticker}

Cotação máxima: R$ {round(máxima),2}
Cotação mínima: R$ {round(mínima),2}
Cotação Atual: R$ {round(atual),2}

Qualquer dúvida estou a disposição.

Att.
Luiz Barbas"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")
pyautogui.click(x=384, y=991)