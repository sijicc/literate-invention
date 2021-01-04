import PySimpleGUI as sg
import json
import glob
from natsort import natsorted
from os import getcwd
from pathlib import Path

sg.theme('default')
cwd = getcwd()

text_column = [
    [sg.Text('Pick directory of whoever you want to check,'
             '\nthen click on "Merge" and wait for a bit.'
             '\nAfter you see "Merged!" in output area'
             '\npress "Fix encoding" button, then wait'
             '\nfor a "Fixed!" in output area. After that'
             '\nYou are done, you can do whatever you want.')],
    [sg.Text('Remember to pick directory,'
             '\nthen merge and fix first.'
             '\nElse it will just crash.', text_color="red")]
]

input_column = [
    [sg.Input(cwd, size=(25, 1), key="-DIRECTORY-"), sg.FolderBrowse()],
    [sg.Button('Merge'), sg.Button('Fix encoding')],
    [sg.InputText(key="-WORD-", size=(25, 1)), sg.Button('Count')],
    [sg.Button('Call duration'), sg.Button('Message amount')],
    [sg.Button('Exit')]
]

result_column = [
    [
        sg.Output(size=(30, 10))
     ]
]

layout = [
    [
        sg.Column(text_column),
        sg.VSeparator(),
        sg.Column(input_column),
        sg.VSeparator(),
        sg.Column(result_column),
     ]
]

window = sg.Window('Facebook thingy', layout)
while True:
    event, values = window.read()
    counted_word = values["-WORD-"]
    path = values["-DIRECTORY-"]
    window.Refresh()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break  # exits if you close window on X or exit button

    if event == 'Merge':
        output_file = []  # declare empty list to extend
        print(path)
        for file_name in natsorted(glob.glob(path + "/message_*.json")):
            print(file_name)
            with open(file_name) as json_file:
                messages = json.load(json_file)
            json_messages = messages["messages"]
            output_file.extend(json_messages)
        with open('merged.json', 'w') as outfile:
            json.dump(output_file, outfile, indent=1)
        print("Merged!")

    if event == 'Fix encoding':
        cwd = getcwd() + "/merged.json"
        with open(cwd) as json_file:
            data = json.load(json_file)

        out = []
        for i in data:
            if 'content' in i:
                i["content"] = i["content"].encode('latin1').decode('utf8')
                # print(i)
                out.append(i)
            if 'content' not in i:
                # print('no')
                out.append(i)
                continue
        with open("merged.json", "w") as output:
            json.dump(out, output, indent=1)
        print("Fixed!")

    if event == 'Count':
        cwd = getcwd() + "/merged.json"
        file = open(cwd, "r", encoding="utf8")
        data = file.read()
        counted_word_enc = counted_word.encode("unicode_escape").decode('utf8')
        poss1 = data.count('"' + counted_word_enc + '"')
        poss2 = data.count(' ' + counted_word_enc + '"')
        poss3 = data.count(' ' + counted_word_enc + ' ')
        poss4 = data.count('"' + counted_word_enc + ' ')

        sum = poss1 + poss2 + poss3 + poss4
        print('"' + str(counted_word) + '" was used: ' + str(sum) + ' times')

    if event == 'Call duration':
        cwd = getcwd()
        cwd = getcwd() + "/merged.json"
        sum = 0
        with open(cwd) as json_file:
            data = json.load(json_file)
        for i in data:
            if i["type"] == "Call":
                a = i["call_duration"]
                sum += a
        days = (sum - sum % 86400) / 86400
        hours = (sum - days * 86400 - sum % 3600) / 3600
        minutes = (sum - days * 86400 - hours * 3600 - sum % 60) / 60
        seconds = (sum - days * 86400 - hours * 3600 - minutes * 60)
        print("Call duration is: " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
        window.Refresh()

    if event == 'Message amount':
        cwd = getcwd()
        cwd = getcwd() + "\\merged.json"
        with open(cwd) as json_file:
            data = json.load(json_file)
        print("Total message amount is: " + str(len(data)))
