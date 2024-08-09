from IPython.display import Markdown, display

def mprint(markdown_text):
    """
    Render markdown text in a Jupyter notebook.

    Args:
        markdown_text (str): The markdown text to be rendered.

    Returns:
        None: The function displays the rendered markdown directly.
    """
    display(Markdown(markdown_text))

