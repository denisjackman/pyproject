import cgitb
cgitb.enable()
import xml.dom.minidom

doc = xml.dom.minidom.parse("http://devolv001.dev.betfair:8080/CheltenhamWarRoom/FirstRaceChecker")
 
mapping = {}
 
for node in doc.getElementsByTagName("nextRace"):
    venue = node.getElementsByTagName("venue")
    MarketName = node.getElementsByTagName("MarketName")
    MarketTime = node.getElementsByTagName("MarketTime")
 
# mapping now has the same value as in the SAX example:
print ' Test '

