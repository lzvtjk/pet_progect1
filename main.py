import play

play.set_backdrop("white")

@play.when_program_starts #функція для початку програми 
def start():
    global player , speech
    text1 = play.new_text(words = " g - glasses , p - play guitar, c - cry" , x = 0 , y = 260 , font_size = 40)
    text2 = play.new_text(words = " j - jump , п - прибирати , пробіл - піти" , x = 0 , y = 230 , font_size = 40)
    player = play.new_image(image = "kuromi.jpg" , x = 0 , y = 0 , size = 100 )
    speech = play.new_text(words = "Hello who are you" , x = 0 , y = -250)


@play.repeat_forever #повторювати завжди(ігровий цикл)
async def do():
    if play.key_is_pressed("g") or play.key_is_pressed("G"):
        speech.words = "are you serious"
        await play.timer(2.0)
        player.image = "Glasses kuromi.jpg"
        speech.words = "cool bro"
    if play.key_is_pressed("p") or  play.key_is_pressed("P"):
        speech.words = "maybe something else"
        await play.timer(2.0)
        player.image = "Guitar kuromi.jpg"
        speech.words = ""
    if play.key_is_pressed("c") or  play.key_is_pressed("C"):
        player.image = "Whining kuromi.jpg"
        speech.words = ""
        await play.timer(2.0)
    if play.key_is_pressed("j") or  play.key_is_pressed("J"):
        player.image = "insidious kuromi.jpg"
        speech.words = "i`m tired"
        await play.timer(2.0)
        player.image = "Joyful kuromi.jpg"
        speech.words = "enough, you can jump on your own"
        player.image = "Lol kuromi.jpg"
    if play.key_is_pressed("") or  play.key_is_pressed(""):
        player.image = ""
        speech.words = ""
        await play.timer(3.0)
    if play.key_is_pressed("") or  play.key_is_pressed(""):
        player.image = ""
        speech.words = ""
        await play.timer(3.0)


play.start_program() #запуск програми