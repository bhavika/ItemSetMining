"""
An implementation of the PCY Algorithm in Frequent Itemset Mining.
Source: http://infolab.stanford.edu/~ullman/mining/pdf/assoc-rules2.pdf
@author: Bhavika Tekwani
"""

import collections
import itertools
from pprint import pprint


def hash_fn_pass1(i, j, n):
    return i * j % n


def hash_fn_pass2(i, j, n):
    return i * j % n


def pcy(baskets, hash_buckets, support, items_range, hash_fn, modn):
    items = [i for i in range(1, items_range+1)]

    # Support for each item
    item_counter = collections.Counter(x for basket in baskets for x in basket)

    print("Item counts", item_counter)

    item_pairs = list(itertools.combinations(items, 2))

    # Support for each item pair
    item_pair_counts = {k: 0 for k in item_pairs}

    for b in baskets:
        for p in item_pairs:
            if p[0] in b and p[1] in b:
                item_pair_counts[p] += 1

    print("Support for each item pair: ")
    pprint(item_pair_counts)

    hash_pair_buckets = {k:0 for k in range(hash_buckets)}
    bucket_pairs = collections.defaultdict(list)

    for b in baskets:
        item_pairs_basket = list(itertools.combinations(b, 2))
        for p in item_pairs_basket:
            bucket = hash_fn(p[0], p[1], modn)
            print("Pair {} went to bucket {}".format(p, bucket))
            hash_pair_buckets[bucket] += 1
            bucket_pairs[bucket].append(p)

    print("Pass 1 - hash each item pair to a bucket based on a hash function")
    pprint(hash_pair_buckets)

    # filter buckets based on support
    frequent_buckets = [k for k, v in hash_pair_buckets.items() if v > support]
    print("Frequent buckets are {} based on a support of {}.".format(frequent_buckets, support))

    # pairs in frequent buckets - pass 2 of pcy
    pass2_pairs = set()
    for fb in frequent_buckets:
        fb_pairs = bucket_pairs[fb]
        for f in fb_pairs:
            pass2_pairs.add(f)

    print("Pass 2 of PCY algorithm yields the following frequent pairs: ")
    pprint(pass2_pairs)


def pass2_pcy(item_pairs_pass1, hash_buckets, hash_fn_stage2, modn):
    hash_pair_buckets = {k:0 for k in range(hash_buckets)}
    bucket_pairs = collections.defaultdict(list)

    for p in item_pairs_pass1:
        bucket = hash_fn_stage2(p[0], p[1], modn)
        print("Pair {} went to bucket {}".format(p, bucket))
        hash_pair_buckets[bucket] += 1
        bucket_pairs[bucket].append(p)

    print("Hash each item pair to a bucket based on a hash function - Pass 2 ")
    pprint(hash_pair_buckets)

