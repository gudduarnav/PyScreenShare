from io import BytesIO

try:
    import pyscreenshot
except ImportError as __ex:
    print("Install pyscreenshot. Exception:", str(__ex))
    exit(1)

# return gzip of PNG image of screen
def captureScreen(imsize=(640, 480), compresslevel=9, quality=50):
    f_img = BytesIO()
    pyscreenshot.grab().resize(imsize).save(f_img, "JPEG", quality=quality)
    f_img.seek(0)
    return f_img.getvalue()

# read file and send
def readFiletoMemory(filename):
    f_mem = BytesIO()
    with open(filename, "r") as f:
        f_mem.write(f.read().encode("UTF-8"))

    return f_mem.getvalue()



def main():
    print(readFiletoMemory("helper.py"))
if __name__ == "__main__":
    main()




