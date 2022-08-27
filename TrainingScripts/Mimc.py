# Define a static function

def Main():
    mesh_01 = Grp(name, BBDir, meshList, treePath, meshParentDir)

    # 现在mesh_01就是包含了相应数据的一个对象，里面包含了一些方法
    # Python 的类名，不需要全大写
    # 可以用对象里的方法获取想要的数据作为Matchinfo的入参
    info_01 = Matchinfo(mesh_01.getLowList())