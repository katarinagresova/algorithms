def solution(s):
    for k in range(1, len(s) - 1):
        splits = kmers(s, k)
        if all_equal(splits):
            return len(splits)
            break
    return 1
        
def kmers(seq, k):
  return [seq[i:i+k] for i in range(0,len(seq),k)]
  
def all_equal(splits):
    return all(x==splits[0] for x in splits)
