#%%
print("Hello!")


def user_name():

    name = ''
    while name == '':
        name = input("What is your name?: ").capitalize()

    if name != "":
         return ("Welcome," + ' ' + name)

print(user_name())


def Dog():
    
    doge = input("Do you like dogs? ")
    
    if doge == 'yes':
        print("Me too, this is a picture of my dog")
        print('o____')
        print(" ||||\ ")
        return ' '
    
print(Dog())

#%%
def animil():
    
    animals = input("Do you like other animals? ").capitalize()
    
    if animals == 'Yes':
        fave = input("what's your favourite type of animal? (farm, wild or pet) ")
    if fave == 'farm':
        print('   ________')
        print('  /        \ ')
        print(' /     #    \ ')
        print("/            \ ")
        print(' |    ##    |')
        print(' |    ##    |')
        print(' |   ____   |')
        print(' | # |  | # |')
        print(' |   |  |   |')
        print('Me Too!')
        return ' '

    elif fave == 'pet':                
        print('   ___      ___  ')
        print('  /   \    /   \ ')
        print(' /     \  /     \ ' )
        print('(       \/       )')
        print(' \              / ')
        print('  \            /  ')
        print('   \          / ')
        print('    \        / ')
        print('     \      / ')
        print('      \    / ')
        print('       \  / ')
        print('        \/ ')
        print('Me Too!')
        return ' ' 

    else:
        print('           ___')
        print('          |    \ ' )
        print('          |     \ ')
        print('          |      \ ')
        print('  o       |       \ ')
        print('  ( o     |        \ ')
        print(' ___)_____|         \ ')
        print('(                    \ ')
        print(' |_                   \ ')
        print('   |_                  \ ')
        print('     |____              ------------- ')
        print('     /    /              ')
        print('    /     \     ')
        print('Me Too!')
        return ' '
        
print(animil())

#%%
def origin():
    
    city = input("Where do you live? ").capitalize()

    if city == 'Bristol':

        print('_____                             _____')
        print('|___|\                           /|___|')
        print('|   | \                         / |   |')
        print('|   | |\                       /| |   |')
        print('|   | | \                     / | |   |')
        print('|   | |  \                   /  | |   |')
        print('|   | |  |\_________________/   | |   |')
        print('|   |_|__|___|____|____|____|___|_|   |')
        print('       |                       |')
        print('       |                       |')
        print('       |                       |')
        print('       |                       |')
        print('       |                       |')
        print('       |                       |')
        print('       |                       |')  
        print("That's where I'm from too!")
        return ' '

    elif city == 'New york':
        print('''                       /\  ____ 
                       <> ( oo )
                       <>_| .. |_
                       <>    @   \ 
                      /~~\ .  . _ |
                     /~~~~\     | |
                    /~~~~~~\/ __| |
                    |[][][]/ /  [m]
                    |[][][[m]
                    |[][][]|
                    |[][][]|
                    |[][][]|
                    |[][][]|
                    |[][][]|
                    |[][][]|
                    |[][][]|
                    |[][][]|
                    |[][][]|
                    |[|--|]|
                    |[|  |]|
                    ========
                   ==========
                   |[[    ]]|
                   ==========''')
        print('Wow! What a great city to live in!')
    return ' '
    

print(origin())
#%%

