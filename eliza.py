import random
import time
import sys

# Some words used for creating in context responses
words_swap = {
    "ARE": "AM",
    "WERE": "WAS",
    "YOU": "I",
    "YOUR": "MY",
    "IVE":" YOU'VE ",
    "IM":" YOU'RE",
    "YOU": "ME",
    "ME": "YOU",
    "AM": "ARE",
    "WAS": "WERE",
    "I": "YOU",
    "MY": "YOUR",
    "YOUVE": "I'VE",
    "YOURE": "I'M"
}

# Dictionary and Replies based on the keyword found
replies = {
    "CAN YOU": [
        "DON'T YOU BELIEVE THAT I CAN.",
        "PERHAPS YOU WOULD LIKE TO BE ABLE TO.",
        "YOU WANT ME TO BE ABLE TO*"
    ],
    "CAN I": [
        "PERHAPS YOU DON'T WANT TO*",
        "DO YOU WANT TO BE ABLE TO*"
    ],
    "YOU ARE": [
        "WHAT MAKES YOU THINK I AM*",
        "DOES IT PLEASE YOU TO BELIEVE I AM*",
        "PERHAPS YOU WOULD LIKE TO BE*",
        "DO YOU SOMETIMES WISH YOU WERE*"
    ],
    "YOURE": [
        "WHAT MAKES YOU THINK I AM*",
        "DOES IT PLEASE YOU TO BELIEVE I AM*",
        "PERHAPS YOU WOULD LIKE TO BE*",
        "DO YOU SOMETIMES WISH YOU WERE*"
    ],
    "I DONT": [
        "DON'T YOU REALLY*",
        "WHY DON'T YOU*",
        "DO YOU WISH TO BE ABLE TO*",
        "DOES THAT TROUBLE YOU?"
    ],
    "I FEEL": [
        "TELL ME MORE ABOUT SUCH FEELINGS*",
        "DO YOU OFTEN FEEL*",
        "DO YOU ENJOY FEELING*"
    ],
    "WHY DONT YOU": [
        "DO YOU REALLY BELIEVE I DON'T*"
        "PERHAPS IN G00D TIME I WILL*",
        "DO YOU WANT ME TO*"
    ],
    "WHY CANT I": [
        "DO YOU THINK YOU SHOULD BE ABLE TO*"
        "WHY CAN'T YOU*"
    ],
    "ARE YOU": [
        "WHY ARE YOU INTERESTED IN WHETHER OR NOT I AM*",
        "WOULD YOU PREFER IF I WERE NOT*"
        "PERHAPS IN YOUR FANTASIES I AM*"
    ],
    "I CANT": [
        "HOW DO YOU KNOW YOU CAN'T*",
        "HAVE YOU TRIED?",
        "PERHAPS YOU CAN NOW*"
    ],
    "I AM": [
        "DID YOU COME TO ME BECAUSE YOU ARE*",
        "HOW LONG HAVE YOU BEEN*",
        "DO YOU BELIEVE IT IS NORMAL TO BE*",
        "DO YOU ENJOY BEING*"
    ],
    "IM": [
        "DID YOU COME TO ME BECAUSE YOU ARE*",
        "HOW LONG HAVE YOU BEEN*",
        "DO YOU BELIEVE IT IS NORMAL TO BE*",
        "DO YOU ENJOY BEING*"
    ],
    "YOU": [
        "WE WERE DISCUSSING YOU-- NOT ME.",
        "OH, I*",
        "YOU'RE NOT REALLY TALKING ABOUT ME. ARE YOU?"
    ],
    "I WANT": [
        "WHAT WOULD IT MEAN TO YOU IF YOU GOT*",
        "WHY DO YOU WANT*",
        "SUPPOSE YOU SOON GOT*",
        "WHAT IF YOU NEVER GOT*",
        "I SOMETIMES ALSO WANT*"
    ],
    "WHAT": [
        "WHY DO YOU ASK?",
        "DOES THAT QUESTION INTEREST YOU?",
        "WHAT ANSWER WOULD PLEASE YOU THE MOST?",
        "WHAT DO YOU THINK?",
        "ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
        "WHAT IS IT THAT YOU REALLY WANT TO KNOW?",
        "HAVE YOU ASKED ANYONE ELSE?",
        "HAVE YOU ASKED SUCH QUESTIONS BEFORE?",
        "WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?"
    ],
    "HOW": [
        "WHY DO YOU ASK?",
        "DOES THAT QUESTION INTEREST YOU?",
        "WHAT ANSWER WOULD PLEASE YOU THE MOST?",
        "WHAT DO YOU THINK?",
        "ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
        "WHAT IS IT THAT YOU REALLY WANT TO KNOW?",
        "HAVE YOU ASKED ANYONE ELSE?",
        "HAVE YOU ASKED SUCH QUESTIONS BEFORE?",
        "WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?"
    ],
    "WHO": [
        "WHY DO YOU ASK?",
        "DOES THAT QUESTION INTEREST YOU?",
        "WHAT ANSWER WOULD PLEASE YOU THE MOST?",
        "WHAT DO YOU THINK?",
        "ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
        "WHAT IS IT THAT YOU REALLY WANT TO KNOW?",
        "HAVE YOU ASKED ANYONE ELSE?",
        "HAVE YOU ASKED SUCH QUESTIONS BEFORE?",
        "WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?"
    ],
    "WHERE": [
        "WHY DO YOU ASK?",
        "DOES THAT QUESTION INTEREST YOU?",
        "WHAT ANSWER WOULD PLEASE YOU THE MOST?",
        "WHAT DO YOU THINK?",
        "ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
        "WHAT IS IT THAT YOU REALLY WANT TO KNOW?",
        "HAVE YOU ASKED ANYONE ELSE?",
        "HAVE YOU ASKED SUCH QUESTIONS BEFORE?",
        "WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?"
    ],
    "WHEN": [
        "WHY DO YOU ASK?",
        "DOES THAT QUESTION INTEREST YOU?",
        "WHAT ANSWER WOULD PLEASE YOU THE MOST?",
        "WHAT DO YOU THINK?",
        "ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
        "WHAT IS IT THAT YOU REALLY WANT TO KNOW?",
        "HAVE YOU ASKED ANYONE ELSE?",
        "HAVE YOU ASKED SUCH QUESTIONS BEFORE?",
        "WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?"
    ],
    "WHY": [
        "WHY DO YOU ASK?",
        "DOES THAT QUESTION INTEREST YOU?",
        "WHAT ANSWER WOULD PLEASE YOU THE MOST?",
        "WHAT DO YOU THINK?",
        "ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
        "WHAT IS IT THAT YOU REALLY WANT TO KNOW?",
        "HAVE YOU ASKED ANYONE ELSE?",
        "HAVE YOU ASKED SUCH QUESTIONS BEFORE?",
        "WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?"
    ],
    "NAME": [
        "NAMES DON'T INTEREST ME.",
        "I DON'T CARE ABOUT NAMES-- PLEASE GO ON."
    ],
    "CAUSE": [
        "IS THAT THE REAL REASON?",
        "DON'T ANY OTHER REASONS COME TO MIND?",
        "DOES THAT REASON EXPLAIN ANYTHING ELSE?",
        "WHAT OTHER REASONS MIGHT THERE BE?"
    ],
    "SORRY": [
        "PLEASE DON'T APOLOGIZE.",
        "APOLOGIES ARE NOT NECESSARY.",
        "WHAT FEELINGS DO YOU HAVE WHEN YOU APOLOGIZE.",
        "DON'T BE SO DEFENSIVE!"
    ],
    "DREAM": [
        "WHAT DOES THAT DREAM SUGGEST TO YOU?",
        "DO YOU DREAM OFTEN?",
        "WHAT PERSONS APPEAR IN YOUR DREAMS?",
        "ARE YOU DISTURBED BY YOUR DREAMS?"
    ],
    "HELLO": [
        "HOW DO YOU DO .,. PLEASE STATE YOUR PROBLEM."
    ],
    "HI": [
        "HOW DO YOU DO .,. PLEASE STATE YOUR PROBLEM."
    ],
    "MAYBE": [
        "YOU DON'T SEEM QUITE CERTAIN.",
        "WHY THE UNCERTAIN TONE?",
        "CAN'T YOU BE MORE POSITIVE?",
        "YOU AREN'T SURE?",
        "DON'T YOU KNOW?"
    ],
    "NO": [
        "ARE YOU SAYING NO JUST TO BE NEGATIVE?",
        "YOU ARE BEING A BIT NEGATIVE.",
        "WHY NOT?",
        "ARE YOU SURE?",
        "WHY NO?"
    ],
    "YOUR": [
        "WHY ARE YOU CONCERNED ABOUT MY*",
        "WHAT ABOUT YOUR OWN*"
    ],
    "ALWAYS": [
        "CAN'T YOU THINK OF A SPECIFIC EXAMPLE?",
        "WHEN?",
        "WHAT ARE YOU THINKING OF?",
        "REALLY. ALWAYS?"
    ],
    "THINK": [
        "DO YOU REALLY THINK SO?",
        "BUT YOU ARE NOT SURE YOU.",
        "DO YOU DOUBT YOU."
    ],
    "ALIKE": [
        "IN WHAT WAY?",
        "WHAT RESEMBLANCE DO YOU SEE?",
        "WHAT DOES THE SIMILARITY SUGGEST TO YOU?",
        "WHAT OTHER CONNECTIONS DO YOU SEE?",
        "COULD THERE REALLY BE SOME CONNECTION?",
        "HOW?"
    ],
    "YES": [
        "YOU SEEM QUITE POSITIVE.",
        "ARE YOU SURE?",
        "I SEE.",
        "I UNDERSTAND."
    ],
    "FRIEND": [
        "WHY DO YOU BRING UP THE TOPIC OF FRIENDS?",
        "DO YOUR FRIENDS WORRY YOU?",
        "DO YOUR FRIENDS PICK ON YOU?",
        "ARE YOU SURE YOU HAVE ANY FRIENDS?",
        "DO YOU IMPOSE ON YOUR FRIENDS?",
        "PERHAPS YOUR LOVE FOR FRIENDS WORRIES YOU."
    ],
    "COMPUTER": [
        "DO COMPUTERS WORRY YOU?",
        "ARE YOU TALKING ABOUT ME IN PARTICULAR?",
        "ARE YOU FRIGHTENED BY MACHINES?",
        "WHY DO YOU MENTION COMPUTERS?",
        "WHAT DO YOU THINK MACHINES HAVE TO DO WITH YOUR PROBLEM?",
        "DON'T YOU THINK COMPUTERS CAN HELP PEOPLE?",
        "WHAT IS IT ABOUT MACHINES THAT WORRIES YOU?"
    ],
    "SPORTS": [
        "OH, DO YOU LIKE SPORTS?",
        "WHICH YOU SAY IT WAS YOUR FAVORITE SPORT?"
    ],
    "BOOK": [
        "DO YOU LIKED?",
        "WHAT WAS ABOUT?"
    ],
    "BOOKS": [
        "DO YOU LIKED?",
        "WHAT WAS ABOUT?"
    ],
    "MONEY": [
        "THAT'S AN INTERESTING TOPIC TO DISCUSS. TELL ME MORE..."
    ],
    "NOKEYFOUND": [
        "SAY, DO YOU HAVE ANY PSYCHOLOGICAL PROBLEMS?",
        "WHAT DOES THAT SUGGEST TO YOU?",
        "I SEE.",
        "I'M NOT SURE I UNDERSTAND YOU FULLY.",
        "COME COME ELUCIDATE YOUR THOUGHTS.",
        "CAN YOU ELABORATE ON THAT?",
        "THAT IS QUITE INTERESTING."
    ]
}

