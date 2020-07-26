"""
Show test result for calculation time in copy a list
maintainer: V4ld3rr4m4
"""
import time
import copy 

# Firstable define our big list
our_list = []
for x in range(1999999):
	our_list.append(x)

# function  decorator to shoe execution time of any funtion
def timer(function):
	def wrapper(list1):
		t_start = time.time()
		rtval = function(list1)
		t_end = time.time()
		print(f'Take: {round(t_end-t_start,3)} seg.')
		return rtval

	return wrapper

# Slice ---------------------------------------
@timer
def by_slice(list1):
	list2 = list1[:]
	return list2

# Extend --------------------------------------
@timer
def by_extend(list1):
	list2 = []
	list2.extend(list1)
	return list2

# List ----------------------------------------
@timer
def by_list(list1):
	list2 = list(list1) 
	return list2

# List Comprehension ---------------------------
@timer
def by_list_comprehension(list1):
	list2 = [i for i in list1] 
	return list2

# List DeepCopy  -------------------------------
@timer
def by_deepcopy(list1):
	list2 = copy.deepcopy(list1) 
	return list2

clone_x = our_list
clone_slice = by_slice(our_list)
clone_extend = by_extend(our_list)
clone_list = by_list(our_list)
clone_comp = by_list_comprehension(our_list)
clone_deep = by_deepcopy(our_list)


clone_x[0] = "CERO"
clone_slice[0] = "SLICED"
clone_extend[0] = "EXTENDED"
clone_list[0] = "LISTED"
clone_comp[0] = "COMPRENHENSED"
clone_deep[0] = "DEEPED"

print(f"""
      Copy X ( No funciona) {clone_x[0:5]}
      by_slice  -> {clone_slice[0:5]}
      by_extend -> {clone_extend[0:5]}
      by_list   -> {clone_list[0:5]}
      by_lComp  -> {clone_comp[0:5]}
      by_deep   -> {clone_deep[0:5]}
      original  -> {our_list[0:5]}
""")
