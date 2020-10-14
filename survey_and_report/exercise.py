from typing import Dict

# Survey answers submitted by User
questions_answers: Dict = {
    'Q1_answer': "Very short",
    'Q2_answer': "Everyday",
    'Q3_answer': ["Dandruff", "Hair loss", "Dry hair",
                  "Psoriasis", "Head lice", "Bamboo hair"],
    'Q4_answer': {
        "price": 120,
        "currency": "Eur",
    },
    'Q5_answer': {
        "choice": "Yes",
        "yes_choices": ["Applying Aloe liquid", "Applying lemon",
                        "Applying garlic water", "Do not washing"]
    },
}

# Here you receive user's answers and you have to figure out what kind of report text to return
report_text = ''


# if questions_answers["Q1_answer"] == "Very short":
#     report_text += "Lorem ipsum 1. Question - ANSWER_1 dolor sit amet," \
#                 "consectetur adipiscing elit. Mauris sed ligula vitae tellus" \
#                 "pellentesque vehicula nec eu velit. Curabitur luctus et" \
#                 "nibh et ornare. Suspendisse non mattis lacus. Cras vitae mi" \
#                 "ornare, euismod velit sit amet, iaculis tortor. In tempor" \
#                 "purus sapien. Donec tincidunt 1. Question - ANSWER_1 metus" \
#                 "nec dui tristique malesuada. Praesent lectus nunc, accumsan" \
#                 "vel justo in, imperdiet faucibus leo. Nullam efficitur massa" \
#                 "nec turpis tincidunt, feugiat viverra erat rutrum. Aliquam" \
#                 "eget auctor lectus, mollis blandit ipsum. Phasellus maximus" \
#                 "finibus arcu a tincidunt."
#
# if questions_answers["Q1_answer"] == "Short":
#     report_text += "Lorem ipsum 1. Question - ANSWER_2 dolor sit amet," \
#                   "consectetur adipiscing elit. Ut et augue id leo egestas" \
#                   "interdum in eu lectus. Aliquam vel finibus nisi." \
#                   "Vestibulum mattis sagittis lectus sed pulvinar." \
#                   "Sed aliquam felis tortor, sed scelerisque nibh cursus" \
#                   "sit amet. Donec a sollicitudin nisi. Mauris non enim ac" \
#                   "felis lobortis commodo. Sed laoreet tellus non felis rutrum," \
#                   "in hendrerit ipsum porta. Sed quis sem velit."
#
# if questions_answers["Q1_answer"] == "Medium":
#     report_text += "Sed vel bibendum tortor. Proin a aliquet tortor." \
#                   "Vivamus rhoncus 1. Question - ANSWER_3 risus nec ultricies" \
#                   "rutrum. Mauris bibendum lectus risus, non porttitor urna" \
#                   "interdum quis. Suspendisse quis risus scelerisque," \
#                   "1. Question - ANSWER_3 feugiat augue nec, semper leo." \
#                   "Fusce euismod facilisis mi, tristique sollicitudin metus" \
#                   "hendrerit non. Nulla ac sodales quam, sit amet finibus" \
#                   "metus. Ut in felis tellus. Sed aliquet metus ullamcorper " \
#                   "st vestibulum mattis. Cras nisi sem, euismod in egestas vel," \
#                   "ullamcorper ac sapien. In porttitor elementum faucibus."
#
# if questions_answers["Q1_answer"] == "Medium":
#     report_text += "Mauris urna nunc, eleifend id sapien eget, tincidunt" \
#                   "enenatis risus. Vestibulum imperdiet enim at nibh sodales," \
#                   "1. Question - ANSWER_4 or ANSWER_5 or ANSWER_6 eget" \
#                   "scelerisque odio finibus. Nullam ut mi eget sapien accumsan" \
#                   "aculis. Vestibulum in maximus metus, 1. Question - ANSWER_4" \
#                   "or ANSWER_5 or ANSWER_6 vitae venenatis sapien. Nullam" \
#                   "auctor odio vehicula, posuere elit in, ullamcorper lectus." \
#                   "Mauris pharetra dapibus congue. Suspendisse potenti."
#
# # print(report_text)
#
# # Second question report text
# if questions_answers["Q2_answer"] == "Everyday"\
#         or questions_answers["Q2_answer"] == "2 times a week":
#     report_text += "Mauris urna nunc, eleifend id sapien eget," \
#                    "2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis" \
#                    "risus. Vestibulum imperdiet enim at nibh sodales," \
#                    "eget scelerisque odio finibus. Nullam ut mi eget sapien" \
#                    "accumsan iaculis. Vestibulum in maximus metus, vitae" \
#                    "venenatis sapien. Nullam auctor odio vehicula, posuere" \
#                    "elit in, ullamcorper lectus. Mauris pharetra dapibus" \
#                    "congue. 2. Question - ANSWER_1 or ANSWER_3" \
#                    "Suspendisse potenti."
#
# if questions_answers["Q2_answer"] == "1 time a week"\
#         or questions_answers["Q2_answer"] == "3 times a week":
#     report_text += "In nisl ligula, porttitor vel lobortis vel," \
#                    "commodo quis mi. Nullam sollicitudin odio ut felis" \
#                    "tristique tempus. Cras sagittis auctor nulla" \
#                    "2. Question - ANSWER_2 or ANSWER_4 eget accumsan." \
#                    "Nam condimentum lacus non tortor auctor semper. Suspendisse" \
#                    "justo nisi, molestie quis purus sed, dapibus porta urna." \
#                    "Praesent leo massa, aliquet blandit eros at, consectetur" \
#                    "vestibulum elit. Aliquam laoreet ex ex, et dapibus" \
#                    "2. Question - ANSWER_2 or ANSWER_4 ligula interdum a." \
#                    "Praesent quis libero arcu. Donec felis libero," \
#                    "tristique et sapien non, feugiat eleifend diam."
#
# # print(report_text)
#
# # Third question report text
# if "Psoriasis" in questions_answers["Q3_answer"] and\
#         "Dry hair" in questions_answers["Q3_answer"] and\
#         "Dandruff" in questions_answers["Q3_answer"]:
#     report_text += "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
#                    "Sed sollicitudin leo in 3. Question - ANSWER_4, ANSWER_3" \
#                    "and ANSWER_1 lectus cursus tincidunt. Nullam dapibus" \
#                    "tincidunt libero nec volutpat. Cras sit amet massa a" \
#                    "turpis malesuada ornare vitae sed arcu. Maecenas eleifend" \
#                    "rutrum augue, eget imperdiet sem gravida sed. Vestibulum" \
#                    "vel libero consectetur, 3. Question - ANSWER_4, ANSWER_3" \
#                    "and ANSWER_1 pellentesque lacus nec, facilisis nisl." \
#                    "Phasellus faucibus lobortis tincidunt. Duis tristique" \
#                    "congue bibendum. Morbi semper cursus felis et consequat." \
#                    "Nulla posuere, quam eget pulvinar 3. Question - ANSWER_4," \
#                    "ANSWER_3 and ANSWER_1 dignissim, odio sem euismod leo, at" \
#                    "ornare purus massa quis sapien. Aliquam eget libero nec" \
#                    "lectus placerat congue. Aenean nec tortor a ligula aliquam" \
#                    "pharetra. Aenean et magna enim."
#
# elif "Hair loss" in questions_answers["Q3_answer"] and\
#         "Head lice" in questions_answers["Q3_answer"]:
#     report_text += "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
#                    "Vestibulum dictum, dui non auctor tristique, odio sem 3." \
#                    "Question - ANSWER_2 and ANSWER_5 convallis lacus," \
#                    "non gravida libero erat id justo. Praesent in varius nisi." \
#                    "Phasellus suscipit elit sit amet aliquam tincidunt. In" \
#                    "pellentesque gravida risus, et 3. Question - ANSWER_2" \
#                    "and ANSWER_5 rhoncus quam. Vestibulum ac risus nulla." \
#                    "Phasellus iaculis interdum pulvinar. Vivamus sit amet" \
#                    "sagittis risus. Morbi ut pellentesque sapien."
#
# elif "Very oily hair" in questions_answers["Q3_answer"] and\
#         "Dry hair" in questions_answers["Q3_answer"] or \
#         "Dandruff" in questions_answers["Q3_answer"]:
#     report_text += "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
#                    "Cras viverra luctus nunc, non ultrices mauris molestie" \
#                    "vitae. Sed gravida purus finibus 3. Question - ANSWER_4," \
#                    "ANSWER_3 or ANSWER_1 efficitur congue. Vestibulum magna" \
#                    "urna, volutpat vitae auctor non, pharetra vel leo." \
#                    "Interdum et malesuada fames ac ante ipsum primis in" \
#                    "faucibus. Vestibulum elementum sagittis tortor," \
#                    "vel porta leo tristique ac. Phasellus ac metus est." \
#                    "3. Question - ANSWER_4, ANSWER_3 or ANSWER_1 Aenean" \
#                    "vel malesuada ex, nec rutrum justo. Sed ultricies" \
#                    "venenatis mauris, in pharetra ante vulputate nec." \
#                    "Proin viverra convallis augue elementum volutpat."
# else:
#     report_text += "Consectetur adipiscing elit, sed do eiusmod tempor" \
#                    "incididunt ut labore et dolore magna aliqua. Ut enim" \
#                    "ad minim veniam, quis nostrud exercitation ullamco" \
#                    "laboris nisi ut aliquip ex ea commodo consequat. Duis aute" \
#                    "irure dolor in reprehenderit in voluptate velit esse" \
#                    "cillum dolore eu fugiat nulla pariatur. Excepteur" \
#                    "sint occaecat cupidatat non proident, sunt in culpa" \
#                    "qui officia deserunt mollit anim id est laborum."
#
# # Fourth question report text
#
# Q4: Dict = questions_answers["Q4_answer"]
#
# if (
#     Q4["price"] > 120 and Q4["currency"] == "Eur" or
#     Q4["price"] > 265 and Q4["currency"] == "USD"
# ):
#     calculation_1: int = round(Q4["price"] * 1.3)
#     report_text += "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
#                    f"Calories: {calculation_1}" \
#                    "Vivamus hendrerit arcu eros, nec bibendum mi" \
#                    "sodales id. Ut auctor nisl a placerat porttitor." \
#                    "Duis at tortor posuere, gravida sapien in," \
#                    "fermentum ligula. Quisque eu ipsum lobortis, hendrerit" \
#                    "justo vitae, varius nisi. Etiam in leo feugiat purus" \
#                    "facilisis tempor. Fusce congue metus non massa mollis," \
#                    "id imperdiet ex viverra." \
#                    f"Cras Calories: {calculation_1}" \
#                    "imperdiet lectus at imperdiet ornare."
#
# elif (
#     Q4["price"] < 60 and Q4["currency"] == "Eur" or
#     Q4["price"] < 132 and Q4["currency"] == "USD"
# ):
#     calculation_2: int = round(Q4["price"] * 1.3 * 1.1)
#     report_text += "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
#                    "Integer porta at odio ac rhoncus." \
#                    f"Calories: {calculation_2}" \
#                    "nteger viverra porta eros nec ultrices." \
#                    "Nullam ante sem, tincidunt vitae orci id," \
#                    "vestibulum auctor risus. Phasellus sit amet" \
#                    "lobortis eros. Maecenas convallis dolor ex," \
#                    "vel congue ipsum ornare eu. Nunc in mattis dolor," \
#                    "quis posuere lorem." \
#                    f"Calories: {calculation_2}" \
#                    "Nullam condimentum semper diam, lacinia tempor eros" \
#                    "tristique ut. Etiam ultrices imperdiet tortor at" \
#                    "eleifend. Aenean lorem felis, volutpat eu euismod at," \
#                    "congue id erat. Duis luctus quam vitae mattis tempus."
#
# else:
#     calculation_3: int = round(Q4["price"] * 1.3 * 15.2)
#     report_text += "Sed at aliquam ex. Vestibulum maximus erat in justo" \
#                    "maximus posuere." \
#                    f"Calories: {calculation_3}" \
#                    "Suspendisse tellus magna, faucibus scelerisque dapibus et," \
#                    "luctus egestas nibh. Pellentesque eleifend mauris ac" \
#                    "volutpat ullamcorper. Aenean vitae velit et nulla egestas" \
#                    "viverra sit amet eu eros." \
#                    f"Calories: {calculation_3}" \
#                    "Nunc congue rutrum sem"
#
Q5: Dict = questions_answers["Q5_answer"]

