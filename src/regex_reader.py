from IPython.display import Markdown, display, clear_output
import regex as re
import pandas as pd


def printmd(string: str):
    """Print text as markdown"""
    display(Markdown(string))


def highlight_patterns(text: str, regex: str):
    """Prints text with highlited regexes

    Args:
        text (str): text to search.
        regex (str): regex expression for search.
    """
    scale_factor = 0
    for find in re.finditer(regex, text):
        min_, max_ = find.span()
        scaling = 13 * (scale_factor)
        min_, max_ = min_ + scaling, max_ + scaling
        text = text[:min_] + "<mark>" + text[min_:max_] + "</mark>" + text[max_:]
        scale_factor += 1
    printmd(text)


def print_promt(max_size: int):
    """Print informative prompt.

    Args:
        max_size (int): Biggest number of possible range
    """
    print(
        f"""
Options:\n
        1. 'd' to go to next page
        2. 'a' to go to previous page
        3. Number to go to a specific page
        4. X to quit.
        Please enter numbers between 0 and {max_size}\n"""
    )


def pattern_visualizer(df: pd.DataFrame, text_col: str, regex: str):
    """Print elements of a text pandas column one-by-one higlighting matches of
    the given regex.

    Args:
        df (pd.DataFrame): DataFrame of intrest that has a column with text.
        text_col (str): Name of column that contains text.
        regex (str): Regex pattern to search.
    """
    counter = 0
    counter_past = -1

    max_size = df.shape[0] - 1
    print_promt(max_size)
    while True:

        entered_key = input(">")
        if entered_key == "X":
            return
        elif entered_key == "prompt":
            print_promt(max_size)
        elif entered_key == "clear":
            clear_output(wait=False)
        elif entered_key == "a":
            counter -= 1
        elif entered_key == "d":
            counter += 1
        elif entered_key.isdigit():
            int_entered_key = int(entered_key)
            counter = (
                int_entered_key
                if int_entered_key >= 0 and int_entered_key <= max_size
                else counter
            )

        counter = min(max_size, counter)
        counter = max(0, counter)
        if counter != counter_past:
            show_line(df.loc[counter, text_col], regex)
        counter_past = counter






        
        
        













    
   
        
