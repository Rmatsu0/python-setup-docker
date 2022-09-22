len = 29
if len != 0:
	print("no zero!")
else:
	print("good lucky number!")

ending = "sekai"

def makoto(ending):
	if ending == "sekai":
		print("」」」」」」」」")
	elif ending == "kotoha":
		print("nice boat")
	else:
		print("good days")

def andor(num):
	if num > 0 and num < 100:
		print ("1 ~ 99 number")
	elif num > 99 or num == 0:
		print ("100 over number and minus 0")
	else:
		print ("minus number")


def main():
	#ending = "sekai"
	#ending = "kotoha"
	ending = "makoto"
	makoto(ending)

if __name__ == "__main__":
	main()
	andor(99)
	andor(0)
	andor(299)
	andor(-3)