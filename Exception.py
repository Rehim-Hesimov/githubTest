try:
	f=open('currupt_file.txt')
	if f.name=='currupt_file.txt':
		raise Exception

except Exception :
	print("Error!")
else:
	print(f.read())
	f.close()
finally:
	print("Executing Finally...")

