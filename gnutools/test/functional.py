from gnutools.fs import name, parent, listfiles


def test_imports(root):
    print(root)
    """
    Test import functions from a librory

    :param root:
    :return:
    """
    def try_import(m):
        try:
            exec(f'from {m} import *')
            print(f"=1= TEST PASSED : {m}")
        except Exception as e:
            print(f"=0= TEST FAILED : {m} ({e})")

    def path2module(m):
        return f"{lib_name}.{m.split('/' + lib_name)[1][1:].replace('/', '.')}"
    lib_name = name(root)
    modules = set([parent(file) for file in listfiles(root, [".py"])])
    modules = [path2module(m) for m in modules]
    modules = set([m for m in modules  if not ("__pycache__" in m or m[-1]==".")])
    [try_import(m) for m in modules]


