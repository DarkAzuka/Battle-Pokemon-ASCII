from replit import clear
import random

print('''
              _                              
  _ __   ___ | | _____ _ __ ___   ___  _ __  
 | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
 | |_) | (_) |   <  __/ | | | | | (_) | | | |
 | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
 |_|                                         
Welcome - Battle Pokemon ASCII art Especial - for Anel Arciniega
''')

pikachu = ('''
               Pikachu   
  .__                           __.
   \ `\~~---..---~~~~~~--.---~~| /   
    `~-.   `                   .~         _____ 
        ~.                .--~~    .---~~~    /
         / .-.      .-.      |  <~~        __/
        |  |_|      |_|       \  \     .--'
       /-.      -       .-.    |  \_   \_
       \-'   -..-..-    `-'    |    \__  \_ 
        `.                     |     _/  _/
          ~-                .,-\   _/  _/
         /                 -~~~~\ /_  /_
        |               /   |    \  \_  \_ 
        |   /          /   /      | _/  _/
        |  |          |   /    .,-|/  _/ 
        )__/           \_/    -~~~| _/
          \                      /  \
           |           |        /_---` 
           \    .______|      ./
           (   /        \    /        Amw
           `--'          /__/

''')

squirtle = ('''
      Squirtle
         ___
    _.-~~   ~~~-.
   /         _   ~.
  |#`       /#`    \
  
  |-'|      |-'|    |
  /--        --     |-.
  \__   .  .        / /\_  
   \ ~~--___---~~/\| |   ~-.
.---`~~--____---_)  \ \-__  \

) <    |__    __\_   \ \     |
~-.__ /   ~~~~   \   \ \     |
      ~-.   |     .~-.-' |    |
      | \___|___/     / /     | 
      | /   |   \     | |  /  |
      \     |   ~-___ \ \/  /
      /\__ / `._ /   ~-\ \_/
    /    \_____|      |`~
    |      |    |      |   
     \     |    |      |
      >______)   /_/\/\_\
''')

bulbasur = ('''
                 __....___ ,  .
               _.-~ __...--~~ ~/\
      
      Amw      / /  /          |  |
              | |  |            \  \
      
      __ _..---..-~\           |  | 
      |  ~  .-~-.    \-.__      /  | 
     /     \.-~        .-~-._/   // 
    |/-. <| __  .-\    \     \_ //  
    || o\   \/ /o  |    ~-.-~  \/         
    /  ~~        ~~              |      
    \__         ___--/   \  _-~-  \ 
    / ~~--.--~~    /     |/   __  |
    |/\ \          |_~|   /    \|  |
    |\/  \__       /_-   /\        |
    |_ __| |`~-.__|_ _ _/  \ _ _ _/
    ' '  ' ' ''   ' ' '     ' ` `
''')

images = [pikachu, squirtle, bulbasur]
vida_usuario = int(80)
vida_pc = int(80)

# elegir pokemon a base de una lista
usuario_pokemon = int(input("Que pokemon tu eligues: [0] Pikachu, [1] Squirtle, [2] Bulbasur.\n"))

pc = random.randint(0, 2)
print(f"Pc:{images[pc]}")

def rand_dmg(hp):
    min_dmg = 1
    try:
        max_dmg = int(hp / 2)
    except:
        return 0

    try:
        return random.randint(min_dmg, max_dmg)
    except:
        return min_dmg
#mientras no se termine el juego sigue el bucle
end_game = False
while end_game == False:
    attacks_count = 0
    while vida_pc > 0 and vida_usuario > 0:
        if attacks_count % 2:
            vida_pc -= rand_dmg(hp=vida_pc)
            print("Te atacaron con Placaje!\n")
        else:
            vida_usuario -= rand_dmg(hp=vida_usuario)
            print("Te atacaron con Araniazo!\n")

        attacks_count += 1
        print("vida_pc", vida_pc)
        print("vida_usuario", vida_usuario)
        attack_usuario = None
        #turno usuario
        while attack_usuario != "P" and attack_usuario != "A":
            print('Tu turno:')
            print(images[usuario_pokemon])
            attack_usuario = input("Que ataque quieres usar [A]araniazo, [P] placaje ?")
            if attack_usuario == "A":
                print(f"Usas Araniazo!")
                vida_pc -= 10
                print(f"la vida de Pc es: {vida_pc}, Tu vida es:{vida_usuario}\n")
            elif attack_usuario == "P":
                print(f"Usas Placaje!")
                vida_pc -= 12
                print(f"la vida de Pc es: {vida_pc}, Tu vida es {vida_usuario}\n")
        if vida_usuario <= 0:
            print('Pc Gana !!!\n')
            end_game == True
        elif vida_pc <= 0:
            print("YOU WIN !!")
            end_game == True