import subprocess

def read_text(text):
	subprocess.call(["python","sp_scr.py",text])
"""
def main():
	read_text("hello world")
	read_text("this is the second one")
	read_text("and this is the third")

if __name__ == '__main__':
	main()
"""