def hobby():

    choice = input("Do you like sport? ").capitalize()
    if choice == 'Yes':
        sport = input("What is your favourite sport? ").capitalize()

        if sport == "Netball":
            print("You don't deserve an image")

        elif sport == "Hockey":
            print('                                  ')
            print('                                  ')
            print('                        /\  ')
            print('                       /  \ ')
            print('                      /  /   ')
            print('                     /  /    ')
            print('                    /  /     ')
            print('                   /  /      ')
            print('                  /  /      ')
            print('                 /\ /        ')
            print('                /  \         ')
            print('               /  /          ')
            print('              /  /           ')
            print('   ____      /  /           ')
            print('  /__  \    /  /              ')
            print(' .*  *. \__/  /               ')
            print(':      :     /                ')
            print(' *.__.*_____/                     ')
            return ' '

        elif sport == "Football":

            print('''''                                                                      
          ____        ____          
         /    \______/    \       ######                                                     .mMNh  
         \    |      |    /      ########                                  oo:               +NMNN. 
          \  /        \  /       ###                                       :NNd:            .mMNNm  
           \ \        / /        #######                                    dNMm:           sMMNNo -
            \ \      / /         ########                                   dNMNo :+       /NMNNh -d
             \_\    /_/          ###  ###                                  +NMNN+ +No     -mMMNd..hM
                \  /             ###  ###                                 -mMMNN- hMd    .hNMMd-.hNN
                /  \             ########                                .dNMMMs /NMh    hNNMd-.hNNm
              _/____\_            ######                                -dNNNNh`-mMN+  .hNNNd.-dNNd-
                                .-----                                 :mNNNNy.-dMNy` .hNMNy.:dNNy. 
                       :hy.   :hNNNNNNmmhyo/-                         omNNMN+:mNNs -dNNNo +NNd/:+ 
                       -hMy+++yNN     NNMNNNNmdhs+:-...-+h.         -hNNNNd: omNN+  +mNNh-.yNm+-sNo 
                    /ymNNMNNNNNNNd   oyNNNMNMNNMNNNNNmmmh:         omNNMmo -yNNd: .yNNNo./mms./dNs  
                   shs+/oNd   omNNNNNNMNMNNNNMNsosyso+:.         :dNNNNy- +mNNs. +mNNh--yms-:hNNs   
                      ..oMs:/ohNNNNNMMNMMNNNNNNNh-             :yNNNNh: /hNNh- -hNNd/-sdo-:yNNm+    
                     -sdNdyyso+/:/+smMMNMNNNNMMNNh           :yNMMNh: /hNNh:`.sNMmo-+y+.:hNNNh:     
                .--.  /ms.          .yNMNNNNNMMMNm.        /hNNNNy:./hNNh/ .omNms-/s:./hNNNmo       
           .:/shmmdyyyms:.           :NNMNNMNMMMMd.     .+dNMNdo--odNmy: -smNms. ---+dNNMms.        
           .+syyo/+yy+hNNNh/+s.      oNMNMNNNMMMN/    -smNMNh/.:smNdo. :ymNd+.   :ymNNMms-.o-       
               :ymNm- .sdmNds-     .sNNNMNNNNNNd:   :ymNMNy:./hNmy/ .+dNmy:   -odNNMNmo-.omh        
              oNNNh/     ...      /dNNNNNNNNMNs.  /hNNNdo--odmh/..:ymNdo-  ./hmNNNNh+.-smNh.        
              sNN+             .+dNNNMNNMNMNh:``+dNNNd+.:ymh+-`:odNds:``./ymNNNNms:./ymNNs.         
               -/            -smNNNNNNNNNNd/  :hNNNd+.:yho-.-odNms:. -+ymNMMNmy/.-odNNNh:           
                          ./hNMNNNNNNNNNmo. .sNNNNo.:ys:.-+hmms:..  smNNNNNh+--/ymNNNd/             
                        -smNNNNNNNNNNNNy-  -dNNNd:  -.-+hmmy/:/ohm/ oMNmy+--/ymNNMNh/ .-            
                      /hmNMNNNMMNNNNNmo   .dNMNh-   :smNNhshdmNNNy..sy/-:+hmNNNNms:.:yd:            
                   .+dNNNNNNMmhNNMMNm:    hMNNy   -yNNNNMNNNMNmy/   :/ydNNNNNmy/--odNd:             
                  +dNNMNNMNms/yNNNNm/    +NMNh.  /mMMNNNNNmds/--:+  dNNNNNds/--+hNNNs.              
                /dNNNNNNNNh-.hMMNNNo    .mNMm-  /NNNMNNyso+oshdmNs -mNdy+::/sdNNNms-                
              .sNNNNNNNNNo  yNMNMMm.    sNNN+  -mNMMNNNmmNNNNNds:  ++/:+shmNNMNdo-                  
             -hNMNNNMNNN+  +NNNNMMy    -mMNh  .dNMMMNNNNmdhs/-...  ohdNNNNNNms:..:o                 
            -dNMNNNNNNN+  .mNNNMMMh    sNMm:  sNMMNNNMmysosyyhddy.-NNMNNmds:.-/ydy-                 
           .dNNMMNNNNNh   /NNNNMMMm.  :mNN+  oNMMMNNNNNNNNNMNmh+.-hmdho/--:ohmNh/                   
           yMNNNMMNMNN+   sMNNNNMMNh/omMm+ -yNMNMMNNNNNdhhyo/.  .///:/oydmNNmy/                     
          :NMNNNNNNMNN:   sMMMNNNNNNMNho::smNMMNNNNNNNmhysoooo- +hdmNNNNNmh+-                       
          sMNNNNNNNMNN:   +NMMNNNNNNMmyydNNNNNMNNNNNNNNMNNNmh/ :mNNMNmdy/-.:-                       
          dNNNNNNNNNNN+   -mNMNNNNNNNMNNNNNNNNNMNNNNNNdyso:..-+dmdyo/:-:oyds.                       
          dMMNNNNNNNNMh    sMMNNNNNNNNNNMMmyNmodNNNNNNds/-   ---://oyhdmNd/                         
          yMMNNNNNNMNNN+   .dNNMNNNNNNNNNMd.hNh:/hNNNNNMNNdhso/:///:::::-.                          
          oNNNNNNNNNNNMm/   -dNNNNNNNNNNMNN+.hNd/.:sdNNNNMNNMNNNNmmdddhy:                           
          .dNNNNNNNNNMMNm+   -hNNMNNNNNNMNNm-.hNNy: .:shmNNNMNNMMNNNmh/.                            
           /mMNMNNNNNMMMMNy-  .sNMNNNNNNMMNNd: sNNNy:.:++++ossyyyo+:.                               
            /mNNNNMNNNNNNNNms-  :hNMNMNNNNNMMm/ :dNMNh+:+hdhs+:.                                    
             :dNNNNNNNNNNNMNNNh/. :ymNNNMMMMNNNy-.+dNNNmo::smNNmhs+:.                               
              .omNNNNNNNNNNNNNNNmho::odmNNMMNNMNmo..+dNNNNy:./hNNMMNmh+-                            
                -smNMNNNNNNNNNNNNNNNmhyhNNNNNNNNNNd/ .+dNNNNy- :smNNMMNNh+.                         
                  .+hNNNNNNNNNNNNNMMNNNMNNNNNNNNMMNNh+. /hNNNms. -smNMMNNNms.                       
                     -+ymNNMNNNNNNNNNNNNNNNNNNNNNNNNNNmo-./hNMNd-  -yNMNMNNMm/                      
                        .:ohmNNNMNMMMNNNNNNNNNNNNNNNNMMMm+  +mNNm-   +mNNNNMNNy                     
                            .-/oydmNNNNMMNNNNNNNNNNNNNNNN+   .yNMd.   -hNNNMMNMy                   
                              +yo:::/+sydmmmNNNNNNNNNNNNN/     sNNo     sNNMMMNNo                   
                              hMNNmdyo//- ..-:sNNNNNNNNNNo      yNd      oNMMNNMN-                  
                             .mNNNNNNMNNm.    .dNNNNNNNMMd      -NN.      sNMMNNN+                  
                             oMMNNNNNMMMN/     +MNNNNNNNNN+      hN.      .dMNMMMs                  
                            .mMNNNMMMNNNMy     :NNNNNNNNNNN/     sh        /NNMMNs                  
                            yNNmsdNMMMNNMN:    :NNNNNNNNNNNNo.   o/         dMMMM+                  
                           -s+: :NNNNNNydNd-   +NdoNMNMNMmmNNd+.            sNMMN-                  
                               .dMNNNNm. -oo   o/. dNNNNMh.:+sso.           /NNMs                   
                               yMNMMMNo            +NNNNMd                  :NNd.                   
                              sNNNNNNs`            .mNNNMN-                 sNm-                    
                             oNNMNNNo`              sMMNNM+                 hd-                     
                            oNNNMNm:                -mNNMMh                :y.                      
                           sNNNMNy.                  oNNNNN:                                        
                          yNNNNm/                     dNMNNy                                        
                        .hNMNNy.                      -mMMMm-                                       
                       -dMNNm+                         /NNNMs                                       
                      /mNNNd-                           oNNNN/                                      
          -oyyyo:-  -yNNNNs`                   :+o+:.    sMMNm:                                     
      /syydNNNNNNNNmNNNNMNyoo+oo+/.        .:/oNNNMMNmdyshMMNNNy//////:.                           
     sNh+:+dNNNNNmmmmmmmmmmmmNNNNNN/      /mmhydMNNNNNNNmmmmmmmmNNNNNNNNd-                          
      -  sNNy/-.              .-omd-      -o. sNNho/--..         ..-:odNh.                          
         -o/                     .            /h:                     `-  ''''')
            return ' '

    else:
        gamer = input("Are you a gamer? ").capitalize()
        if gamer == 'Yes':
            game = input("What's your favourite game? ").capitalize()   
            if game == 'Fortnite':
                print('''                                
                      :dN:                            `  ` `   .-:hd+`                              
                       yNyssyyyyyhhyhyhhydhhdyddhdydmhmddmhdhyhddmmmmh-//-.````             `.`     
                     `:ymhhhddddhyhddddhyysyhhhhhhhhhhsoooooooooooyysoosmhoo+++//:--.  `..:syys     
                     `:oNhoooooooooooooooooooooooo+ooooooooooosssssossssmmdyoosoooooooooooosddh     
    `/o/::-:----::::/yhdmysssoooossoosssosssssssssoooooooooooosssssssyyymNmssssyyyyyhyyoooohddo     
    .yhyso+s+/:::::-:so++/oooooooosoososyyyyyysosyyyyyyhhhhhhyyhhdmdhhhymhyyyyyyyso///sssssddd/     
                          ::::::::---....````   :/+syhhhhddhy:-/o/hhh+```  ````       -oyyyddd-     
                                                   :yyyyyyhyy...:sdddds.                `/hddd`     
                                                   `.:yyssso/----.:hdddh:                .ydds      
                                                     +ddhdh.       ohdddh/                          
                                                    -yhyhhs         -dhdds                          
                                                    -yhyyhy-         `/:-.                        
                                                                            ''')

            elif game == 'Pacman':

                print('                     ##########                                   #######          ')
                print('                ####################                         ##################    ')
                print('             #########################                      ####################   ')      
                print('           ########################                        #####     #####     ##  ')
                print('          ######################                           ####    ######    ###   ')
                print('         ####################                   @@@        ####    ######    ###   ')
                print('         #################                     @@@@@       #####     #####    ###  ')      
                print('         ####################                   @@@        ######################  ')                 
                print('          ######################                           ######################  ')
                print('           ########################                        ######################  ')
                print('             #########################                     ######################  ')
                print('                ####################                       ####  ####  #####  ###  ')
                print('                     ##########                            ##     ###  ###     ##  ')
                
            return ' ' 

        else:
            spare_time = input('What do you like to do in your spare time?')
            if spare_time != '':
                print('How interesting!  I would love to try that one day!')                
            return ' '

