import play

play.set_backdrop("white")

@play.when_program_starts #функція для початку програми 
def start():
    text1 = play.new_text(words = " г - гладити , з - зіграти , с - спати" , x = 0 , y = 260 , font_size = 40)
    text2 = play.new_text(words = " к - кормити , п - прибирати , пробіл - піти" , x = 0 , y = 230 , font_size = 40)
    play.new_image(image = "kuromi.jpg" , x = 0 , y = 0 , size = 80)


@play.repeat_forever #повторювати завжди(ігровий цикл)
def do():
    pass

play.start_program() #запуск програми