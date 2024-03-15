def clearScr() -> None:
    import os
    os.system("cls||clear"); # Simplistic method to clear the console, if cls doesn't work run clear, and vice versa.

# Safely gets input of any type
# getInput("Enter your age", int); would try for int(response)
# getInput("Enter your age", str); would try for str(response)
def getInput(prompt: str, dataType: any, clear: bool = True) -> any:
    while True:
        if clear:
            clearScr();
        response = input(prompt);
        try:
            return dataType(response);  # This equates to int(response) if dataType transferred is int. This works with all types theoretically.
        except ValueError:
            match dataType.__name__: # Implement valid descriptions for different types, or don't, the default case _: handles every unimplemented case
                case "float":
                    print("Bitte geben Sie eine valide Zahl ein.");
                    clear = False;
                case "str":
                    print("Bitte geben Sie valide Symbole ein.");
                    clear = False;
                case _:
                    print("Bitte versuchen Sie es erneut.");
                    clear = False;

computerStreichholzZahl: int = 7;
streichholzMenge: int = 29;
while True:
    clearScr();
    print("Streichhölzer:", streichholzMenge);
    nutzerStreichholzZahl: int = getInput("Geben Sie an, wieviele Streichhölzer Sie ziehen wollen (1-6 Streichhölzer): ", int, False);
    if nutzerStreichholzZahl > 6 or nutzerStreichholzZahl > streichholzMenge:
        input("Bitte geben Sie eine kleinere Zahl an.");
        continue;
    streichholzMenge = streichholzMenge - computerStreichholzZahl;
    if streichholzMenge == 0 or streichholzMenge < 0:
        print("Sie haben verloren.");
        break;
    input("PC zieht " + str(computerStreichholzZahl-nutzerStreichholzZahl) + ".");