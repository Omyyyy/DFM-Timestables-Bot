import pyautogui # Library to control keyboard and mouse
import time # For delays and timer
import webbrowser # To open the webpage remotely
import pyperclip # To get what is on the clipboard

pyautogui.PAUSE = 0.065 # Adjusting speed of keyboard and mouse clicks

def start():
    rounds = int(input("target score? ")) # Get target score from user
    webbrowser.open('https://www.drfrostmaths.com/timestables-game.php') # Open the DFM Timestables game in browser
    time.sleep(3) # Wait for webpage to load
    pyautogui.click(x = 397, y = 531) # Click the start button
    start_time = time.time() # Click on start button
    for i in range(rounds): # Loop for the number of times the user inputs
        pyautogui.click(x=389, y=498, clicks = 3) # Triple click on question to select
        pyautogui.hotkey('ctrl', 'c') # Copy to the clipboard
        expr = pyperclip.paste() # Get what's on the clipboard - now the question is in the program
        pyautogui.click(x = 1053, y = 274) # Click on the answer box
        if len(expr) == 2: # Check if it's a power question
            result = int(expr[0]) ** int(expr[1]) # If yes, evaluate the power
            pyautogui.typewrite(str(result)) # Write it to the screen
           
        else: # If it's not a power question
            toeval = expr.replace("×", "*").replace("÷", "/") # Replace math operators with Python operators for evalution
            pyautogui.typewrite(str(eval(toeval)) # Evaluate the expression and write it to the screen
            
        if i >= 70: # Max is 70, DFM just doesn't accept input after 70 for some reason
            break # Stop the loop if we're at 70 questions

    return time.time() - start_time, rounds # Return the total time taken and the number of questions done

time_taken, rounds = start() # Call the start function and get the total time taken and number of questions done
print(f"{rounds} questions in {time_taken} seconds") # Print info
