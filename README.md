Maximum-Path-Sum
================

Find the maximum total from top to bottom of random triangles.

Example output:

```
$ python path.py 15 99
                             73 
                           79  03 
                         22  40  44 
                       28  68  56  41 
                     61  71  25  18  67 
                   44  45  20  26  21  42 
                 47  79  99  82  46  06  92 
               89  36  77  19  60  51  99  41 
             12  27  07  40  17  54  01  93  44 
           32  12  73  51  22  58  03  57  54  73 
         96  74  25  88  35  37  96  67  71  77  37 
       25  24  63  17  37  27  54  24  98  27  74  80 
     36  27  10  08  18  34  32  75  11  39  21  17  59 
   62  26  55  31  27  23  77  70  16  89  09  67  93  62 
 99  30  49  42  19  99  41  21  51  40  44  81  67  46  52 

Triangle: 15 lines, 120 points, 16384 paths
Solution: 73+3+44+41+67+42+92+99+93+57+71+98+39+89+44 = 952

