# SpeedyQTtoPY
It transforms the windows drawn with QT Editor in the basic program written in python automatically saving time

nome SpeedyQTtoPY
autore Porcari Daniele
Anno di Grazia del Signore Gennaio 2022

Questo piccolo script serve a costruire direttamente il file main.py di una applicazione
disegnata con QT editor.
Per usarlo devi aver installato PYQT, QTDesigner. Avvialo nel tuo ambiente python preferito
ed in poco tempo avrai la base di partenza per la tua applicazione.
I file .ui di qt designer devono essere nella cartella ui
Il programma costruisce la cartella py_scripts in cui troverai tutti gli script ottenuti dai file
.ui con pyuic e il programma base chiamato main.py
Nel file sintassi.py ci sono le costanti con :
    il nome della finestra principale che deve essere lo stesso nome della MainWindow
    il percorso dove trovare i file .ui


This little script is used to build an application's main.py file directly
designed with QT editor.
To use it you need to have PYQT, QTDesigner installed. Start it in your favorite python environment
and in a short time you will have the starting point for your application.
The qt designer .ui files must be in the ui folder
The program builds the py_scripts folder where you will find all the scripts obtained from the files
.ui with pyuic and the base program called main.py
In the syntax.py file there are the constants with:
    the name of the main window which must be the same name as the MainWindow
    the path to find the .ui files
