import PySimpleGUI as sg

def salva_dati(nome, cognome, marca, carburante, auto_elettriche):
    file = open("risposte.txt", "a")
    file.write(f"Nome: {nome}, Cognome: {cognome}, Mrca: {marca}, Carburante: {carburante}, auto_elettriche: {', '.join(auto_elettriche)}\n")
    sg.popup("Le risposte alle tue domande sono state salvate.")
    file.close()

layout = [
    [sg.Text("Nome"), sg.InputText(key="nome")],
    [sg.Text("Cognome"), sg.InputText(key="cognome")],
    [sg.Text("Quale la tua marca preferita di auto?")],
    [sg.InputText(key="marca")],
    [sg.Text("Che carburante utilizza la tua auto?")],
    [sg.Checkbox("Benzina", key="benzina"), sg.Checkbox("Disel", key="disel"), sg.Checkbox("Elettrico", key="elettrico"), sg.Checkbox("Altro", key="altro")],
    [sg.Text("Pensi che le nuove auto elettriche saranno il futuro?")],
    [sg.Radio("Si", "auto_elettriche", key="si"), sg.Radio("No", "auto_elettriche", key="no")],
    [sg.Button("Salva")]
]

window = sg.Window("Questionario", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Salva":
        nome = values["nome"]
        cognome = values["cognome"]
        marca = values["marca"]
        carburante = [c for c in ["Benzina", "Disel", "Elettrico", "Altro"] if values[c.lower()]]
        auto_elettriche = "Si" if values["si"] else "No"
        salva_dati(nome, cognome, marca, carburante, auto_elettriche)

window.close()
