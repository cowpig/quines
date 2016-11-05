def quine():
	import inspect
	print(inspect.getsource(quine))
	print("quine()")

quine()
