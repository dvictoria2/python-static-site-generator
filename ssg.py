import typer
from ssg.site import Site

import ssg.parsers

def main(source="content", dest="dist"):
    #config = {"source": source, "dest": dest}
    config = {
        "source": source,
        "dest": dest,
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        #"parsers": [ssg.parsers.ResourceParser(),],
        "parsers": [
            ssg.parsers.ResourceParser(),
            ssg.parsers.MarkdownParser(),
            ssg.parsers.ReStructuredTextParser(),
        ],
    }
    Site(**config).build()

typer.run(main)