if Q5["choice"] == "I don't know":

    report_text += "Phasellus ac sem ornare, ANSWER_I_DONT_KNOW euismod" \
                   "tellus id, sagittis felis. Nullam viverra est nibh," \
                   "et dignissim elit tincidunt nec. Integer vel dolor" \
                   "aliquam, eleifend metus in, tincidunt erat. Nam id" \
                   "facilisis tortor. Donec malesuada, libero nec tincidunt" \
                   "ANSWER_I_DONT_KNOW commodo, nulla velit imperdiet" \
                   "mauris, sit amet cursus dui quam maximus justo." \
                   "In accumsan nisi ut orci finibus ullamcorper. Aliquam" \
                   "consequat risus non orci dapibus, id commodo erat egestas."

if Q5["choice"] == "No":

    report_text += "Nam maximus et massa laoreet congue. In facilisis egestas" \
                   "neque. Nullam ac euismod nibh. ANSWER_NO Aenean pulvinar" \
                   "lacinia ligula, nec lobortis magna accumsan sed. Duis" \
                   "tempor pellentesque quam. ANSWER_NO Sed non est dui." \
                   "Sed commodo odio vel augue pellentesque, et sagittis" \
                   "dolor tristique. Phasellus mollis magna eu egestas" \
                   "viverra. Cras elementum erat vel libero venenatis," \
                   "ut suscipit nibh scelerisque."

