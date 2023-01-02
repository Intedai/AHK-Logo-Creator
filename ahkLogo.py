from PIL import Image, ImageDraw, ImageFont
from os import getcwd


#- Handles the logo creation -#

#Directory that contains the base images that will be used to create the logo
IMG_DIR = f"{getcwd()}\\images\\"

#Height and width of the base images
DIM = 401

#base images for creating the logo, the ahk logo is made out of 3 keys: left, middle and right
LEFT = Image.open(f"{IMG_DIR}LEFT.png")
MID = Image.open(f"{IMG_DIR}MID.png")
RIGHT = Image.open(f"{IMG_DIR}RIGHT.png")

#position of the letters that will be drawn on the base images
CHAR_X = 94
CHAR_Y = 204

#size for the letter on every key
LETTER_SIZE = 106

#creates a new image with the same size as the keys from the AHK logo and draws the char on it in the position (CHAR_X, CHAR_Y) and returns it
def draw_letter(image: Image.Image, char: str) -> Image.Image:
    """
    draws a character on an image

    :param image: the image
    :param char: character to draw on the image
    :returns: the key as a :py:class:`~PIL.Image.Image` object.
    """

    #creates a duplicate of the image given to not change the original image
    new_image = Image.new('RGBA',(DIM,DIM))
    new_image.paste(image)

    #draws the letter in the position and size specified above, with the ariel.ttf font
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype('arial.ttf', LETTER_SIZE)
    text_color = (0, 0, 0)
    text_pos = (CHAR_X, CHAR_Y)
    draw.text(text_pos, char, font=font, fill=text_color)

    #returns the duplicate image with the letter on it
    return new_image


def create(text: str) -> Image.Image:
    """
    Creates a logo with the AHK keys from the official logo

    :param text: text for the logo
    :returns: the logo as a :py:class:`~PIL.Image.Image` object.
    """

    space_len = 100
    match len(text):
        case 0:
            error_ahk_text = create("Error: Text must have atleast 1 character")

        # 1 character
        case 1:
            logo = draw_letter(MID, text)

        #2 or more characters
        case _:
            space_count = text.count(' ')
            logo = Image.new('RGBA',(space_count*space_len+DIM*(len(text)-space_count),DIM))

            first_char = text[0]
            last_char = text[len(text)-1]

            #left key from the AHK logo, which is the first character
            logo.paste(draw_letter(LEFT,first_char))

            #where to paste the next key
            paste_x = DIM+1

            #middle key from the AHK logo, it is used for all
            #of the middle characters in a logo that has more than 3 characters
            for char in  text[1:-1]:
                if char != ' ':
                    logo.paste(draw_letter(MID,char),(paste_x,0))
                    #adds the dimension of the key to paste_x so the next paste will be near the curr key
                    paste_x+=DIM
                else:
                    #adds the space_len to paste_x so there will be a space between the next and last key
                    paste_x+= space_len
            
            #right key from the AHK logo, which is the last character
            logo.paste(draw_letter(RIGHT,last_char),(paste_x,0))

    #final image
    return logo