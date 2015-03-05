from .into import into


def odo(source, target, **kwargs):
    """ Push one dataset into another

    Parameters
    ----------

    source: object or string
        The source of your data.  Either an object (e.g. DataFrame),
    target: object or string or type
        The target for where you want your data to go.
        Either an object, (e.g. []), a type, (e.g. list)
        or a string (e.g. 'postgresql://hostname::tablename'
    raise_on_errors: bool (optional, defaults to False)
        Raise exceptions rather than reroute around them
    **kwargs:
        keyword arguments to pass through to conversion functions.

    Examples
    --------

    >>> L = odo((1, 2, 3), list)  # Convert things into new things
    >>> L
    [1, 2, 3]

    >>> _ = odo((4, 5, 6), L)  # Append things onto existing things
    >>> L
    [1, 2, 3, 4, 5, 6]

    >>> odo([('Alice', 1), ('Bob', 2)], 'myfile.csv')  # doctest: +SKIP

    Explanation
    -----------

    We can specify data with a Python object like a ``list``, ``DataFrame``,
    ``sqlalchemy.Table``, ``h5py.Dataset``, etc..

    We can specify data with a string URI like ``'myfile.csv'``,
    ``'myfiles.*.json'`` or ``'sqlite:///data.db::tablename'``.  These are
    matched by regular expression.  See the ``resource`` function for more
    details on string URIs.

    We can optionally specify datatypes with the ``dshape=`` keyword, providing
    a datashape.  This allows us to be explicit about types when mismatches
    occur or when our data doesn't hold the whole picture.  See the
    ``discover`` function for more information on ``dshape``.

    >>> ds = 'var * {name: string, balance: float64}'
    >>> odo([('Alice', 100), ('Bob', 200)], 'accounts.json', , dshape=ds)  # doctest: +SKIP

    We can optionally specify keyword arguments to pass down to relevant
    conversion functions.  For example, when converting a CSV file we might
    want to specify delimiter

    >>> odo('accounts.csv', list, has_header=True, delimiter=';')  # doctest: +SKIP

    These keyword arguments trickle down to whatever function ``into`` uses
    convert this particular format, functions like ``pandas.read_csv``.

    See Also
    --------

    odo.resource.resource  - Specify things with strings
    datashape.discover      - Get datashape of data
    odo.convert.convert    - Convert things into new things
    odo.append.append      - Add things onto existing things
    """
    return into(target, source, **kwargs)
