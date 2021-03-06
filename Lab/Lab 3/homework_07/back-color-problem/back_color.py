from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes

#ADD#

def generate_quiz():                            
    text_list = []                              #create lists
    color_list = []

    for x in shapes:
        text_list.append(x["text"])             #add things to list
        color_list.append(x["color"])

    selected_text = choice(text_list)           #select one random things from lists
    selected_color = choice(color_list) 
    quiz_type = choice([0, 1])
    if quiz_type == 1:
        selected_text = selected_text + "(1)"
    else:
        selected_text = selected_text + "(0)"
    return [selected_text,
            selected_color,                     #outputs
            quiz_type]                          # 0 : meaning, 1: color

def is_inside(l_1, l_2):
    if l_2[0] < l_1[0] < l_2[0] + l_2 [2] and l_2[1] < l_1[1] < l_2[1] + l_2[3]:
        x = True
    else:
        x = False

    return x


def mouse_press(x, y, text, color, quiz_type):
    print(x, y, text, color, quiz_type)
    shape_info = {}
    if quiz_type == 0:
        for shape in shapes:
            if shape["text"] == text:
                shape_info = shape

    elif quiz_type == 1:
        for shape in shapes:
            if shape["color"] == color:
                shape_info = shape
    
    is_inside()
    

    # for s in shapes:
        # if is_inside([x, y], s["rect"]) == True:        #check if user clicked answer
        #     user = s
        #     print(user)
        #     print("----------")
    
            # if quiz_type == 0:                                       #if quiz type  is 0
            #     if selected_text == user["text"] + "(0)":                        #if selected text and user's text the same -> correct
            #         return True
            #     else:
            #         return False
            # else:                                               #if quiz type is 1
            #     if selected_color == user["color"] + "(1)":                       #if selected colour and user's colour the same -> correct
            #         return True
            #     else:
            #         return False
        

#adkjfbgqeiygG dsfHA L P-