print(hobby())
#%%


def miniGame():

    quiz = input("Do you want to play a game?").capitalize()
    if quiz == 'Yes':
        import random
        number = random.randint(1, 100)
        print("Hi, I'm thinking of a number between 1 and 100.")
        num_guesses = 0
        
        while num_guesses < 6:
            guess = input("enter a guess: ")
            guess = int(guess)
            num_guesses += 1
            if guess < number:
                print("That was too low")
            elif guess > number:
                print("That was too high")
            else:
                break
        if guess == number:
            print("#1 Victory Royale! You guessed correctly! Well done")
        else:
            print("STOOPID!")
            print("The right number was", number)
        
        return ' '

print(miniGame())    
#%%


def meme():
    end = 0
    end = input("Thank you for your time! Did you enjoy this experience?: ").capitalize()
    if end == 'Yes':
        print(''' 
                                                                            hhhhdddhhhhhhddh   
                                                                           dddddddmmmmmmddmmmmdh 
                                                                         ddmmdddmmmmmmmNmmmNNNNNmdh
                                                                        dmmmmddmmmmmNmmmmmmmNNNNNNNmmd
                                                                       dmmmddddmmmmmmmmmmmmmmmmmmmNNNNmh
                                                                     ddmmmddhhddddmmmmmmmmmmmmNNNNmmmNmmd
                                                                   dmNNmdhhysssooyhhhhyyhhdmmNNNNmmmmmmmmd
                                                                  hmmNNNdysooo+++++osso++oosyhdmmmmmmmmmmNm
                                                                 dNNNNmyso+++++///++++++++++oydNmmdmmmmmNNdd
                                                                dmNNNmdso+++++//////////++++oshmmmmmmmmmNNmd
                                                                dmNNNmhso+++++++////////+++++oymmddmmmmmNNNm
                                                                dNMMNdysoo+o++++++//////+++++oydmddmmmNNNNNN
                                                               dmNNMNdysoo+++++++++///+++++++osdmdddmmNNNNNN
                                                              dmNMMmdyoo++++++++++////////+/+shmddmmmNNNNNNN
                                                              dmNMNmhsooooo++++++++//////++++shmddmmmNNNNNNN
                                                             ddmNMNdyssyyyyyyssooooososssssssyhmddmmNNNNNNNN
                                                             dmmNNmhsossyyhhhyysooosyyhhhhyyyyyddmmmNNNNNNNN
                                                             dmmNNmhsooooosoooooo++ososssssssssydmmmNNNNNNNNN
                                                            dmmmmmdhso+++oo++++o++++++++++ooooosdmmmmmNNNNNNNN
                                                            dmmmmmdhyooo+++++ooo+++++++++++oooosdmNNmmNNNmNNNN
                                                            mmmmmmmdysooo+++oooo++++o+++++++oosydmNNNNNNmmNNNN
                                                            mmmmmNmdhysooooooooo+++++ooo++++osyhdmNNNNNNmmNNNN
                                                            NmmmNNmmddyssoooosyysssyyssooooosyhdmNNMNNNNmNMNNN
                                                            mmmmNmmmmmdyssssssyhhhddhsssssssydmmmNNMNNNNNNNNNN
                                                            dmmNNmmmmNdyyyhdddddhhddhhdddhyyhmmmmmNMMNNNNNNNN
                                                            dmNNmmmmNmhyhddddddhhdddhhdddyhdmNmmmNMMNNNMMNNN
                                                            dmNNmNNNNNmdhysssssssssssosshhhdmmmNNNNMMNNNMNN
                                                            dmmNNNNNNmmmdysssssssyyysssyhddmmmNNNNNMNNNNMNNN
                                                            ddmNNNNMNmmmmdssssyyyyysyyhhdmmmNNNNNNNNNNNNNNNNN
                                                             dmNmmNNMmddmmhhyyhhhhhyhddmmNNNmmmmNNNNNNNNNNNNN
                                                              dmmmNNNmhyhdmddddddddddmmNNNmmddhdmNNNNNNNNNNNN
                                                               dmmmmmmysshmmmmmmmmNNNNNNmmdhysyhmNNNNNNNNNNN
                                                                dmmmmmmysshmmmmmmmmNNNNNNmmdhysyhmNNNNNNNNNNN
                                   yyyyyyyyyyyyyyyyhhhhyhhhhhhhdddddmmdsooshdmmmmNNNNNmmddhysssshdmmmmmmmNNNNmmmdddhhhhhhhhhhhhh
                                 yyhhhyyyyyyhyyyyyyyhhhyhhhhhhhdddddmmhsooosydmmmmNNNmmdhhyssssshdmmddmmmmmmmmddddddhhhhhhhhhhhhhh
                               yyyhhhyyyyyyyyyyyyhhhhhhhhhhhhhhddddddmdhysossyhhdmmddhhyysssssshddmddddddmmmdddddddddddhhhhhhhhhhhhhhhhyy
                              yyhhhhhhyyyyyhhhhhhhhhhhhhddddhhhdddddddmmmmdddddhddddddddddddmmmmmddddddddddddddddddddddddddhhddddhddddddddh  
                             yhhhddhhhhhhhhhhdddddddddddddddddddddddddmmmmmmmNNNmmmmmmmmmmmNNNNdddddddddddddddddddddddddddddddddddddddddmmdhy
                            yhhdddddddddddddddddddddddddddddddddddddddmmmmmmmmmmmmmmmmmmmmmmmmmdddddddddddddddddddddddddddddddddddddddddmmmddhhh
                           yhhdddddddddddddddddddddddddddddddddddhdddddmmmmmmmmmmmNNNmmmmNNmmmddddddddddddddddddddddddddddddddddddmmmddmdddmmddhh
                          yhhddddddddddddddddddddddddddddddddddddddddddmmmmmmmmmmmmmmmmmmmmmdddddddddddddddddddddddddddddddddddddmmmmddmmdmmmmmddh  
                         yhhhddmmmmddddddddddddddddddddddddddddddddddddmmmmmmmmmmmmmmmmmmmdhdddddddddddddddddddddddddddddddddddmmmmmmmdddmmmmmmmmhy
                        yhhdddmmmmmmmmdddddddddddddddddddddddddddddddddmmmmmmmmdddddddddddhhdddddddddddddddddddddddddddddddddmmmmmmmmmdddmmmmmmmmmyo 
                       yhddddmmmdddmmmmmddddddddddddddddddddddddddddddddmmmmmmdddddddhhddhdddddddddddddddddddddddddddddmmmmmmmmmmmmmmmdddmmmmmmmmmhs 
                      yhhdddmmmmddddddmmddddddddddddddddddddddddddddddddddddddddhhdddhhddddddddddddddddddddddddddddddmmmmmmmmmmmmmmmmmddddddddmmmmdhy 
                    yhhdmddddddddmmddmmmddmmmddddddddddddddddddddddddddddhhhhddddhhhhhhhhhddddddddddddddddddddddddddddmmmmmmmmmmmmmmmmmddmmmmmmmmmmdh  
                   yhdddddddddmmmmdmmmmmmmddddddddddddddddddddddddddddddddhhddddddddhdhhhdddddddddddddddmdddddddmmmmmmmmmmmmmmmNmmmmmmmmmmmmmmmddmmmdhy 
                  yhddddddmmmmmmmddmmmmmNmmmmmddddddddddddddddddddddddddddhddddddddddddhhddddddddmmmddddmmmmmmmmmmmmmmmmmmmmmNNmmmmmmmmmmmmmmmmmmmmmmmd
                 yhdddddmmmmmdmmmmmmmNNNmmmmmmmmmmmddddddddddddddddmddddmdhdddddddddhddddddddddmmmmmdddddmmmmmmmmmmmmmmmmmmmmN   mNmmmmmmmmmmmmmmmmmmmmd
                yhddddddmmmmmmmmmmmmmmmmmh dmmmmmmmmmmmdddddddddddddmmdddddhhhhhhhddddddddddddddmmmddmmdddmmmmmmmmmmmmmmmmmmmmN    NNmmmmmmmmmmmddmmmmmmddd 
               yhhdddddmmmmmmmmNNmmmNmmh   dmdmmmmmmmmmmdddddddddddmmdddddhyhdddhhdmmdddddddmmmmdddddddddddmmmmmmmmmmmmmmmmmmmNd   dmmmmmmmmmmmmmmmmmmmddddd 
              yhhddddmmmmmmmmmmmmmmmmNmh    hdmmmmmmmmmmmdddddddddddddddmmmddhdddddmmdddddddddddddddddddddddmmmmmmmmmmmmmmmmmmmNm    ddmmmmmmmmmmmmmmmmmdddddddh 
             yhhdmddddddddddmmmmmmmmmmd      hdmmmmmmmmmmmddddddddddddmmmmmmmmdddddddddddddddddmmmmmmmmddddddmmmmmmmmmmmmmmmmmmmNmd     dmNNmmmmmmmmmmmmmdddddd 
            yhdddddddddmmmmmmmmmmmmmdh       hhdmdddddddddddddddddddddddmmmNNNNmNmmmmddmmmmmmNNmmmmmmmmmmmddddmmmmmmmmmmmmmmmmmmmmmmm     hmmmmmmmmmmmmmmmdddddmmdd
           hdddddddddddmmmmmmmmmmmd        hdmdddddddddddddddddddddmddmmmNNNNNNNmmmNNNmNNNNNNmmmmmmmmmmmdddddmmmmmmmmmmmmmmmmmmmmmmmdd      mmmmmmmmmmmmmddddmmmd 
           hdddddddddddmmmmmmmmNmd         hdmmdmmmmddddddddddddddddmddmNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmdddddddmmmmmmmmmmmmmmmmmmmNNNm    dmmmmmmmNmmmmmmmmmmmmmdd
          yhddddddddmmmmmmmmmmNmdh       hdmmmmdmmmmdddddddddddddddddmmmNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmmddddddmmmmmmmmmmmmmmmmmNNNNNNmd    dmmmmmmmmmmmmmmmmmmmd 
         hhdddddddmmmmmmNNmmmmmd         ddmmdmmmmmmdddddddddddmmmmmdmNNNNNNNmNNNNNNNNNNNNNNNNNNNNmmmmmmmmddddddmmmmmmmmmmmmmmmmmNNNmmmmdd     dmmmmNNmmmmmmmmmmmddd
        yhddddddddddmmmmmmmmdhh         hddmmmmmmmmmdddddddddmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmddddddmmmmmmmmmmmmmmmmmmmmmmmmmdd     dmmNNNmmmmmmdddmmmdd
        yhddhhdhddddddmmmmdd            dmmmmmmmddddddddddmddddmmmmmNNNNmNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmdddddmmmmmmmmmmmmmmmmmmNNNmNNmmdd      dmNNNmmmmddddddddddhh
       ydddddddddddddmmmmdh            hdmmmmmmdddddddddddmmddddmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmddddmmmmmmmmmmmmmmmmmNNNNNmmmmmmmd     ddNmmdhyyyyyyyyyhhd
      yyyyyyyssssossyhdh              hdmmmmmmmddddddddddddddddmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmddddmmmmmmmmmmmmmmmmNNNNNmmmmmmmmdh     yyysssysssooossyhh 
        ooo+++++++/+oos               dmmmmmmmddddddddddddddddmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmNNmNNNNmmmmmmmmmdh     hhyhhhhysoooosyyy
        oooooosssssssss             hhdmmmmmmmmmddddddddddmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmNNmmmmmmddmmmdd    hhhhhhhysoooosyyy
        ooooossyyss                 hdmmmmmmmmmmmddddddmddmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNNNNNNNmmmmmmmmmmNNNmmmmmmmmmmmmmmmmmdmmdddh   hhhhhhhysoosssyy
        soooos                       hhdmmmmmmmmmmmmmmddmmmmNNNmmmmmmmNNNNNNNNNNmNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmmmmmmddhhhhhh  hhhhhhyysssyyyyy
        sssooss                     hddmmmmmmmmmmmmmmmmmNNmmmmmmmmmmmmmmmmmmmmmNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNmmmmmNNmmdh
        ssssssyyyyyys                hdmmmmmmmmmmmmNNNNmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNNNNmmmmdh
        ssssyyysssyyyyy               hmmmmmNmmmNmmmmmmmmmmmmmmmmmmNmmmmmmmmmmNNNNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdh
          ssssssssssssss               dmddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNmNNNNmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd
                                      yddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNdhyhdmmNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdd
                                      hdmdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmNNmNmdyy    ddmNNmmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd
                                      yhdddmmmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNmNmy       ydmNNmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd
                                      yhddmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNNNNdy         yhmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy
                                      hdmdmmmmmmmmmmmmmmmmmmmmmmmmNNNNNNNNNmdhy           shdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy
                                      hmmmmmmdmmmmmmmmmmmmmmmmmmmmmNNNNNNNmhs               ydmmmNNmmmmmmNmmmmmmmmmmmmmmmmmmmmmmmmmh
                                      hmmmmmmdmmmmmmmmmmmmmmmmmmmmNmNNNNNmhys                 yhdmmNNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy
                                      ydmddmmmmmmmmmmmmmmmmmmmmmmmNmmNmNNdy                     sydmNmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdhy
                                      yhmddmmmmmmmmmmmmmmmmmmmmmmmNNNNNmdy                        shmNNNmNmmmmmmmmmmmmmmmmmmmmmmmmmmmdy
                                      ydmmmmmmmmmmmmmmmmmmmmmmmmmNNNNNdys                           ydmNNNmmmmmmmmmmmmmmmmmmmmmmmmmmmdhs
                                      shmmmmddmmmmmmmmmmmmmmmmmmmNNNmdys                            ydmmNNNNNNNNNmmmmmmNmmmmmmmmmmmmddhy
                                      sdmmmmddmmmmmmmmmmmmmmmmmmmNNmdy                               hdmmmmmmNNNNNNNNmmmmmmmmmmmmmmmmmmdy
                                     symdmmmmmmmmmmmmmmmmmmmmmmmmmmhy                                  hmmmmmmmmNNNNNmmmmmmmmmNNNNNNmmmmdhy
                                     yhmddmmmmmmmmmmmmmmmmmmmmmmmhys                                    mNNNNmmmmmmmmmNNNNNmmmmmmmmmmmmmmdhy
                                     yddddmmmmmmmmmmmmmmmmmmmmmmmss                                     hmmmmmmmmmmmmmmmmNNNNNNmmmmmmmmmmmmhs
                                    shddmdmmddmmmmmmmmmmmmmmmmmmds                                       hmmmmmmmmmmmmmNmmmNNmNNmNNmmmmmmmddyy
                                    yhddmmddddmmmmmmmmmmmmmmmmmdyo                                        hdmmmmmmmmmmmNdmmmmmmmmmmmmmmmmmmmhys
                                    yhddmmmmmmmmmmmmmmmmmmmmmmmhs                                         shmNNNNNNNmmmmmmmmmmmmmmmmNNmmmmmmmdhh
      ydmdydhs++ddhhd              shdddNmyshMNmdmmmmmmmmmmmmmdys                                         hdmNNNhooMNNmmmmNNNNNNmmmmmmmmmmNMoohmh     y+oh                        my
       yds./ymshdo-:mdyossssoosyyyyydmmmNh  sMNmmNNNmmmNNNNmmdhys                                         o+sNMMs  MNNNNmNMm++mNNNmNNmNNmmNM  omhyy   d  dN                     ms  Mh
        sN+  yNN+  hNmdyssshdhNdysdNNmhodh +NNyyhdymNNmysyhmNdyooyNs  dysyhmmmhohhyyNmdyssyddhsmdhssshmmds  :sNMs  mhsydNNdo  +ydMNdhyyymNNM  omy  ydMdyydMdsyhysshddsddhssyhysNMs  Mh
         +No  h/  dMMs  /o   sMy  sMMh  omMNMd     mdo     .dmho+yms       +mdo     N+.     omMs:      ydo  :omNs       +md+  +ydMo      omM  om   omMo  sMs  *     dMy        mNs.  Mh
          yms-  +hmmd  oNhmo  Ny  sMMd  smNmNd  +NNNo  hdh+  dho+yNs  Ndmd  yho  dmmd   hds  oMdhhddo  oMN     Ns  NMNh  hMd     Mdhhdd   sM      hdhmo  sMs  yMNy  sM/  NdNs  mNs  Mh
           yho  dhsdy  sNoms  Ny  yMMh  omNmNd  +MMm+     o+omh++yNs  Mdmm  sho  mmdh       oyM/       oMN  +MhNs  MMMd  hNd  dMNm        sM   o   ddmo  sMs  yMNs  oN:  MyNs  mNd  Mh
           sys  dh+sM+  yho  +Md/  dho  smmdmd  +MNNy   hhhsmNh++sms  ohy+  ddo  mmhN   yhhshNN   hh/  +MN  :hmMs  MMMd  hNd  sdmh  ohy   sN  omd  +dMo  sMo  yNmy  oN+  ohy/  mNd  My
           shy  mh//ydy    oymydho    o smNmmd  sMmmmds    oddy++smy      +dNms  mhshds    +ymNy    s  oNM     Ny  NNMm  dNN     Ns      sM/  NMd  +ms:  Ms//yMNy+  Mmy+       Myd  My
           /oydhhhs//++syhhhys+/+oydmmNNmNmmmNNNNNNmmmmmNNNNdso+++ohhhddhddhsyhddhhs++ssyhddyso+shdhhdddhdhyhhdhddddddmNNNNNNNNNNNNNNNNNNNNNNNNNNmNNNNNNNMMNNNNNNNNNNNNNhoyyo  /Mddddd
                                  ohdddddddddmddddddmmdddmdy                                                        oydNmmmmmmmmmmmmmmmmmmmmmdmmmmNmmmmmNmmmmmm                 Md  My  
                                  shhddddddddddddddddddmdhy                                                           oymmdmmmmmmddmmmmmmdmmNmmmNNddmmNmmNNmmmmmdd               omyo  
                                  syhhhddddddmmmmmddddmdhy                                                              ydddmmmmmmmmmddmmdmmNNNNNmdmmNNNNMNNNNmdddmN
                                  oyhhhhhhddddddddddddddys                                                                 ooshdddddddddddmmNNNNNNNmmmmNMMNNMNNmmmNNMM
                                  yhhhhyyhhhhhhhhddhhhhhhys                                                                  +oyyhhddddmmmmmmmNmmmmmdddmNMNNNNNNmmmmNNNN
                               yhhhhhhhhhhhhhhhhhhhhhhhhhhhy                                                                   yhhdmNNNNNNMNNNNNNNNmdmmmmmNNNMMMNNNNNNNNN
                            yyyyhhyyhhhhyyhhhhhhhhhhddddddhys                                                                    mmNNMMMMMMMMMMMMMMNNNNNmdmmNMMNNNMMMMMNNM
                           yhhhdddddddddddddddddddddmmmmdddhy                                                                   hmNNMMMMNNMMNMMMMNNMMMNNNNNNNMMNNNNNmdddmmNN
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ''')
    else:
            print('''                                                                                           
                                                                                                                                                   oso/----------------:::::::--:------....................``...........---------------------------------::-:::-::::::::--------.----:----...``                   
                                                                                                                                                  ys/::::::::::::::::://///////::::::----------.................--------:-::---:::::::::::::::::::::::::::::::::::://:::::::::::::-:::::::://:.`                
                                                                                                                                                  ys/::::::::::::-::::////////////:::-------::--..........---------------------:::::::::::::::::::::::::::::::::::::::::::::::::--::::::////////.               
                                                                                                                                                 yyo::::::::::------::::://////////:::::::::::--.----------------------:------:::::::::::::::::::::::::::::::/:::///::::::::::::::::::://////////-              
                                                                                                                                                yhy+:::::::::::::---:::::::::////////::::::::---.---:::::-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://///////+/`             
                                                                                                                                               yhhs:::://://:::::::::::::::::::://///:::://::-----:::/:::::::::::////////////:///::::::::::::::::::::::::::::::::::::::::::::::::::::::///////////.             
                                                                                                                                               yhho::://////::::::::::/::::::::::///////::::-----:://///::///////////+++++++///////////////:::::::::::::::::::::::----::::::::::::://////////////+-             
                                                                                                                                               yhy+:://++++++///////::////////::://////::::-----::://///////////++++++oooo++++++++///////////:/:::::::::::::::-:-:------::::::::/:://///////////++-             
                                                                                                                                               hhs/::/+oooooosssso++++/////////////////:::::---:::////++++++++++oooososoooooo++++//////////////////::::::::::::-----------::::::/://////////////++-             
                                                                                                                                              yhyo:::///+++/+sssysssso++++++///////+///:::::-----::://++++++++ooooosssssooo++++//////////////////////://///::::::------::::::::////////////////+++-             
                                                                                                                                             hhs/-:::::///::+oooooso+//++++++++/++++//:::-------::://++++++++ooosssooo++////:::::::::::////////////////////////::::::--::::::///////////////////+-             
                                                                                                                                             yyy+----::::::::///++++//:://+++++++++///::---------::://++++++++ooosoo+///:::::------:::-::::://///////////++++//+///:::::::::::////////////////////-             
                                                                                                                                             ys+:-----:::::::::::::::::::://++++++//::-----------::://////+++++oooo+//::::::::------::-::::::::://///////+++++++//////::::::::://////////////////+-             
                                                                                                                                            sso:-------::::::::::--------:::::////::------...----::::////////+++oo+//::::::::::::---:::::::::::://///////+++++++++++////:::::::///////////////////-             
                                                                                                                                           ys+:--------::::::::::-----------:::::---------.-.----:::://///////++++///:://::::-------:::::/::/::///////////++++++++++++//////:::://////////////////-             
                                                                                                                                          yyo:-----------:::::::-----------::::------------------:::::////////++++/:::::::::::------::::////////////////+++++++++o++++++//////////////////////////-             
                                                                                                                                         yys/---------------:-----------:::----------------------::::::///////+////::////////////::::::://///+++++++////+++++++oooo++++++/////////////////////////-             
                                                                                                                                        yys/------------------------:::-::----------------------::::::::::////////://++++++//+oooo++++/////////++oooo+++++++++oooooo+++++++++/////////////////////-             
                                                                                                                                       yys+:-----------------------::::------------------------:::::::::://///////::://///::-:+sssssssooo+++/++//++ooooo++++++ooooooo+++++++//////////////////////-             
                                                                                                                                      yyyo:---------.---..--..--------------------------------:::::::::::://///////:::::::::-:/+ooossso+++ooooooo+ooossssooooooooooo+o+++++++/////////////////////-             
                                                                                                                                     yyyy/----------.-...........----------------------------:::::::::::::////////:::---------:://++++////+oosssssssssyyyyysssooooooo++++++++/////////////////////-             
                                                                                                                                     yyys:---------................-------------------------:::::::::::::::///////:::-----------:::::::////++ooossssyysyysyyssssoooo+++++++++/////////////////////-             
                                                                                                                                     yyyo:---------.........-.....--.---------------------:::::::::::::::::///////:::::---------::::::::///+++oooooo++++++oooooo++++++++//////////////////////////-             
                                                                                                                                     yyy+:----------........-......---------.---------------:::::::::::::::////:/::::::::------::::::/:////++++++++/////://///////////++//////////////////////////-             
                                                                                                                                     yys/:----------................--------.---------------::::::::::::::::/:::::::::::::-----::::::::////+++++++/////////://////////////////////////////////////-             
                                                                                                                                     yyo::-----------..-................-.-......-----------::::::::::::::::/:::::-:::::::::::::::::::::///////////////////://:://:///////////////////////////////-             
                                                                                                                                     yy+:----:-------..............----...-.......-----------:::::::///:::///::::::------::::::::::::::::::://:///////////:::::::::::::::::///////////////////////-             
                                                                                                                                      s+::-:::---------........--------.---........---------::::::::::://////::::--------------::::::::::::::::::::/::::::::::::::::::::::::::////////////////////.             
                                                                                                                                      o/::::::----------.....------::::----.......-------::-:::::::::::///+/+/:::------------------------------::::::::::-::::::::::::::::::::/:::////////////////.             
                                                                                                                                      o/:::::::-:-----------------::/++:-------------:::::::::---::::::://++++/::---------------------------------:::--:-:-::::::::::::::::/::/:://///////////////-             
                                                                                                                                      o/:::::::--:----------------::/++/----------::::////////:::::::::::/+++++/:-----.---------------------------:::::::::::::::::::::::::://////////////////////-             
                                                                                                                                      o/::::::::::--------------..-::://:::---::::://////++++++++///:::////++++//:--------------------------------:::::::::::::::::::::::::///////////////////////.             
                                                                                                                                      o+:::::::::::----------......-::::----:::::////++oossyyyyyyso////////++o++/::---...--.---------------------:::::::::::::::::::::::://///////////////////////.             
                                                                                                                                      o+:::::::::::--------........-----------::///+ossyyyhhhhhhhyso//////+++oo+//::---.....-------------------:::::::::::::::::::://:////////////////////////////.             
                                                                                                                                      so/:::::::::---------.....-..-------------://oosyyyyyyyhhyyyso+////++++oo+//:::-----------------------:::-:::::::::::://////////////////////////////////////.             
                                                                                                                                      oo/:::::::::------........-.----------.-----:/+ooooooooooooo++++//++++ooo+//:::::---------------------::::::::://///////////////////////////////////////////-             
                                                                                                                                      oo+/::::::::-------.......-.---------...-...--:://+++++++////////+++ooooo+/:::::::---------------------::::::://////////////////////////////////////////////-             
                                                                                                                                      sso/::::::::--------....-.-..--.............-----::://////////++++ooooo++//::::::::---------------::::::::::::///////////////////++/+///////////////////////-             
                                                                                                                                      yys/::::::::--------..-......-..................----:::::://////++++/////::::::::::-----------::::::::::::://////////////////////++/+++/////++//////////////-             
                                                                                                                                      yys/::::::---------...--.........................------:::::::::/::/://::::::::::::---------:::::::::::://///////////////////////////+++++++++++////////////-             
                                                                                                                                      yyy+::::::------------..........................------------:::::::::::::::::::::::------:::::::::::::////////////+////////++++++++++++++++++++++++++///////-             
                                                                                                                                      yyy+::::::------------.......-............-...--------------------::-:::::::::::::-------::::::::::////////+++++++++++++++++++++++++++++++++++++++//++++++//-             
                                                                                                                                      yyo::::::::-----------.......................--------------------::::::::::::::::---:::::::::::://///////++++++++++++++++++++++++++++++++++++++++/+++++/+//-             
                                                                                                                                      yys/:::::::-----------......................----------------:::::::::::::::::::::::::::::::::////////++++++++++++++++++++++++++++++++++++++++++++++++++////-             
                                                                                                                                      yys/::::::-----------.................-.....-------::-----::::::::::::::::::::::::::::::::::////////+++++++++++++ooooo++++++++++++++++++++++++++++++//+/+//-             
                                                                                                                                       yyy+:::::::------------------------.----....-------:::::-:::::::::::/:::::/::::::::::::::/:///////++++++++++++oooooooo++ooo++++++++++++++++++++++++++///+//-             
                                                                                                                                        yy+:::::::--------::::---------------.--------:::::::::::::::://///////:///://:::///::::://///++++++++oooo+++ooooooooooooo+++o++++++++++++++++++++++++////-             
                                                                                                                                        yyo:::::::---:::::::::::::----------------::::::::::::::::::://////////////:://///////:://///+++++++++oooooooooooooooooooooooo++++++++++++++++++++++++++++-             
                                                                                                                                        yyy/::::-::::::::::::::::::-::---------::::::::::::::::::::::///////////////////////////////++++++++++oooooooooooooooooooooooo++++++++++++++++++++++++++//-             
                                                                                                                                        yhy/::::--::::-----------::::/:::::::::::://////////////////////////////////////////////////++++++++oooooooooooooooooooooooooooo+++o++++++++++++++++++++//-             
                                                                                                                                         hh+-:-::::::-----........-----::::///////////////+++++++++++++///////////////////++++/////++++++++++ooooooooooooooooooooooooooooooo++++++++++++++++++++//-             
                                                                                                                                          ho::::::--------..............-----::::////+++++++ooo+++o++oo+++++++///////////++++++////++++++++++++++oooooooooooooooooooooooo+oo++++++++++++++++++++/+-             
                                                                                                                                          s/:-:-:----------..............--..-------:::////////+++o+ooooooooo+++//////++++++++///++++++++++++++ooooooooooooooooooooooooo+++++++++++++++++++++++++-             
                                                                                                                                          yy+:::::----------...................-...-----------:::::////+++ooooo+++/////+++++++////+++++++++++++oooooooooooooooooooooo+oo++++++++++++++++++++++++++-             
                                                                                                                                          yyo:::::------------.....................-------------::::::://////+++++///+++++++++/////++++++++++++oooooooooooooooooooooooooo++o++++++++++++++++++++++-             
                                                                                                                                          hhs/::::----:----------.-.............--------------:::::::::/::///++++////////++++//////++++++++++++oooooooooooooooooooooooooooooo+++++++++++++++++++++-             
                                                                                                                                          hyo:::::--:-----:--:::::::-------------------:::::::///////////++++/++/////////++//////+++++++++++++ooooooooooooooooooooooooooooo++++++++++++++++++++++-             
                                                                                                                                           hhs/::::--:-----::::://////////::::::::::::::::////////+++++++++++++++/////////////////+++++++++++++oooooooooooooooooooooooooo+o+++++++++++++++++++++++-             
                                                                                                                                            hho:::::::::::-:::::::://///++++++++++++///++++++++++++++++++++++//////////////////++++++++++++++++ooooooooooooooooooooooooo++++++++++++++++++++++++++-             
                                                                                                                                             hs/::::::::::-::-::::::::::::///////++++++++++++++++++++/////++//////////////////++++++++++++++o++ooooooooooooooooooooooooo++++++++++++++++++++++++++-             
                                                                                                                                              yo/::::::::::::::::::::-----:::::::////////////////////////////////////++++++++++++++++++++ooooooooooooooooooooooooooooooo++++++++++++++++++++++++++-             
                                                                                                                                               ys+::::::::::::-----------------::::::::://///////////////////////////++++++++++++++++o++ooooooooooooooooooooooooooooooooo++++++++++++++++++++++++++-             
                                                                                                                                                o+/::::-::::-----------------------::::::::://////////////////////+++++++++++++o+++oooooooooooooooooooooooooooooooooooooooooo++++++++++++++++++////-             
                                                                                                                                                 //:::--:::--------....---...---------::::::///////////////////++++++++++++oooooooooooooooooooooooooooooooooooooooooooooooooo++++++++++++++++/////.             
                                                                                                                                                 //::::---:-----..........-..----------:::::::///////////////++++++++++++oooooooooooooooooooooooooooooooooooooooooooooooo+ooo++++++++++++++++++///.             
                                                                                                                                                 ///::::::------......-......----------::::::://///////+++++++++++++++o+ooooooooooooooooooooooooooooooooooooooooooooooooo+ooo++++++++++++++++++///.             
                                                                                                                                                  //::::::--------------..-----------::::::::::///////+++++++++++++++oooooooooooooooooooooooooooooooooooooooooooooooooooooooo+ooo+ooo++++o+++++///.             
                                                                                                                                                  ///::::::::-----------------------::::::::::::////////++++++++++++ooooooooooooooooooooooooooooosssoossssssssssssssoosoooooooooooooooooooo++++///.             
                                                                                                                                                   ///::::::::::--:::--:--:-:---:::::::::::::::://////++++++++++++++oooooooooooooooooooooooosooossssssssssssssssssssssssssssssssssssssssooo++++///.             
                                                                                                                                                    ////::::::::::::::::::::::::::::::::::///////////++++++++++ooooooooooooooooossssssssssssssssssssssssssssssssssssssssssyyyyyyyyyyssssooo++++///.             
                                                                                                                                                    /////://:::::::://////::::::::::::///////////+++++++++++ooooooooooooosoosssssssssssssssssssssssssssssssssyyyysyyyyyyyyyyyyyyyyyyssssooo+++++//.             
                                                                                                                                                      //://////////////////:::::::://////////+++++++++ooooooooooooooooooossssssssssssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyysssooo++++++//-             
                                                                                                                                                    /:---://///////////////:::///////////++++++++++o+oooooooooooooooossosssssssssssssssssssssyssyyyyyyyyyyyyyyyyyyyyyyyhhhhhyyyyyysssssooo++++++/+-             
                                                                                                                                                  /-...--:////+++///+/////////////////+++++++ooooooooooooooooooooooossssssssssssssssssssssssyyyyyyyyyyyyyyyyyyhhhyhhhyhyyyyyyyyyssssssoooo++++++++-             
                                                                                                                                               /-...--:://////+++/+++/////////////++++++oooooooooooooooooooooosssssssssssssssssssssssssyyssyyyyyyyyyyyyyyyyhhhhhhhhhyyyyyyyyyssssoooooo++++++++++-             
                                                                                                                                            +:...-::://////////++++++///////////++++++++oooooooooooooooooooooosssssssssssssssssysyyyyyyyyyyyyyyyyyhyyhyyhhhhhhhhhhyyyyyyyyyssssssooooooo++++++++o:             
                                                                                                                                        //:-..`.--://////////////++++++++++//+++++++++++ooooooooooooooooooosssssssssssssssssysyyyyyyyyyyyyyyyyyyyyhhhyhyyhhyyyyhhhyyyyyysssssssssooooooooo+++++oos:             
                                                                                                                                       ::.`...--:///////////////++++++++++++++++++++++++oooooooooooooooooosssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyhhyhhhyhhhyyyyyyyyyssssssssssssoooooooo++oosso-             
                                                                                                                                    /:.....--:::////////:::::///++++++++++++++++++++++ooooooooooooooosssssssssssssyysssssyyyyyyyyyyyyyyyyyyyyhyyyyyyhhyyyyyyyyyyyyysyssssssssssssoooooooooooosss+:.             
                                                                                                                                  /:.``..--:::://///////:::::///++++++++++++/++++++++++ooooooooooooooossssssssssssysyyssyyyyyyyyyyyyyyyyyyyyhhhhyyyyyyyyyyyyyyyyyyssssssssssssssoooooooooooosso+:-`             
                                                                                                                                /:.```..-:::::://///////::::///+++++++++++///:////+++++ooooooooooooooossssssssssssssyyysyyyyyyyyyyyyyyyyyyyhhhhhyyyyyyyyyyyyyyssssssssssssssssoooooooooooossso/:..`             
                                                                                                                              /:.``...--::::///////////::::://++++++++++++/::::::://++++oooooooooooooossssssssssssssyyyyyyyyyyyyyyyyyyyyyhhhhhhhyyyyyyyyyyyyyysssssssssssssssooooooooooosssso/-...`             
                                                                                                                            /-````...--::://////////////::////++++++++++++//:::::::://+++oooooooosooossssssssssyssssyyyyyyyyyyyyyyyyyhyyyyyyyyyyyyyyyyyyyyyyyyssssssssssosssoooooooossssssso/-...``             
                                                                                                                         +:.````..-----::///////////:::/:://++++++oo+o+o+o+:::::--:::////+++ooosososssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssossoooooooooooooossssss+/-..````             
                                                                                                                        /-````....-----::///////////:::::///++++oooooooooo+:::::--:::://///++oooossssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssssssoooooooooooooosssssss+:-...````             
                                                                                                                     s/-````....-------::///////////::/:///++++++ooooooooso::::::::::::://///++ooossssssssyssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssssssssssoooosoooooooooossssssssso+:-...`````             
                                                                                                                  yo:.`````......-----::////////://://:////++++++ooooooooso:::::::::::::://///++oosssssssssyyysyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysssysssssssooooooooooooooooossssssssssso/-...```````             
                                                                                                                s/-``````........----::////+//////::///////+++++ooooooooss+::::::::::::::::://++++ooosssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyssssssssssooooooooooooooooossssssssso+:-....```````             
                                                                                                              +:.``````.........----::////////////:://////+++++ooooooossss+:::::::::::::-:::::///+++oossssssssssssssyyyssyyyyyyyyyyyyyyyyyyyyyyssssssssssssoooooooooooooooooooossso+/-......```````             
                                                                                                            /-.``````.........-----:::////+////////://///+++++ooooooosssso/::::::::::::::::::::::////++ooooooossssssssssssyyyyyyyyyyyyyyyysssyysssssssssssooooooooooooooooooooooo+:--....`..```````             
                                                                                                        os+:.-.````.....--..-------::////////////:://////+++++ooooossyyso+/:::::::::::::::::::::::::::///+ooooooossssssssssysssyyyysyyyyyyssysssssssssssooooooooooooooooooooooo+/-..`````...```````             
                                                                                                       oo+:.-:.```......----------:::////////////:///////++++ooooosyyyso+/::::::::::::::::::::::::::://///+ooooosssssssssssssssyysssyyysyyssyyysssssssssooooooo+++++oooooooo++:-..`````````````````             
                                                                                                      ++:..-//`````.......--------:::////////////:://////++++oooosyhyso+///:::::::::::::::::::::::////////++oooosssssssssssssssssssyyyyyyyyyyyyssssssoooooooooooo+ooooooo++/:-.````````````````````             
                                                                                                  +/:-.```-://``````......----::::::::///////////:://////++++oooshhhss+/:::::::::::::::::::::::::/::///////++++oossoossossssssssssssyyyyyysssssssssoooooo++++++++oooo++++/-..``````````````````````             
                                                                                            o+/:-.`` `   `-:/:```````....--:::::::::::://////////:///////++++ooshhhyso/::::::::::::::::::::::::::://://///////++ooooossosssssssssssssssssssssssssooo+oooo+++++++++++++/:-..````````````````````````             
                                                                                         +//-.``         `-:/:.````......-:::::::::::::///////::////////+++++oshhhyso+/:::::::::::::::::::::::::::::::///////////++ooooooooosssssssssssosssooooooooo+oooo+++++++++//:--.``...``````````````````````             
                                                                                 +/:-..``  `         `.-:::-.`...``..-:::::::----:::://////::////////+++oosyhhysoo/::::::::::::::::::::::::::::::::::::::///////+++oooooooooooooooooooooooooooo++o+++o+++++++/:-..````..-----....```````````````             
                                                                                +/:-.``     ````    `````.-::::-.........-::::-------:::://///:::///////+++ossyhhsoo+/:::::::::::::::::::::::::::::::::::::///////////+++++++++++++++++++++++++++++o+++++++++//:-.`````.-::/++++++//:-..```````````             
                                                                           ++/-.````    ```````     ` ```---::::-..........-:::---::-::::://///:////////++ooosyhyooo/:::::::::::::::--:::::::::::::::::::://://////////////+++/++++++++++++++++++++++++++++/:-..```..--://+++oossssssso/:-..```````             
                                                                        +/:.`````` ` ```````````````````.-:-::::-...........--::-:::--:::://///////////+++++++syyo++:::-::::::::::-------:--:::::::::::::://////////////////////++/++++++++++++++++++++++//:..``..-:///++++ooosyyyyyyyyyyso/:-..``              
                                                                    ++:-````````  ``````````````````````.-:-::::-............----::--:::::////////////////////+oss+/:-:----:::::-------------:--:::::::::::///////::::::::://///+/////+/++++++++++++++++/:-...--:///++++++ooossyyyyyhhhhhhyyys+/--`             
                                                                    +/-.`` ``````````````````````````````.-::-::-..```.-----....---:::::::://///////////::---:::/+os+/--------::::-----------------:::::::::::::/:::::::::-::::///////////////////+++++//:--.--://++++++++++oossyyyyhhhhhhhhhhhhyyso-             
                                                                  +/-.``  ```` `````````````.-...````````.-:::-.`````.-:/::--.....-----::::/++//////::::::--.--://os+:------::::::-------------------:--:::::::::::::::::--::::::://///////////////////::---::/++++++++++++oosssyyyyhhhhhhyyhhhhyhyy/             
                                                                                                                                                                                                                                   AM I A JOKE TO YOU?
                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                      ''')
            print("Zoom Out")
            return ' '



print(meme())    
    
    
    
    
    
    
    
    
    
    
