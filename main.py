import scratchattach as scratch3
session = scratch3.login("Iegend-", "kitloin!@")
from time import sleep
from random import randint
conn = session.connect_cloud("612229554")
while True:
    conn.set_var("CLOUD1", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD2", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD3", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD4", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD5", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD6", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD7", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD8", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    conn.set_var("CLOUD9", "21041524340405035543742380810351122852644853654354653954653354652954642454641954643256575051535051515051505051505051505051505051505051505051505051505051505051505051505051505051")
    conn.set_var("ONLINE", "29")
