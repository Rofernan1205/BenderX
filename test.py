import os

def main():
    path = os.path.join("app", "styles", "styles.qss")
    if os.path.exists(path):
        print("Si existe")
    else:
        print("No existe")

if __name__ == '__main__':
    main()