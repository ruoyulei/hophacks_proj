import subprocess


def main():
	print "world"
	arr = ["python", "process_call.py","&>","/dev/null"]
	#f = open('/dev/null', 'w')
	#ps = subprocess.Popen(("python", "process_call.py"), stdout=subprocess.REDIRECTION, stderr=subprocess.REDIRECTION)
	#output = subprocess.check_output(("a.txt"), stdin=ps.stdout)
	#ps.wait()
	#subprocess.stdout = f
	subprocess.call(arr)


if __name__ == '__main__':
	main()