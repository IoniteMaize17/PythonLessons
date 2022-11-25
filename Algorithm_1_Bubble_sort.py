def bubble_sort(a):
	while True:
		swap=False
		i=0
		hold=0
		while i+1<len(a):
			if a[i]<a[i+1]:
				i=i+1
			elif a[i]>a[i+1]:
				hold=a[i]
				a[i]=a[i+1]
				a[i+1]=hold
				i = i+1
				swap = True
		if swap == False:
			return a