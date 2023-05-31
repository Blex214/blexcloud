import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import search
import plot
import scrape
import threading

sg.ChangeLookAndFeel('DarkBlue13')

layout1 = [[sg.Text('Google something(Keyword) and select the number of links to read(Search Deph)')],

          [sg.Text('Keyword:'),
          sg.Input(size=(20, 1), enable_events=True, key='-KEYWORD-'),
          sg.Text('Search Deph:'), 
          sg.Input(size=(5, 1), enable_events=True, key='-SEARCH DEPH-')],

          [sg.Listbox(values=[], size=(60, 20), enable_events=True, key='-LIST-')],

          [sg.Button('Enter_Key', visible=False, bind_return_key=True)],
]

layout2 = [
          [sg.Text('Make a WordCloud!', justification='center')],
          [sg.Button('Generate', size=(20,5))]
]

tabs = [[sg.TabGroup([[sg.Tab('Search', layout1),
                       sg.Tab('Word Cloud', layout2)]])],

                       [sg.Button('Exit')]
]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

window = sg.Window('Version 1.0', tabs, icon='icon.ico', grab_anywhere=True)
# Event Loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):                # always check for closed window
        break
    if event == 'Enter_Key':
        if(window['-KEYWORD-'].get() != '' and window['-SEARCH DEPH-'].get() != '' and window['-SEARCH DEPH-'].get().isnumeric() == True):
            window['-LIST-'].update([])
            search.urls = []
            search_thread = threading.Thread(target = search.Google, args = (window['-KEYWORD-'].get(), int(window['-SEARCH DEPH-'].get())),daemon=True)
            search_thread.start()
            search_thread.join()
            window['-LIST-'].update(search.urls) 
        else:
             continue
    if event == 'Generate':
        if (search.urls!=[]):
            data = []
            for i in search.urls:
                x = scrape.scrape_page(i, clean=True) 
                data.append(x)
            #data = scrape.scrape_page(search.urls)
            fig = plot.plot_word_cloud(data)
            #window['wordCloud'].update(fig)
        else:
            continue