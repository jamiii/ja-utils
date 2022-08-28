"""
JA Utils - Python module for nbs
"""

__version__ = "0.1.0"

from pathlib import Path
from IPython.display import display

def path_info(path: Path, no_files: int = 3):
    """
    Return path information like files, directories, and file size

    :param path: path object
    :type path: Path
    :param no_files: number of files to list per dir
    :type no_files: int
    """
    assert isinstance(path, Path), 'path should be a Path object'
    display([[e.name, e.stat().st_size] for e in L(path.ls())])
    display([list(d.name + d.ls(no_files) + d.stat().st_size) for d in path.iterdir() if d.is_dir()])
    

# source: https://github.com/PaleNeutron/jupyter2clipboard
def to_clipboard( content ):
    '''
    A function that copies a str content to your clipboard when run in Jupyter.
    
    Args:
        * content (``str``): content to copy to the local clipboard
    
    Returns:
        str
    '''
    content = f"String.raw`{content}`"
    ipy = get_ipython()
    ipy.run_cell_magic( "javascript", "",
        '''
        function copyToClipboard(text) {
            if ( window.clipboardData && window.clipboardData.setData ) { return clipboardData.setData( "Text", text ); }
            else if ( document.queryCommandSupported && document.queryCommandSupported( "copy" ) ) {
                var textarea = document.createElement( "textarea" );
                textarea.textContent = text;
                textarea.style.position = "fixed";  // Prevent scrolling to bottom of page in Microsoft Edge.
                document.body.appendChild( textarea );
                textarea.select();
                try { return document.execCommand( "copy" ); }
                catch ( ex ) {
                    console.warn( "Copy to clipboard failed.", ex );
                    return false;
                }
                finally { document.body.removeChild( textarea ); }
            }
        };
        ''' +  "copyToClipboard( {} );".format(content))
    return content