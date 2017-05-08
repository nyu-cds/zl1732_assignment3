from pyspark import SparkContext
from operator import mul

sc = SparkContext()

# create an RDD holding list from 1 to 1000
nums = sc.parallelize(range(1, 1001))

# calculate the product
result = nums.fold(1, mul)

print(result)