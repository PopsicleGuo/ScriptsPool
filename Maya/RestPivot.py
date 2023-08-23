"""
    This script is helping the user to reset the debris cluster asset back into the origin
    The following transform will be updated
        DC_xxxx_xxxx
        Main
        Lod0-n
        Collision
    The script goes the following steps
        Get selected DC transform and its child
        Center Pivot all transform
        Move the DC_xxx transform into origin
        Freeze all transform
"""

import pymel.core as pm
import maya.cmds as cmds
import re




class DCWorldSpace:

    def __init__(self):
        self.subNodes = []
        self.dcMeshList = []
        self.dc_collision = []
        self.dc_shadow = []
        self.lod_matrix = [[] for _ in range(6)]
        self.re_pattern = r'(?!lod\d)[A-Za-z]{3,7}\d'
        self.sel_node = pm.selected()  # Get the user selected node name during initialization
        self.root_node = None
        self.__lod0_idx = {}  # for internal hash mapping

    def initialize_root_node(self):
        if len(self.sel_node) == 0:
            pm.confirmDialog(title='Error', message="   You haven't selected a node yet!!!   ", button=['Ok'],
                             defaultButton='Ok')
            exit()
        else:
            self.root_node = self.sel_node[0]
            if not self.check_root_translation():
                pm.makeIdentity(self.root_node, apply=True)

    def filter_transform(self):
        child_rows = pm.listRelatives(self.root_node, type='transform',
                                      ad=True)  # To get all the transforms which are under the root node

        for child in child_rows:  # filter all mesh/collision related transform node into different list
            self.check_status(child)
        print(" Nodes assignment have been done !!")

        ''' Use a hash mapping to store every node name and list index for further match pivot   '''
        self.__lod0_idx = {self.lod_matrix[0][index].name().split('|')[-1]: index
                           for index in range(0, len(self.lod_matrix[0]))}

        if self.__lod0_idx is not None:
            print("lod0 index builder process has been done !!")

    def match_pivot(self, target, current):
        return pm.matchTransform(current, target, piv=True)

    # Check every child node's parent name and assign it to lod or other list
    def check_status(self, item):
        name = item.longName().split('|')[-1]
        if re.search(self.re_pattern, name) is None:
            self.subNodes.append(item)
        else:
            node_name = str(item.getParent()).lower()
            if 'lod0' in node_name:
                self.lod_matrix[0].append(item)
            elif 'lod1' in node_name:
                self.lod_matrix[1].append(item)
            elif 'lod2' in node_name:
                self.lod_matrix[2].append(item)
            elif 'lod3' in node_name:
                self.lod_matrix[3].append(item)
            elif 'lod4' in node_name:
                self.lod_matrix[4].append(item)
            elif 'lod5' in node_name:
                self.lod_matrix[5].append(item)
            elif 'collision' in node_name:
                self.dc_collision.append(item)
            elif 'shadow' in node_name:
                self.dc_shadow.append(item)

    def split_string(self, content):
        return [x for x in content]

    ''' 
        This func will identify the node name of lod with the name in lod0
        Then return the fit list index number of lod0 for next pivot match step
    '''
    def align_with_standard_node(self, traf_node):
        non_lod0_node = traf_node.name().split('|')[-1]
        if non_lod0_node in self.__lod0_idx.keys():
            return self.__lod0_idx[non_lod0_node]


    def check_root_translation(self):
        rot_position = self.root_node.getTranslation()
        for i in list(map(int, rot_position)):
            if i != 0:
                return False
        return True

    def star_process(self):

        self.initialize_root_node()  # Check the process running condition is enough or not

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

            print("Start to freeze some nodes in main ")
            for trans_val in self.subNodes:
                #print("Freeze parent node {} translate".format(str(trans_val)))
                pm.makeIdentity(trans_val, apply=True)

            print("Start to freeze collision nodes!")
            for trans_val in self.dc_collision:
                #print("Freeze mesh node {} translate".format(str(trans_val)))
                pm.makeIdentity(trans_val, apply=True)

            print("Start to freeze all lods related nodes")
            for row in range(len(self.lod_matrix)):
                for column in self.lod_matrix[row]:
                    pm.makeIdentity(column, apply=True)

            print("Start to freeze shadow nodes !!")
            for trans_val in self.dc_shadow:
                #print("Freeze mesh node {} translate".format(str(trans_val)))
                pm.makeIdentity(trans_val, apply=True)

            ''' Step 4 Reset all nodes except the root node '''
            for ver_val in self.subNodes:
                ver_val.zeroTransformPivots()

            for ver_val in self.dc_collision:
                ver_val.zeroTransformPivots()

            for row in range(len(self.lod_matrix)):
                if len(self.lod_matrix[row]) != 0:
                    for column in self.lod_matrix[row]:
                        column.zeroTransformPivots()

            for ver_val in self.dc_shadow:
                ver_val.zeroTransformPivots()

            print("All DC mesh related nodes has applied zero transform !!")

            ''' Step 5 Set center pivot for lod related mesh node '''
            for node in self.lod_matrix[0]:
                node.centerPivots()

            ''' Match each node of other lods with lod0 object  '''
            for row in range(1, len(self.lod_matrix)):
                if len(self.lod_matrix[row]) != 0:
                    for col_index in range(len(self.lod_matrix[row])):
                        lod0_id = self.align_with_standard_node(self.lod_matrix[row][col_index])
                        self.match_pivot(self.lod_matrix[0][lod0_id],
                                         self.lod_matrix[row][col_index])

            ''' Step 6 Set center pivot for shadow related mesh node '''
            for row in range(len(self.dc_shadow)):
                lod0_id = self.align_with_standard_node(self.dc_shadow[row])
                self.match_pivot(self.lod_matrix[0][lod0_id],
                                 self.dc_shadow[row])

            ''' Step 7 Set center pivot for collision related mesh node '''
            for node in self.dc_collision:
                node.centerPivots()

        except:
            pm.displayError("The main process gets error !!")
        finally:
            pm.confirmDialog(title='Confirm', message='  Process Finished  ', button=['Ok'], defaultButton='Ok')


# Main function of UI button
def click_rs_button():
    main_inst = DCWorldSpace()
    main_inst.star_process()

# Set a window for easy understanding
pm.window(title='DC_Pivot', widthHeight=(300, 100))
pm.columnLayout(adjustableColumn=True)

# Add a text label to guide user a bit
pm.text(label='Choose DC transform node, and then click button!!', width=250)

# Add the button
pm.button(label='Reset', command=click_rs_button)
pm.showWindow()
