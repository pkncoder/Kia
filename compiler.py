
# This grabs the code from the code file
def grabCode(file):
    # Open the file and read it out
    return open(file, "r").read()

# This is the thing that creates the tokens
def tokenizer(code):
    # Make some variables to add to for returning the string
    # Make a var for if we're in quotes or not
    in_quotes = False

    # Make a variable to tell if we are in curly brackets or not
    in_curry_brackets = False

    # Temp string, the string that will be added to the list
    temp_string = ""

    # Token list, the list of the token lists of tokens
    token_list = []

    # Temp token list, used to store any tokens in one line
    temp_token_list = []
    
    # Make a list for the code, of all of the strings
    charList = list(code)
    

    # Loop the array
    for char in charList:
        # Test to see if it is NOT a quote
        if char != '"' and char != '{' and char != '}':
            # If it is a space and in quotes is false
            if char == ' ' and in_quotes == False:
                # Add the temp string to the temp token list as a new token
                temp_token_list += [temp_string]

                # Reset the temp string
                temp_string = ""
            
            # Test to see if the char is not a space, any parrenthesses, and in quotes is false, or a newline
            # This is used for things outside of quotes, like println or input or assignments
            elif char != ' ' and char != '(' and char != ')' and in_quotes == False and char != '\n':
                # Add the current char to the temp string
                temp_string += char
            
            # If in quotes is true, just add everything and anything into the temp string
            elif in_quotes == True and in_curry_brackets == False:
                # Add to the string
                temp_string += char

            # Now if we're in quotes and we come across curry brackets, we need to concate
            elif in_quotes == True and in_curry_brackets == True:
                # Add to the string
                temp_string += char

            # If the user makes a new line, then add the temp_token_list to the token_list
            elif char == '\n':
                # Add the list
                token_list += [temp_token_list]

                # Reset the temp_token_list
                temp_token_list = []

        # In quotes detector and swapper
        elif char == '"' and in_quotes == False:
            in_quotes = True

            # Add the temp string to the token list as a new token
            temp_token_list += [temp_string]

            # Reset the temp string
            temp_string = ""
        
        elif char == '"' and in_quotes == True:
            in_quotes = False
            # Add the temp string to the token list as a new token
            temp_token_list += [temp_string]

            # Reset the temp string
            temp_string = ""

        # In curly brackets detector and swapper
        elif char == '{' and in_curry_brackets == False:
            in_curry_brackets = True

            # Add the temp string to the token list as a new token
            temp_token_list += [temp_string]

            # Reset the temp string
            temp_string = ""
        
        elif char == '}' and in_curry_brackets == True:
            in_curry_brackets = False
            # Add the temp string to the token list as a new token
            temp_token_list += [temp_string]

            # Reset the temp string
            temp_string = ""
    
    # Add the temp token list to the token list at the end with the buffer
    token_list += [temp_token_list]

    # Finnaly return the value needed
    return token_list


'''
Funcs {

print
println
input

}
'''