from datetime import datetime
import telegram

def sendVideo(filename):
    # initializing a telegram bot 
    bot = telegram.Bot('token')
    # to send video
    if bot.get_updates():
        chat_id =  'id'
        # provide the file path here in fpath variable
        fpath = f"D:\\python_idleprog\\Practice\\{filename}"
        video=open(fpath,'rb')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        bot.send_message(chat_id,"Motion Detected "+current_time)
        bot.send_video(chat_id,video, supports_streaming=True)
    else:
        pass




