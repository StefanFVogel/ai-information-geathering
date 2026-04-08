---
author: '[[Alex Sprogis]]'
channel_id: UC5Ns-Tc7anOZdf6FWGiM25A
date: '2026-03-26'
duration: 2548
language: de
relevance: '3'
source_type: youtube
status: processed
tags:
- ohne programmieren
- visualmakers
- Webdesign
- Automatisierung
- Datenbanken
- tech education
- education
- lowcode
- Appdesign
- '[ai]'
- nocode
title: 'GSD Framework für Claude Code: Version 1 & 2 im PRAXISTEST. Was ist besser?'
type: inbox
url: https://www.youtube.com/watch?v=dWXX0_gQujI
---

## Summary

*Ask Claude to summarize this transcript.*


📌 Links:
Mein AI Coding Starter Kit: https://link.alexsprogis.de/claude-code-starter-kit
(Einsteigerfreundliches Framework für professionelle Entwicklung)

Wispr Flow*: https://link.alexsprogis.de/wi

---

## Transcript

[00:00:00] Getchgit, dann ist wohl eins der
[00:00:01] beliebtesten Cloud Code Frameworks im
[00:00:03] Bereich AI Engineering der letzten
[00:00:04] Monate. Jetzt kam vor kurzem Gadget dann
[00:00:07] 2 heraus, aber nicht als neue Version
[00:00:09] des ursprünglichen Frameworks, sondern
[00:00:11] als eigene CLI Anwendung, also somit als
[00:00:14] Cloud Code Konkurrenzprodukt. Warum GSD
[00:00:16] so beliebt ist, wie die Versionen
[00:00:18] gegeneinander abschneiden, wo die
[00:00:19] Unterschiede liegen und was du zukünftig
[00:00:21] nutzen solltest, allkläre ich dir in
[00:00:23] diesem Video. Also lass uns direkt
[00:00:25] reinstarten. Also, warum ist GS
[00:00:27] eigentlich so beliebt und wieso macht es
[00:00:28] Sinn, solche Frameworks für AI
[00:00:30] Engineering, also Softwareentwicklung
[00:00:32] mit AI zu nutzen? Wenn du gerade noch am
[00:00:34] Anfang mit Softwareentwicklung und KI
[00:00:36] stehst, dann hast du wahrscheinlich
[00:00:37] schon von dem Begriff Vibecoding gehört
[00:00:39] und gegebenenfalls auch schon mal durch
[00:00:41] einfaches Prompting Anwendung mit Cloud
[00:00:42] Code oder anderen Applikationen wie
[00:00:44] Lovable und Cerstellt. Mit diesem
[00:00:46] Vorgehen kommt man auch recht schnell
[00:00:47] zum Ergebnis. Also, wenn ich jetzt
[00:00:48] deiner KI sage, bitte stelle mir ein
[00:00:50] Projektmanagement Tool, dann kann ich
[00:00:52] sehr stark davon ausgehen, dass ich
[00:00:53] innerhalb von ein paar Minuten ein
[00:00:54] vorzeigbares Ergebnis bekomme. Das
[00:00:56] Problem ist allerdings, dass dieses
[00:00:58] Vorgehen eben keinen professionellen
[00:01:00] Rahmen vorgibt, den es für echte
[00:01:01] Software Projekte eigentlich braucht.
[00:01:03] Das heißt, du wirst mit dieser
[00:01:04] Vorgehensweise früher oder später in
[00:01:06] diverse Probleme laufen. Das fängt damit
[00:01:08] an, dass du bei diesem Ansatz kein
[00:01:09] sinnvolles Kontextmanagement hast. Das
[00:01:11] heißt, früher oder später wird dein
[00:01:12] Coding Agent Dinge vergessen, was dazu
[00:01:14] führt, dass er deine Anforderung nicht
[00:01:16] so umsetzen wird, wie du sie dir
[00:01:17] vorstellt. Er wird höchstwahrscheinlich
[00:01:19] bestehende Funktionalitäten durch
[00:01:20] Änderung überschreiben und sie damit
[00:01:22] kaputt machen. Oder er wird wichtige
[00:01:23] Entscheidungen, die ihr getroffen habt,
[00:01:24] früher oder später nicht mehr
[00:01:25] berücksichtigen. Das liegt einfach an
[00:01:27] einem bekannten Phänomen, das sich
[00:01:29] Kontextrod nennt. Das heißt, je größer
[00:01:31] dein Projekt wird, je größer deine
[00:01:33] Codebase wird, desto stärker nimmt die
[00:01:35] Leistungsfähigkeit deines AI Coding
[00:01:37] Agents ab. Dein Coding Agent arbeitet
[00:01:39] während der gesamten Session mit einem
[00:01:40] Kontextfenster, was sozusagen sein
[00:01:42] Erinnerungsspeicher ist. Das könntest du
[00:01:43] dir mal als leeres Glas vorstellen und
[00:01:46] mit jeder Nachricht, die du schreibst,
[00:01:47] mit jeder Antwort, die dir dein Coding
[00:01:49] Agent formuliert, mit jedem Codefall,
[00:01:51] das erstellt oder bearbeitet, fühlt sich
[00:01:53] dieses Glas mit Wasser und irgendwann
[00:01:55] ist das Glas dann kurz vom Überlaufen.
[00:01:57] Was dein Coding Agent dann automatisch
[00:01:58] macht, ist einmal die Verdichtung dieses
[00:02:01] Kontextfensters. Das heißt, er stellt
[00:02:03] sich eine Zusammenfassung aus der
[00:02:04] gesamten Session Historie. Das Modell
[00:02:06] entscheidet dabei selber, welche Inhalte
[00:02:08] es als wichtig genug empfindet, damit
[00:02:10] sie in die Zusammenfassung aufgenommen
[00:02:12] werden. Alles andere, was dann vorher
[00:02:14] passiert ist, vergisst es. So. Und jetzt
[00:02:16] kann es eben sein, dass kleinere
[00:02:17] Entscheidungen, die ihr getroffen habt
[00:02:18] oder auch Detailinformationen durch
[00:02:20] diese Verdichtung verloren gehen. Und
[00:02:22] das führt dann eben zu einer spürbar
[00:02:24] schlechteren Performance des Coding
[00:02:25] Agents. Deswegen gibt es den Begriff
[00:02:27] Context Engineering. Das ist quasi die
[00:02:29] Art und Weise, wie du deinen Kontext
[00:02:30] verwaltest. Ich habe dazu sogar ein
[00:02:32] komplett eigenes Video gemacht, das
[00:02:33] verlinke ich dir mal hier an dieser
[00:02:34] Stelle. Für jetzt erstmal nur so viel.
[00:02:37] Die Regel Nummer 1 ist: Speichere dein
[00:02:39] Wissen niemals in dem Gedächtnis eines
[00:02:41] AI Coding Agents, sondern immer in
[00:02:44] Dateien. Cloud Code hat z.B. dafür sowas
[00:02:46] wie die cloud.md MD oder andere Formate
[00:02:48] wie Rules, Skills, Subagents oder auch
[00:02:51] projektbezogene Dokumente, die du dir
[00:02:52] erstellen kannst, wie ein PR, also ein
[00:02:54] Product Requirements Dokument, wo all
[00:02:56] deine Projektanforderungen, Visionen,
[00:02:58] Zielgruppe und so weiter drinne stehen.
[00:03:00] Das Ganze lässt sich auch noch ergänzen
[00:03:01] durch separate
[00:03:02] Featurespezifikationsfalls,
[00:03:04] wo dann User Stories, Akzeptanzkriterien
[00:03:06] und Testergebnisse dokumentiert sind,
[00:03:08] denn nur mit diesem Vorgehen behältst du
[00:03:10] selber als auch dein Coding Agent bei
[00:03:12] größer werdenden Projekten den
[00:03:13] Überblick. Ehrlicherweise geht man ganz
[00:03:16] genauso eben auch in normalen
[00:03:17] Softwarepjekten vor. Jetzt kann man sich
[00:03:19] so eine Struktur selbst erarbeiten. So
[00:03:20] habe ich das z.B. auch gemacht. Mein AI
[00:03:23] Coding Starter Kit ist im Prinzip
[00:03:24] genauso ein vorkonfiguriertes
[00:03:26] Projekttemplate speziell für
[00:03:27] Webanwendung mit Cloud Code. Da ist z.B.
[00:03:29] ein Set aus spezialisierten Skills und
[00:03:31] Agents enthalten, die quasi ein
[00:03:33] komplettes Death Team simulieren. Also
[00:03:35] vom Requirements Engineer, der die
[00:03:37] Anforderung erstellt bis hin zum
[00:03:38] Deathops Engineer, der am Ende deine
[00:03:40] Anwendung live bringt. Das kannst du dir
[00:03:42] übrigens auch kostenlos klonen. Den Link
[00:03:43] findest du einfach in der
[00:03:44] Videobeschreibung und mit dazu bekommst
[00:03:46] du eine komplette Setup und
[00:03:47] Bedienungsanleitung dazu. Das Ganze ist
[00:03:49] super einfach für Einsteiger im AI
[00:03:51] Engineering Bereich geeignet. Ich habe
[00:03:53] schon so viel positives Feedback von
[00:03:54] Nonis bekommen, die damit ihre ersten
[00:03:56] sicheren und skalibbaren Software
[00:03:58] Service Apps erstellt haben. Na ja, oder
[00:03:59] man nimmt eben sowas wie vorhandene
[00:04:01] Frameworks wie das Gadget Done
[00:04:02] Framework. Das geht noch mal einen
[00:04:03] Schritt weiter und liefert dir noch
[00:04:05] tiefergehende Prinzipien, Methoden und
[00:04:07] Workflows, damit du Softwarep Projekte
[00:04:09] strukturiert, professionell und eben
[00:04:11] auch vollständig dokumentiert angehst.
[00:04:13] Da gibt's gerade auch kein Entweder
[00:04:14] oder, also man muss das immer so
[00:04:15] bisschen von Projekt zu Projekt
[00:04:17] unterscheiden und auch schauen, wo
[00:04:18] liegen meine eigenen Kenntnisse, welche
[00:04:20] Anforderung habe ich jetzt z.B. an das
[00:04:22] Projekt und dann wählt man eben das
[00:04:24] passende Framework dazu. Gadget dann ist
[00:04:26] im Kern also ein Context Engineering
[00:04:28] System. Es nimmt dein Projekt und
[00:04:30] zerlegt es in kleine atomare Aufgaben
[00:04:32] und jede Aufgabe bekommt einen eigenen
[00:04:34] frischen Kontext. Das ist sozusagen auch
[00:04:36] die Grundregel bei GSD, die besagt, dass
[00:04:39] jeder Task in einen Kontextfenster
[00:04:41] passen muss. Wie groß die Kontextfenster
[00:04:43] sind, das hängt natürlich immer davon
[00:04:44] ab, welches Modell du gerade verwendest.
[00:04:46] Cloud hat jetzt z.B. das Kontextfenster
[00:04:48] von 200.000 1000 Token auf eine Million
[00:04:50] Token angehoben. Das heißt, das Problem
[00:04:52] mit dem Context Rod wird also Stück für
[00:04:54] Stück reduziert. Nichtsdestotrotz wird
[00:04:56] Context Engineering auf absehbare Zeit
[00:04:58] weiterhin wichtig bleiben. GSD verfolgt
[00:05:00] außerdem einen Spectriven Ansatz. Das
[00:05:02] heißt, bevor man in die Entwicklung
[00:05:04] startet, werden erstmal alle
[00:05:06] Anforderungen für das Projekt
[00:05:07] spezifiziert. Das ist gerade beim AI
[00:05:08] Engineering super wichtig, denn nur wenn
[00:05:11] der Agent vorab genau weiß, was er
[00:05:12] entwickeln soll, stimmt am Ende auch die
[00:05:14] Outbookqualität. und das muss eben in
[00:05:16] einem entsprechenden Detailgrad
[00:05:17] festgehalten werden. Außerdem ist GSD
[00:05:19] Stack agnostisch. Das heißt, egal ob du
[00:05:21] Webanwendung, Mobile Apps oder Desktop
[00:05:23] Anwendung entwickeln möchtest, für all
[00:05:25] diese Usases eignet sich das Framework.
[00:05:27] GSD enthält diverse vorkonfigurierte
[00:05:29] Slash Commons, Agents und
[00:05:31] Planungsdateien und einen eigenen
[00:05:34] Entwicklungsworkflow. Einfach gesagt ist
[00:05:36] der unterteilt in die Phasen Research,
[00:05:38] Plan, Execute und Verify. Lass uns das
[00:05:41] mal ganz kurz durchgehen, damit du
[00:05:42] verstehst, was in welcher Phase
[00:05:44] passiert. Also in der Researchphase
[00:05:45] sammelt GSD erstmal Information. Das
[00:05:47] heißt, er startet mehrere Agents
[00:05:49] parallel, die sich das Projekt aus
[00:05:51] mehreren Sichten anschauen. Das heißt,
[00:05:53] einer recherchiert den Textdeck, einer
[00:05:54] schaut sich die Best Practices an und
[00:05:56] einer prüft die potenziellen Fallsticke.
[00:05:58] Und jeder dieser Agenten arbeitet in
[00:06:00] seinem eigenen frischen Kontextfenster.
[00:06:02] Am Ende werden die Ergebnisse dann
[00:06:04] zusammengefasst und in einer
[00:06:05] Researchdatei dokumentiert. Das ist dann
[00:06:08] quasi die Grundlage für alle
[00:06:09] Entscheidungen, die danach getroffen
[00:06:10] werden. Danach geht's dann in die
[00:06:12] Planphase und hier wird's jetzt spannt,
[00:06:13] weil GSD nicht nur einen einzigen
[00:06:15] Agenten nutzt, der den Plan schreibt,
[00:06:17] sondern auch einen zweiten, der den Plan
[00:06:18] aktiv hinterfragt, um Schwachstellen
[00:06:20] aufzudecken und erst wenn beide Agents
[00:06:22] am Ende zufrieden sind, wird der Plan
[00:06:24] dann finalisiert. Die Aufgaben werden
[00:06:26] dabei in Waves gruppiert. Das heißt,
[00:06:28] somit kann dann alles, was unabhängig
[00:06:30] voneinander ist, später parallel
[00:06:32] ausgeführt werden. In der Execute Phase
[00:06:34] wird dann tatsächlich der Code
[00:06:35] produziert und auch hier gilt jetzt
[00:06:37] wieder jede Aufgabe bekommt einen
[00:06:38] eigenen Subagenten mit frischem
[00:06:40] Kontextfenster. Der Subagent bekommt
[00:06:42] dann eben genau den Plan, der für den
[00:06:44] Kontext und für seine Aufgabe wichtig
[00:06:46] ist. Am Ende jeder Aufgabe wird dann
[00:06:48] automatisch ein Gitcomit erstellt. Und
[00:06:50] zum Schluss gibt's dann noch die Verifyp
[00:06:51] Phase. Da prüft GSD, ob die Ergebnisse
[00:06:53] dann tatsächlich auch den Anforderung
[00:06:55] entsprechen. Das heißt, es werden Tests
[00:06:57] ausgeführt. Der Output wird quasi gegen
[00:06:59] den ursprünglichen Plan geprüft und du
[00:07:00] bekommst eine Zusammenfassung, was
[00:07:02] gebaut wurde und wie du das dann selber
[00:07:04] eben auch noch verifizieren kannst. So
[00:07:06] und dieser Zyklus, der wiederholt sich
[00:07:08] jetzt Phase für Phase, bis das ganze
[00:07:10] Projekt steht. Jetzt gibt es neuerdings
[00:07:12] zwei Versionen von GSD. Das ist einmal
[00:07:15] Version 1 als quasi reines Prompt
[00:07:17] Framework, das in Cloud Code lebt.
[00:07:19] Sprich, was du letztendlich bei dir
[00:07:21] lokal installierst, ist am Ende eine
[00:07:23] Projektstruktur, die GSD mitbringt.
[00:07:24] Letztendlich, wenn man es genau nehmen
[00:07:25] will, besteht sie eigentlich nur aus
[00:07:27] verschiedenen Markdown Dateien. Das
[00:07:29] heißt, die Magie dahinter ist erstmal
[00:07:30] nur eine reine Arbeitsanleitung für
[00:07:32] deinen Cloud Code Agent. Mehr mehr ist
[00:07:34] es eigentlich nicht. Das heißt jetzt
[00:07:35] aber natürlich nicht, dass es was
[00:07:36] schlechtes wäre, sogar im Gegenteil. Es
[00:07:38] ist sogar ziemlich gut, weil damit ist
[00:07:40] es an sich keine Blackbox. Du weißt ganz
[00:07:42] genau, welche Instruktionen Cloud von
[00:07:44] dem Framework bekommt, um dann eben
[00:07:46] strukturiert zu funktionieren. Das gibt
[00:07:48] dir auch die Möglichkeit, das Framework
[00:07:50] auf deine eigenen Bedürfnisse
[00:07:51] anzupassen. Version 2 ist jetzt eine
[00:07:53] komplett eigenständige CLI Anwendung,
[00:07:55] die nicht mehr in Cloud lebt, sondern
[00:07:57] ein eigenes Konkurrenzprodukt geworden
[00:07:59] ist. Und zwar sind die Entwickler von
[00:08:00] GSD der Meinung, dass das vorherige
[00:08:02] Framework zwar gut funktioniert hat,
[00:08:04] aber man eben sich darauf verlassen
[00:08:05] musste, dass der Cloud Agent die
[00:08:07] Instruktion in den Dateien tatsächlich
[00:08:09] auch in der Tiefe liest und auch so
[00:08:12] wirklich anwendet. Sie konnen dafür aber
[00:08:13] natürlich keine Garantie geben. Und um
[00:08:15] eben hier sicherzugehen, dass das
[00:08:17] genauso passiert und auch um die
[00:08:18] Qualität noch mal weiter zu erhöhen,
[00:08:20] haben sie sich dann entschieden, ihre
[00:08:21] eigene CLI Anwendung zu entwickeln.
[00:08:23] Beide Versionen lösen im Kern das
[00:08:24] gleiche Problem, aber eben teilweise auf
[00:08:26] sehr unterschiedliche Arten und Weisen.
[00:08:28] Und genau das wollen wir uns gleich mal
[00:08:29] anhand eines Beispielprojekts anschauen.
[00:08:31] Wenn dir das Video bis hierhin gefällt,
[00:08:32] dann würde ich mich sehr darüber freuen,
[00:08:34] wenn du ein Abo da lässt, denn aktuell
[00:08:36] haben knapp 90% der Zuschauer den Kanal
[00:08:38] noch nicht abonniert und mit diesem
[00:08:39] einen Klick würdest du mir extrem
[00:08:41] helfen. Also, vielen Dank und weiter
[00:08:43] geht's. So, ich habe hier schon mal das
[00:08:44] Repository geöffnet. Den Link findest du
[00:08:46] eben auch in der Videobeschreibung und
[00:08:49] hier findest du auch alles, was du
[00:08:50] wissen musst, wie du mit dem Framework
[00:08:52] arbeitest. Ich kopiere mir schon mal den
[00:08:54] Befehl zur Installation. Das machen wir
[00:08:55] gleich gemeinsam. Und ansonsten, was ich
[00:08:58] dir hier noch mal zeigen wollte, ist
[00:08:59] auch noch mal die Anleitung, wie das
[00:09:00] Ganze funktioniert von Initialisierung,
[00:09:02] Discuss Face, Plan Face, Execute Face
[00:09:06] und dann Verify Work. Das sind die
[00:09:08] unterschiedlichen Phasen und ähm genau
[00:09:10] das gucken wir uns gleich an, wie das
[00:09:11] dann tatsächlich auch funktioniert. Also
[00:09:13] lass uns mal rüb springen in die
[00:09:15] Entwicklungsumgebung und es einmal
[00:09:16] installieren. So, wenn du mein Setup
[00:09:18] schon gesehen hast, dann weißt du, ich
[00:09:19] arbeite gerne in VS Code, also einer
[00:09:22] kostenlosen IDE von Microsoft und dann
[00:09:25] eben auch gerne mit der Cloud Code
[00:09:27] Extension, um hier den Chat visuell zu
[00:09:29] haben. Also für die Installation
[00:09:31] brauchen wir einmal ein neues Terminal.
[00:09:33] Das öffne ich einmal, dann mache ich mir
[00:09:35] das ein bisschen größer und dann haue
[00:09:36] ich einmal den Befehl rein zur
[00:09:38] Installation.
[00:09:40] Und da sehen wir jetzt direkt, wir
[00:09:42] können einmal den Coding Agent
[00:09:44] auswählen, für den wir das installieren
[00:09:46] wollen. Ich wähle jetzt hier einfach mal
[00:09:48] die ein für Cloud Code. Dann haben wir
[00:09:50] die Wahl zwischen einer globalen
[00:09:52] Installation oder einer lokalen
[00:09:53] Installation. Das heißt, einmal kann man
[00:09:55] das Projekt übergreifen, installieren
[00:09:56] oder eben auch nur für dieses
[00:09:58] spezifische Projekt. Ich mache das jetzt
[00:09:59] mal nur für dieses Projekt und dann
[00:10:02] zeigt es uns erstmal alles an, was es
[00:10:04] installiert hat und wir können
[00:10:05] eigentlich direkt loslegen. Wir können
[00:10:06] das Ganze dann starten über GSD, dann
[00:10:09] sind wir direkt in der Umgebung drinne
[00:10:10] und können es jetzt über die
[00:10:12] verschiedenen Commands aufrufen oder wir
[00:10:14] können das Ganze jetzt eben auch über
[00:10:16] den Cloud Code Agent bedienen. Dafür
[00:10:17] lade ich jetzt einmal die Umgebung hier
[00:10:19] neu. Dann kann ich das Terminal
[00:10:21] eigentlich schließen und habe dann hier
[00:10:23] alle Befehle sichtbar. Genau. Also GSD
[00:10:28] und wir geben hier mal an New Project
[00:10:30] und starten mal den Workflow. So, was er
[00:10:33] jetzt hier einmal macht, ist er wird mir
[00:10:34] gleich Fragen stellen, um zu verstehen,
[00:10:36] was ich denn gerne bauen möchte. Wir
[00:10:38] können uns hier parallel auch schon mal
[00:10:39] die Struktur anschauen, die das
[00:10:41] Framework mitbringt. Also, wir haben
[00:10:42] hier die unterschiedlichsten Agents, die
[00:10:44] hier vorkonfiguriert sind. Wir haben die
[00:10:47] unterschiedlichsten Commands, wo wir
[00:10:49] jetzt auch gerade den Initialize Project
[00:10:52] oder New Project Workflow gestartet
[00:10:55] haben. Dann noch weitere Templates,
[00:10:58] Kommandos und Konfiguration und das ist
[00:11:00] es eigentlich schon. Und jetzt wie
[00:11:02] gesagt fragt mich der Agent hier, was
[00:11:04] ich gerne bauen möchte. Und ich sage
[00:11:06] jetzt hier einfach mal bitte ein
[00:11:08] einfaches Projektmanagement Tool mit
[00:11:10] Canban Board. Lokale Speicherung. Es
[00:11:12] gibt kein eigenes Backend, das ist rein
[00:11:15] für einen Test. So, jetzt geht's hier
[00:11:16] weiter. Die Frage ist jetzt, welche
[00:11:18] Technologie für das Front-End verwendet
[00:11:19] wird. Ich will jetzt hier mal React,
[00:11:22] dann welches kann man bzw. welche kann
[00:11:24] man Spalten brauchst du? Nehmen wir
[00:11:26] einfach mal die Standardspalten und
[00:11:28] sollen die Karten per Drag and Job
[00:11:29] verschoben werden? Jep, jetzt gibt es
[00:11:31] weitere Fragen, die ich hier beantworten
[00:11:33] kann. So, wählen wir das mal und Tailwin
[00:11:36] CSS. Weiter geht's. Genau, jetzt sagt es
[00:11:39] mir auch, ich habe genug Kontext. Soll
[00:11:40] ich die Project MD erstellen und kann
[00:11:43] jetzt hier aktiv auswählen? Bitte legt
[00:11:45] das Projektfeile an. Und das ist hier so
[00:11:48] ein bisschen natürlich diese Human in
[00:11:49] the Loop Funktion. Äh die V1 wird mich
[00:11:51] immer wieder Fragen zugegebener Zeit ähm
[00:11:54] und bitten Sachen zu reviewen, mir
[00:11:55] anzuschauen oder ich kann auch noch mal
[00:11:57] tiefer reingehen in Themen und noch mal
[00:11:59] in die Diskussion mit ihm gehen.
[00:12:02] Jetzt fragt es mich auch noch mal in
[00:12:03] welchem Modus ich arbeiten möchte. Im
[00:12:06] Yolomodus, also Auto approve und einfach
[00:12:08] ausführen. Das heißt, es wird mich hier
[00:12:09] gar nicht weiter fragen. Dann haben wir
[00:12:11] noch die Granularität. Also wie fallen
[00:12:13] soll der Scope in Phasen aufgeteilt
[00:12:16] sein? Das heißt wenig und breite Phasen,
[00:12:18] das heißt drei bis fünf Phasen mit ein
[00:12:20] bis drei Plan je Phase Standard, also
[00:12:23] ausgewogene Phasengröße und so weiter.
[00:12:25] Das heißt, ich kann hier noch mal geben
[00:12:26] mit ihm ihm mitgeben, wie sehr soll er
[00:12:28] hier ins Detail gehen und wie soll er
[00:12:30] das aufteilen. Ich sage jetzt mal wenige
[00:12:32] Breite Phasen. So, auch noch mal wie die
[00:12:34] Ausführung stattfinden soll, ob parallel
[00:12:36] oder sequentiell. Ich möchte gerne
[00:12:38] parallel, damit wir schneller zum Ziel
[00:12:40] kommen und Planning Dogs in
[00:12:42] Gitcommitten. Ja, das macht Sinn, dass
[00:12:43] wir regelmäßig eben Speicherstände
[00:12:45] erstellen, damit das, falls das System
[00:12:47] hier Fehler macht, wir immer wieder zu
[00:12:49] einem alten Stand zurückkommen können.
[00:12:50] So, Research vor jeder Phase
[00:12:52] recherchieren kostet Token und Zeit. Das
[00:12:55] ja, machen wir einfach mal. Plan, check.
[00:12:58] Pläne auf Zielerreichung prüfen. Ja, auf
[00:13:00] jeden Fall. Das System soll selber
[00:13:02] prüfen, ob es eine Ziele erreicht hat.
[00:13:04] Nach jeder Phase prüf Requirements
[00:13:05] erfüllt. Auch das wähle ich einmal an.
[00:13:08] Und dann können wir noch sagen AI
[00:13:09] Models. Welche AI Modelle für die
[00:13:12] Planning Agents? Balance, dann würde
[00:13:14] Sonet wählen für Qualität, dann Opus für
[00:13:17] Budget, HikuQu und so weiter. Da wähle
[00:13:20] ich jetzt einfach mal hier balanced aus
[00:13:22] bei recommended. Also, du siehst hier
[00:13:24] schon, wenn du bisher nur den Cloud Code
[00:13:26] Agent an sich kennst, das System
[00:13:28] versucht hier schon mal so ein bisschen
[00:13:30] die Basisarbeit zu machen, schon mal so
[00:13:32] ein bisschen den Arbeitsmodus auch zu
[00:13:34] finden, wie es dann hier gleich dann
[00:13:36] auch entwickeln wird. hat es mir hier
[00:13:38] quasi den Plan erstellt und zwar zeigt
[00:13:41] es mir hier die verschiedenen Phasen an.
[00:13:43] Wir haben scheinbar die Phase Board, wo
[00:13:46] das grundsätzliche Kanmanboard hier
[00:13:48] erstmal aufgesetzt wird, dann die Phase
[00:13:50] für Cards. Das heißt, hier haben wir die
[00:13:53] unterschiedlichen Aufgaben für die
[00:13:55] einzelnen Karten, die dann auf die die
[00:13:57] Tasks sozusagen, die auf dem
[00:13:59] Projektboard platziert sind und für die
[00:14:01] Persistance, also die Datenspeicherung.
[00:14:03] Und jetzt kann ich ih mitgeben, passt so
[00:14:05] und damit den Plan freigeben. Lass uns
[00:14:08] mal schauen, wie er das Ganze hier
[00:14:09] aufgesetzt hat. Wir finden hier also die
[00:14:12] projects.m
[00:14:14] und da finden wir eben alles drinne, was
[00:14:16] er mich hier gerade abgefragt hat. Dazu
[00:14:19] schreibt er sich jetzt selber die
[00:14:21] requirements.m.
[00:14:23] Da finden wir jetzt hier die
[00:14:25] verschiedenen Anforderungen und als
[00:14:28] nächstes kommt hier die Roadmap. So,
[00:14:30] jetzt sehen wir hier auch die Phasen,
[00:14:33] die er mir aufgelistet hat. Ich lass mir
[00:14:34] das hier mal kurz in der Vorschau
[00:14:35] anzeigen. Und zwar plant er gerade mit
[00:14:38] drei Phasen und setzt hier die erste
[00:14:40] Aufgabe in Phase 1 um. Dann hat er sich
[00:14:42] zwei Aufgaben für Phase 2 ausgesucht und
[00:14:45] noch zwei Aufgaben für Phase 3. Jetzt
[00:14:48] hat er auch die Roadmap fertig. Die
[00:14:51] können wir uns jetzt auch einmal
[00:14:52] anschauen.
[00:14:54] Da zeigt uns jetzt nämlich ganz genau,
[00:14:56] wie er vorgehen würde. Hat ja auch noch
[00:14:57] mal die Details zu den einzelnen Phasen
[00:14:59] aufgelistet und das können wir jetzt
[00:15:02] einmal freigeben.
[00:15:04] So, nachdem wir jetzt hier die
[00:15:05] Initialisierungsphase abgeschlossen
[00:15:07] haben, schlägt uns auch direkt vor, wie
[00:15:09] es direkt weitergeht. Also, wir können
[00:15:10] jetzt direkt mit der Discuss Phase
[00:15:12] starten. Das heißt, wir können noch mal
[00:15:14] mit ihm in die Diskussion gehen, noch
[00:15:16] mal über Anforderung sprechen, auch noch
[00:15:18] mal die bereits erstellten Dokumente,
[00:15:20] noch mal Fetune oder wir können direkt
[00:15:23] in die Planphase übergehen. Das heißt,
[00:15:25] da recherchiert er schon mal so ein
[00:15:27] bisschen die Umsetzung, plant die
[00:15:29] Umsetzung, bevor es dann später in die
[00:15:31] Initialisierung geht. Und genau das
[00:15:32] können wir jetzt eben über die
[00:15:33] verschiedenen Befehle hier ausführen.
[00:15:34] Sagen wir z.B., Wir wollen in die
[00:15:36] Discuss face, dann können wir hier
[00:15:38] einfach die Discuss Face starten und
[00:15:40] dann führt er uns durch den Prozess.
[00:15:42] Gleich ist aber natürlich auch für die
[00:15:44] Plan phase, die im Anschluss kommt oder
[00:15:47] natürlich auch für die darauffolgende
[00:15:49] Phase, die Execute Phase, wo er dann
[00:15:51] eben mit der Implementierung startet.
[00:15:53] Das heißt, er würde dann sozusagen, wie
[00:15:55] vorhin schon erwähnt, verschiedene Waves
[00:15:57] starten. Das heißt, also verschiedene
[00:15:59] Agents losschicken, die die parallele
[00:16:01] Umsetzung vornehmen und den Code dann
[00:16:04] produzieren.
[00:16:05] Zum Schluss gibt's dann noch die Verify
[00:16:08] Phase und da können wir dann eben noch
[00:16:10] mal ja das Ergebnis von verschiedenen
[00:16:13] Agents prüfen lassen und auch schauen,
[00:16:15] sind die Ziele, die wir uns gesetzt
[00:16:17] haben, erreicht, sind die Anforderungen,
[00:16:18] die wir erstellt haben, erfüllt und das
[00:16:20] Projekt oder die jeweilige Phase
[00:16:22] abgeschlossen.
[00:16:24] Ich kürze das an dieser Stelle mal ein
[00:16:25] bisschen ab, weil der Prozess an sich
[00:16:26] schon recht lange dauert. Also vor allen
[00:16:28] Dingen natürlich erstmal den richtigen
[00:16:29] Rahmen zu schaffen. Das dauert ein
[00:16:31] bisschen an Zeit, man muss auch einiges
[00:16:32] an Input geben, aber man hat dann eben
[00:16:35] auch eine sehr sehr gute Basis und alles
[00:16:37] ist eben dokumentiert, damit man dann
[00:16:39] eben auch eine entsprechende
[00:16:40] Outputqualität erwarten kann. Ich habe
[00:16:42] jetzt einen kleinen Case vorbereitet, äh
[00:16:44] wo wir jetzt einmal direkt reinschauen
[00:16:46] werden. Und zwar habe ich ein ein
[00:16:48] zumindest teilweise funktionierendes
[00:16:50] Incident Management Tool mit GSD V1
[00:16:53] erstellen lassen. Das heißt, in dem
[00:16:55] Szenario sind wir sozusagen ein SAS
[00:16:57] Unternehmen, ein Software ist
[00:16:57] Serviceunternehmen und haben ein
[00:16:59] Incident Management entwickelt. Das
[00:17:01] heißt, immer wenn Probleme auflaufen,
[00:17:03] werden Tickets erstellt und die landen
[00:17:05] bei uns in unserem Incident Management
[00:17:07] System. Und da in das Projekt will ich
[00:17:08] mal kurz mit dir reinschauen. Beide
[00:17:11] Versionen haben von mir übrigens das
[00:17:12] gleiche Briefing bekommen. Das heißt,
[00:17:14] beide Versionen sind auf Basis dieses
[00:17:16] Dokuments erstellt worden, wo ich
[00:17:18] einfach einen Überblick über die
[00:17:20] Applikation, die ich haben wollte,
[00:17:21] gegeben habe mit Hintergrund und
[00:17:23] Problem, mit Zielgruppe und Nutzer,
[00:17:25] betroffene Systeme, funktionale
[00:17:27] Anforderungen und so weiter. Also das
[00:17:29] ist sozusagen hier mein PRD, also mein
[00:17:31] Product requirements Document, was beide
[00:17:33] bekommen haben und auf dessen Basis
[00:17:35] jetzt gearbeitet haben. Ansonsten habe
[00:17:38] ich nichts weiter ergänzt an
[00:17:39] Kommentaren. Ich habe quasi nur die
[00:17:41] Fragen beantwortet, die sie mir gestellt
[00:17:42] haben. Das waren aber im Grunde genommen
[00:17:44] zu 80% die gleichen Fragen, die beide
[00:17:46] Frameworks gefragt haben. Genau. Von dem
[00:17:50] her ist das schon sehr vergleichbar. So,
[00:17:52] damit du dann jetzt mal auch ein Gefühl
[00:17:54] dafür bekommst, welche Dokumente und in
[00:17:55] welchem Umfang vor allen Dingen auch
[00:17:57] erstellt werden, habe ich mal das
[00:17:58] Projekt geöffnet. Ich habe das jetzt mal
[00:18:00] einfach so zur Hälfte durchentwickelt
[00:18:02] und was wir hier sehen können, ist
[00:18:03] natürlich die gleiche die gleiche
[00:18:05] Struktur, die wir eben auch schon in
[00:18:07] unserem Beispielprojekt gesehen haben.
[00:18:08] Das heißt, es gibt hier die Project MD
[00:18:10] requirements, Roadmap State, wo alles
[00:18:12] eben festgehalten wird. Und dann gibt es
[00:18:14] für die verschiedenen Phasen, äh ich
[00:18:16] habe jetzt hier mal zwei Phasen
[00:18:17] durchlaufen lassen. Einmal die
[00:18:18] Foundation und Coreincident Board, gibt
[00:18:21] es wiederum eigene Dokumente. Das heißt,
[00:18:23] auch hier gibt es noch mal wieder eigene
[00:18:26] Pläne, die das ganze System erstellt,
[00:18:28] eine Zusammenfassung. Außerdem gibt es
[00:18:30] Kontextdateien, Decision Logs, also hier
[00:18:32] wird auch jede kleinste
[00:18:34] Architekturentscheidung, die ähm gefällt
[00:18:37] wird, wird hier dokumentiert und
[00:18:39] festgehalten. Genauso wie Research
[00:18:41] Ergebnisse, Validierung der bestehenden
[00:18:44] Geschichten, Verifikation etc. Das wird
[00:18:47] eben alles hier dokumentiert. Jetzt
[00:18:50] natürlich noch die spannende Frage: Wie
[00:18:51] sieht denn eigentlich das Ergebnis aus?
[00:18:53] So schaut das Ganze aktuell aus. Wir
[00:18:55] haben ein Dashboard mit Kennzahlen. Wir
[00:18:58] haben eine Inzidentübersicht. Wenn ich
[00:19:00] jetzt hier auch mal einen Inzident
[00:19:02] anklicke, dann bekomme ich hier die
[00:19:04] Details. Und was haben wir noch? Wir
[00:19:07] haben die Funktion einen neuen Inzident
[00:19:09] anzulegen. So, das kann ich natürlich
[00:19:11] hier auch machen. Optisch ist das Ganze,
[00:19:13] na ja, sagen wir mal so, es funktioniert
[00:19:15] zumindest, aber es reißt ein jetzt nicht
[00:19:18] vom Hock ab. Wenn wir das gleich mal mit
[00:19:19] dem V2 Ergebnis vergleichen, dann werden
[00:19:22] wir sehen, dass die V2 da visuell
[00:19:23] deutlich ansprechender geworden ist.
[00:19:25] Aber und das ist mir noch mal wichtig zu
[00:19:27] erwähnen, davon sollte man sich jetzt
[00:19:28] nicht abschrecken lassen. Die UI ist ja
[00:19:30] im Prinzip das einfachste, was man im
[00:19:31] Nachgang verbessern kann. Ich habe zudem
[00:19:33] jetzt ehrlicherweise auch keine
[00:19:35] besonderen Vorgaben für das Projekt
[00:19:36] gemacht. Man kann also das Ganze einfach
[00:19:38] mit ein paar Prompts zum Styling
[00:19:40] verbessern, vielleicht noch eine
[00:19:41] Component Library mit einbinden. Was
[00:19:43] wirklich zählt, ist das, was dahinter
[00:19:44] liegt und zwar natürlich einmal die
[00:19:46] Projektstruktur, die Anwendungslogik,
[00:19:48] das Datenmodell und die ganzen Planning
[00:19:50] Dokumente. Und da hat die V1 solide
[00:19:53] abgeliefert. So, jetzt noch ein Teil,
[00:19:55] der mich persönlich sehr beeindruckt hat
[00:19:57] und zwar hat GSD einen Workflow, um
[00:19:59] bestehende Codebases, also Brownfield
[00:20:01] Projekte zu analysieren. Und das ist für
[00:20:03] mich jetzt ein Case, den gerade
[00:20:05] vielleicht noch viel übersehen, weil es
[00:20:06] geht ja nicht immer nur darum,
[00:20:07] Greenfield Projekte zu bauen. In der
[00:20:09] Realität sitzen die meisten Unternehmen
[00:20:11] ja auf Bestandssoftware, die keiner so
[00:20:13] richtig versteht. Die wurden vielleicht
[00:20:14] mal irgendwann in der Vergangenheit von
[00:20:16] einem Entwickler oder einer Entwicklerin
[00:20:18] gebaut und die sind mittlerweile aber in
[00:20:19] Rente oder bei einem anderen Unternehmen
[00:20:21] und jetzt wird das Ganze irgendwie noch
[00:20:23] betrieben. Man ist aber schon bisschen
[00:20:24] nervös, weil wenn da jetzt ein Fehler
[00:20:26] auftritt, dann weiß man nicht ganz
[00:20:27] genau, wie man den beheben kann. Und um
[00:20:30] so eine Software zu analysieren, braucht
[00:20:31] es ja normalerweise Wochen. Jedenfalls,
[00:20:34] wenn es auch keine passende
[00:20:35] Dokumentation dazu gibt. Das ist ja
[00:20:36] häufig auch der Fall, dass äh ja
[00:20:39] Softwareentwickler dokumentationsfaul
[00:20:41] sind. Ich schließe mich da auf gar
[00:20:42] keinen Fall von aus. Für mich ist das
[00:20:44] auch eher eine lästige Arbeit und umso
[00:20:46] schöner ist es jetzt, dass GSD einen
[00:20:48] genau dabei unterstützt. Die V1 hat
[00:20:50] nämlich eine Funktion, die sich Map
[00:20:52] Codebase nennt. Die offizielle
[00:20:54] Empfehlung ist quasi, wenn man bereits
[00:20:55] einen bestehenden Code hat in einem
[00:20:58] Projekt und GSD dort reinstalliert, dann
[00:21:00] ist das erste, was man einmal macht,
[00:21:02] diese Map Codebase Funktion auszuführen.
[00:21:04] Und was dann passiert, das ist ziemlich
[00:21:05] beeindruckend. Und zwar startet GSD dann
[00:21:08] vier parallele Mapperagenten und jeder
[00:21:11] analysiert eine andere Dimension deiner
[00:21:13] Codebase. Das heißt, der eine schaut
[00:21:14] sich den Stack an, der andere die
[00:21:15] Architektur, dann die Coding Conventions
[00:21:17] und einer schaut sich bekannte
[00:21:19] Problemstellung an. So, also sogenannte
[00:21:21] Concerns. Und jeder dieser Agenten
[00:21:23] arbeitet wieder mit einem frischen
[00:21:25] Kontextfenster. So, nach dieser Analyse
[00:21:27] hast du jetzt sieben fokussierte
[00:21:29] Dokumente in dem Planning Ordner. Und
[00:21:31] zwar ist das einmal die Stack MD,
[00:21:34] Architecture MD, Structure MD,
[00:21:35] Conventions MD, Testing MD, Integrations
[00:21:37] MD und Concerns. Sprich, du hast danach
[00:21:40] eine vollständige strukturierte
[00:21:42] Dokumentation deiner Codebase und die
[00:21:44] Artefakte werden dann auch automatisch
[00:21:46] in die Planphase geladen, wenn du von da
[00:21:49] aus dann weitermachst. Das heißt, jede
[00:21:51] neue Phase weiß dann, was in der
[00:21:53] Codebase bereits existiert und wie sie
[00:21:55] genau gebaut worden ist. Ich habe mir
[00:21:57] hier mal für meinen Test ein altes
[00:21:59] Legacy Projekt rausgesucht und zwar ist
[00:22:01] das ein alter Fußballmanager. Der eignet
[00:22:04] sich sehr gut für diese Analyse, weil
[00:22:06] das Projekt recht umfangreich ist und
[00:22:08] der der Code ist ungefähr so 2003 rum
[00:22:11] entstanden, wurde immer noch ein
[00:22:12] bisschen weiterentwickelt, aber
[00:22:13] grundsätzlich ist hier erstmal ein recht
[00:22:15] alter Technologiestack auch vorhanden,
[00:22:17] was das natürlich auch extrem spannend
[00:22:19] macht. So, das Ganze habe ich mir jetzt
[00:22:21] einfach mal runtergezogen oder geklont
[00:22:23] und mal die Analyse laufen lassen vom
[00:22:25] GSD Framework.
[00:22:27] So, ich habe jetzt hier das ganze
[00:22:29] Projekt mir einmal gezogen, wie gesagt,
[00:22:32] und einmal die Map Codebase Funktion
[00:22:34] ausgeführt. Also auch wieder hier
[00:22:36] einfach über den Slash Command
[00:22:39] Map Codebase ausgeführt und die Analyse
[00:22:42] laufen lassen. Dann wie gesagt startet
[00:22:44] GSD hier verschiedene Subagents, die das
[00:22:46] ganze Projekt dann einmal analysieren
[00:22:48] aus den verschiedenen Sichten. So und
[00:22:50] dann legt es uns die Ergebnisse hier in
[00:22:52] den Planning Ordner in den Ordner
[00:22:54] Codebase und da gibt es jetzt eben die
[00:22:56] komplette Dokumentation über das
[00:22:59] Bestandsprojekt und ich möchte mit dir
[00:23:01] mal in ein paar Sachen reinschauen.
[00:23:02] Gucken wir z.B. mal auf das Architecture
[00:23:04] File. Ich öffne mal hier die Vorausschau
[00:23:06] und da sieht man eben genau, was das
[00:23:10] Ganze hier eigentlich ist, worauf es
[00:23:11] basiert, die verschiedenen Layer, die es
[00:23:14] hier gibt in dem Projekt. Und wie du
[00:23:17] siehst, genau ist das recht umfassend.
[00:23:19] Wir haben den Datenflow, äh Key
[00:23:21] Abstractions,
[00:23:23] Entry Points, also alles rund um die
[00:23:25] Architektur. Wenn wir uns mal die
[00:23:27] Concerns angucken, das finde ich immer
[00:23:29] extrem spannend, dann sehen wir hier auf
[00:23:31] jeden Fall, es gibt eine gewisse Tag
[00:23:33] Dept, also technische Schulden
[00:23:35] sozusagen. Wir haben hier so eine Liste
[00:23:38] mit all dem, was die Agents so gefunden
[00:23:40] haben, bekannte Bugs, die es gibt,
[00:23:43] Security Considerations, auch das also
[00:23:46] alles dokumentiert. Was haben wir noch
[00:23:49] hier? Vielleicht noch mal den Text, den
[00:23:51] wir uns anschauen können. Da sehen wir
[00:23:54] noch mal ganz genau, was haben wir hier
[00:23:55] eigentlich? Wir haben primär PHP in
[00:23:57] diesem Projekt. Ansonsten haben wir noch
[00:23:58] JavaScript, also Query Based. Wir haben
[00:24:01] SQL, eine MySQL Datenbank. Wir haben
[00:24:04] hier die Details zur Laufzeitumgebung,
[00:24:06] Frameworks, ähm Abhängigkeiten bzw. die
[00:24:10] Dependencies,
[00:24:12] Konfiguration,
[00:24:13] Datenbank, Plattform Requirements und so
[00:24:16] weiter. Wir haben außerdem hier einmal
[00:24:17] die komplette Projektstruktur,
[00:24:20] die analysiert worden ist
[00:24:22] und auch bekannte Konventionen, die
[00:24:25] gefunden worden sind. Also wirklich ähm
[00:24:27] ja verschiedene Naming Patterns, unter
[00:24:29] anderem Klassen, die verwendet worden
[00:24:31] sind, Variablen, die verwendet worden
[00:24:33] sind, Codingstyle wurde analysiert
[00:24:36] und ja, also wirklich aus allen
[00:24:39] möglichen Perspektiven hier eine sehr
[00:24:41] detaillierte Dokumentation und jetzt
[00:24:43] könnte man natürlich mit Hilfe von Cloud
[00:24:44] Code hier auch einen Migrationsplan
[00:24:47] schreiben. Also einmal runterbrechen,
[00:24:50] in welche Module würde man das jetzt
[00:24:51] z.B. aufteilen? Wie könnte man dieses
[00:24:53] große Projekt Stück für Stück migrieren
[00:24:55] in einen modernen Text und das dann mit
[00:24:58] Hilfe von Cloud Code planen und später
[00:25:00] eben auch umsetzen? Aber jetzt mal ganz
[00:25:02] ehrlich, also allein dafür ist es wert,
[00:25:05] das Ganze mal auszuprobieren, vor allen
[00:25:06] Dingen mal in ein echten Bestandsprojekt
[00:25:08] und sich dann mal die Dokumentation
[00:25:09] anzuschauen, weil wie gesagt, wie viele
[00:25:11] Applikationen gibt es da draußen, wo es
[00:25:13] keine Dokumentation gibt, wo es keinen
[00:25:15] aktiven Entwickler mehr gibt, der das
[00:25:16] Ganze supporten kann und wo einfach
[00:25:18] jeder darauf hofft, dass das Ganze
[00:25:19] weiterhin stabil läuft und sich niemand
[00:25:21] so richtig dran traut, ein
[00:25:22] Migrationsprojekt rauszumachen. Ich bin
[00:25:24] ja selber in einem Industriekonzern groß
[00:25:26] geworden und genau da war das eben auch
[00:25:28] der Fall und ja, mit so einer
[00:25:30] Möglichkeit jetzt sich das Ganze mal
[00:25:31] eben dokumentieren zu lassen, absolut
[00:25:33] crazy. So, jetzt noch mal ganz kurzer
[00:25:35] Spoiler an der Stelle, weil natürlich
[00:25:36] jetzt auch die Frage aufkommt, wie ist
[00:25:38] das dann in der V2? Gibt's das da auch
[00:25:41] die kurze Antwort? Ja und nein. Die
[00:25:43] lange Antwort ist, in V2 gibt es kein
[00:25:46] dediziertes Map Codebase Kommando, so
[00:25:48] wie jetzt in der V1, weil die Codebase
[00:25:50] Analyse da ein bisschen anders gelöst
[00:25:52] ist. V2 hat drei spezialisierte
[00:25:55] Subagents und zwar einmal der Scout, der
[00:25:57] Researcher und der Worker. Und der
[00:25:58] Scout, der macht bei jeder Planphase
[00:26:00] automatisch eine Codebase Review. Sprich
[00:26:02] vor jedem Slice, wie es in der V2 heißt,
[00:26:05] statt Phase in der V1 wird die Codebase
[00:26:07] analysiert und das Ganze wird dann als
[00:26:09] komprimierten Kontext an den Worker
[00:26:11] übergeben. Also bei der V1 hast du eben
[00:26:13] diese sieben persistenten Dokumente, die
[00:26:14] du lesen, prüfen und mit deinem Team
[00:26:16] besprechen kannst. Und bei der V2
[00:26:18] passiert das eher im Hintergrund
[00:26:20] automatisch, aber dafür eben weniger
[00:26:22] transparent. Sprich, für Legacy
[00:26:24] Projekte, wo du die Analyse explizit als
[00:26:26] Gesprächsgrundlage und für
[00:26:27] Migrationspläne brauchst, ist die V1
[00:26:30] deswegen aus meiner Sicht die deutlich
[00:26:31] bessere Wahl. Bei der V2 profitierst du
[00:26:34] davon, dass er dass die Analyse quasi
[00:26:36] bei jedem Schritt eben automatisch
[00:26:37] mitläuft, aber du siehst sie eben nicht
[00:26:38] als separates Artefakt in deinem
[00:26:40] Projekt. Okay, also jetzt zur Version 2.
[00:26:42] Hier ändert sich einiges. GSD V2 ist wie
[00:26:45] gesagt kein Prompt Framework mehr.
[00:26:47] sondern eine eigenständige Typescript
[00:26:49] Anwendung gebaut auf dem sogenannten
[00:26:51] PSDK. Sprich, es läuft eben nicht mehr
[00:26:53] in Cloud Code, sondern ist eine eigene
[00:26:55] CLI Anwendung. Und das ist tatsächlich
[00:26:57] ein ziemlich großer Unterschied, denn in
[00:26:59] der V1 hast du quasi das LM, also Cloud,
[00:27:02] gebeten, den Kontext zu managen. Du hast
[00:27:04] ih per Prompt einfach gesagt, ne, bitte
[00:27:06] halte dich an diese Struktur. Das ist so
[00:27:07] ganz vereinfacht gesagt, was was das GSD
[00:27:10] Cloud mitgegeben hat. Und das hat eben
[00:27:12] in den meisten Fällen auch funktioniert
[00:27:13] oder funktioniert bei mir aktuell auch
[00:27:15] sehr gut, aber eben nicht immer. Und in
[00:27:17] V2 passiert das Ganze dann eben
[00:27:19] programmatisch. Die Anwendung
[00:27:21] kontrollieren also direkt bzw. GSD2
[00:27:23] kontrolliert direkt, welcher Kontext
[00:27:25] wann geladen wird und so kann GSD2 auch
[00:27:29] Kontext Windows lehren und genau die
[00:27:31] richtigen Dateien zur richtigen Zeit
[00:27:33] einbinden. Und das passiert eben alles,
[00:27:34] ohne dass das LM selbst die Entscheidung
[00:27:36] dafür treffen muss. Dazu kommen dann
[00:27:37] auch ein paar Features, die es in der V1
[00:27:39] nicht gab. sowas wie die Crash Recovery.
[00:27:41] Das heißt, wenn eine Session abstürzt,
[00:27:43] erkennt die V2 über Logiles, wo es quasi
[00:27:46] aufgehört hat und macht dann nahtlos
[00:27:48] weiter. Dann gibt's das Costracking. Du
[00:27:50] siehst bei jedem Prompt, den du
[00:27:51] absendest, was der einzelne Task kostet.
[00:27:54] Das Ganze wird aufgeschlüsselt nach
[00:27:56] Phase und Modell. Dann gibt es die Stuck
[00:27:58] Detection. Das heißt, wenn sich ein
[00:28:00] Modell im Kreis dreht, dann erkennt die
[00:28:02] V2 das automatisch. Und dann gibt es die
[00:28:04] Git Worktree Isolation. Das heißt, jeder
[00:28:06] Milestone läuft in seinem eigenen Workth
[00:28:08] und am Ende gibt's dann einen sauberen
[00:28:10] Merch. Dazu gibt es zwei Modi. Einmal
[00:28:12] der Step Mode. Da pausiert der Agent
[00:28:14] quasi zwischen den Einheiten und du
[00:28:16] bestätigst dann jeden einzelnen Schritt
[00:28:18] und es gibt den Auto Mode, da gibst du
[00:28:20] einmal den Auftrag und dann kannst du
[00:28:22] quasi vom Rechner weggehen und wenn du
[00:28:24] zurückkommst, ist der Code quasi fertig
[00:28:26] mit sauberer Git History. Das ist eben
[00:28:28] gedacht für die größtmögliche Autonomie.
[00:28:31] So, jetzt stellt sich natürlich die
[00:28:32] Frage, wenn das Ganze nicht mehr in
[00:28:34] Cloud läuft oder in Cloud Code läuft,
[00:28:36] was bedeutet das eben für die Kosten?
[00:28:37] Und das werden wir gleich beim Setup
[00:28:39] sehen, denn jetzt braucht es natürlich
[00:28:41] einen eine ja Verbindung zu einem
[00:28:43] externen Service, zu einem externen
[00:28:45] LMbieter und da bietet die V2 einmal die
[00:28:50] Oarth Option für Cloud Code für Gemini
[00:28:52] und Co. Aber die würde ich eben nicht
[00:28:54] empfehlen, weil die weil Anthropic oder
[00:28:57] auch Google es mittlerweile in den Terms
[00:28:59] verboten haben, die LMs oder die
[00:29:02] Subscriptions jeweils für Third Party
[00:29:04] Services einzusetzen. Deswegen muss man
[00:29:06] ab jetzt quasi immer über die AP gehen,
[00:29:08] wenn man sowas nutzt und damit kommen
[00:29:10] natürlich dann eben auch größere Kosten
[00:29:12] auf ein zu. Wie sich das Ganze dann in
[00:29:14] der Praxis gestaltet, da möchte ich dir
[00:29:16] gleich schon mal so einen kleinen
[00:29:17] Einblick zu geben und dir zeigen, was
[00:29:18] mich jetzt dieses kleine Beispielprojekt
[00:29:20] mal gekostet hat. Das gleiche wollen wir
[00:29:23] natürlich jetzt noch mal mit der Version
[00:29:25] 2 machen. Das heißt, auch die werden wir
[00:29:26] jetzt einmal installieren und einmal den
[00:29:28] Workflow so ein bisschen durchspielen.
[00:29:31] So, das Ganze ist natürlich wieder auch
[00:29:33] hier wunderbar dokumentiert. Ich kopiere
[00:29:35] mir mal wieder den Befehl. Hier steht
[00:29:37] natürlich jetzt erstmal alles, was neu
[00:29:39] ist im Vergleich zu der alten Version.
[00:29:42] Das Ganze ist ausführlich dokumentiert.
[00:29:44] Noch mal die genaue Abgrenzung hier. Man
[00:29:46] kann auch Projekte von der Version 1 in
[00:29:49] die Version 2 migrieren. Dafür gibt es
[00:29:50] auch einen dedizierten Workflow.
[00:29:52] Ansonsten gibt's auch noch mal eine
[00:29:54] Beschreibung, wie das Ganze
[00:29:55] funktioniert. Was wir gleich ausfüen
[00:29:57] werden, ist hier unter anderem mal diese
[00:30:00] dieser Auto Workflow, wo wir eben
[00:30:02] möglichst autonom äh das Framework
[00:30:05] arbeiten lassen können. So, auch hier
[00:30:08] haue ich das einfach direkt mal wieder
[00:30:09] rein und lass das Ganze installieren.
[00:30:12] So, jetzt gibt es hier gleich eine
[00:30:13] Besonderheit und zwar kann ich das Ganze
[00:30:16] natürlich nicht über die Cloud Code
[00:30:17] Extension bedienen, weil es handelt sich
[00:30:19] ja um ein eigenes Produkt, um eine
[00:30:20] eigenes CLI, deswegen müssen wir gleich
[00:30:23] sozusagen im Terminal entwickeln. Nach
[00:30:25] der Installation können wir das einfach
[00:30:26] über GSD starten. Dann sehen wir hier
[00:30:29] die V2 und dann können wir einfach mal
[00:30:31] mit dem GSD Auto Mode anfangen und in
[00:30:36] diesen autonomen Arbeitsmodus
[00:30:38] reinstarten. Und dann führt uns das
[00:30:39] System quasi durch den gesamten Prozess.
[00:30:43] So, what's the vision? Tell me what you
[00:30:44] wann to build. Okay, ich nutze jetzt
[00:30:46] einfach mal den gleichen Prompt, den ich
[00:30:47] eben auch verwendet habe
[00:30:50] für unseren ersten Test und lass ihn das
[00:30:53] jetzt hier mal erarbeiten. So, ich mache
[00:30:55] das hier mal außerdem ein bisschen
[00:30:56] größer.
[00:30:59] So, jetzt gibt er mir einmal aus, was er
[00:31:00] verstanden hat. Das bestätige ich mir
[00:31:01] jetzt einmal. Ja, das passt. Let's go.
[00:31:06] Und dann legt er wahrscheinlich los. So,
[00:31:09] er arbeitet auf jeden Fall fleißig.
[00:31:11] Etwas, was ich jetzt immer wieder
[00:31:12] festgestellt habe auch im Testing, ist,
[00:31:14] dass ich die Limits meiner Cloud API
[00:31:17] erreiche. Also, ich bin aktuell im RP
[00:31:20] Tier 2. Das heißt, ich habe pro Minute
[00:31:22] ein Kontextfenster von 450.000 Token.
[00:31:25] Jetzt ist dieser Prozess natürlich recht
[00:31:27] tokenintensiv
[00:31:28] und sorgt dafür, dass ich regelmäßig die
[00:31:31] AP Limits erreiche. Das heißt, ich muss
[00:31:33] dann wieder eine Minute warten, dann
[00:31:34] habe ich wieder äh ein freies
[00:31:36] Kontextfenster sozusagen und kann dann
[00:31:38] ähm weitermachen. Aber das ist auch so
[00:31:40] ein bisschen die bittere Realität. Das
[00:31:42] heißt, die Tiers hängen so ein bisschen
[00:31:44] davon ab, wie sehr du deinen Konto
[00:31:46] auflädst für die Cloud RP. Und aktuell
[00:31:50] waren das bei mir eben nur so 50 €.
[00:31:52] Deswegen bin ich da gerade in Tier 2. Um
[00:31:54] in Tier 3 zu rutschen, müsstest du dein
[00:31:56] Konto mit mindestens, ich glaube, 200 €
[00:31:58] nagelbänlich fest äh aufladen, um dann
[00:32:02] in das nächste höhere äh Limit sozusagen
[00:32:05] äh reinzugehen. So, jetzt stellt er mir
[00:32:07] auf jeden Fall auch ein paar Rückfragen,
[00:32:09] z.B. zum Stack. Das war ja eben genauso.
[00:32:11] Ich kann jetzt also einfach hier mit den
[00:32:12] Falltasten navigieren und ähm gebe jetzt
[00:32:16] einfach mal ein paar Informationen auch
[00:32:17] hier. Also, wie welche Spalten soll das
[00:32:19] System haben? Fixed Colums. Und jetzt
[00:32:22] kann ich hier noch mal das ganze
[00:32:23] reviewen und dann eben absenden. Und
[00:32:26] genauso wie im in der V1 gerade eben
[00:32:29] versucht er jetzt erstmal zu verstehen
[00:32:31] genau was sind eigentlich die
[00:32:33] grundlegenden Informationen, die wir
[00:32:34] hier brauchen, um das Projekt in Gang zu
[00:32:36] bringen. So, ich gebe ihm auch hier noch
[00:32:39] mal wieder eine Antwort. Das passt so.
[00:32:42] Perfect. I have a clear picture now.
[00:32:44] Jetzt gibt er mir hier noch mal wieder
[00:32:45] die Zusammenfassung. Und das kann ich
[00:32:47] wahrscheinlich gleich noch mal wieder
[00:32:48] bestätigen. Genau. Did I capture
[00:32:50] everything correctly? Also, meine
[00:32:52] Aufgabe ist das jetzt quasi einmal zu
[00:32:54] reviewen. Ich sag yes, das passt. Gebe
[00:32:56] eben die finale Bestätigung und dann
[00:32:58] erstellt er uns jetzt auch wieder
[00:33:00] erstmal diese ganzen Basisdokumente.
[00:33:03] So, also wir bekommen jetzt hier die
[00:33:04] Anforderungen in Tasks und wir haben die
[00:33:08] Roadmap. Das sieht alles recht ähnlich
[00:33:10] aus zu dem, was wir eben schon
[00:33:12] entwickelt haben. Und ich sag jetzt
[00:33:13] einfach ähm
[00:33:16] correct äh let's go.
[00:33:20] So, dieser Automode, der führt uns jetzt
[00:33:21] weitesgehen durch den gesamten Prozess.
[00:33:23] Wir können aber in den verschiedensten
[00:33:26] Schritten noch mal wieder eingreifen und
[00:33:28] auch z.B. die Discussphase starten, mit
[00:33:31] der wir dann noch mal tiefer in
[00:33:33] Anforderung oder auch in die Basis
[00:33:36] unserer App reingehen können, um noch
[00:33:37] mal sparing mit Cloud bzw. mit GSD ist
[00:33:41] es jetzt ja zu betreiben, damit das
[00:33:42] System besser versteht, was eigentlich
[00:33:44] passieren soll. Also, ich würde auch
[00:33:46] sagen, für den ersten Eindruck äh reicht
[00:33:49] es erstmal. Lass uns mal ähm in meinen
[00:33:51] Beispielcase reinschauen, den ich jetzt
[00:33:53] hier auch mit GSD2 entwickelt habe.
[00:33:55] Analog zu der V1 Version gerade eben.
[00:33:58] Ich bin jetzt hier also wieder in meinem
[00:33:59] Incident Management Beispiel, dass ich
[00:34:01] entwickelt habe mit der V2 und lass uns
[00:34:04] mal hier ein Blick auf die
[00:34:05] Projektstruktur werfen. Also, wir
[00:34:07] erkennen so ein paar Sachen wieder hier
[00:34:08] wie die Project MD, Requirements, State
[00:34:11] MD, wir haben hier auch noch die Agents
[00:34:13] MD, aber diese Dokumente, die kennen wir
[00:34:15] auch aus der V1. So, was ich was ich
[00:34:18] jetzt hier unterscheidet, ist, dass wir
[00:34:20] nicht in Phasen planen, sondern in
[00:34:23] Milestones und in Slices.
[00:34:26] So, das heißt, es gibt ja für jeden
[00:34:27] Milestone einmal entsprechenden Kontext
[00:34:30] und dann eben auch noch mal für jeden
[00:34:32] Slice. GSD2 versucht das Projekt also
[00:34:35] noch besser aufzuteilen und zu
[00:34:37] dokumentieren. Das sehen wir gleich auch
[00:34:38] noch mal, wenn wir hier mal in einen
[00:34:39] Slice reinschauen, denn ein Slice ist
[00:34:41] wiederum unterteilt in einzelne
[00:34:43] Aufgaben.
[00:34:45] Ähm, davor hat aber natürlich jeder
[00:34:46] Slice auch noch wiederum seine eigenen
[00:34:48] Informationen, z.B. die Assessments,
[00:34:51] Plan, Research, Summary und User
[00:34:53] Acceptance Tests. So und wenn wir uns
[00:34:56] mal die Tasks anschauen, dann haben wir
[00:34:58] hier auch die einzelnen Tasks, die
[00:35:00] wiederum auch jeweils einen Plan und
[00:35:02] eine Zusammenfassung haben. Hier T01,
[00:35:04] T01, T02, T02, T03, T03. Also, du siehst
[00:35:10] hier die Planung schon deutlich
[00:35:12] umfangreicher. Lass uns aber auch hier
[00:35:14] mal kurz einen Blick auf das Ergebnis
[00:35:16] werfen. So, das ist jetzt hier die
[00:35:18] Ansicht, die mir die V2 erstellt hat.
[00:35:20] Die ist optisch schon deutlich
[00:35:22] ansprechender im Vergleich zu GSD1. Wir
[00:35:26] haben hier auch genau die Übersicht der
[00:35:28] bestehenden Incidents. Wenn ich hier mal
[00:35:30] einen öffne, bekomme ich hier eine
[00:35:32] Zusammenfassung auch mit der gesamten
[00:35:34] Timel sogar. kann hier Kommentare
[00:35:36] hinzufügen und wenn ich zurückgehe, kann
[00:35:39] ich hier auch einen neuen Inzident
[00:35:40] anlegen. Also ja, optisch auf jeden Fall
[00:35:43] deutlich entsprechender als die Version
[00:35:44] 1 eben. So und um dir noch mal ganz kurz
[00:35:46] einen Einblick zu geben, was mich jetzt
[00:35:48] diese Teilanwendung gekostet hat, es
[00:35:50] gibt jetzt letztendlich nur ein
[00:35:52] Front-End, was aktuell noch sehr
[00:35:54] limitierte Funktionalitäten hat mit dem
[00:35:56] Dashboard, der Incident Übersicht und
[00:35:58] der Anlage von neuen Incidents. Und es
[00:35:59] gibt auch nur eine lokale Speicherung.
[00:36:01] Das Ganze wird also in meinem Browser
[00:36:03] Cash gespeichert, weil ich jetzt keinen
[00:36:05] Backend anlegen wollte und so weiter.
[00:36:07] Dieser Prozess hat mich jetzt hier schon
[00:36:09] etwas über 20 US-Dollar gekostet.
[00:36:12] Dementsprechend
[00:36:13] ähm ja solltest du natürlich überlegen,
[00:36:16] welches Framework du auch einsetzt, weil
[00:36:18] gerade über die APs sind die Modelle
[00:36:21] schon recht kostintensiv. Opus 4.6
[00:36:23] natürlich auch eins der teuersten
[00:36:24] Modelle mit 5 USDollar pro 1 Million
[00:36:27] Input Token und 15$ pro 1 Million Output
[00:36:29] Token. Dementsprechend laufen die Kosten
[00:36:31] ja natürlich auch dann recht schnell
[00:36:32] auf. Okay, also ich möchte mal
[00:36:34] versuchen, dir meine ehrliche
[00:36:36] Einschätzung dazu zu geben. Also was die
[00:36:38] V2 gut macht, ist einmal die
[00:36:40] Planningstruktur. Aus meiner Sicht, die
[00:36:41] ist ziemlich beeindruckend. Das hat mir
[00:36:43] jetzt für dieses Beispielprojekt 30
[00:36:45] Planning Dokumente erstellt für den
[00:36:47] Incident Hub. ähm mehr als in der V1, da
[00:36:49] waren es jetzt 19 an der Zahl und jeder
[00:36:52] Task hat einen eigenen Plan mit
[00:36:54] Zeiteinschätzung und jeder Slice wird
[00:36:56] quasi nach Abschluss noch mal bewertet.
[00:36:58] Jetzt muss man natürlich auch gucken,
[00:36:59] dass man darüber noch den Überblick
[00:37:01] behält. Also ja, ich würde sagen, schau
[00:37:03] dir das mal in Ruhe an, probier das mal
[00:37:05] ein bisschen aus, schau mal in die
[00:37:07] Dokumente rein und dir den Inhalt an.
[00:37:09] Ich denke, dann bekommst du ein Gefühl
[00:37:11] dafür, ähm warum und ob das notwendig
[00:37:14] ist. Ein Konzept, was ich auch spannend
[00:37:16] fand, ist die Boundary Map. Also, stell
[00:37:18] dir vor, du hast quasi fünf Slices in
[00:37:20] deinem Projekt und Slice 1 baut das
[00:37:23] Datenmodell, Slice 2 baut die UI und Sli
[00:37:25] 3 ist quasi für die AI Integration
[00:37:27] gedacht. Und jetzt muss Slice 2
[00:37:29] natürlich wissen, welche Datentypen und
[00:37:31] Funktion Slice 1 bereitgestellt hat,
[00:37:33] sonst baut der Slice vielleicht
[00:37:34] irgendwas, was an anderer Stelle gar
[00:37:36] nicht genutzt werden kann. So und die
[00:37:37] Boundary Map definiert quasi genau das,
[00:37:39] also was liefert eigentlich jeder Slice
[00:37:42] an die anderen und was braucht er quasi
[00:37:44] auch von ihnen? Also letztendlich sind
[00:37:46] das sozusagen Übergabe Checklisten
[00:37:48] zwischen den einzelnen Bauabschnitten
[00:37:49] und das verhindert eben, dass Slices
[00:37:51] aneinander vorbeientwickeln. Die V2 hat
[00:37:53] auch den stärkeren Testdriven
[00:37:54] Development Ansatz. Das heißt allein für
[00:37:57] mein Beispielprojekt jetzt bei diesem
[00:37:58] Incident Management hat's allein für die
[00:38:00] Statusübergänge der Incidents ca. 20
[00:38:04] Tests geschrieben, bevor überhaupt die
[00:38:05] DUI implementiert worden ist. Das heißt,
[00:38:08] da wird eigentlich von Beginn an
[00:38:09] versucht, alle Edge Cases irgendwie
[00:38:11] abzudecken, um halt Fehler zu
[00:38:12] reduzieren. Die V1 hat da deutlich
[00:38:15] pragmatischer losgelegt und eigentlich
[00:38:17] erstmal angefangen, die UI zu bauen.
[00:38:19] Außerdem gab es noch einen größeren
[00:38:20] Unterschied bei der Installation der
[00:38:22] Dependencies und zwar hat die V1 sich
[00:38:24] quasi direkt zum Start mit 12 Libraries
[00:38:27] eingedeckt und die V2, dem gegenüber
[00:38:29] gerade mal drei Dependencies
[00:38:30] installiert. Das waren React, NextJs und
[00:38:32] der React DOM. Alles andere kommt bei
[00:38:35] der V2 eben erst, wenn es der jeweilige
[00:38:37] Slice dann auch braucht. Zum Start ist
[00:38:39] das Ganze also ein bisschen
[00:38:40] minimalistischer. Dadurch kann es aber
[00:38:41] eben auch passieren, dass die
[00:38:43] Featureentwicklung etwas länger dauert,
[00:38:45] wenn dann eben noch entsprechende
[00:38:46] Dependencies nachinstalliert werden
[00:38:47] müssen. Dann muss man natürlich auch
[00:38:49] noch mal einen Blick auf die Kosten
[00:38:50] werfen. Ich nutze jetzt persönlich den
[00:38:52] Cloud Code Max Plan, das heißt, ich
[00:38:54] zahle ungefähr 100 US-Dollar pro Monat
[00:38:57] für diesen Service und kann damit die V1
[00:38:59] unbegrenzt nutzen. natürlich im Rahmen
[00:39:01] meiner persönlichen Limits. Äh man kann
[00:39:03] aber natürlich auch dann noch das
[00:39:05] variable Upgrade Feature nutzen. Das
[00:39:07] heißt, wenn ich die Limits erreicht
[00:39:08] habe, dann kann ich die noch erweitern
[00:39:10] sozusagen, indem ich zusätzlich für den
[00:39:12] Service zahle. So, damit sind aber meine
[00:39:14] Kosten erstmal in einem recht klaren
[00:39:16] Rahmen. Wenn ich die V2 dem gegenüber
[00:39:18] nutzen möchte, dann muss ich in meinem
[00:39:20] Fall auf die Cloud Abi zugreifen. So und
[00:39:24] da ist es natürlich so, dass Opus 4.6
[00:39:26] eins der teureren Modelle ist mit 5
[00:39:29] USDollar pro 1 Million Input Token und
[00:39:31] 15 USDLAR pro 1 Million Output Token.
[00:39:34] Und da der Prozess an sich natürlich
[00:39:36] recht kontext intensiv oder Token
[00:39:38] intensiv ist, kann es natürlich sein,
[00:39:40] dass ich eben bei entsprechender Größe
[00:39:42] von einem Projekt dann auch
[00:39:44] dementsprechende Kosten verursache. Dem
[00:39:46] muss man sich einfach ganz klar bewusst
[00:39:48] sein. Natürlich könnte man das Ganze
[00:39:50] eben auch mit Open Source oder lokalen
[00:39:51] Modellen betreiben, wenn man das Ganze
[00:39:54] möchte. So lassen sie natürlich auch
[00:39:55] Kosten einsparen. Jetzt nur im Vergleich
[00:39:58] Opus 4.6 innerhalb der Subscription oder
[00:40:01] über die AP ist man natürlich mit der
[00:40:03] Subscription ganz klar im Vorteil. Wann
[00:40:05] nimmst du jetzt also was? Wenn du eh
[00:40:07] schon primär mit Cloud Code arbeitest,
[00:40:09] dort eine Subscription hast und bei
[00:40:10] jedem Schritt die Kontrolle behalten
[00:40:12] willst und auch schnell starten willst
[00:40:14] oder wenn du vor allen Dingen bestehende
[00:40:16] Codebases explizit analysieren möchtest
[00:40:18] für z.B. als Grundlage für ein
[00:40:20] Migrationsprojekt, dann bist du mit der
[00:40:23] Version 1 auf jeden Fall sehr gut
[00:40:25] ausgestattet. Das letzte Update der
[00:40:26] Version gab es erst vor wenigen Tagen.
[00:40:29] Das heißt, die Version 1 wird gerade
[00:40:31] auch noch aktiv weiterentwickelt bzw.
[00:40:34] supported. Wie lange das natürlich so
[00:40:35] ist, kann ich dir nicht genau sagen,
[00:40:38] aber selbst wenn, kann man ja auch die
[00:40:39] Prinzipien aus dem bestehenden Framework
[00:40:41] in sein eigenes übertragen. Wenn du auf
[00:40:43] der anderen Seite maximale Autonomie
[00:40:45] willst, vielleicht CICD Pipelines
[00:40:47] brauchst und im Team arbeitest, dann
[00:40:49] eignen sich eher die V2. Da bekommst du
[00:40:51] einfach die granularere Planung mit den
[00:40:53] Boundary Maps und den Assessments, also
[00:40:56] den Nachbewertung von den entwickelten
[00:40:57] Artefakten. Grundsätzlich kann man
[00:40:59] glaube ich sagen, dass es gerade nicht
[00:41:01] das eine perfekte Framework gibt. Das
[00:41:03] muss man einfach gerade von Projekt zu
[00:41:04] Projekt bewerten. Da stellt sich auch
[00:41:06] immer dann so ein bisschen die Frage,
[00:41:07] geht's ein neues Projekt? Ist das ein
[00:41:09] bestehendes Projekt? Wie groß ist das
[00:41:10] Projekt? Wie viele Entwickler sind an
[00:41:12] dem Projekt beteiligt? Und es kann eben
[00:41:13] auch sein, dass du gar kein Framework
[00:41:15] brauchst, weil das Projekt einfach super
[00:41:16] klein ist. Dann macht es eher Sinn
[00:41:18] direkt mit dem Cloud Code Agent loszule?
[00:41:20] Ich würde sagen, probier die Frameworks
[00:41:22] einfach mal aus, entwickel mal was damit
[00:41:24] und dann stellst du, glaube ich, schnell
[00:41:25] für dich selber fest, ob die Ergebnisse
[00:41:27] für dich stimmen und ob der Workflow für
[00:41:29] dich passt. Also noch mal in wenigen
[00:41:30] Worten zusammengefasst: GST V1 ist ein
[00:41:33] Prompt Framework für einen
[00:41:35] kontrollierten Speckdriven Workflow
[00:41:36] direkt in Cloud Code und GSTV2 ist eine
[00:41:39] eigenständige CLI für maximale Autonomie
[00:41:42] und Teamfeatures. Beide lösen das
[00:41:45] Context Drop Problem und geben dem
[00:41:46] Modell einen strukturierten Kontext zur
[00:41:49] richtigen Zeit. Wenn dir die beiden
[00:41:50] Frameworks gerade noch zu komplex
[00:41:52] erscheinen, weil du erst in die Thematik
[00:41:54] einsteigst, dann möchte ich dir an
[00:41:55] dieser Stelle noch mal mein AI Coding
[00:41:57] Starter Kit ans Herz legen. Das kannst
[00:41:59] du dir einfach kostenlos runterladen und
[00:42:01] das liefert dir einen perfekten Einstieg
[00:42:02] in die Welt von Cloud Code. Den Link
[00:42:04] dazu findest du einfach in der
[00:42:05] Videobeschreibung. Mich würde auch
[00:42:07] interessieren, was deine Meinung dazu
[00:42:09] ist. Nutzt du schon GSD oder vielleicht
[00:42:11] auch ein anderes Framework? Schreib es
[00:42:12] mir mal gerne in die Kommentare. Wenn
[00:42:14] dir das Video gefallen hat, dann lass
[00:42:15] super gerne ein Like und ein Abo da.
[00:42:16] Darüber würde ich mich extrem freuen.
[00:42:18] Alle Links auch zu den anderen
[00:42:19] Frameworks findest du natürlich in der
[00:42:21] Videobeschreibung. Ansonsten noch mal
[00:42:23] vielen Dank fürs Zuschauen und ich
[00:42:25] hoffe, wir sehen uns beim nächsten Video
[00:42:26] wieder. Bis dahin, mach's gut. Yeah.