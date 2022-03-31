from pyrogram import filters, Client, idle
import session_gen
from datetime import datetime
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup,InlineKeyboardButton

import oxfordapi



app = session_gen.gen_session()

@app.on_message(filters.command("start"))
def send_wlc(client,message):
    chat_id = message.chat.id
    client.send_message(chat_id=chat_id, text="Hi there! ")
    



@app.on_inline_query()
def answer(client, inline_query):
    print(inline_query)
    text = inline_query.query
    id = inline_query.id
    print(text)
    result = oxfordapi.get_result(text)
    meaning = oxfordapi.get_meaning(result)
    audio = oxfordapi.get_audio(result)
    example = oxfordapi.get_example(result)
    
        
    
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title=f"{text}",
                input_message_content=InputTextMessageContent(
                    f"**{text.upper()}** : {meaning}\n**Example** : {example}"
                ),
                description=meaning,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Pronunciation",
                            url=audio
                        )]
                    ]
                )
            ),
            
            
            
           
        ],
        cache_time=1
    )


app.run()  # Automatically start() and idle()
