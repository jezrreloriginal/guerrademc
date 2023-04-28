# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("mcpi")
define b = Character("mcchi")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cenario

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mcchi



    b " vcs viram minha nova musica ?"

menu:

    "sim eu já vi":
        jump choco1

    "não eu não vi.":
        jump choco2


label choco1:
    show mcchi

    b "então vc sabe, que eu tomei a coroa, não como mais pipoka agr é sushi !."
   
    jump mcpi
    

    
label choco2:

    hide mcchi
    show mcpi
    
    a "nem vai ver, essa ai é a famosa flopadona."

    jump mcpi

label mcpi:

    hide mcpi
    show mcchi
    b "falou galera fui "

 

label mccpi:
    show mcpi 
    a " rala recalcada "

    return