# Used to keep track of repetitions in user input
prev_input = None

# Used when no word from the dictionary was found on the user input
NO_KEY_FOUND = "NOKEYFOUND"

# Commands identified fron input analysis
COMMAND_RESPONSE = "RESPONSE"
COMMAND_QUIT = "QUIT"


def initialize():
    print("*** ELIZA / DOCTOR ***")
    print("CREATED BY JOSEPH WEIZENBAUM")
    print("This Python version was ported by Walter Palladino")
    print("On December 2022 inspired on several implementations on BASICs, C and Python")
    print()
    print("You can stop the program using words like BYE, SHUT UP or just Ctrl + C :)")
    print()
    print("HI! I'M ELIZA. WHAT'S YOUR PROBLEM?")
    print()


def get_input():

    print("< ", end='')

    text = input()

    #   Remove single and double quotes from the input
    text = text.replace('"', '').replace("'", '')
    text = text.upper()

    return text


def process_input(text):

    global prev_input

    if prev_input != None and text == prev_input:
        print("PLEASE DON'T REPEAT YOURSELF!")
        return { "command": COMMAND_RESPONSE, "reply": "O.K. IF YOU FEEL THAT WAY I'LL SHUT UP...."}

    # Keep track of the last input to check for repetitions
    prev_input = text

    # Check if the user wants to leave?
    if any(bye in text for bye in ["SHUT", "BYE"]):
        return { "command": COMMAND_QUIT, "reply": "O.K. IF YOU FEEL THAT WAY I'LL SHUT UP...."}

    # Parse the input looking for keywords 
    words_found = []
    for keyword, data in replies.items():
        if text.find(keyword) > -1:
            words_found.append(keyword)
    
    # If no keyword was found the last entry NOKEYFOUND will be used
    if len(words_found) == 0:
        # No keyword found
        words_found.append(NO_KEY_FOUND)
    
    reply = ""
    #   Build a response
    response_idx = random.randint(0, len(replies[words_found[0]]) - 1)
    response = replies[words_found[0]][response_idx]

    # Check if the reply should be composed
    if response[-1] != "*":
        reply += response
    else:
        reply += response[:-1]
        if words_found[0] in words_swap:
            if reply.find(words_found[0]) >= 0:
                reply = reply.replace(words_found[0], words_swap[words_found[0]])

        #   Strip the original text to compose the reply
        stripped_text = text[text.find(words_found[0]) + len(words_found[0]):]
        stripped_text = stripped_text.strip()

        # Clean and format reply
        reply += " " + stripped_text
        # Complete the reply format by adding an interrogation character at the end
        reply += "?"

    return {"command": COMMAND_RESPONSE, "reply": reply}


# Print replay on screen
def print_message(message, delay=0.025):
    
    if delay <= 0:
        print("> " + message)
    else:
        message = "> " + message  
        for c in message:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        print()


# Main entry point
if __name__ == "__main__":

    initialize()
    
    while True:
        # Get user inputs
        text = get_input()
        # Process the input
        result = process_input(text)
        # Display the result
        print_message(result["reply"])
        # If chooses to quit then end the program
        if result["command"] == COMMAND_QUIT:
            quit()
