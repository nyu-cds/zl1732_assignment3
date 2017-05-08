from pyspark import SparkContext
from operator import add
import numpy as np

sc = SparkContext()

# create an RDD holding list from 1 to 1000
nums = sc.parallelize(range(1, 1001))

# map to square root, add and calculate mean
avg_sqrt = nums.map(lambda x: np.sqrt(x)).fold(0, add) / nums.count()

print(avg_sqrt)