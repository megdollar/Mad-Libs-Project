# A dictionary of blank spaces and answers to be passed in to the game function. 
blank_space1  = ["__0__", "__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"]
answer_key  = ["python", "function", "loop", "list", "dictionary", "for", "while", "string"]

# The following are simple, medium, and hard strings to pass in to the function.

game_string = blank_space1[0] + " is a highly readable programming language. \nA " \
                + blank_space1[1] +  " is a sequence of program instructions that performs a specific task using input and output. \nA " \
                + blank_space1[2] + " is a sequence of instructions that repeat until a certain criteria is met. \nA " \
                + blank_space1[3] + " is mutable and can contain mixed types of data. \nA " \
                + blank_space1[4] + " is a mutable array used to store information for easy recall. \nA " \
                + blank_space1[5] + " loop iterates over iterable object capturing each element to local variable to be used in attached block. \nA" \
                + blank_space1[6] + " loop executes any numver of times if the test expression is true. \nAn immutable character " \
                + blank_space1[7] + " is text you can display to the user."
end = 0
string_end = 0


#function simple uses input simple string, raw input, blank space, and outputs the filled in string
def game():
    global game_string, end, string_end, DEBUG
    print game_string[0: string_end]

    R2 = "0" 
    i = 0
    for i in range(0,end):
        while R2 != answer_key[i]:
            R2 = raw_input("\nWhat should go in " + blank_space1[i] + "?").lower()
        print "\ncorrect"
        game_string = game_string.replace(blank_space1[i], R2)
        #string_end = 292 + or - answers to this point, need to create separate string_end function to calculate this

        print game_string[0: string_end]

# main function displays instructions and uses raw input to determine which level the user wishes to play

def main():
    global end, string_end
    print "Welcome to MadLibs. Please select a level of difficulty and try to fill in the blanks."
    R1 = "0"
    while R1 != "1" and R1 != "2" and R1 != "3":
        R1 = raw_input("Key in the number associate with your desired level: 1 = Simple, 2 = Medium, 3 = Hard? ")
        if R1 == "3":
            end = 8
            string_end = 616
            game()
        elif R1 == "2":
            string_end = 478
            end = 6
            game()
        elif R1 == "1":
            string_end = 292
            end = 4
            game()
        else:
            print "enter 1, 2 or 3 dummy"
    return R1

#program starts here    
main()



