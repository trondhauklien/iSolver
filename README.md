# iSolver
Denne koden vil sammen med robotsett fra Fischertechnik legge grunnlaget for å kunne skanne sudokuer, komme med en gyldig løsning, for så å printe løsningen den kommer fram til. Den bruker Fischertechnik sin TXT-kontroller som hovedprosseseringsenhet, med FTCommunity firmware. "Operativsystemet" er basert på en forenklet linux-versjon, og kan styre blant annet motorer, samtidig som den kan ta input fra sensorer, trykknapper og et kamera. Fordelen med å bruke FTCommunity firmware i dette prosjektet er at man får muligheten til å programmere roboten i Python.

# Innhold
I denne mappen finner du bestanddelene i applikasjonen som kan lastes opp til TXT-kontrolleren, ved hjelp av brukergrensesnittet som er tilgjengelig ved å skrive ip-adressen til TXT-kontrolleren inn i en nettleser.
Følgende objekter er tilgjengelig i denne mappen. Her står det også beskrevet hva hver enkelt fil eller mappe gjør.
### app
Mappe som inneholder 