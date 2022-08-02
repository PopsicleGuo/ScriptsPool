'''
    This script is helping the user to reset the debris cluster asset back into the origin
    The following transform will be updated
        DC_xxxx_xxxx
        Main
        Lod0-n
        Collision
    The script goes the following steps
        Get selected DC transform and its childs
        Center Pivot all transform
        Move the DC_xxx transform into origin
        Freeze all transform
'''

import pymel.core as pm
import re


class DCWorldSpace:

    def __init__(self):
        self.subNodes = []
        self.dcMeshList = []
        self.re_pattern = r'(?!lod\d)[A-Za-z]{3,7}\d'
        self.sel_node = pm.selected()
        self.root_node = None

    def root_node_check(self):
        if len(self.sel_node) == 0:
            pm.confirmDialog(title='Error', message="   You haven't selected a node yet!!!   ", button=['Ok'],
                             defaultButton='Ok')
            exit()
        else:
            self.root_node = self.sel_node[0]

    def filter_transform(self):
        allChilds = pm.listRelatives(self.root_node, type='transform', ad=True)  # To get all the transforms which are under the root node

        for child in allChilds:  # filter all mesh/collision related transform node into different list
            nod_name = child.longName().split('|')[-1]
            if re.search(self.re_pattern, nod_name) == None:
                self.subNodes.append(child)
            else:
                self.dcMeshList.append(child)

    def star_process(self):

        self.root_node_check()  # Check the process running condition is enough or not

        ful_path = self.root_node.fullPath()
        if not ful_path.split('|')[-1].startswith('DC_'):  # Check the artist selected transform
            pm.displayError("You haven't selected a node which starts with 'DC_' ")
            exit()

        ''' Step 0: it gets the right node into different node list '''
        self.filter_transform()

        ''' Step 1 center pivot for the root node '''
        try:
            if self.root_node:
                print("Reset root node {} center pivot".format(str(self.root_node)))
                self.root_node.centerPivots()

            ''' 
                Step 2 Set the center pivot for the root node, and move it into origin
            '''
            root_cod = (self.root_node.getPivots()[0]) * -1
            print("Get current node {}'s pivot coordinate is {}".format(str(self.root_node), str(root_cod)))
            print("Moving the root transform into origin")
            pm.move(str(self.root_node), root_cod, r=True)
            print("Done~")

            ''' Step 3 freeze transformations for DC, main, lod*, collision nodes '''
            print("Freeze root node {} translate".format(str(self.root_node)))
            pm.makeIdentity(self.root_node, apply=True)
            print("The root node has been frozen !")

            for trans_val in self.subNodes:
                print("Freeze parent node {} translate".format(str(trans_val)))
                pm.makeIdentity(trans_val, apply=True)

            for trans_val in self.dcMeshList:
                print("Freeze mesh node {} translate".format(str(trans_val)))
                pm.makeIdentity(trans_val, apply=True)

            ''' Step 4 Reset all nodes except the root node '''
            for ver_val in self.subNodes:
                ver_val.zeroTransformPivots()

            for ver_val in self.dcMeshList:
                ver_val.zeroTransformPivots()

            ''' Step 5 Set center pivot for all dc related mesh node '''
            for node in self.dcMeshList:
                print("Reset DC mesh node {} center pivot".format(str(node)))
                node.centerPivots()

        except:
            pm.displayError("The main process gets error !!")
        finally:
            pm.confirmDialog(title='Confirm', message='  Process Finished  ', button=['Ok'], defaultButton='Ok')


# Running the process
def main():
    main_inst = DCWorldSpace()
    return main_inst.star_process()


if __name__ == '__main__':
    main()
