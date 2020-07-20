# Recursive to Iterative

# Approach 1: Simulate the stack

def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n - 1)

def factorial_iter(n):
  original_n = n
  results = {}
  inputs_to_resolve = [n]
  while inputs_to_resolve:
    n = inputs_to_resolve.pop()
    if n < 2: 
      results[n] = 1
    else:
      # we want n-1
      if n-1 not in results:
        else:
          inputs_to_resolve.append(n)
          inputs_to_resolve.append(n-1)
      else:
        results[n] = n*results[n-1]

# Approach 2: Tail End Recursion

