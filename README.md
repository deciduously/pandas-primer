# Ben's Pandas Primer

Hi Skip!  I do this best in medium-length bloggy-type tutorial form, [it turns out](https://dev.to/deciduously).  Bear with me.

So, without a clear idea of the shape of your dataset, it's tough to put together a "template" you can just copy/paste.  When you said "excel database" are you you talking some super fancy shit with forms and whatnot?  Or just a bunch of sheets?  Either way this library will help you out but the complexity involved will naturally differ.

In any case, I'm using the [sample data](https://community.tableau.com/docs/DOC-1236) found here, renamed to `sample.xls`, to demonstrate the basics of using [Pandas](https://pandas.pydata.org/).  I'm not going to bother with a separate "intro to Python" section, just explaining as I go along - let me know if I lose ya but Python is as close to English as we can reasonably get.  It should also be noted that *my* Python is pretty scarce, but if anything that's a testament to how easy to use this thing is.

Pandas provides two main abstractions, the 1D "Series" or the 2D "dataframe".  We're going to use the "dataframe" which is a 2D size-mutable tabular structure.  The columns can be heterogenously typed and labelled.  This data structure is clearly a natural fit for an Excel worksheet, and Pandas provides functionality to import Excel data out of the box.

First, you'll need to [install Python 3](https://www.python.org/downloads/windows/), and then Pandas with `pip3 install pandas`.  You'll also need `xlrd`: `pip3 install xlrd`.

Create a file called "whatever.py" or, you know, whatever.  At the top, add:

```python
import pandas as pd # alias for brevity
from pandas import ExcelFile
```

We'll access all pandas functions with `pd.func`.  Below that, we'll do the actual import - convention is to use `df` for your dataframe:

```python
df = pd.read_excel('sample.xls', 'Orders')
```

`read_excel` takes the file name followed by the sheet in question.  You get one dataframe per sheet.  Make sure it works by enumerating the columns:

```python
print(df.columns)
```

I get:

```
$ python whatever.py
Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
       'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',
       'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'],
      dtype='object')
```

Groovy.  We can pull out columns to Python variables by indexing into `df` with square brackets, like you would regular Python list.  For instance, to get the 0th element of `my_list = [2,3,4]`, you'd write `my_list[0]` - this gets you `2`.

```python
order_ids = df['Order ID']
print(order_ids)
```

I get:

```
0       CA-2016-152156
1       CA-2016-152156
2       CA-2016-138688
3       US-2015-108966
4       US-2015-108966
5       CA-2014-115812
6       CA-2014-115812
7       CA-2014-115812
8       CA-2014-115812
9       CA-2014-115812
10      CA-2014-115812
11      CA-2014-115812
12      CA-2017-114412
13      CA-2016-161389
14      US-2015-118983
15      US-2015-118983
16      CA-2014-105893
17      CA-2014-167164
18      CA-2014-143336
19      CA-2014-143336
20      CA-2014-143336
21      CA-2016-137330
22      CA-2016-137330
23      US-2017-156909
24      CA-2015-106320
25      CA-2016-121755
26      CA-2016-121755
27      US-2015-150630
28      US-2015-150630
29      US-2015-150630
             ...      
9964    CA-2016-146374
9965    CA-2016-146374
9966    CA-2016-146374
9967    CA-2017-153871
9968    CA-2017-153871
9969    CA-2017-153871
9970    CA-2015-103772
9971    CA-2015-103772
9972    CA-2016-130225
9973    US-2016-103674
9974    US-2016-103674
9975    US-2016-103674
9976    US-2016-103674
9977    US-2016-103674
9978    US-2016-103674
9979    US-2016-103674
9980    US-2015-151435
9981    CA-2017-163566
9982    US-2016-157728
9983    US-2016-157728
9984    CA-2015-100251
9985    CA-2015-100251
9986    CA-2016-125794
9987    CA-2017-163629
9988    CA-2017-163629
9989    CA-2014-110422
9990    CA-2017-121258
9991    CA-2017-121258
9992    CA-2017-121258
9993    CA-2017-119914
Name: Order ID, Length: 9994, dtype: object
```

Quite helpfully, Pandas will avoid clogging up `stdout` and just show you the beginning and end of the column.

It sounds like you'll be looking to filter your data.  We can store a subset of the dataframe with:

```python
filtered_df = df[(df.State == 'California')]
print(filtered_df)
```

You can chain queries:

```python
filtered_df = df[(df.State == 'California') & (df.Quantity > 2)]
print(filtered_df)
```

```
$ python whatever.py
      Row ID        Order ID Order Date  Ship Date  ...     Sales Quantity Discount    Profit
5          6  CA-2014-115812 2014-06-09 2014-06-14  ...    48.860        7     0.00   14.1694
6          7  CA-2014-115812 2014-06-09 2014-06-14  ...     7.280        4     0.00    1.9656
7          8  CA-2014-115812 2014-06-09 2014-06-14  ...   907.152        6     0.20   90.7152
8          9  CA-2014-115812 2014-06-09 2014-06-14  ...    18.504        3     0.20    5.7825
9         10  CA-2014-115812 2014-06-09 2014-06-14  ...   114.900        5     0.00   34.4700
10        11  CA-2014-115812 2014-06-09 2014-06-14  ...  1706.184        9     0.20   85.3092
11        12  CA-2014-115812 2014-06-09 2014-06-14  ...   911.424        4     0.20   68.3568
19        20  CA-2014-143336 2014-08-27 2014-09-01  ...   213.480        3     0.20   16.0110
20        21  CA-2014-143336 2014-08-27 2014-09-01  ...    22.720        4     0.20    7.3840
26        27  CA-2016-121755 2016-01-16 2016-01-20  ...    90.570        3     0.00   11.7741
63        64  CA-2015-135545 2015-11-24 2015-11-30  ...    25.824        6     0.20    9.3612
64        65  CA-2015-135545 2015-11-24 2015-11-30  ...   146.730        3     0.00   68.9631
65        66  CA-2015-135545 2015-11-24 2015-11-30  ...    79.760        4     0.00   22.3328
81        82  CA-2014-139451 2014-10-12 2014-10-16  ...    14.900        5     0.00    4.1720
89        90  CA-2016-109806 2016-09-17 2016-09-22  ...    20.100        3     0.00    6.6330
97        98  CA-2017-157833 2017-06-17 2017-06-20  ...    51.312        3     0.20   17.9592
129      130  US-2016-125969 2016-11-06 2016-11-10  ...   238.560        3     0.00   26.2416
133      134  CA-2016-145583 2016-10-13 2016-10-19  ...    20.040        3     0.00    9.6192
135      136  CA-2016-145583 2016-10-13 2016-10-19  ...    11.520        4     0.00    3.4560
137      138  CA-2016-145583 2016-10-13 2016-10-19  ...    76.176        3     0.20   26.6616
138      139  CA-2016-145583 2016-10-13 2016-10-19  ...    65.880        6     0.00   18.4464
139      140  CA-2016-145583 2016-10-13 2016-10-19  ...    43.120       14     0.00   20.6976
141      142  CA-2017-106180 2017-09-18 2017-09-23  ...     8.820        3     0.00    2.3814
142      143  CA-2017-106180 2017-09-18 2017-09-23  ...    10.860        3     0.00    5.1042
143      144  CA-2017-106180 2017-09-18 2017-09-23  ...   143.700        3     0.00   68.9760
145      146  CA-2015-110744 2015-09-07 2015-09-12  ...   671.930        7     0.00   20.1579
153      154  CA-2015-124919 2015-05-31 2015-06-02  ...    58.380        7     0.00   26.2710
154      155  CA-2015-124919 2015-05-31 2015-06-02  ...   105.520        4     0.00   48.5392
155      156  CA-2015-124919 2015-05-31 2015-06-02  ...    80.880        6     0.00   21.0288
171      172  CA-2014-118962 2014-08-05 2014-08-09  ...    20.940        3     0.00    9.8418
...      ...             ...        ...        ...  ...       ...      ...      ...       ...
9836    9837  US-2016-125402 2016-09-25 2016-10-01  ...    10.900        5     0.00    5.1230
9839    9840  US-2016-125402 2016-09-25 2016-10-01  ...   479.976        3     0.20  161.9919
9840    9841  US-2016-125402 2016-09-25 2016-10-01  ...    44.736        8     0.20    4.4736
9842    9843  US-2016-125402 2016-09-25 2016-10-01  ...   483.136        4     0.20   60.3920
9846    9847  CA-2017-169327 2017-09-02 2017-09-04  ...    43.100        5     0.00   11.2060
9847    9848  CA-2017-169327 2017-09-02 2017-09-04  ...   511.500        5     0.00  132.9900
9848    9849  CA-2017-169327 2017-09-02 2017-09-04  ...   147.920        5     0.20   46.2250
9854    9855  CA-2017-138870 2017-06-19 2017-06-23  ...    50.320        4     0.00   21.1344
9884    9885  CA-2014-112291 2014-04-03 2014-04-08  ...    62.310        3     0.00   22.4316
9905    9906  US-2015-129007 2015-09-13 2015-09-15  ...   131.880        7     0.00   55.3896
9906    9907  US-2015-129007 2015-09-13 2015-09-15  ...    25.032        3     0.20    7.8225
9907    9908  US-2015-129007 2015-09-13 2015-09-15  ...   717.720        3     0.20   71.7720
9908    9909  US-2015-129007 2015-09-13 2015-09-15  ...   207.350        5     0.00   24.8820
9909    9910  US-2015-129007 2015-09-13 2015-09-15  ...    44.670        3     0.00   12.0609
9912    9913  CA-2015-132388 2015-10-10 2015-10-12  ...   362.136        3     0.20  -54.3204
9913    9914  CA-2015-132388 2015-10-10 2015-10-12  ...    31.050        3     0.00   14.9040
9928    9929  CA-2016-129630 2016-09-04 2016-09-04  ...    24.270        3     0.00    8.7372
9929    9930  CA-2016-129630 2016-09-04 2016-09-04  ...  2799.960        5     0.20  944.9865
9931    9932  CA-2015-104948 2015-11-13 2015-11-17  ...   683.332        4     0.15  -40.1960
9932    9933  CA-2015-104948 2015-11-13 2015-11-17  ...    29.960        7     0.00   13.4820
9941    9942  CA-2017-164028 2017-11-24 2017-11-30  ...   223.580       14     0.00   87.1962
9942    9943  CA-2014-143371 2014-12-28 2015-01-03  ...   998.820        9     0.00   29.9646
9943    9944  CA-2014-143371 2014-12-28 2015-01-03  ...    51.150        5     0.00   13.2990
9954    9955  CA-2015-141593 2015-12-14 2015-12-16  ...    34.248        3     0.20   11.5587
9973    9974  US-2016-103674 2016-12-06 2016-12-10  ...   271.960        5     0.20   27.1960
9974    9975  US-2016-103674 2016-12-06 2016-12-10  ...    18.690        7     0.00    5.2332
9977    9978  US-2016-103674 2016-12-06 2016-12-10  ...    13.860        7     0.00    0.0000
9978    9979  US-2016-103674 2016-12-06 2016-12-10  ...    13.376        4     0.20    4.6816
9979    9980  US-2016-103674 2016-12-06 2016-12-10  ...   437.472       14     0.20  153.1152
9992    9993  CA-2017-121258 2017-02-26 2017-03-03  ...    29.600        4     0.00   13.3200

[1348 rows x 21 columns]

```


It supports a SQL-like `groupby`:

```python
df2 = df.groupby(["Region"])[['State']].count()
print(df2)
```

```
$ python whatever.py
         State
Region        
Central   2323
East      2848
South     1620
West      3203
```

All in all, I find Pandas a lot more ergonomic than Excel, and the resulting programs infinitely more readable and tweakable.  There's a lot of info in [the docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html).  I know it's not necessarily a *simple* solution, but it is *powerful* and *expressive* - I prefer to use this to ask questions about datasets over Excel any day.

Does this sound like it might be headed towards helpful?  If not, what's missing?  I might be able to put togethe a more concretely useful example with a little more insight into what your data looks like.  I assume the data itself is proprietary, but how many sheets are we talking?  Lots of cross-sheet talk?  Pandas will do all of it, there's some good info in [this section](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging) abaout dataframe merging - your SQL know-how should translate nicely.  There's even a guide for people [who are comfortable with SQL](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html).  If you need more examples, just holla.
