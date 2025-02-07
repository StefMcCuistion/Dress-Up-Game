# Random Character Generator GDD
![A color-coded diagram of the player character of this dress up game, showing the separate pieces that make up the character. ](randomcharactergenerator/assets/img/gdd/spr_protag_base_v2.png)
## What is this? 
This is the GDD, or 'game design document', for this random character generator project. Here, all planned features for the finished product will be described. When plans change, descriptions will be updated. This document will be used throughout development to keep the project focused. 
## Top-level Description
### A simple 2D random character generator. 
You know the 'randomize' feature in video game character creators, usually represented by a dice button? That's this whole game! After generating a character, you can save an image of them to your PC if you wish!
The tone of the game is cozy and cutesy. It isn't meant to be used over the long-term, just to provide some joy and entertainment for as long as it captures interest. 
The character whose appearance is randomized is a cartoon girl in an anime-adjascent style. Her hairstyle, hair color, skin color, and clothing will all be changed each time you randomize her, as well as whether she's a human or a catgirl. The outfit pieces which are randomized include her shoes, bottom, top, and socks/tights. 

![A catgirl with a big old-fashioned coat, black booty-shorts, and a blonde emo hairstyle which covers one eye. ](randomcharactergenerator/assets/img/gdd/example_character.png)

After the game has been published as a free itch.io game, it will be adapted into a proper character creator, giving the user full control over the character's appearance. 

# Program features
The game will feature four screens: a splash screen, a start screen, an options screen, and a gameplay screen. 
## Splash screen
This screen will display when the program is launched, and will pass after a moment. It will show the splash art for Studio Meow Tao against a black screen, and then fade to black before fading into the start screen. 

![A pink-and-black yin-and-yang symbol where each half has a cartoon cat face and cat ears. ](randomcharactergenerator/assets/img/gdd/studio_meow_tao_logo_small.png)

## Start screen (a.k.a Main Menu)
This is the screen that will display after the splash screen has passed. It will feature pretty background art, a title, and a menu. Gentle background music will be playing, which will persist between screens. 

The UI will be aesthetically appealing and match the tone of the game, including a custom mouse cursor. The menu options will be 'START', 'OPTIONS', and 'QUIT'. The options can be navigated by mouse, by WASD keys, or by arrow keys. The selected button (or the button being hovered over if the mouse is in use) will be visually different by becoming larger and highlighted. There will be sound effects for changing the selected button and using/activating that button. 

Selecting a button will fade to black and then fade into that screen. 

## Options screen
The options screen can be accessed from the start screen. On top of its unique background art, it includes the following: 
1. Resolution (Cycle through options with arrow buttons)
2. Fullscreen (Box which toggles between having a checkmark or being empty)
3. Master Volume (Slider)
4. Music Volume (Slider)
5. Sound Effects Volume (Slider)
6. Return to Main Menu (Button)

