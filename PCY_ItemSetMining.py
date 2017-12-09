'''
An implementation of the PCY Algorithm in Frequent Itemset Mining. 
Source: http://infolab.stanford.edu/~ullman/mining/pdf/assoc-rules2.pdf
@author: Bhavika Tekwani 
'''

import collections
import itertools
from pprint import pprint




def hash_fn(i, j):
    return i * j % 11

def pcy(baskets, hash_buckets, support, items_range, hash_fn):
    items = [i for i in range(1, items_range+1)]

    # Support for each item
    item_counter = collections.Counter(x for basket in baskets for x in basket)
    item_pairs = list(itertools.combinations(items, 2))

    # Support for each item pair
    item_pair_counts = {k:0 for k in item_pairs}

    for b in baskets:
        for p in item_pairs:
            if p[0] in b and p[1] in b:
                item_pair_counts[p] += 1

    print("Support for each item pair")
    pprint(item_pair_counts)

    hash_pair_buckets = {k:0 for k in range(hash_buckets)}
    bucket_pairs = collections.defaultdict(list)

    for b in baskets:
        item_pairs_basket = list(itertools.combinations(b, 2))
        for p in item_pairs_basket:
            bucket = hash_fn(p[0], p[1])
            print("Pair {} went to bucket {}".format(p, bucket))
            hash_pair_buckets[bucket] += 1
            bucket_pairs[bucket].append(p)


    print("Hash each item pair to a bucket based on a hash function - ")
    pprint(hash_pair_buckets)

    # filter buckets based on support
    frequent_buckets = [k for k, v in hash_pair_buckets.items() if v > support]

    # pairs in frequent buckets - pass 2 of pcy
    pass2_pairs = set()
    for fb in frequent_buckets:
        fb_pairs = bucket_pairs[fb]
        for f in fb_pairs:
            pass2_pairs.add(f)

    print("Pass 2 of PCY algorithm yields the following frequent pairs: ")
    pprint(pass2_pairs)


baskets = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [1, 3, 5], [2, 4, 6], [1, 3, 4],
[2, 4, 5], [3, 5, 6], [1, 2, 4], [2, 3, 5], [3, 4, 6]]

pcy(baskets, 11, 4, 6, hash_fn)
