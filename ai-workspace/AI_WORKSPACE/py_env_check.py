import pkgutil, sys, os


def main(root=None):
	print('HAS_PYYAML', pkgutil.find_loader('yaml') is not None)
	print('PYTHON_EXE', sys.executable)
	print('CHECK_ROOT', os.path.abspath(root) if root else os.getcwd())


if __name__ == '__main__':
	root = sys.argv[1] if len(sys.argv) > 1 else None
	main(root)
