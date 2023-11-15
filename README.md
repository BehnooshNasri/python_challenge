# python_challenge
Notes and reference:

•	For the text file formatting I used Stack Overflow to figure out how to write in a new line: https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time

•	Setting and opening the file (both PyBank and PyPoll) in this specific way was done with help from my tutor: 
CSV_PATH = os.path.join("Resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))


•	For PyBank: AskBCS helped me figure out that if I set my rows as lists then each time I loop, I won’t have the issue of it calculating as zero as it had already looped through in a previous one. 

•	For PyBank: ChatGPT helped me figure out this line as my code wasn’t running correctly: 
row.append(profit_losses - prev_amount)

•	For PyPoll: I used ChatGPT to figure out how to correctly use dictionary and looping through it to find the candidate.

•	For PyPoll: for this line to convert to percentage and format it and rounded to 2 decimal point, I got it from ChatGPT and Stack Overflow: https://stackoverflow.com/questions/5202233/how-to-change-39-54484700000000-to-39-54-and-using-python 
 print(f"{candidate}: {percentage:.2f}% ({votes})")

