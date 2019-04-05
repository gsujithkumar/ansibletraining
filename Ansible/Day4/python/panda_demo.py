#!/usr/bin/python
import pandas as pd

data={
        'docker': [3,4,5],
        'ansible': [10,20,30]
}

trend = pd.DataFrame(data);
print(trend);