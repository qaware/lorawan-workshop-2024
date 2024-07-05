# LoRaWAN Workshop am 19.07.2024

Wir bauen eine Python Funktion um auf LoRaWAN Sensoren zu reagieren!

![overview.png](overview.png)

### Erste Schritte:
  - Herausfinden, wie die URL von eurem Python Server in GitPod lautet.
    - <details><summary>So geht's</summary><img src="templates/02_gitpod_url.png" alt="Screenshot of the GitPod Workspace's Ports tab"></details>
    - -> Die URL muss von uns in TTN eingetragen werden, ansonsten bekommt ihr keine Daten ;) 
  - Herausfinden, welche Daten in welchem Format bei euch ankommen 
    - Empfehlung: Nicht `print()`, sondern den Debugger nutzen ;)
    - [Beispiel aus der TTN Doku](https://www.thethingsindustries.com/docs/the-things-stack/concepts/data-formats/#uplink-messages)
  - Herausfinden, wie sich die Meross Steckdose steuern lässt.
    - Vielleicht gibt es hier im Repository eine hilfreiche Datei?
  - Entscheiden, wie euer Team mit den Inputdaten umgehen will.

**Hinweis**:
  - Bitte den 1-Sekunden Delay bei der Steckdose nicht umgehen, sonst sperrt uns ggf. Meross.

### Weitere Schritte:
  - Wie könnte man auf Trends und nicht nicht nur auf Schwellwerte reagieren?
  - Wie kann man garantieren, dass die Steckdose nach 10 Minuten wieder ausgeht? 
    - (Tipp: Mit `curl -X POST` im zweiten Terminal kann man die eigene API aufrufen)
  - Was könnte man [nütz](https://www.geeksforgeeks.org/how-to-add-graphs-to-flask-apps/)liches in der App anzeigen?

### Hilfreiche Links

- Python Flask
  - [Doku](https://flask.palletsprojects.com/en/3.0.x/)
- Meross Python Library
  - [Github Repo](https://github.com/albertogeniola/MerossIot)
  - [Doku](https://albertogeniola.github.io/MerossIot/)
- GitPod.io
  - [Dashboard](https://gitpod.io/workspaces)
  - [Doku zum Öffnen von Ports](https://www.gitpod.io/docs/configure/workspaces/ports)
- TheThingsNetwork: 
  - [Console](https://eu1.cloud.thethings.network/console/applications)
  - [Doku mit Uplink Beispiel](https://www.thethingsindustries.com/docs/the-things-stack/concepts/data-formats/#uplink-messages)

