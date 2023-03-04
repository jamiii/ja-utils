"""
JA Utils - Python module for nbs
"""

__version__ = "0.1.0"

from pathlib import Path
from IPython.display import display
import random
import os
import numpy as np
import torch


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
    
def seed_everything(seed: int = 42, verbose = False):
    """
    Seed numpy, torch, etc. to provide consistant train/val comparisons.
    
    :param seed: value to seed backend routines
    :type seed: int
    :param verbose: display result of modules that have been seeded
    """
    assert isinstance(seed, int), 'seed must be int'
    res = []
    try: random.seed(seed)
    except NameError as ne: res.append(ne); pass
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    try: torch.manual_seed(seed)
    except NameError as ne: res.append(ne); pass
    try: torch.cuda.manual_seed(seed)
    except NameError as ne: res.append(ne); pass
    try: torch.cuda.manual_seed_all(seed)
    except NameError as ne: res.append(ne); pass
    try: torch.backends.cudnn.deterministic = True
    except NameError as ne: res.append(ne); pass
    try: torch.backends.cudnn.benchmark = True
    except NameError as ne: res.append(ne); pass
    if verbose:
        print (res)

# source: https://github.com/PaleNeutron/jupyter2clipboard
def to_clipboard( content: str ) -> str:
    """
    A function that copies str content to your clipboard when run in Jupyter.
    
    Parameters
    ----------
    content
        the content to copy to the local clipboard
    
    Returns
    -------
        str
            copied content
    
    .. code-block:: python

        # kaggle dataset - https://www.kaggle.com/datasets/jmiloser/utils
        import sys
        
        package_paths = ['/kaggle/input/utils/']
        for pth in package_paths:
            sys.path.append(pth)

        from nbutils import to_clipboard, seed_everything
        from datetime import datetime
        from pytz import timezone
        
        tz = timezone("US/Eastern")
        
        to_clipboard(datetime.now(tz).strftime('%y%m%d-%H-%M: '));        
        
    """
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