import os
import random
import time
import pygame

def notify(title, message):
    os.system(f'''
              osascript -e 'display notification "{message}" with title "{title}"'
              ''')

def main():
    words = [
        ("привет", "hello"), 
        ("мир", "world"),
        ("яблоко", "apple"),
        ("кошка", "cat"),
        ("солнце", "sun"),
        ("дом", "house"),
        ("машина", "car"),
        ("книга", "book"),
        ("школа", "school"),
        ("дерево", "tree"),
        ("вода", "water"),
        ("город", "city"),
        ("парк", "park"),
        ("компьютер", "computer"),
        ("музыка", "music"),
        ("фильм", "movie"),
        ("спорт", "sport"),
        ("работа", "work"),
        ("день", "day"),
        ("ночь", "night"),
        ("здоровье", "health"),
        ("еда", "food"),
        ("путешествие", "travel"),
        ("любовь", "love"),
        ("семья", "family"),
        ("дружба", "friendship"),
        ("игра", "game"),
        ("улица", "street"),
        ("пляж", "beach"),
        ("праздник", "holiday"),
        ("время", "time"),
        ("год", "year"),
        ("месяц", "month"),
        ("неделя", "week"),
        ("час", "hour"),
        ("минута", "minute"),
        ("секунда", "second"),
        ("цвет", "color"),
        ("красный", "red"),
        ("синий", "blue"),
        ("зеленый", "green"),
        ("желтый", "yellow"),
        ("черный", "black"),
        ("белый", "white"),
        ("коричневый", "brown"),
        ("серый", "gray"),
        ("оранжевый", "orange"),
        ("фиолетовый", "purple"),
        ("розовый", "pink"),
        ("серебряный", "silver"),
        ("золотой", "gold"),
        ("большой", "big"),
        ("маленький", "small"),
        ("высокий", "tall"),
        ("низкий", "short"),
        ("толстый", "fat"),
        ("худой", "thin"),
        ("красивый", "beautiful"),
        ("уродливый", "ugly"),
        ("интересный", "interesting"),
        ("скучный", "boring"),
        ("счастливый", "happy"),
        ("грустный", "sad"),
        ("злой", "angry"),
        ("спокойный", "calm"),
        ("горячий", "hot"),
        ("холодный", "cold"),
        ("быстрый", "fast"),
        ("медленный", "slow"),
        ("новый", "new"),
        ("старый", "old"),
        ("хороший", "good"),
        ("плохой", "bad"),
        ("правильный", "right"),
        ("неправильный", "wrong"),
        ("легкий", "easy"),
        ("трудный", "difficult"),
        ("дешевый", "cheap"),
        ("дорогой", "expensive"),
        ("близкий", "close"),
        ("дальний", "far"),
        ("свободный", "free"),
        ("занятый", "busy"),
        ("громкий", "loud"),
        ("тихий", "quiet"),
        ("чистый", "clean"),
        ("грязный", "dirty"),
        ("пустой", "empty"),
        ("полный", "full"),
        ("простой", "simple"),
        ("сложный", "complex"),
        ("правда", "truth"),
        ("ложь", "lie"),
        ("вопрос", "question"),
        ("ответ", "answer"),
        ("проблема", "problem"),
        ("решение", "solution"),
        ("идея", "idea"),
        ("цель", "goal"),
        ("успех", "success"),
        ("неудача", "failure"),
        ("работник", "worker"),
        ("учитель", "teacher"),
        ("студент", "student"),
        ("врач", "doctor"),
        ("инженер", "engineer"),
        ("полицейский", "police officer"),
        ("пожарный", "firefighter"),
        ("пилот", "pilot"),
        ("певец", "singer"),
        ("актер", "actor"),
        ("писатель", "writer"),
        ("художник", "artist"),
        ("музыкант", "musician"),
        ("спортсмен", "athlete"),
        ("путешественник", "traveler"),
        ("друг", "friend"),
        ("враг", "enemy"),
        ("сосед", "neighbor"),
        ("родитель", "parent"),
        ("ребенок", "child"),
        ("брат", "brother"),
        ("сестра", "sister"),
        ("дедушка", "grandfather"),
        ("бабушка", "grandmother"),
        ("дядя", "uncle"),
        ("тетя", "aunt"),
        ("племянник", "nephew"),
        ("племянница", "niece"),
        ("кузен", "cousin"),
        ("соседка", "neighbor"),
        ("муж", "husband"),
        ("жена", "wife"),
        ("сын", "son"),
        ("дочь", "daughter"),
        ("внук", "grandson"),
        ("внучка", "granddaughter"),
        ("парень", "boyfriend"),
        ("девушка", "girlfriend"),
        ("животное", "animal"),
        ("собака", "dog"),
        ("кошка", "cat"),
        ("лошадь", "horse"),
        ("корова", "cow"),
        ("свинья", "pig"),
        ("овца", "sheep"),
        ("коза", "goat"),
        ("курица", "chicken"),
        ("утка", "duck"),
        ("гусь", "goose"),
        ("кролик", "rabbit"),
        ("рыба", "fish"),
        ("птица", "bird"),
        ("змея", "snake"),
        ("ящерица", "lizard"),
        ("жаба", "frog"),
        ("пчела", "bee"),
        ("муравей", "ant"),
        ("паук", "spider"),
        ("жук", "beetle"),
        ("бабочка", "butterfly"),
        ("медведь", "bear"),
        ("тигр", "tiger"),
        ("лев", "lion"),
        ("слон", "elephant"),
        ("жираф", "giraffe"),
        ("зебра", "zebra"),
        ("крокодил", "crocodile"),
        ("кенгуру", "kangaroo"),
        ("пингвин", "penguin"),
        ("кит", "whale"),
        ("дельфин", "dolphin"),
        ("акула", "shark"),
        ("черепаха", "turtle"),
        ("краб", "crab"),
        ("рак", "lobster"),
        ("картошка", "potato"),
        ("морковь", "carrot"),
        ("лук", "onion"),
        ("чеснок", "garlic"),
        ("помидор", "tomato"),
        ("огурец", "cucumber"),
        ("капуста", "cabbage"),
        ("а", "a"),
        ("б", "b"),
        ("в", "v"),
        ("г", "g"),
        ("д", "d"),
        ("е", "ye"),
        ("ё", "yo"),
        ("ж", "zh"),
        ("з", "z"),
        ("и", "ee"),
        ("й", "y"),
        ("к", "k"),
        ("л", "l"),
        ("м", "m"),
        ("н", "n"),
        ("о", "o"),
        ("п", "p"),
        ("р", "r"),
        ("с", "s"),
        ("т", "t"),
        ("у", "oo"),
        ("ф", "f"),
        ("х", "kh"),
        ("ц", "ts"),
        ("ч", "ch"),
        ("ш", "sh"),
        ("щ", "shch"),
        ("ъ", "hard sign"),
        ("ы", "i"),
        ("ь", "soft sign"),
        ("э", "eh"),
        ("ю", "yu"),
        ("я", "ya")
    ]
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Notification Interval")
    font = pygame.font.Font(None, 32)
    text = font.render("""remind in every..? (in seconds):""", True, (255, 255, 255))
    text_rect = text.get_rect(center=(200, 150))

    input_box = pygame.Rect(100, 200, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    interval = ""

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            how_long = int(interval)
                            done = True
                        except ValueError:
                            interval = ""
                    elif event.key == pygame.K_BACKSPACE:
                        interval = interval[:-1]
                    else:
                        interval += event.unicode

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)
        txt_surface = font.render(interval, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        screen.blit(text, text_rect)
        pygame.display.flip()

    pygame.quit()

    while True:
        random_word, meaning = random.choice(words)
        notify("Random Russian Word", f"{random_word} - {meaning}")
        time.sleep(how_long)
    

if __name__ == "__main__":
    main()
