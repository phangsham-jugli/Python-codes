#finally block
import io
try:
    eh=open("practice_file.txt","tw")
    data=eh.read()
    eh.close()

except FileNotFoundError as err:
    print("File not found")
    print(err)
except io.UnsupportedOperation as io_err:
    print(io_err )
else:
    print(data)
finally:
    print("it run even there is error")