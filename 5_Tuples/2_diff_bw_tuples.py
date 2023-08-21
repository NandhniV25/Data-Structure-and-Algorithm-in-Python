# tuples vs list
# tuple(map(sum, zip(tuple1, tuple2)))
# tuple(a + b for a, b in zip(t1, t2))
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple(map(sum, zip(tuple1, tuple2))))

# both => len(), max(), min(), sum(), any(), all(), sorted(), count(), index()
# not used in tuples => append(), insert(), remove(), pop(), clear(), sort(), reverse() => applicable to list only