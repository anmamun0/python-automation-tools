
try :
    f = open('does.txt')

except FileNotFoundError as e:
    print (f"This - {e}")
else:
    print("This will run only if Exception is not running")

finally:
    print('Run this anyway')

print('Hello done')
