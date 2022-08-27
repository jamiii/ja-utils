# Use 
# import sys
# utils_path = '/path_to/ja-utils'
# sys.path.append(utils_path)
# import utils
#
#Reload this module in Jupyter
#%load_ext autoreload
#%autoreload 2

from pathlib import Path
from IPython.display import display

def path_info(path: Path, no_files: int = 3):
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