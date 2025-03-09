# HA AtmoWEB Integration für Home Assistant

Diese Integration ermöglicht die Steuerung und Überwachung von Memmert-Geräten mit AtmoWEB-Schnittstelle in Home Assistant. Sie bietet Sensoren, Klimasteuerung und Schalter für verschiedene Gerätefunktionen.

## Funktionen

- **Sensoren**: Überwachung von Temperatur (`Temp1Read`) und Luftfeuchtigkeit (`HumRead`).
- **Klimasteuerung**: Anzeige der aktuellen Temperatur und Einstellung der Zieltemperatur (`TempSet`).
- **Schalter**: Steuerung der Türverriegelung (`DoorLock`) und des Signalhorns (`HornSet`).

## Voraussetzungen

- Home Assistant mit installiertem HACS (Home Assistant Community Store).
- Ein Memmert-Gerät mit aktiviertem AtmoWEB (siehe Handbuch, Abschnitt 2.3).
- Die IP-Adresse des Geräts im lokalen Netzwerk.

## Installation über HACS

1. **HACS installieren** (falls noch nicht geschehen):
   - Folgen Sie den Anweisungen unter [HACS-Dokumentation](https://hacs.xyz/docs/setup/download).

2. **Dieses Repository hinzufügen**:
   - Gehen Sie in Home Assistant zu **HACS > Integrationen**.
   - Klicken Sie auf die drei Punkte (oben rechts) und wählen Sie **Benutzerdefinierte Repositories**.
   - Geben Sie die URL dieses Repositories ein: `https://github.com/cyber5de/ha-atmoweb`.
   - Wählen Sie als Kategorie **Integration** aus und klicken Sie auf **Hinzufügen**.

3. **Integration installieren**:
   - Suchen Sie in HACS nach "HA AtmoWEB".
   - Klicken Sie auf **Installieren** und warten Sie, bis der Download abgeschlossen ist.

4. **Home Assistant neu starten**:
   - Gehen Sie zu **Einstellungen > System > Neustart** oder führen Sie `ha core restart` über die Kommandozeile aus.

5. **Integration konfigurieren**:
   - Gehen Sie zu **Einstellungen > Geräte & Dienste > Integration hinzufügen**.
   - Suchen Sie nach "HA AtmoWEB" und wählen Sie es aus.
   - Geben Sie die IP-Adresse Ihres Memmert-Geräts ein, wenn Sie dazu aufgefordert werden.

## Manuelle Installation (optional)

Falls Sie HACS nicht verwenden möchten:
1. Laden Sie den Ordner `custom_components/ha-atmoweb` aus diesem Repository herunter.
2. Kopieren Sie ihn in das Verzeichnis `custom_components/` Ihrer Home Assistant-Installation (z. B. `/config/custom_components/` unter Linux).
3. Starten Sie Home Assistant neu.
4. Fügen Sie die Integration über die Benutzeroberfläche hinzu (siehe oben).

## Konfiguration

Die Integration verwendet einen Konfigurationsfluss über die Home Assistant-Benutzeroberfläche. Geben Sie einfach die IP-Adresse Ihres Geräts ein, und die Integration testet die Verbindung automatisch.

## Unterstützte Entitäten

- **Temperatur-Sensor**: Zeigt die aktuelle Temperatur (`Temp1Read`) in °C an.
- **Luftfeuchtigkeits-Sensor**: Zeigt die aktuelle Luftfeuchtigkeit (`HumRead`) in % an.
- **Klimasteuerung**: Ermöglicht das Einstellen der Zieltemperatur (`TempSet`).
- **Schalter**:
  - **Türverriegelung**: Ein/Aus (`DoorLock`).
  - **Signalhorn**: Ein/Aus (`HornSet`).

## Fehlerbehebung

- **Verbindung fehlgeschlagen**: Stellen Sie sicher, dass die IP-Adresse korrekt ist und das Gerät im Netzwerk erreichbar ist. Überprüfen Sie auch, ob die Fernsteuerung aktiviert ist (siehe Memmert-Handbuch).
- **Keine Daten**: Prüfen Sie die Logs unter **Einstellungen > System > Protokolle**, um Fehlerdetails zu sehen.

## Beitrag

Falls Sie Verbesserungen vorschlagen oder Fehler melden möchten, erstellen Sie ein Issue unter: [https://github.com/cyber5de/ha-atmoweb/issues](https://github.com/cyber5de/ha-atmoweb/issues).

## Lizenz

Diese Integration steht unter der MIT-Lizenz (Details siehe `LICENSE`-Datei, falls vorhanden).

---

Vielen Dank, dass Sie HA AtmoWEB nutzen!
