def loader(arg):
    try:
        with open(arg, 'r') as f:
            return f.read()
    except (FileNotFoundError, IOError, FileExistsError):
        return f'такого файла нет'


if __name__ == '__main__':
    print(loader('nofile.txt'))
    print(loader('n0file.txt'))
