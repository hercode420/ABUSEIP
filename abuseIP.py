def abuseIP():
    import requests  # Requests serve a gestire la comunicazione con l'API web
    import json
    import pandas  # E una libreria di programmazione python che utilizza la manipoazione e l'analisi dei dati
    import csv  # utilizzato per l'importazione ed esportazione di una tabella di dati.

    print("+-----------------------------------------------+")
    print("|                                               |")
    print("|                   HackTool                    |")
    print("|                                               |")
    print("+-----------------------------------------------+")
    print("|                 Abuseipdb                     |")
    print("+-----------------------------------------------+")

    file_path = str(input('Percorso del file: ')) #file_path e un variabile chiede all'utente il percorso del file
    IP_CSV = pandas.read_csv(file_path) #IP_CSv e una varibile che leggge il file csv utilizzando il modulo PANDAS

# Converte in un elenco la colonna del file CSV chiamato "" IP "" nel file esistente. Cosi da convertilo in un eleco ottimizzato.
    ip=IP_CSV['IP'].tolist()


    API_KEY = '5e2850ef5a64344c01a8a9449926b95c6656f56f3bb8dfca8c5979527f55c253d154f8b33478904c' #Chiave di AbuseIPDB
    url = 'https://api.abuseipdb.com/api/v2/check' #L'url dell'API dove si può comunicare

    #CSV_columns serve per identificare le colonne che verranno ricevute dalla riposta dell'API in formato JSON
    csv_columns = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','usageType','isp','domain','hostnames','totalReports','numDistinctUsers','lastReportedAt']

    #E' l'intestazione della richiestta HTTP
    headers = {
        'Accept': 'application/json', #I dati accettati a JASON
        'Key': API_KEY# le Chiavi di API
    }
    #Quindi si aprira il file Abuse_result.csv per aggiungere le i nomi delle colonne
    with open("ReportIP.csv","a", newline='') as filecsv: # "_a_" Significa aggiungere se il file esite, se non crearlo
        writer = csv.DictWriter(filecsv, fieldnames=csv_columns) #WRITE è una variabile per definire i nomi delle colonne del file CSV
        writer.writeheader() #da scrivere nel file utilizzando (Write.writeheader())
    for i in ip: #Avvia un ciclo, esegue un lavoro ripetuto per ogni "_IP_" presente nell'elenco "IP"
        parameters = {   #PARAMETERS verrano utilizzati per REQUEST()
            'ipAddress': i, #Qui "_IP_" che si vuole controllare
            'maxAgeInDays': '90'} #Serve per ottenre tutti i risultati RIPORTATI da 90 GIORNI

        respnse = requests.get(url=url,headers=headers,params=parameters) #Questa var invia una richiesta web per ottenere i risultati
        json_Data = json.loads(respnse.content)  #JSON_DATA converte i risultati in formato JSON
        json_main = json_Data["data"] #Serve per ottenere i dati e le chiavi secondarie presenti nella chiave "DATA"
        with open("ReportIP.csv","a", newline='')as filecsv: #Apri il file e aggiungi i DATI sotto le sue colonne
            writer= csv.DictWriter(filecsv,fieldnames=csv_columns)
            writer.writerow(json_main)
abuseIP()