if (
    Q5["choice"] == "Yes" and
    ["Applying lemon"] and ["Applying garlic water"]
    in Q5["yes_choices"]):

    report_text += "Mauris viverra lobortis ante, eget faucibus felis" \
                   "pulvinar et. Suspendisse urna diam," \
                   "ANSWER_YES and ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3" \
                   "elementum nec tincidunt ornare, convallis condimentum" \
                   "nisi. Nam gravida ac magna eget cursus. ANSWER_YES" \
                   "and ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 Maecenas" \
                   "fermentum lacus eu tempor condimentum. Quisque tristique" \
                   "viverra justo, et mollis magna ornare a. In lacus elit," \
                   "vestibulum a ex facilisis, faucibus gravida dui. Morb" \
                   " consectetur egestas tempor. Sed neque ex, condimentum" \
                   "congue facilisis non, aliquet sed odio."

if (
    Q5["choice"] == "Yes" and
    ["Applying Aloe liquid"] and ["Do not washing"]
    in Q5["yes_choices"]):

    report_text += "Fusce sem est, maximus ac efficitur in, accumsan eu" \
                   "libero. Praesent facilisis, augue at pretium malesuada," \
                   "ANSWER_YES and ANSWER_YES_CHOICE_1, ANSWER_YES_CHOICE_4" \
                   "erat eros eleifend velit, at iaculis nunc nisi nec odio." \
                   "Ut consequat ac metus a bibendum. Donec venenatis" \
                   "euismod eros ac dignissim. Donec dictum odio a augue" \
                   "tincidunt interdum."

else:
    report_text += "Lorem ipsum dolor sit amet, consectetur adipiscing elit." \
                   "Pellentesque sed scelerisque nulla, at mattis mauris." \
                   "Vestibulum dignissim viverra nulla quis tempus." \
                   "(Any other case) Donec finibus nisl sapien, sed auctor" \
                   "elit sodales ac. Nulla dictum ante ante, eget maximus" \
                   "mi efficitur nec."


print(report_text)