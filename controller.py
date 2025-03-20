import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleSpellCheck(self,e):
        linguaInserita= self._view._selezionaLingua.value
        fraseInserita=self._view._frase.value
        modalitàInserita=self._view._selezionaModalità.value
        #controlli sul formato con messaggio sull'interfaccia
        #dobbiamo controllare se i campi sono vuoti, se si stampiamo che sono vuoti
        if linguaInserita == None:
            self._view._output.controls.append((ft.Text("Selezionare una lingua!", color="red")))
            self._view.update()
            return
        if modalitàInserita == None:
            self._view._output.controls.append((ft.Text("Selezionare una modalità!", color="red")))
            self._view.update()
            return

        if fraseInserita == "":
            self._view._output.controls.append((ft.Text("Scrivere la frase su cui effettuare il controllo!", color="red")))
            self._view.update()
            return
        #risultato perchè tutto è andato per il verso giusto
        risultato= self.handleSentence(fraseInserita,linguaInserita,modalitàInserita) #è una tupla
        if risultato == None:
            self._view._output.controls.append((ft.Text("il controllo non ha prodotto alcun risultato!", color="red")))
            self._view.update()
            return

        # printo sull'interfaccia
        self._view._output.controls.append((ft.Text(f"Frase inserita: {fraseInserita}", color="green")))
        self._view._output.controls.append((ft.Text(f"Parole errate: {risultato[0]}", color="green")))
        self._view._output.controls.append((ft.Text(f"Tempo richiesto dalla ricerca: {risultato[1]}", color="green")))
        self._view.update()


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text