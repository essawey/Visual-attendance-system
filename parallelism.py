from sendEmail import send_startEmail, send_endEmail
import threading
from IoT import  loading, printLCD


startEmail_completed = False
endEmail_completed = False

# Create an event to signal the loadingThread to exit
startEmail_loadingEvent = threading.Event()
endEmail_loadingEvent = threading.Event()

def startEmail_FunCall(DR_EMAIL, COURSE_CODE, OTP_PASSCODE):
    global startEmail_completed
    send_startEmail(DR_EMAIL, COURSE_CODE, OTP_PASSCODE)
    startEmail_completed = True
    # Set the event to signal the loadingThread to exit
    startEmail_loadingEvent.set()

def endEmail_FunCall(DR_EMAIL, COURSE_CODE, FILE_PATH):
    global endEmail_completed
    send_endEmail(DR_EMAIL, COURSE_CODE, FILE_PATH)
    endEmail_completed = True
    # Set the event to signal the loadingThread to exit
    endEmail_loadingEvent.set()


def parallelism_startEmail(DR_EMAIL, COURSE_CODE, OTP_PASSCODE):
    startEmail_Loading_Thread = threading.Thread(target=loading, args=(1.9, startEmail_loadingEvent))
    startEmail_Thread = threading.Thread(target=startEmail_FunCall, args=(DR_EMAIL, COURSE_CODE, OTP_PASSCODE))

    # Start the threads
    startEmail_Loading_Thread.start()
    startEmail_Thread.start()

    # Wait for start Email Thread to complete
    startEmail_Thread.join()
    startEmail_Loading_Thread.join()

    if startEmail_completed:
        printLCD("sending completed.")

def parallelism_endEmail(DR_EMAIL, COURSE_CODE, FILE_PATH):
    endEmail_Loading_Thread = threading.Thread(target=loading, args=(1.9, endEmail_loadingEvent))
    endEmail_Thread = threading.Thread(target=endEmail_FunCall, args=(DR_EMAIL, COURSE_CODE, FILE_PATH))

    # end the threads
    endEmail_Loading_Thread.start()
    endEmail_Thread.start()

    # Wait for end Email Thread to complete
    endEmail_Thread.join()
    endEmail_Loading_Thread.join()

    if endEmail_completed:
        printLCD("sending completed.")