# Amp_Controller (Mark Levinson control signal's non standard usage of pulse control)
# Constant to Plulse conversion from constant 12V input
#This assumes your Mark Levinson APM is on Standby as start state
#Your input to the Mark Levinson Should connect to GPIO21 for + and a GRND
#The control Signal from constant high or low should connect to a 12 V relay
#the switch signals from the relay to toggle on/off should be connected to GPIO twenty six and GRND
Solves this issue: http://www.remotecentral.com/cgi-bin/mboard/rc-custom/thread.cgi?18902,1
