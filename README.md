This program was made for interaction with a small dataset, which can be changed but not significantly.

Next, I will explain every algorithm and how it works.

- Filtering algorithm
When a user asks for the algorithm (line 85), it is also asked by which key and value it needs to 
be filtered, before it continues, it checks if the given string is numeric, so it could be remade to 
the integer. After receiving information, a program is using the “def filter function” (line 35). First,
it creates a new array, then it starts the main “for loop”, which is needed for looking through 
every index in the list. Then, starts the second loop, which is finding the keys of the dictionaries. 
So, if the needed key was found, it continues and checks if this index and key have the same 
value as the user gave, we add this object into the return array “f”. After, its comebacks to the 
output filtering section and gives the output of the received user information. Moreover, if the 
given data was wrong or cannot be used, the program asks to try entering the info again.
To test the algorithm, I was entering different inputs, not only from the given dataset but also 
words that had nothing to do with the program. By checking every kind of input, I managed to 
give a user an error, with an option to continue the interaction.
There were no limitations noticed.

- Aggregation algorithm
After receiving a command to use the aggregate algorithm (line 102), the user was asked to 
enter the key, that he wants to aggregate. The program continues in the “def aggregate 
function” (line 46). At the start of the function, it creates a new array “g”. By creating a “for loop” 
the function looks through every index in the array, and then just adds for asked values from 
each index. Then, it returns the average of the received information from the main array. 
Coming back to the output part, where used “try-except” to avoid errors, by entering incorrect or 
non-existing information. If no errors were found, we get the average number as the output and 
the rounded version of it for convenience.
The main idea of this algorithm is every needed key should have a number in it as a value, so 
every time the input key does not include an integer as a value it is an error. By writing keys, 
which included suitable keys and non-suitable ones, and by getting different outputs, I could 
manage to find all the bugs and get rid of them.
No limitations were noticed.

- Sorting function
Using a sorting algorithm (line 121), the program asks for a key that needs to be sorted. By 
applying “try-except” functions I am trying to avoid errors by incorrect input, if no mistakes were 
found the program continues. Coming next to the “def sorting function” (line 54), where first, the 
“new_arr” array is created, which is equal to our dataset “arr” to not to change the original. The 
boolean “flag” variable, is needed for the “while loop”. The loop is needed to imitate the “bubble 
sort” function. It works the next way: looking through the array, the function tries to find the key, 
which is equal to the inputted one. And by looking at the values, it replaces their position in 
decreasing ways. If the variable is less than the next one, the last take the first’s place. When 
there are no changes in the loop, the boolean object is not switching back to “True”, so the loop 
stops.
I have tested the algorithm by entering different objects from the dataset and out of it. If the 
input is incorrect for the program in any way, it will give an error, but give the option to try again.
