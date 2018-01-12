### Park-Chen-Yu Algorithm for Frequent Itemset Mining

The Park-Chen-Yu or PCY algorithm is a hash based improvement over the Apriori algorithm for mining frequent itemsets.

Source: http://infolab.stanford.edu/~ullman/mining/pdf/assoc-rules2.pdf

## Usage:

Specify baskets, number of buckets (hash_buckets), support threshold & the range of items 
(difference of minimum & maximum item number):

    baskets = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [1, 3, 5], [2, 4, 6], [1, 3, 4],
    [2, 4, 5], [3, 5, 6], [1, 2, 4], [2, 3, 5], [3, 4, 6]] 

    hash_buckets = 11
    support = 4
    items_range = 6

    mod_n = 11

Run PCY: 
    pcy(baskets, hash_buckets, support, items_range, hash_fn_pass1, mod_n)


Run only pass 2 of PCY:
 

    item_pairs_1 = [(1, 2), (2, 6), (4, 6), (5, 6), (1, 4), (3, 4), (2, 4), (3, 5)]
    hash_buckets = 9
    modn = 9
    
    pass2_pcy(item_pairs_1, hash_buckets, hash_fn_pass2, modn)
