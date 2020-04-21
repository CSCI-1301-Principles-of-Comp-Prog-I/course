import copy
import sys
import random

def cons(x, l):
    new_l = copy.copy(l)
    new_l.insert(0,x)
    return new_l

def head (l):
    if l == []:
        print("Cannot call head on the empty list.", file=sys.stderr)
        sys.exit()
    x , *xs = l
    return x

def tail (l):
    if l == []: return []    
    x, *xs = l
    return xs

def append(l1,l2):
    return l1 + l2

def reverse(l):
    new_l = copy.copy(l)
    new_l.reverse()
    return new_l

def repeat(x,n):
    if n < 0:
        print ("Cannot call repeat with negative values.", file=sys.stderr)
        sys.exit()
    return [x] * n

def _take(n,acc,l):
    if n == 0:
        return acc
    elif n < 0:
        print ("Cannot call take with negagive values.", file=sys.stderr)
        sys.exit()
    x = head(l)
    rest = tail(l)
    return _take (n-1,cons(x,acc),rest)

def take(n,l):
    if l == []: return []
    return reverse (_take(n,[],l))

def drop(n,l):
    if n == 0:
        return l
    elif n < 0:
        print ("Cannot call drop with negative values.", file=sys.stderr)
        sys.exit()
    es = tail (l)
    return drop (n-1, es)

def _length(acc, l):
    if l == []:
        return acc
    return _length(1+acc,tail(l))

def length(l):
    return _length(0,l)

def _randint_list(n, acc, low, high):
    if n == 0: return acc
    x = random.randint(low,high)    
    return _randint_list (n - 1, cons(x,acc), low, high)

def randint_list(n, low, high):
    if n < 0:
        print ("Cannot call randint_list with negative values.", file=sys.stderr)
        sys.exit()
    return _randint_list(n,[], low, high)

def _randfloat_list(n, acc, low, high):
    if n == 0: return acc
    x = random.randint(low,high)    
    return _randfloat_list (n - 1, cons(x,acc), low, high )

def randfloat_list(n, low, high):
    if n < 0:
        print ("Cannot call randint_list with negative values.", file=sys.stderr)
        sys.exit()
    return _randfloat_list(n,[], low, high)

def unique(l):
    if l == []:
        return []
    e = head (l)
    es = tail (l)
    new_tail = [x for x in es if x != e]
    return cons(e, unique(new_tail))

def list_range(low, high):
    return list(range(low, high))

def foldl(op, acc, l):
    if l == []:
        return acc
    x , *xs = l
    return foldl(op, op(x,acc), xs)

def all(l):
    return foldl(both,True,l)

def any(l):
    return foldl(one,False,l)

def both(b1,b2):
    return  b1 and b2

def one(b1,b2):
    return  b1 or b2

